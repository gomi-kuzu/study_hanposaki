from manim import *
import numpy as np
import math


# ============================================================
# エルミート関数（sec23_1.py と同じ）
# ============================================================
def hermite_poly(n, x):
    """物理学のエルミート多項式 H_n(x) を漸化式で計算する"""
    if n == 0:
        return np.ones_like(x) if hasattr(x, "__len__") else 1.0
    if n == 1:
        return 2.0 * x
    h_prev = np.ones_like(x) if hasattr(x, "__len__") else 1.0
    h_curr = 2.0 * x
    for k in range(1, n):
        h_next = 2.0 * x * h_curr - 2.0 * k * h_prev
        h_prev, h_curr = h_curr, h_next
    return h_curr


def hermite_function(n, x):
    """エルミート関数 psi_n(x) = (2^n n! sqrt(pi))^{-1/2} exp(-x^2/2) H_n(x)"""
    norm = 1.0 / np.sqrt((2 ** n) * math.factorial(n) * np.sqrt(np.pi))
    return norm * np.exp(-x ** 2 / 2.0) * hermite_poly(n, x)


# ============================================================
# 固有関数計算：エルミート基底での表現行列 L
# ============================================================
def build_hermite_L(N, gamma, D):
    """
    エルミート関数基底 (n = 0, ..., N-1) での OU 作用素の表現行列。
    L psi_n = gamma [alpha_n psi_{n-2} + 1/2 psi_n - alpha_{n+2} psi_{n+2}]
           + (D/2)[alpha_n psi_{n-2} + (-n - 1/2) psi_n + alpha_{n+2} psi_{n+2}]
    """
    L = np.zeros((N, N), dtype=np.float64)

    def alpha(n):
        if n < 2:
            return 0.0
        return 0.5 * math.sqrt(n * (n - 1))

    for n in range(N):
        a_n = alpha(n)
        a_np2 = alpha(n + 2)
        # 対角
        L[n, n] += gamma * 0.5 + (D / 2.0) * (-n - 0.5)
        # 下 (m = n-2)
        if n - 2 >= 0:
            L[n - 2, n] += gamma * a_n + (D / 2.0) * a_n
        # 上 (m = n+2)
        if n + 2 < N:
            L[n + 2, n] += -gamma * a_np2 + (D / 2.0) * a_np2
    return L


def build_lattice_L(x_grid, gamma, D):
    """
    格子点法での OU 作用素の表現行列（中心差分）。
    (L~ p)_m = gamma (x_{m+1} p_{m+1} - x_{m-1} p_{m-1}) / (2 dx)
            + (D/2) (p_{m+1} - 2 p_m + p_{m-1}) / dx^2

    境界は Dirichlet: p(x_0) = p(x_{M-1}) = 0 と固定して、
    内部格子点 m = 1, ..., M-2 のみを未知数とする (M-2)x(M-2) 行列を返す。
    こうしないと境界の空行から縮退したゼロ固有値が生じてしまう。
    """
    M = len(x_grid)
    dx = x_grid[1] - x_grid[0]
    N = M - 2  # 内部点のみ
    L = np.zeros((N, N), dtype=np.float64)
    for i in range(N):
        m = i + 1  # 対応する格子点インデックス
        # 中央
        L[i, i] += -2.0 * (D / 2.0) / (dx * dx)
        # 左隣 (m-1)
        if i - 1 >= 0:
            L[i, i - 1] += -gamma * x_grid[m - 1] / (2.0 * dx)
            L[i, i - 1] += (D / 2.0) / (dx * dx)
        # 右隣 (m+1)
        if i + 1 < N:
            L[i, i + 1] += gamma * x_grid[m + 1] / (2.0 * dx)
            L[i, i + 1] += (D / 2.0) / (dx * dx)
    return L


def compute_eigenfunctions_hermite(N, gamma, D, x_plot, num_modes=4):
    """エルミート基底で計算した固有関数（低次から num_modes 個）を x_plot 上で返す"""
    L = build_hermite_L(N, gamma, D)
    eigvals, eigvecs = np.linalg.eig(L)
    # 実数部のみ扱う（数値誤差の複素成分は無視）
    eigvals = eigvals.real
    eigvecs = eigvecs.real
    # 実部が大きい順（0 に近い順）に並べる
    order = np.argsort(-eigvals)
    eigvals = eigvals[order]
    eigvecs = eigvecs[:, order]

    # 基底関数の値をあらかじめ計算
    psi_vals = np.zeros((N, len(x_plot)))
    for n in range(N):
        psi_vals[n] = hermite_function(n, x_plot)

    modes = []
    for i in range(num_modes):
        v = eigvecs[:, i]
        phi = psi_vals.T @ v  # shape (len(x_plot),)
        modes.append((eigvals[i], phi))
    return modes


