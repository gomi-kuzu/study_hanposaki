from manim import *
import numpy as np
import math


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


class FunctionTimeEvolutionSolver(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        title = Text("関数の時間発展の解き方", font_size=36, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.7)

        # ============================================================
        # Part 1: 前回の復習
        # ============================================================
        subtitle1 = Text("前回の復習", font_size=28, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.4)

        recap_text = Text(
            "22話では、確率密度関数の時間発展を線形作用素で表現した",
            color=WHITE, font_size=26,
        )
        recap_text.shift(UP * 1.8)
        self.play(Write(recap_text), run_time=0.8)
        self.wait(0.6)

        pde_eq = MathTex(
            r"\frac{\partial}{\partial t}p(\mathbf{x},t) = \mathcal{L}p(\mathbf{x},t)",
            color=YELLOW,
            font_size=42,
        )
        pde_eq.shift(UP * 0.7)
        pde_box = SurroundingRectangle(pde_eq, color=YELLOW, buff=0.3)
        self.play(Write(pde_eq), Create(pde_box), run_time=0.9)
        self.wait(0.8)

        general_sol = MathTex(
            r"p(\mathbf{x},t) = e^{\mathcal{L}t} p(\mathbf{x},0)",
            color=GREEN,
            font_size=36,
        )
        general_sol.shift(DOWN * 0.5)
        self.play(Write(general_sol), run_time=0.8)
        self.wait(0.6)

        today_text = Text(
            "今回は、この方程式を線形代数的に解く方法を紹介する",
            color=GOLD, font_size=26, weight=BOLD,
        )
        today_text.shift(DOWN * 1.8)
        self.play(Write(today_text), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(recap_text), FadeOut(pde_eq), FadeOut(pde_box),
            FadeOut(general_sol), FadeOut(today_text),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: 基底展開の考え方
        # ============================================================
        subtitle2 = Text("基底展開の考え方", font_size=28, color=GOLD)
        subtitle2.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle2), run_time=0.5)
        self.wait(0.4)

        recall_text = Text(
            "11話で見たように、抽象的な作用素は基底をとれば表現行列になる",
            color=WHITE, font_size=26,
        )
        recall_text.shift(UP * 1.8)
        self.play(Write(recall_text), run_time=0.8)
        self.wait(0.6)

        idea_text = Text(
            "関数空間に基底 |ψ₀⟩, |ψ₁⟩, ... をとって展開する",
            color=TEAL, font_size=26,
        )
        idea_text.shift(UP * 1.0)
        self.play(Write(idea_text), run_time=0.8)
        self.wait(0.6)

        expansion = MathTex(
            r"p(\mathbf{x},t) = c_0(t)|\psi_0\rangle + c_1(t)|\psi_1\rangle + c_2(t)|\psi_2\rangle + \cdots",
            color=YELLOW,
            font_size=34,
        )
        expansion.shift(UP * 0.1)
        exp_box = SurroundingRectangle(expansion, color=YELLOW, buff=0.25)
        self.play(Write(expansion), Create(exp_box), run_time=1.0)
        self.wait(0.8)

        basis_note = Text(
            "|ψₙ⟩: 基底関数（時間に依らない）",
            color=GREEN, font_size=22,
        )
        basis_note.shift(DOWN * 0.9)
        coeff_note = Text(
            "cₙ(t): 各基底に対応する係数（時間に依存）",
            color=ORANGE, font_size=22,
        )
        coeff_note.shift(DOWN * 1.4)
        self.play(Write(basis_note), Write(coeff_note), run_time=0.8)
        self.wait(1.0)

        key_text = Text(
            "時間発展の情報はすべて係数 cₙ(t) に押し込まれる！",
            color=GOLD, font_size=26, weight=BOLD,
        )
        key_text.shift(DOWN * 2.2)
        self.play(Write(key_text), run_time=0.8)
        self.wait(1.2)

        self.play(
            FadeOut(recall_text), FadeOut(idea_text),
            FadeOut(basis_note), FadeOut(coeff_note), FadeOut(key_text),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: 基底展開して微分方程式に持ち込む
        # ============================================================
        subtitle3 = Text("微分方程式に持ち込む", font_size=28, color=TEAL)
        subtitle3.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle3), run_time=0.5)
        self.wait(0.4)

        # 展開の式を上に移動
        self.play(
            expansion.animate.shift(UP * 1.5).scale(0.85),
            exp_box.animate.shift(UP * 1.5).scale(0.85),
            run_time=0.6,
        )
        self.wait(0.3)

        rhs_text = Text(
            "右辺：作用素 ℒ は表現行列 L に置き換わる",
            color=WHITE, font_size=24,
        )
        rhs_text.shift(UP * 0.5)
        self.play(Write(rhs_text), run_time=0.7)
        self.wait(0.5)

        lhs_text = Text(
            "左辺：|ψₙ⟩ は時間に依らないので、時間微分は係数にかかる",
            color=WHITE, font_size=24,
        )
        lhs_text.shift(DOWN * 0.1)
        self.play(Write(lhs_text), run_time=0.7)
        self.wait(0.4)

        lhs_eq = MathTex(
            r"\frac{\partial}{\partial t}p(\mathbf{x},t) = "
            r"\dot{c}_0(t)|\psi_0\rangle + \dot{c}_1(t)|\psi_1\rangle + \cdots",
            color=GREEN,
            font_size=30,
        )
        lhs_eq.shift(DOWN * 0.9)
        self.play(Write(lhs_eq), run_time=0.9)
        self.wait(0.8)

        self.play(FadeOut(rhs_text), FadeOut(lhs_text), FadeOut(lhs_eq))
        self.wait(0.2)

        result_text = Text(
            "全体としては、係数ベクトル 𝐜(t) についての行列方程式に帰着",
            color=WHITE, font_size=24,
        )
        result_text.shift(DOWN * 0.3)
        self.play(Write(result_text), run_time=0.8)
        self.wait(0.5)

        matrix_ode = MathTex(
            r"\frac{d}{dt}\mathbf{c}(t) = L\,\mathbf{c}(t)",
            color=YELLOW,
            font_size=48,
        )
        matrix_ode.shift(DOWN * 1.4)
        matrix_box = SurroundingRectangle(matrix_ode, color=YELLOW, buff=0.3)
        self.play(Write(matrix_ode), Create(matrix_box), run_time=1.0)
        self.wait(0.8)

        merit_text = Text(
            "偏微分方程式 → 有限次元の連立常微分方程式！",
            color=GOLD, font_size=26, weight=BOLD,
        )
        merit_text.shift(DOWN * 2.6)
        self.play(Write(merit_text), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(expansion), FadeOut(exp_box),
            FadeOut(result_text), FadeOut(matrix_ode), FadeOut(matrix_box),
            FadeOut(merit_text),
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: 具体例 -- オルンシュタイン・ウーレンベック過程
        # ============================================================
        subtitle4 = Text("具体例：オルンシュタイン・ウーレンベック過程", font_size=28, color=BLUE)
        subtitle4.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle4), run_time=0.5)
        self.wait(0.4)

        ou_intro = Text(
            "1次元のフォッカー・プランク方程式を考える",
            color=WHITE, font_size=26,
        )
        ou_intro.shift(UP * 1.8)
        self.play(Write(ou_intro), run_time=0.8)
        self.wait(0.5)

        ou_eq = MathTex(
            r"\frac{\partial}{\partial t}p(x,t) = "
            r"\gamma \frac{\partial}{\partial x}\bigl(x\,p(x,t)\bigr)"
            r"+ \frac{D}{2} \frac{\partial^2}{\partial x^2} p(x,t)",
            color=YELLOW,
            font_size=34,
        )
        ou_eq.shift(UP * 0.8)
        self.play(Write(ou_eq), run_time=1.0)
        self.wait(0.8)

        ou_params = MathTex(
            r"a(x) = -\gamma x, \qquad B(x) = \sqrt{D}",
            color=TEAL,
            font_size=30,
        )
        ou_params.shift(DOWN * 0.1)
        self.play(Write(ou_params), run_time=0.8)
        self.wait(0.6)

        ou_name = Text(
            "→ オルンシュタイン・ウーレンベック過程",
            color=GOLD, font_size=26, weight=BOLD,
        )
        ou_name.shift(DOWN * 0.8)
        self.play(Write(ou_name), run_time=0.7)
        self.wait(0.8)

        L_ou = MathTex(
            r"\mathcal{L} = "
            r"\gamma \frac{\partial}{\partial x} x"
            r"+ \frac{D}{2}\frac{\partial^2}{\partial x^2}",
            color=GREEN,
            font_size=32,
        )
        L_ou.shift(DOWN * 1.8)
        L_ou_box = SurroundingRectangle(L_ou, color=GREEN, buff=0.25)
        self.play(Write(L_ou), Create(L_ou_box), run_time=0.9)
        self.wait(1.2)

        self.play(
            FadeOut(ou_intro), FadeOut(ou_eq), FadeOut(ou_params),
            FadeOut(ou_name), FadeOut(L_ou), FadeOut(L_ou_box),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: エルミート関数を基底に採用
        # ============================================================
        subtitle5 = Text("基底：エルミート関数", font_size=28, color=GOLD)
        subtitle5.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle5), run_time=0.5)
        self.wait(0.4)

        hermite_intro = Text(
            "基底関数としてエルミート関数を用いる",
            color=WHITE, font_size=26,
        )
        hermite_intro.shift(UP * 1.9)
        self.play(Write(hermite_intro), run_time=0.7)
        self.wait(0.5)

        hermite_def = MathTex(
            r"\psi_n(x) = \left(2^n n! \sqrt{\pi}\right)^{-1/2} e^{-x^2/2} H_n(x)",
            color=YELLOW,
            font_size=34,
        )
        hermite_def.shift(UP * 1.0)
        self.play(Write(hermite_def), run_time=1.0)
        self.wait(0.6)

        hermite_note = Text(
            "Hₙ(x): 8話で登場したエルミート多項式",
            color=TEAL, font_size=22,
        )
        hermite_note.shift(UP * 0.3)
        self.play(Write(hermite_note), run_time=0.7)
        self.wait(0.7)

        # エルミート関数のグラフをプロット
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-0.8, 0.9, 0.4],
            x_length=8,
            y_length=3.2,
            axis_config={"color": WHITE, "include_tip": False, "stroke_width": 2},
        )
        axes.shift(DOWN * 1.8)
        x_label = MathTex("x", color=WHITE, font_size=28).next_to(axes.x_axis.get_end(), RIGHT, buff=0.15)
        y_label = MathTex(r"\psi_n(x)", color=WHITE, font_size=28).next_to(axes.y_axis.get_end(), UP, buff=0.15)

        self.play(
            FadeOut(hermite_note),
            Create(axes), Write(x_label), Write(y_label),
            run_time=0.9,
        )
        self.wait(0.3)

        colors = [YELLOW, GREEN, BLUE, PURPLE]
        graphs = VGroup()
        legend_items = VGroup()
        for n, col in enumerate(colors):
            graph = axes.plot(
                lambda x, n=n: hermite_function(n, x),
                x_range=[-3.8, 3.8],
                color=col,
                stroke_width=3,
            )
            graphs.add(graph)
            label = MathTex(rf"\psi_{n}", color=col, font_size=26)
            legend_items.add(label)

        legend_items.arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        legend_items.next_to(axes, RIGHT, buff=0.2).shift(LEFT * 0.5 + UP * 0.5)

        for graph, label in zip(graphs, legend_items):
            self.play(Create(graph), Write(label), run_time=0.7)

        self.wait(0.8)

        decay_note = Text(
            "原点から離れると 0 に近づく → 確率密度の表現に相性が良い",
            color=GOLD, font_size=24,
        )
        decay_note.to_edge(DOWN, buff=0.3)
        self.play(Write(decay_note), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(hermite_intro), FadeOut(hermite_def),
            FadeOut(axes), FadeOut(x_label), FadeOut(y_label),
            FadeOut(graphs), FadeOut(legend_items), FadeOut(decay_note),
        )
        self.wait(0.3)

        # ============================================================
        # Part 6: エルミート関数の性質
        # ============================================================
        subtitle6 = Text("エルミート関数の性質", font_size=28, color=TEAL)
        subtitle6.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle6), run_time=0.5)
        self.wait(0.4)

        prop_intro = Text(
            "エルミート関数は次の便利な漸化式を満たす",
            color=WHITE, font_size=26,
        )
        prop_intro.shift(UP * 1.9)
        self.play(Write(prop_intro), run_time=0.8)
        self.wait(0.5)

        diff_prop = MathTex(
            r"\frac{d}{dx}\psi_n(x) = \sqrt{\tfrac{n}{2}}\,\psi_{n-1}(x) - \sqrt{\tfrac{n+1}{2}}\,\psi_{n+1}(x)",
            color=YELLOW,
            font_size=32,
        )
        diff_prop.shift(UP * 0.9)
        self.play(Write(diff_prop), run_time=1.0)
        self.wait(0.7)

        mult_prop = MathTex(
            r"x\,\psi_n(x) = \sqrt{\tfrac{n}{2}}\,\psi_{n-1}(x) + \sqrt{\tfrac{n+1}{2}}\,\psi_{n+1}(x)",
            color=YELLOW,
            font_size=32,
        )
        mult_prop.shift(UP * 0.0)
        self.play(Write(mult_prop), run_time=1.0)
        self.wait(0.7)

        key_prop = Text(
            "微分や x 倍が、n のズレた基底の線形和で書ける！",
            color=GOLD, font_size=26, weight=BOLD,
        )
        key_prop.shift(DOWN * 1.0)
        self.play(Write(key_prop), run_time=0.8)
        self.wait(0.6)

        use_prop = Text(
            "→ この性質を使えば、微分方程式を基底展開できる",
            color=GREEN, font_size=24,
        )
        use_prop.shift(DOWN * 1.8)
        self.play(Write(use_prop), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(prop_intro), FadeOut(diff_prop), FadeOut(mult_prop),
            FadeOut(key_prop), FadeOut(use_prop),
        )
        self.wait(0.3)

        # ============================================================
        # Part 7: 展開結果
        # ============================================================
        subtitle7 = Text("展開結果", font_size=28, color=ORANGE)
        subtitle7.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle7), run_time=0.5)
        self.wait(0.4)

        result_intro = Text(
            "計算は割愛して、結果だけ確認する",
            color=WHITE, font_size=26,
        )
        result_intro.shift(UP * 1.9)
        self.play(Write(result_intro), run_time=0.7)
        self.wait(0.4)

        alpha_def = MathTex(
            r"\alpha_n = \frac{1}{2}\sqrt{n(n-1)}",
            color=TEAL,
            font_size=32,
        )
        alpha_def.shift(UP * 1.1)
        alpha_box = SurroundingRectangle(alpha_def, color=TEAL, buff=0.2)
        self.play(Write(alpha_def), Create(alpha_box), run_time=0.8)
        self.wait(0.6)

        drift_expand = MathTex(
            r"\frac{\partial}{\partial x}(x\psi_n(x)) = "
            r"\alpha_n \psi_{n-2}(x) + \tfrac{1}{2}\psi_n(x) - \alpha_{n+2}\psi_{n+2}(x)",
            color=GREEN,
            font_size=28,
        )
        drift_expand.shift(UP * 0.1)
        self.play(Write(drift_expand), run_time=1.0)
        self.wait(0.6)

        diff_expand = MathTex(
            r"\frac{\partial^2}{\partial x^2}\psi_n(x) = "
            r"\alpha_n \psi_{n-2}(x) + \left(-n-\tfrac{1}{2}\right)\psi_n(x) + \alpha_{n+2}\psi_{n+2}(x)",
            color=BLUE,
            font_size=28,
        )
        diff_expand.shift(DOWN * 0.7)
        self.play(Write(diff_expand), run_time=1.0)
        self.wait(0.8)

        combine_text = Text(
            "ドリフト項と拡散項を合わせて cₙ(t) の微分方程式が得られる",
            color=WHITE, font_size=24,
        )
        combine_text.shift(DOWN * 1.6)
        self.play(Write(combine_text), run_time=0.8)
        self.wait(0.6)

        cn_ode = MathTex(
            r"\frac{d}{dt}c_n(t) = ",
            r"\gamma \alpha_{n+2} c_{n+2}(t) + \tfrac{\gamma}{2} c_n(t) - \gamma \alpha_n c_{n-2}(t)",
            r"+ \tfrac{D\alpha_{n+2}}{2} c_{n+2}(t) + \tfrac{D}{2}\!\left(-n-\tfrac{1}{2}\right)\! c_n(t) + \tfrac{D\alpha_n}{2} c_{n-2}(t)",
            color=YELLOW,
            font_size=26,
        )
        cn_ode.shift(DOWN * 2.6)
        self.play(Write(cn_ode), run_time=1.2)
        self.wait(1.5)

        self.play(
            FadeOut(result_intro), FadeOut(alpha_def), FadeOut(alpha_box),
            FadeOut(drift_expand), FadeOut(diff_expand),
            FadeOut(combine_text), FadeOut(cn_ode),
        )
        self.wait(0.3)

        # ============================================================
        # Part 8: 行列方程式に帰着して一般解へ
        # ============================================================
        subtitle8 = Text("行列方程式に帰着", font_size=28, color=GOLD)
        subtitle8.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle8), run_time=0.5)
        self.wait(0.4)

        summarize_text = Text(
            "係数をまとめて表現行列 L にまとめると...",
            color=WHITE, font_size=26,
        )
        summarize_text.shift(UP * 1.9)
        self.play(Write(summarize_text), run_time=0.7)
        self.wait(0.5)

        final_ode = MathTex(
            r"\frac{d}{dt}\mathbf{c}(t) = L\,\mathbf{c}(t)",
            color=YELLOW,
            font_size=48,
        )
        final_ode.shift(UP * 0.6)
        final_box = SurroundingRectangle(final_ode, color=YELLOW, buff=0.3)
        self.play(Write(final_ode), Create(final_box), run_time=0.9)
        self.wait(0.8)

        sol_text = Text(
            "→ 21話と同じく、行列指数関数で一般解が書ける",
            color=GREEN, font_size=26,
        )
        sol_text.shift(DOWN * 0.4)
        self.play(Write(sol_text), run_time=0.8)
        self.wait(0.5)

        matrix_sol = MathTex(
            r"\mathbf{c}(t) = e^{L t}\,\mathbf{c}(0)",
            color=GREEN,
            font_size=40,
        )
        matrix_sol.shift(DOWN * 1.3)
        self.play(Write(matrix_sol), run_time=0.9)
        self.wait(1.0)

        # 注意点
        caveats_title = Text("注意点", color=ORANGE, font_size=26, weight=BOLD)
        caveats_title.shift(DOWN * 2.2 + LEFT * 4.5)
        self.play(Write(caveats_title), run_time=0.5)

        caveats = VGroup(
            Text("• エルミート関数の n は無限まで続く → 適当な次数で打ち切って近似", color=WHITE, font_size=22),
            Text("• 初期状態 p(x,0) を近似する 𝐜(0) をうまく選ぶ必要がある", color=WHITE, font_size=22),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        caveats.shift(DOWN * 3.0)
        for row in caveats:
            self.play(Write(row), run_time=0.7)
            self.wait(0.2)
        self.wait(1.5)

        self.play(
            FadeOut(summarize_text), FadeOut(final_ode), FadeOut(final_box),
            FadeOut(sol_text), FadeOut(matrix_sol),
            FadeOut(caveats_title), FadeOut(caveats),
        )
        self.wait(0.3)

        # ============================================================
        # Part 9: まとめ
        # ============================================================
        subtitle9 = Text("まとめ", font_size=36, color=TEAL)
        subtitle9.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle9), run_time=0.6)
        self.wait(0.4)

        summary = VGroup(
            Text("• 関数を基底展開 → 係数 cₙ(t) の常微分方程式に帰着", color=WHITE, font_size=26),
            Text("• 作用素 ℒ は表現行列 L になり、d𝐜/dt = L𝐜 が得られる", color=WHITE, font_size=26),
            Text("• 例：OU過程ではエルミート関数を基底に取ると相性が良い", color=WHITE, font_size=26),
            Text("• 一般解は行列指数関数：𝐜(t) = exp(Lt)𝐜(0)", color=WHITE, font_size=26),
            Text("• 実際に計算するには基底の打ち切りと初期条件の展開が必要", color=WHITE, font_size=26),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        summary.shift(UP * 0.3)

        for row in summary:
            self.play(Write(row), run_time=0.6)
            self.wait(0.25)
        self.wait(1.0)

        omit_note = Text(
            "※教科書の固有関数の話は割愛",
            color=GOLD, font_size=24, slant=ITALIC,
        )
        omit_note.shift(DOWN * 2.6)
        self.play(Write(omit_note), run_time=0.8)
        self.wait(2.0)

        self.play(
            FadeOut(VGroup(title, subtitle1, summary, omit_note)),
            run_time=1.0,
        )
        self.wait(0.5)
