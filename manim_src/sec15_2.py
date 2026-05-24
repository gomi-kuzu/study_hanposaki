from manim import *
import numpy as np

class PolynomialRegression(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        # タイトル
        title = Text("データを拡張して曲線に対応", font_size=32, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)

        # ============================================================
        # Part 1: 動機 ── 直線では合わないデータ
        # ============================================================
        subtitle1 = Text("直線回帰の限界：曲がったデータへの対応", font_size=28, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.4)

        # 2つの散布図を横に並べる
        ax_lin = Axes(
            x_range=[-0.5, 4.5, 1], y_range=[-1.5, 4.5, 1],
            x_length=4.2, y_length=3.2,
            axis_config={"color": GRAY, "include_tip": True},
        ).scale(0.85)
        ax_lin.shift(LEFT * 3.2 + DOWN * 0.7)

        ax_curve = Axes(
            x_range=[-0.5, 4.5, 1], y_range=[-1.5, 4.5, 1],
            x_length=4.2, y_length=3.2,
            axis_config={"color": GRAY, "include_tip": True},
        ).scale(0.85)
        ax_curve.shift(RIGHT * 2.3 + DOWN * 0.7)

        lin_title = Text("線形なデータ", font_size=22, color=TEAL)
        lin_title.next_to(ax_lin, UP, buff=0.15)
        curve_title = Text("非線形なデータ", font_size=22, color=ORANGE)
        curve_title.next_to(ax_curve, UP, buff=0.15)

        # 直線データ（ノイズ付き）
        np.random.seed(42)
        x_lin = np.array([0.3, 0.8, 1.2, 1.7, 2.1, 2.5, 2.9, 3.4, 3.8, 4.2])
        y_lin = 0.8 * x_lin + 0.3 + np.random.normal(0, 0.25, len(x_lin))

        lin_dots = VGroup(*[
            Dot(ax_lin.c2p(x, y), color=TEAL, radius=0.08)
            for x, y in zip(x_lin, y_lin)
        ])
        lin_fit = ax_lin.plot(lambda x: 0.8 * x + 0.3, x_range=[0, 4.2], color=YELLOW, stroke_width=2.5)

        # 非線形データ（4次多項式 + ノイズ）
        x_curve = np.array([0.3, 0.7, 1.1, 1.5, 1.9, 2.3, 2.7, 3.1, 3.5, 3.9])
        y_curve = (
            2.8
            - 0.55 * (x_curve - 2.0)**2
            + 0.08 * (x_curve - 2.0)**4
            + np.random.normal(0, 0.17, len(x_curve))
        )

        curve_dots = VGroup(*[
            Dot(ax_curve.c2p(x, y), color=ORANGE, radius=0.08)
            for x, y in zip(x_curve, y_curve)
        ])

        # 直線をあてはめたときのダメな例
        lin_bad_fit = ax_curve.plot(lambda x: 0.05 * x + 1.6, x_range=[0, 4.2], color=RED, stroke_width=2.5)

        self.play(Create(ax_lin), Write(lin_title), Create(ax_curve), Write(curve_title), run_time=0.6)
        self.play(FadeIn(lin_dots), FadeIn(curve_dots), run_time=0.5)
        self.wait(0.3)
        self.play(Create(lin_fit), run_time=0.5)
        self.wait(0.3)
        self.play(Create(lin_bad_fit), run_time=0.5)
        self.wait(0.4)

        bad_note = Text("直線では合わない！", color=RED, font_size=22, weight=BOLD)
        bad_note.next_to(ax_curve, DOWN, buff=0.15)
        self.play(Write(bad_note), run_time=0.4)
        self.wait(1.5)

        self.play(
            FadeOut(ax_lin), FadeOut(lin_title), FadeOut(lin_dots), FadeOut(lin_fit),
            FadeOut(ax_curve), FadeOut(curve_title), FadeOut(curve_dots), FadeOut(lin_bad_fit),
            FadeOut(bad_note),
            FadeOut(subtitle1),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: 多項式モデルの導入
        # ============================================================
        subtitle2 = Text("4次多項式モデルの導入", font_size=28, color=ORANGE)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.4)

        poly_intro = Text("4次の多項式でデータを表現してみる：", color=WHITE, font_size=23)
        poly_intro.shift(UP * 1.7)
        self.play(Write(poly_intro), run_time=0.5)
        self.wait(0.3)

        poly_model = MathTex(
            r"f^{(4)}(x) = w_0 + w_1 x + w_2 x^2 + w_3 x^3 + w_4 x^4",
            color=ORANGE, font_size=30
        )
        poly_model.shift(UP * 1.0)
        poly_model_box = SurroundingRectangle(poly_model, color=ORANGE, buff=0.15)
        self.play(Write(poly_model), Create(poly_model_box), run_time=0.8)
        self.wait(0.5)

        # 行ベクトル × 列ベクトルの形式
        vec_form_label = Text("これは行ベクトルと列ベクトルの積として：", color=WHITE, font_size=22)
        vec_form_label.shift(UP * 0.1)
        self.play(Write(vec_form_label), run_time=0.5)
        self.wait(0.3)

        vec_form = MathTex(
            r"f^{(4)}(x) = \begin{bmatrix} w_0 & w_1 & w_2 & w_3 & w_4 \end{bmatrix}"
            r"\begin{bmatrix} 1 \\ x \\ x^2 \\ x^3 \\ x^4 \end{bmatrix}",
            color=WHITE, font_size=26
        )
        vec_form.shift(DOWN * 0.9)
        self.play(Write(vec_form), run_time=0.8)
        self.wait(0.5)

        # 基底との対応
        basis_note = VGroup(
            Text("ここで２部で学んだ「単項式基底の張る関数空間」を思い出そう：", color=TEAL, font_size=21),
        )
        basis_note.shift(DOWN * 2.0)
        self.play(Write(basis_note), run_time=0.5)
        self.wait(0.3)

        basis_eq = VGroup(
            Text("すると、", color=WHITE, font_size=20),
            MathTex(r"\{|1\rangle,\ |x\rangle,\ |x^2\rangle,\ |x^3\rangle,\ |x^4\rangle\}", color=YELLOW, font_size=22),
            Text("が基底、", color=WHITE, font_size=20),
            MathTex(r"\mathbf{w}", color=YELLOW, font_size=22),
            Text("がその空間上の座標であることに気づく", color=WHITE, font_size=20),
        ).arrange(RIGHT, buff=0.1)
        basis_eq.shift(DOWN * 2.6)
        self.play(Write(basis_eq), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(poly_intro), FadeOut(poly_model), FadeOut(poly_model_box),
            FadeOut(vec_form_label), FadeOut(vec_form),
            FadeOut(basis_note), FadeOut(basis_eq),
            FadeOut(subtitle2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: 特徴量ベクトル φ(x) の導入
        # ============================================================
        subtitle3 = Text("特徴量ベクトル（基底関数）の導入", font_size=27, color=TEAL)
        subtitle3.next_to(title, DOWN)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.4)

        phi_intro = Text("列ベクトル部分をまとめて書こう：", color=WHITE, font_size=22)
        phi_intro.shift(UP * 1.7)
        self.play(Write(phi_intro), run_time=0.5)
        self.wait(0.3)

        phi_def = MathTex(
            r"\boldsymbol{\phi}(x) \equiv \begin{bmatrix} 1 \\ x \\ x^2 \\ x^3 \\ x^4 \end{bmatrix}"
            r"\in \mathbb{R}^{D+1}",
            color=TEAL, font_size=30
        )
        phi_def.shift(UP * 0.5)
        phi_def_box = SurroundingRectangle(phi_def, color=TEAL, buff=0.2)
        self.play(Write(phi_def), Create(phi_def_box), run_time=0.8)
        self.wait(0.5)

        phi_name_note = VGroup(
            Text("機械学習では", color=WHITE, font_size=22),
            MathTex(r"\boldsymbol{\phi}(x)", color=TEAL, font_size=26),
            Text("を", color=WHITE, font_size=22),
            Text("特徴量 / 基底関数", color=YELLOW, font_size=22, weight=BOLD),
            Text("などと呼ぶ", color=WHITE, font_size=22),
        ).arrange(RIGHT, buff=0.12)
        phi_name_note.shift(DOWN * 0.65)
        self.play(Write(phi_name_note), run_time=0.6)
        self.wait(0.4)

        phi_nonlinear = VGroup(
            Text("●", color=ORANGE, font_size=20),
            Text("x に対しては", color=WHITE, font_size=22),
            Text("非線形", color=ORANGE, font_size=22, weight=BOLD),
            Text("な写像（x → x², x³, …）", color=WHITE, font_size=22),
        ).arrange(RIGHT, buff=0.12)
        phi_nonlinear.shift(DOWN * 1.3)
        phi_linear = VGroup(
            Text("●", color=GREEN, font_size=20),
            Text("パラメータ", color=WHITE, font_size=22),
            MathTex(r"\mathbf{w}", color=YELLOW, font_size=24),
            Text("に対しては", color=WHITE, font_size=22),
            Text("線形", color=GREEN, font_size=22, weight=BOLD),
            Text("な式", color=WHITE, font_size=22),
        ).arrange(RIGHT, buff=0.12)
        phi_linear.shift(DOWN * 1.9)
        self.play(Write(phi_nonlinear), run_time=0.5)
        self.wait(0.2)
        self.play(Write(phi_linear), run_time=0.5)
        self.wait(0.5)

        # シンプルな表現
        simple_model = MathTex(
            r"f^{(4)}(x) = \mathbf{w}^\top \boldsymbol{\phi}(x)",
            color=YELLOW, font_size=36
        )
        simple_model.shift(DOWN * 2.75)
        simple_model_box = SurroundingRectangle(simple_model, color=YELLOW, buff=0.18)
        self.play(Write(simple_model), Create(simple_model_box), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(phi_intro), FadeOut(phi_def), FadeOut(phi_def_box),
            FadeOut(phi_name_note), FadeOut(phi_nonlinear), FadeOut(phi_linear),
            FadeOut(simple_model), FadeOut(simple_model_box),
            FadeOut(subtitle3),
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: x に非線形・パラメータに線形、双対性
        # ============================================================
        subtitle4 = Text("「パラメータに線形」の意味と双対性", font_size=27, color=GREEN)
        subtitle4.next_to(title, DOWN)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.4)

        dual_intro = VGroup(
            Text("同じモデル", color=WHITE, font_size=23),
            MathTex(r"f^{(4)}(x) = \mathbf{w}^\top \boldsymbol{\phi}(x)", color=YELLOW, font_size=26),
            Text("を2つの視点で見ると：", color=WHITE, font_size=23),
        ).arrange(RIGHT, buff=0.12)
        dual_intro.shift(UP * 1.7)
        self.play(Write(dual_intro), run_time=0.6)
        self.wait(0.4)

        dual_table = VGroup(
            # ヘッダー
            VGroup(
                Text("注目対称", color=GRAY, font_size=21, weight=BOLD),
                Text("解釈", color=GRAY, font_size=21, weight=BOLD),
            ).arrange(RIGHT, buff=0.6),
            Line(LEFT * 5, RIGHT * 5, color=GRAY, stroke_width=1),
            VGroup(
                Text("1", color=WHITE, font_size=21),
                MathTex(r"\mathbf{w}", color=YELLOW, font_size=23),
                Text("パラメータに線形なモデル", color=GREEN, font_size=21),
            ).arrange(RIGHT, buff=0.6),
            VGroup(
                Text("2", color=WHITE, font_size=21),
                MathTex(r"\boldsymbol{\phi}(x)", color=TEAL, font_size=23),
                Text("特徴量に線形なモデル", color=TEAL, font_size=21),
            ).arrange(RIGHT, buff=0.6),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        dual_table.shift(UP * 0.5)
        self.play(Write(dual_table), run_time=0.9)
        self.wait(0.5)

        dual_point = VGroup(
            Text("●", color=ORANGE, font_size=20),
            MathTex(r"\mathbf{w}", color=YELLOW, font_size=24),
            Text("と", color=WHITE, font_size=22),
            MathTex(r"\boldsymbol{\phi}(x)", color=TEAL, font_size=24),
            Text("は", color=WHITE, font_size=22),
            Text("双対な関係", color=ORANGE, font_size=22, weight=BOLD),
            Text("にある", color=WHITE, font_size=22),
        ).arrange(RIGHT, buff=0.12)
        dual_point.shift(DOWN * 0.8)
        self.play(Write(dual_point), run_time=0.5)
        self.wait(0.4)

        dual_insight = VGroup(
            Text("●重要なのは、非線形写像", color=WHITE, font_size=26),
            MathTex(r"\{\boldsymbol{\phi}(x)\}", color=WHITE, font_size=30),
            Text("により、入力空間の曲がった構造を、", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.12)
        dual_insight.shift(DOWN * 1.5)
        dual_insight2 = VGroup(
            Text("特徴量空間では線形モデルとして扱うことができるってこと", color=ORANGE, font_size=26),
        ).arrange(RIGHT, buff=0.12)
        dual_insight2.shift(DOWN * 2.0)
        self.play(Write(dual_insight), run_time=0.5)
        self.play(Write(dual_insight2), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(dual_intro), FadeOut(dual_table),
            FadeOut(dual_point), FadeOut(dual_insight), FadeOut(dual_insight2),
            FadeOut(subtitle4),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: 計画行列 Φ と最小二乗解
        # ============================================================
        subtitle5 = Text("計画行列 Φ と解析解", font_size=28, color=YELLOW)
        subtitle5.next_to(title, DOWN)
        self.play(Write(subtitle5), run_time=0.6)
        self.wait(0.4)

        design_intro = Text("N 個のデータに対して特徴量を縦に並べた行列を作る：", color=WHITE, font_size=22)
        design_intro.shift(UP * 1.7)
        self.play(Write(design_intro), run_time=0.5)
        self.wait(0.3)

        # 計画行列の定義
        design_matrix = MathTex(
            r"\Phi \equiv \begin{bmatrix}"
            r"\boldsymbol{\phi}(x_1)^\top \\"
            r"\boldsymbol{\phi}(x_2)^\top \\"
            r"\vdots \\"
            r"\boldsymbol{\phi}(x_N)^\top"
            r"\end{bmatrix}"
            r"= \begin{bmatrix}"
            r"1 & \phi_1(x_1) & \phi_2(x_1) & \cdots & \phi_M(x_1) \\"
            r"1 & \phi_1(x_2) & \phi_2(x_2) & \cdots & \phi_M(x_2) \\"
            r"\vdots & \vdots & \vdots & \ddots & \vdots \\"
            r"1 & \phi_1(x_N) & \phi_2(x_N) & \cdots & \phi_M(x_N)"
            r"\end{bmatrix}"
            r"\in \mathbb{R}^{N \times (M+1)}",
            color=WHITE, font_size=30
        )
        design_matrix.shift(UP * 0.3)
        self.play(Write(design_matrix), run_time=1.0)
        self.wait(0.5)

        design_name = VGroup(
            Text("この", color=WHITE, font_size=22),
            MathTex(r"\Phi", color=YELLOW, font_size=26),
            Text("を", color=WHITE, font_size=22),
            Text("計画行列", color=YELLOW, font_size=22, weight=BOLD),
            Text("（Design Matrix）と呼ぶ", color=WHITE, font_size=22),
        ).arrange(RIGHT, buff=0.12)
        design_name.shift(DOWN * 1.55)
        self.play(Write(design_name), run_time=0.5)
        self.wait(0.4)

        x_replace_note = VGroup(
            Text("前の動画の", color=WHITE, font_size=22),
            MathTex(r"X", color=TEAL, font_size=26),
            Text("が", color=WHITE, font_size=22),
            MathTex(r"\Phi", color=YELLOW, font_size=26),
            Text("に置き換わるだけ！", color=GREEN, font_size=22, weight=BOLD),
        ).arrange(RIGHT, buff=0.12)
        x_replace_note.shift(DOWN * 2.1)
        self.play(Write(x_replace_note), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(design_intro), FadeOut(design_matrix),
            FadeOut(design_name), FadeOut(x_replace_note),
        )
        self.wait(0.2)

        # 最小二乗解
        lsq_title = Text("最小二乗解はそのまま適用できる！", color=GREEN, font_size=24, weight=BOLD)
        lsq_title.shift(UP * 1.7)
        self.play(Write(lsq_title), run_time=0.5)
        self.wait(0.3)

        cost_phi = MathTex(
            r"J(\mathbf{w}) = (\mathbf{y} - \Phi\mathbf{w})^\top (\mathbf{y} - \Phi\mathbf{w})",
            color=ORANGE, font_size=28
        )
        cost_phi.shift(UP * 0.9)
        self.play(Write(cost_phi), run_time=0.6)
        self.wait(0.3)

        arrow_down = MathTex(r"\Downarrow", color=WHITE, font_size=32)
        arrow_down.shift(UP * 0.2)
        same_method = Text("前回と全く同じ手順（偏微分=0）で解くと…", color=WHITE, font_size=22)
        same_method.shift(DOWN * 0.3)
        self.play(Write(arrow_down), Write(same_method), run_time=0.5)
        self.wait(0.3)

        solution_phi = MathTex(
            r"\hat{\mathbf{w}} = (\Phi^\top \Phi)^{-1} \Phi^\top \mathbf{y}",
            color=YELLOW, font_size=40
        )
        solution_phi.shift(DOWN * 1.3)
        solution_phi_box = SurroundingRectangle(solution_phi, color=YELLOW, buff=0.22)
        self.play(Write(solution_phi), Create(solution_phi_box), run_time=0.8)
        self.wait(0.5)

        phi_vs_x = VGroup(
            VGroup(
                Text("前回：", color=WHITE, font_size=21),
                MathTex(
                    r"\hat{\mathbf{w}} = (X^\top X)^{-1} X^\top \mathbf{y}",
                    color=GRAY, font_size=23
                ),
                Text("　（", color=WHITE, font_size=21),
                MathTex(r"X", color=TEAL, font_size=23),
                Text("はデータ行列）", color=WHITE, font_size=21),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("今回：", color=WHITE, font_size=21),
                MathTex(
                    r"\hat{\mathbf{w}} = (\Phi^\top \Phi)^{-1} \Phi^\top \mathbf{y}",
                    color=YELLOW, font_size=23
                ),
                Text("　（", color=WHITE, font_size=21),
                MathTex(r"\Phi", color=YELLOW, font_size=23),
                Text("は計画行列）", color=WHITE, font_size=21),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        phi_vs_x.shift(DOWN * 2.7)
        self.play(Write(phi_vs_x), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(lsq_title), FadeOut(cost_phi),
            FadeOut(arrow_down), FadeOut(same_method),
            FadeOut(solution_phi), FadeOut(solution_phi_box),
            FadeOut(phi_vs_x),
            FadeOut(subtitle5),
        )
        self.wait(0.3)

        # ============================================================
        # Part 6: 視覚的デモ ── 曲線フィッティングのイメージ
        # ============================================================
        subtitle6 = Text("多項式フィッティングの視覚的イメージ", font_size=27, color=ORANGE)
        subtitle6.next_to(title, DOWN)
        self.play(Write(subtitle6), run_time=0.6)
        self.wait(0.4)

        ax_demo = Axes(
            x_range=[-0.3, 4.3, 1], y_range=[-0.5, 4.5, 1],
            x_length=6.5, y_length=4.5,
            axis_config={"color": GRAY, "include_tip": True},
            x_axis_config={"include_numbers": True},
        ).scale(0.82)
        ax_demo.shift(DOWN * 0.6)

        x_ax_label = ax_demo.get_x_axis_label(MathTex(r"x", font_size=24), direction=RIGHT)
        y_ax_label = ax_demo.get_y_axis_label(MathTex(r"y", font_size=24), direction=UP)

        # トイデータ（4次多項式 + ノイズ）
        np.random.seed(7)
        x_data = np.linspace(0.2, 4.0, 12)
        y_true = 2.8 - 0.55 * (x_data - 2.0)**2 + 0.08 * (x_data - 2.0)**4
        y_data = y_true + np.random.normal(0, 0.17, len(x_data))

        data_dots = VGroup(*[
            Dot(ax_demo.c2p(x, y), color=ORANGE, radius=0.09)
            for x, y in zip(x_data, y_data)
        ])

        self.play(Create(ax_demo), Write(x_ax_label), Write(y_ax_label), run_time=0.5)
        self.play(FadeIn(data_dots), run_time=0.5)
        self.wait(0.3)

        # 直線フィット（悪い例）
        bad_line = ax_demo.plot(lambda x: 0.1 * x + 1.8, x_range=[0, 4.2], color=RED, stroke_width=2.5)
        bad_label = Text("直線（1次）：合わない", color=RED, font_size=20)
        bad_label.to_corner(UR).shift(DOWN * 1.5 + LEFT * 0.3)
        self.play(Create(bad_line), Write(bad_label), run_time=0.6)
        self.wait(0.7)

        # 4次多項式フィット（良い例）
        # 4次多項式でのフィット曲線
        good_curve = ax_demo.plot(
            lambda x: 2.8 - 0.55 * (x - 2.0)**2 + 0.08 * (x - 2.0)**4,
            x_range=[0, 4.2], color=YELLOW, stroke_width=3
        )
        good_label = Text("4次多項式：よく合う！", color=YELLOW, font_size=20)
        good_label.next_to(bad_label, DOWN, buff=0.3)
        self.play(Create(good_curve), Write(good_label), run_time=0.7)
        self.wait(0.8)

        # φ(x) の矢印と注釈
        phi_arrow = Arrow(
            ax_demo.c2p(1.0, 3.2), ax_demo.c2p(1.5, 2.8),
            color=TEAL, buff=0.05, stroke_width=2, max_tip_length_to_length_ratio=0.25
        )
        phi_note = MathTex(
            r"\boldsymbol{\phi}(x)=\begin{bmatrix}1\\x\\x^2\\x^3\\x^4\end{bmatrix}",
            color=TEAL, font_size=20
        )
        phi_note.move_to(ax_demo.c2p(0.5, 3.7))
        self.play(Create(phi_arrow), Write(phi_note), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(ax_demo), FadeOut(x_ax_label), FadeOut(y_ax_label),
            FadeOut(data_dots), FadeOut(bad_line), FadeOut(bad_label),
            FadeOut(good_curve), FadeOut(good_label),
            FadeOut(phi_arrow), FadeOut(phi_note),
            FadeOut(subtitle6),
        )
        self.wait(0.3)

        # ============================================================
        # Part 7: まとめ
        # ============================================================
        subtitle_end = Text("まとめ", font_size=36, color=GOLD, weight=BOLD)
        subtitle_end.next_to(title, DOWN)
        self.play(Write(subtitle_end), run_time=0.7)
        self.wait(0.5)

        summary = VGroup(
            VGroup(
                Text("1.", color=GOLD, font_size=26, weight=BOLD),
                VGroup(
                    Text("曲がったデータには直線回帰では不十分", color=WHITE, font_size=23),
                    Text("→ 多項式などの非線形モデルが必要", color=ORANGE, font_size=22),
                ).arrange(DOWN, buff=0.08, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("2.", color=GOLD, font_size=26, weight=BOLD),
                VGroup(
                    Text("特徴量ベクトル（基底関数）φ(x) の導入", color=WHITE, font_size=23),
                    MathTex(
                        r"\boldsymbol{\phi}(x) = [1,\ x,\ x^2,\ \ldots,\ x^D]^\top",
                        color=TEAL, font_size=22
                    ),
                    Text("x に非線形、パラメータ w に線形（双対な関係）", color=TEAL, font_size=21),
                ).arrange(DOWN, buff=0.08, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("3.", color=GOLD, font_size=26, weight=BOLD),
                VGroup(
                    Text("シンプルなモデル表現：", color=WHITE, font_size=23),
                    MathTex(
                        r"f^{(D)}(x) = \mathbf{w}^\top \boldsymbol{\phi}(x)",
                        color=YELLOW, font_size=24
                    ),
                ).arrange(DOWN, buff=0.08, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("4.", color=GOLD, font_size=26, weight=BOLD),
                VGroup(
                    Text("計画行列 Φ を使えば解析解もそのまま：", color=WHITE, font_size=23),
                    MathTex(
                        r"\hat{\mathbf{w}} = (\Phi^\top \Phi)^{-1} \Phi^\top \mathbf{y}",
                        color=YELLOW, font_size=24
                    ),
                    Text("（X → Φ に置き換えるだけ！）", color=GREEN, font_size=21, weight=BOLD),
                ).arrange(DOWN, buff=0.08, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        summary.scale(0.88)
        summary.shift(DOWN * 0.3)

        for point in summary:
            self.play(Write(point), run_time=0.7)
            self.wait(0.3)

        self.wait(1.5)

        all_final = VGroup(summary, subtitle_end, title)
        self.play(FadeOut(all_final), run_time=1.0)
        self.wait(0.5)