def compute_eigenfunctions_lattice(x_grid, gamma, D, num_modes=4):
    """
    格子点法で計算した固有関数（低次から num_modes 個）。
    L は内部点 (M-2 個) の行列。境界値は 0 として、
    (x_grid 全体に対応する) 長さ M のベクトルを返す。
    """
    M = len(x_grid)
    L = build_lattice_L(x_grid, gamma, D)
    eigvals, eigvecs = np.linalg.eig(L)
    eigvals = eigvals.real
    eigvecs = eigvecs.real
    order = np.argsort(-eigvals)
    eigvals = eigvals[order]
    eigvecs = eigvecs[:, order]

    modes = []
    for i in range(num_modes):
        v_full = np.zeros(M)
        v_full[1:-1] = eigvecs[:, i]  # 境界は 0
        modes.append((eigvals[i], v_full))
    return modes


def normalize_shape(y, x):
    """L2 ノルムで正規化し、符号を「最大絶対値位置で正」になるように調整"""
    norm = np.sqrt(np.trapezoid(y * y, x))
    if norm < 1e-12:
        return y
    y = y / norm
    idx = np.argmax(np.abs(y))
    if y[idx] < 0:
        y = -y
    return y


class SpatialDiscretizationComparison(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        title = Text("空間を分割する数値解法との比較", font_size=36, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.7)

        # ============================================================
        # Part 1: 前回のおさらいと今回のテーマ
        # ============================================================
        subtitle1 = Text("前の動画の最後の前振り", font_size=28, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.4)

        # recap1 = Text(
        #     "前回の最後で、次のことを述べた",
        #     color=WHITE, font_size=26,
        # )
        # recap1.shift(UP * 2.0)
        # self.play(Write(recap1), run_time=0.7)
        # self.wait(0.4)

        recap2 = Text(
            "「同じ線形作用素 ℒ であれば、",
            color=GOLD, font_size=28, weight=BOLD,
        )
        recap3 = Text(
            "基底のとり方によらず固有関数は同じはず」",
            color=GOLD, font_size=28, weight=BOLD,
        )
        recap2.shift(UP * 1.0)
        recap3.next_to(recap2, DOWN, buff=0.2)
        self.play(Write(recap2), run_time=0.7)
        self.play(Write(recap3), run_time=0.7)
        self.wait(0.7)

        idea_text = Text(
            "そこで、エルミート関数とは違う別の近似解法で固有関数を計算し、比較する",
            color=WHITE, font_size=24,
        )
        idea_text.shift(DOWN * 0.3)
        self.play(Write(idea_text), run_time=0.9)
        self.wait(0.5)

        method_text = Text(
            "その方法が「格子点法」（有限差分法）",
            color=YELLOW, font_size=30, weight=BOLD,
        )
        method_text.shift(DOWN * 1.3)
        method_box = SurroundingRectangle(method_text, color=YELLOW, buff=0.25)
        self.play(Write(method_text), Create(method_box), run_time=0.9)
        self.wait(1.2)

        self.play(
            # FadeOut(recap1),
            FadeOut(recap2), FadeOut(recap3),
            FadeOut(recap2), FadeOut(recap3),
            FadeOut(idea_text), FadeOut(method_text), FadeOut(method_box),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: 傾きから速度を決めるという振り返り
        # ============================================================
        subtitle2 = Text("偏微分方程式の振り返り", font_size=28, color=GOLD)
        subtitle2.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle2), run_time=0.5)
        self.wait(0.4)

        review_text = Text(
            "確率密度関数の時間発展の式を振り返ると、",
            color=WHITE, font_size=26,
        )
        review_text.shift(UP * 2.0)
        self.play(Write(review_text), run_time=0.7)
        self.wait(0.4)

        fp_eq = MathTex(
            r"\frac{\partial}{\partial t}p(x,t) = "
            r"\gamma \frac{\partial}{\partial x}\bigl(x\,p(x,t)\bigr)"
            r"+ \frac{D}{2} \frac{\partial^2}{\partial x^2} p(x,t)",
            color=YELLOW,
            font_size=36,
        )
        fp_eq.shift(UP * 0.9)
        self.play(Write(fp_eq), run_time=1.0)
        self.wait(0.6)

        explain_text = Text(
            "x に対する傾きや、その傾きに応じて",
            color=WHITE, font_size=24,
        )
        explain_text2 = Text(
            "その付近の時間変化率（速度）を決めていた",
            color=WHITE, font_size=24,
        )
        explain_text.shift(DOWN * 0.3)
        explain_text2.next_to(explain_text, DOWN, buff=0.2)
        self.play(Write(explain_text), run_time=0.7)
        self.play(Write(explain_text2), run_time=0.7)
        self.wait(0.6)

        strategy_text = Text(
            "→ 格子点法では、予め確率変数空間上に格子状の点を定め、",
            color=GOLD, font_size=26,
        )
        strategy_text2 = Text(
            "隣り合う点の差分から勾配の一次近似を求めて速度とする",
            color=GOLD, font_size=26,
        )
        strategy_text.shift(DOWN * 1.7)
        strategy_text2.next_to(strategy_text, DOWN, buff=0.15)
        self.play(Write(strategy_text), run_time=0.8)
        self.play(Write(strategy_text2), run_time=0.8)
        self.wait(1.2)

        self.play(
            FadeOut(review_text), FadeOut(fp_eq),
            FadeOut(explain_text), FadeOut(explain_text2),
            FadeOut(strategy_text), FadeOut(strategy_text2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: 格子点上の確率密度ベクトル
        # ============================================================
        subtitle3 = Text("格子点上の確率密度ベクトル", font_size=28, color=TEAL)
        subtitle3.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle3), run_time=0.5)
        self.wait(0.4)

        vec_intro = Text(
            "格子点上の確率密度関数値を並べてベクトルを作る",
            color=WHITE, font_size=26,
        )
        vec_intro.shift(UP * 2.0)
        self.play(Write(vec_intro), run_time=0.7)
        self.wait(0.4)

        p_vec = MathTex(
            r"\boldsymbol{p}(t) = "
            r"\begin{bmatrix} p(x_0, t) \\ p(x_1, t) \\ \vdots \\ p(x_M, t) \end{bmatrix}",
            color=YELLOW,
            font_size=42,
        )
        p_vec.shift(UP * 0.1)
        p_vec_box = SurroundingRectangle(p_vec, color=YELLOW, buff=0.3)
        self.play(Write(p_vec), Create(p_vec_box), run_time=1.0)
        self.wait(0.6)

        dx_text = MathTex(
            r"x_m = x_0 + m\,\Delta x, \quad m = 0, 1, \ldots, M",
            color=TEAL, font_size=36,
        )
        dx_text.shift(DOWN * 1.9)
        self.play(Write(dx_text), run_time=0.8)
        self.wait(1.2)

        vec_comment = Text(
            "この”値の集まり”で離散的に確率密度関数を近似する!",
            color=WHITE, font_size=26,
        )
        vec_comment.shift(DOWN * 2.8)
        self.play(Write(vec_comment), run_time=0.7)
        self.wait(0.4)

        self.play(
            FadeOut(vec_intro), FadeOut(p_vec), FadeOut(p_vec_box),
            FadeOut(dx_text), FadeOut(vec_comment)
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: 差分の種類
        # ============================================================
        subtitle4 = Text("差分の種類", font_size=28, color=ORANGE)
        subtitle4.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle4), run_time=0.5)
        self.wait(0.4)

        diff_intro = Text(
            "刻み幅を Δx とすると、以下のような差分の計算方法がある",
            color=WHITE, font_size=24,
        )
        diff_intro.shift(UP * 2.2)
        self.play(Write(diff_intro), run_time=0.7)
        self.wait(0.4)

        forward_label = Text("前進差分", color=BLUE, font_size=24)
        forward_eq = MathTex(
            r"\frac{d}{dx}p(x_m, t) \simeq "
            r"\frac{p(x_m + \Delta x, t) - p(x_m, t)}{\Delta x}",
            color=WHITE, font_size=30,
        )
        forward_group = VGroup(forward_label, forward_eq).arrange(RIGHT, buff=0.5)
        forward_group.shift(UP * 1.2)
        self.play(Write(forward_label), Write(forward_eq), run_time=0.9)
        self.wait(0.5)

        backward_label = Text("後退差分", color=GREEN, font_size=24)
        backward_eq = MathTex(
            r"\frac{d}{dx}p(x_m, t) \simeq "
            r"\frac{p(x_m, t) - p(x_m - \Delta x, t)}{\Delta x}",
            color=WHITE, font_size=30,
        )
        backward_group = VGroup(backward_label, backward_eq).arrange(RIGHT, buff=0.5)
        backward_group.shift(UP * 0.1)
        self.play(Write(backward_label), Write(backward_eq), run_time=0.9)
        self.wait(0.5)

        central_label = Text("中心差分", color=YELLOW, font_size=24)
        central_eq = MathTex(
            r"\frac{d}{dx}p(x_m, t) \simeq "
            r"\frac{p(x_m + \Delta x, t) - p(x_m - \Delta x, t)}{2\Delta x}",
            color=WHITE, font_size=30,
        )
        central_group = VGroup(central_label, central_eq).arrange(RIGHT, buff=0.5)
        central_group.shift(DOWN * 1.0)
        self.play(Write(central_label), Write(central_eq), run_time=0.9)
        central_box = SurroundingRectangle(central_group, color=YELLOW, buff=0.2)
        self.play(Create(central_box), run_time=0.5)
        self.wait(0.6)

        central_note = Text(
            "中心差分は、計算手間はほぼ変わらないのに近似精度が高い",
            color=GOLD, font_size=24, weight=BOLD,
        )
        central_note.shift(DOWN * 2.4)
        self.play(Write(central_note), run_time=0.9)
        self.wait(1.3)

        self.play(
            FadeOut(diff_intro),
            FadeOut(forward_label), FadeOut(forward_eq),
            FadeOut(backward_label), FadeOut(backward_eq),
            FadeOut(central_label), FadeOut(central_eq), FadeOut(central_box),
            FadeOut(central_note),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: 前進差分の直感的な図解
        # ============================================================
        subtitle5 = Text("差分の直感的な意味（前進差分）", font_size=28, color=BLUE)
        subtitle5.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle5), run_time=0.5)
        self.wait(0.4)

        # グラフ
        axes5 = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 0.6, 0.2],
            x_length=8.5,
            y_length=3.6,
            axis_config={"color": WHITE, "include_tip": False, "stroke_width": 2},
        )
        axes5.shift(DOWN * 0.5)
        x_label5 = MathTex("x", color=WHITE, font_size=28).next_to(axes5.x_axis.get_end(), RIGHT, buff=0.15)
        y_label5 = MathTex(r"p(x,t)", color=WHITE, font_size=28).next_to(axes5.y_axis.get_end(), UP, buff=0.15)

        # ある確率密度関数 (ガウシアン風)
        def p_demo(x):
            return 0.55 * np.exp(-0.5 * (x - 0.2) ** 2 / 0.9)

        curve = axes5.plot(p_demo, x_range=[-2.8, 2.8], color=TEAL, stroke_width=3)

        self.play(Create(axes5), Write(x_label5), Write(y_label5), run_time=0.8)
        self.play(Create(curve), run_time=0.9)
        self.wait(0.3)

        # 等間隔の点線
        x_ticks = [-2.0, -1.0, 0.0, 1.0, 2.0]
        dashed_lines = VGroup()
        for xv in x_ticks:
            top = axes5.c2p(xv, 0.6)
            bot = axes5.c2p(xv, 0.0)
            dl = DashedLine(bot, top, color=GRAY, stroke_width=1.5, dash_length=0.08)
            dashed_lines.add(dl)
        self.play(Create(dashed_lines), run_time=0.8)
        self.wait(0.3)

        # 適当な隣り合う3点 x_1, x_2, x_3
        pick_x = [-1.0, 0.0, 1.0]
        pick_labels = [r"x_1", r"x_2", r"x_3"]
        pt_colors = [YELLOW, ORANGE, RED]
        dots = VGroup()
        pt_labels = VGroup()
        val_labels = VGroup()
        for xv, name, col in zip(pick_x, pick_labels, pt_colors):
            yv = p_demo(xv)
            pt = Dot(axes5.c2p(xv, yv), color=col, radius=0.09)
            dots.add(pt)
            # x_i ラベル（横軸下）
            lb = MathTex(name, color=col, font_size=26).next_to(axes5.c2p(xv, 0), DOWN, buff=0.15)
            pt_labels.add(lb)
            # p(x_i, t) ラベル（点の近く）
            vl = MathTex(rf"p({name}, t)", color=col, font_size=22).next_to(pt, UP, buff=0.1)
            val_labels.add(vl)

        for d, lb, vl in zip(dots, pt_labels, val_labels):
            self.play(FadeIn(d, scale=0.5), Write(lb), Write(vl), run_time=0.5)
        self.wait(0.4)

        # x_1 と x_2 の間の傾きを表す割線
        p1 = axes5.c2p(pick_x[0], p_demo(pick_x[0]))
        p2 = axes5.c2p(pick_x[1], p_demo(pick_x[1]))
        # 割線を左右に延長
        vec = np.array(p2) - np.array(p1)
        secant = Line(np.array(p1) - 0.6 * vec, np.array(p2) + 0.6 * vec,
                      color=YELLOW, stroke_width=3)
        self.play(Create(secant), run_time=0.8)
        self.wait(0.3)

        # Δx マーカ（横軸上に）
        dx_bracket = BraceBetweenPoints(
            axes5.c2p(pick_x[0], 0), axes5.c2p(pick_x[1], 0),
            direction=DOWN, color=WHITE,
        )
        dx_label = MathTex(r"\Delta x", color=WHITE, font_size=28).next_to(dx_bracket, DOWN, buff=0.1)
        # x1 と x2 のラベルと被らないよう少し下
        dx_label.shift(DOWN * 0.15)
        self.play(GrowFromCenter(dx_bracket), Write(dx_label), run_time=0.7)
        self.wait(0.4)

        # 前進差分の式（x_1 における傾きの近似）
        forward_visual = MathTex(
            r"\frac{d}{dx}p(x_1, t) \simeq "
            r"\frac{p(x_2, t) - p(x_1, t)}{\Delta x}",
            color=YELLOW, font_size=34,
        )
        forward_visual.to_edge(UP, buff=1.3).shift(LEFT * 3.2 + DOWN * 2)
        self.play(Write(forward_visual), run_time=0.9)
        self.wait(1.3)

        insight = Text(
            "近くの2点を結んだ割線の傾きで、その点での勾配を近似する",
            color=GOLD, font_size=24,
        )
        insight.to_edge(DOWN, buff=0.3)
        self.play(Write(insight), run_time=0.9)
        self.wait(1.5)

        self.play(
            FadeOut(axes5), FadeOut(x_label5), FadeOut(y_label5),
            FadeOut(curve), FadeOut(dashed_lines),
            FadeOut(dots), FadeOut(pt_labels), FadeOut(val_labels),
            FadeOut(secant), FadeOut(dx_bracket), FadeOut(dx_label),
            FadeOut(forward_visual), FadeOut(insight),
        )
        self.wait(0.3)

        # ============================================================
        # Part 6: 中心差分の行列表現
        # ============================================================
        subtitle6 = Text("中心差分の行列表現", font_size=28, color=PURPLE)
        subtitle6.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle6), run_time=0.5)
        self.wait(0.4)

        mat_intro = Text(
            "中心差分を使うと、1階微分の部分は行列で書ける",
            color=WHITE, font_size=26,
        )
        mat_intro.shift(UP * 2.1)
        self.play(Write(mat_intro), run_time=0.8)
        self.wait(0.4)

        first_deriv_mat = MathTex(
            r"\frac{\partial}{\partial x} p(x,t) \to "
            r"\frac{1}{\Delta x}"
            r"\begin{bmatrix} "
            r"0 & \tfrac{1}{2} & 0 & \cdots & 0 & 0 \\ "
            r"-\tfrac{1}{2} & 0 & \tfrac{1}{2} & \cdots & 0 & 0 \\ "
            r"0 & -\tfrac{1}{2} & 0 & \cdots & 0 & 0 \\ "
            r"\vdots & \vdots & \vdots & \ddots & & \vdots \\ "
            r"0 & 0 & 0 & \cdots & -\tfrac{1}{2} & 0 "
            r"\end{bmatrix}"
            r"\begin{bmatrix} p(x_0, t) \\ p(x_1, t) \\ p(x_2, t) \\ \vdots \\ p(x_M, t) \end{bmatrix}",
            color=YELLOW, font_size=32,
        )
        first_deriv_mat.shift(UP * 0.5)
        self.play(Write(first_deriv_mat), run_time=1.4)
        self.wait(1.0)

        same_2nd = Text(
            "同様にして2階微分も行列で表現できる",
            color=WHITE, font_size=26,
        )
        same_2nd.shift(DOWN * 1.5)
        self.play(Write(same_2nd), run_time=0.7)
        self.wait(0.4)

        result_ode = MathTex(
            r"\frac{d}{dt}\boldsymbol{p}(t) = \tilde{L}\,\boldsymbol{p}(t)",
            color=GOLD, font_size=48,
        )
        result_ode.shift(DOWN * 2.7)
        result_box = SurroundingRectangle(result_ode, color=GOLD, buff=0.25)
        self.play(Write(result_ode), Create(result_box), run_time=0.9)
        self.wait(1.4)

        self.play(
            FadeOut(mat_intro), FadeOut(first_deriv_mat),
            FadeOut(same_2nd), FadeOut(result_ode), FadeOut(result_box),
        )
        self.wait(0.3)

        # ============================================================
        # Part 7: 格子点法の固有関数の取り出し方
        # ============================================================
        subtitle7 = Text("格子点法の固有関数", font_size=28, color=GREEN)
        subtitle7.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle7), run_time=0.5)
        self.wait(0.4)

        diff_matrix_note1 = Text(
            r"表現行列 L̃ は、エルミート関数のときとは違う行列になる",
            color=WHITE, font_size=24,
        )
        diff_matrix_note2 = Text(
            "→ 固有ベクトルも当然異なる。では固有関数はどうなるのか？",
            color=WHITE, font_size=24,
        )
        diff_matrix_note1.shift(UP * 2.2)
        diff_matrix_note2.next_to(diff_matrix_note1, DOWN, buff=0.2)
        self.play(Write(diff_matrix_note1), run_time=0.8)
        self.play(Write(diff_matrix_note2), run_time=0.8)
        self.wait(0.6)

        key_point1 = Text(
            "格子点法では、関数の定義域の離散点を",
            color=GOLD, font_size=26, weight=BOLD,
        )
        key_point2 = Text(
            "状態ベクトルの一要素にのみ割り当てている",
            color=GOLD, font_size=26, weight=BOLD,
        )
        key_point1.shift(UP * 0.4)
        key_point2.next_to(key_point1, DOWN, buff=0.2)
        self.play(Write(key_point1), run_time=0.8)
        self.play(Write(key_point2), run_time=0.8)
        self.wait(0.5)

        recipe_lat = Text(
            "→ 固有関数は特殊な計算不要。固有ベクトルの各要素を、",
            color=TEAL, font_size=24,
        )
        recipe_lat2 = Text(
            "そのまま格子点上の値として割り当てるだけで良い",
            color=TEAL, font_size=24,
        )
        recipe_lat.shift(DOWN * 1.2)
        recipe_lat2.next_to(recipe_lat, DOWN, buff=0.2)
        self.play(Write(recipe_lat), run_time=0.8)
        self.play(Write(recipe_lat2), run_time=0.8)
        self.wait(0.7)

        recipe_eq = MathTex(
            r"\varphi_i(x_m) = (\boldsymbol{v}_i)_m",
            color=YELLOW, font_size=40,
        )
        recipe_eq.shift(DOWN * 2.6)
        recipe_eq_box = SurroundingRectangle(recipe_eq, color=YELLOW, buff=0.25)
        self.play(Write(recipe_eq), Create(recipe_eq_box), run_time=0.9)
        self.wait(1.4)

        self.play(
            FadeOut(diff_matrix_note1), FadeOut(diff_matrix_note2),
            FadeOut(key_point1), FadeOut(key_point2),
            FadeOut(recipe_lat), FadeOut(recipe_lat2),
            FadeOut(recipe_eq), FadeOut(recipe_eq_box),
        )
        self.wait(0.3)

        # ============================================================
        # Part 8: 比較についての注意
        # ============================================================
        subtitle8 = Text("比較についての注意", font_size=28, color=ORANGE)
        subtitle8.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle8), run_time=0.5)
        self.wait(0.4)

        cav1 = Text(
            "2つの手法は、いずれも近似で有限次元の線形代数に落としている",
            color=WHITE, font_size=26,
        )
        cav2 = Text(
            "→ 固有関数が厳密に等しいことは確認できない",
            color=WHITE, font_size=26,
        )
        cav1.shift(UP * 2.0)
        cav2.next_to(cav1, DOWN, buff=0.2)
        self.play(Write(cav1), run_time=0.8)
        self.play(Write(cav2), run_time=0.7)
        self.wait(0.6)

        cav3 = Text(
            "しかし、エルミート関数の次数をある程度取り、",
            color=GOLD, font_size=26,
        )
        cav4 = Text(
            "格子の刻み幅をある程度小さくすれば、傾向として比較できる",
            color=GOLD, font_size=26,
        )
        cav3.shift(UP * 0.4)
        cav4.next_to(cav3, DOWN, buff=0.2)
        self.play(Write(cav3), run_time=0.8)
        self.play(Write(cav4), run_time=0.8)
        self.wait(0.6)

        cav5 = Text(
            "固有関数はスカラ倍しても同値なので、値の絶対値の比較には意味がなく、",
            color=TEAL, font_size=26,
        )
        cav6 = Text(
            "プロットしたときの関数形（波形）を比較する",
            color=TEAL, font_size=26,
        )
        cav5.shift(DOWN * 1.2)
        cav6.next_to(cav5, DOWN, buff=0.2)
        self.play(Write(cav5), run_time=0.8)
        self.play(Write(cav6), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(cav1), FadeOut(cav2), FadeOut(cav3), FadeOut(cav4),
            FadeOut(cav5), FadeOut(cav6),
        )
        self.wait(0.3)

        # ============================================================
        # Part 9: 実際に固有関数を計算して比較
        # ============================================================
        subtitle9 = Text("固有関数の比較（OU 過程, γ=1, D=1）", font_size=28, color=YELLOW)
        subtitle9.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle9), run_time=0.5)
        self.wait(0.4)

        setup_text = Text(
            "エルミート関数：99次まで  /  格子点法：[-5, 5] を Δx=0.05 で離散化",
            color=WHITE, font_size=22,
        )
        setup_text.shift(DOWN * 2.7)
        self.play(Write(setup_text), run_time=0.9)
        self.wait(0.3)

        # ---- 数値計算 ----
        gamma_val = 1.0
        D_val = 1.0
        N_hermite = 100  # n = 0..99
        x_min, x_max, dx = -5.0, 5.0, 0.05
        x_grid = np.arange(x_min, x_max + dx / 2, dx)
        num_modes = 4

        x_plot = x_grid  # 同じグリッド上で描画
        modes_h = compute_eigenfunctions_hermite(
            N_hermite, gamma_val, D_val, x_plot, num_modes=num_modes,
        )
        modes_l = compute_eigenfunctions_lattice(
            x_grid, gamma_val, D_val, num_modes=num_modes,
        )

        # 正規化 & 符号をエルミート基準にそろえる
        h_curves_data = []
        l_curves_data = []
        eigvals_h = []
        eigvals_l = []
        for i in range(num_modes):
            lam_h, phi_h = modes_h[i]
            lam_l, phi_l = modes_l[i]
            phi_h_n = normalize_shape(phi_h, x_plot)
            phi_l_n = normalize_shape(phi_l, x_grid)
            # 格子点法の符号をエルミートに合わせる（波形比較のため）
            if float(np.trapezoid(phi_h_n * phi_l_n, x_grid)) < 0:
                phi_l_n = -phi_l_n
            h_curves_data.append(phi_h_n)
            l_curves_data.append(phi_l_n)
            eigvals_h.append(lam_h)
            eigvals_l.append(lam_l)

        # プロット用 y 範囲を決める
        all_vals = np.concatenate(h_curves_data + l_curves_data)
        ymax = float(np.max(np.abs(all_vals))) * 1.15
        y_lim = max(ymax, 1.2)
        y_lim = min(y_lim, 2.5)

        # 左右に分けて 2 つの Axes を用意する
        axes_h = Axes(
            x_range=[-5, 5, 2],
            y_range=[-y_lim, y_lim, y_lim / 2],
            x_length=5.6,
            y_length=4.2,
            axis_config={"color": WHITE, "include_tip": False, "stroke_width": 2},
        )
        axes_l = Axes(
            x_range=[-5, 5, 2],
            y_range=[-y_lim, y_lim, y_lim / 2],
            x_length=5.6,
            y_length=4.2,
            axis_config={"color": WHITE, "include_tip": False, "stroke_width": 2},
        )
        axes_h.shift(LEFT * 3.4 + DOWN * 0.3)
        axes_l.shift(RIGHT * 3.4 + DOWN * 0.3)

        xh_label = MathTex("x", color=WHITE, font_size=26).next_to(axes_h.x_axis.get_end(), RIGHT, buff=0.12)
        yh_label = MathTex(r"\varphi_i(x)", color=WHITE, font_size=26).next_to(axes_h.y_axis.get_end(), UP, buff=0.12)
        xl_label = MathTex("x", color=WHITE, font_size=26).next_to(axes_l.x_axis.get_end(), RIGHT, buff=0.12)
        yl_label = MathTex(r"\varphi_i(x)", color=WHITE, font_size=26).next_to(axes_l.y_axis.get_end(), UP, buff=0.12)

        title_h = Text("エルミート法", color=WHITE, font_size=22).next_to(axes_h, UP, buff=0.15).shift(LEFT*1.5)
        title_l = Text("格子点法", color=WHITE, font_size=22).next_to(axes_l, UP, buff=0.15).shift(LEFT*1.5)

        self.play(
            Create(axes_h), Create(axes_l),
            Write(xh_label), Write(yh_label),
            Write(xl_label), Write(yl_label),
            Write(title_h), Write(title_l),
            run_time=0.9,
        )

        mode_colors = [YELLOW, GREEN, BLUE, PURPLE]

        # 各モードごとに、左（エルミート）と右（格子点法）に同時に描く
        for i in range(num_modes):
            col = mode_colors[i]
            h_pts = [axes_h.c2p(x_plot[k], h_curves_data[i][k]) for k in range(len(x_plot))]
            h_curve = VMobject(color=col, stroke_width=3)
            h_curve.set_points_as_corners(h_pts)

            l_pts = [axes_l.c2p(x_grid[k], l_curves_data[i][k]) for k in range(len(x_grid))]
            l_curve = VMobject(color=col, stroke_width=3)
            l_curve.set_points_as_corners(l_pts)

            self.play(Create(h_curve), Create(l_curve), run_time=0.7)
            self.wait(0.3)

        # 凡例（モード番号と色の対応）
        legend_items = VGroup()
        for i, col in enumerate(mode_colors):
            item = VGroup(
                Line(ORIGIN, RIGHT * 0.35, color=col, stroke_width=3),
                MathTex(rf"\varphi_{i}", color=col, font_size=28),
            ).arrange(RIGHT, buff=0.15)
            legend_items.add(item)
        legend_items.arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        legend_items.to_edge(DOWN, buff=0.5).shift(LEFT * 0.0)
        # 画面下中央に配置
        legend_items.move_to(np.array([0.0, -1.5, 0.0]))
        self.play(FadeIn(legend_items), run_time=0.6)
        self.wait(1.5)

        conclusion = Text(
            "波形は概ね一致 → 固有関数は基底に依らず作用素 ℒ で決まる",
            color=GOLD, font_size=24, weight=BOLD,
        )
        conclusion.shift(DOWN * 3.2)
        self.play(FadeOut(legend_items), Write(conclusion), run_time=0.9)
        self.wait(2.0)

        # 全体クリア（まとめの前に、タイトルと subtitle 以外を消す）
        self.play(
            *[FadeOut(m) for m in self.mobjects
              if m not in (title, subtitle1)],
            run_time=1.0,
        )
        self.wait(0.3)

        # ============================================================
        # Part 10: まとめ
        # ============================================================
        subtitle10 = Text("まとめ", font_size=36, color=TEAL)
        subtitle10.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle10), run_time=0.6)
        self.wait(0.4)

        summary = VGroup(
            Text("• 空間を格子状に区切り、確率密度を格子点上の値ベクトル 𝐩(t) にする", color=WHITE, font_size=24),
            Text("• 差分（前進・後退・中心）で微分を近似 → 中心差分は精度が高い", color=WHITE, font_size=24),
            Text("• 微分の差分近似で作用素 ℒ が表現行列 L̃ になり、d𝐩/dt = L̃𝐩 に帰着", color=WHITE, font_size=24),
            Text("• 固有関数は L̃ の固有ベクトルの各要素をそのまま格子点上の値とすればよい", color=WHITE, font_size=24),
            Text("• エルミート法と格子点法で固有関数を比較すると波形が概ね一致", color=WHITE, font_size=24),
            Text("• → 固有関数は基底の取り方に依らず、作用素 ℒ 自身で決まると確認できた", color=WHITE, font_size=24),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        summary.shift(UP * 0.1)

        for row in summary:
            self.play(Write(row), run_time=0.6)
            self.wait(0.25)
        self.wait(2.0)

        self.play(
            FadeOut(VGroup(title, subtitle1, summary)),
            run_time=1.0,
        )
        self.wait(0.5)
