from manim import *
import numpy as np


class LagrangeMultipliersPCA(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        title = Text("ラグランジュの未定乗数法で解く主成分分析", font_size=36, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.7)

        # ============================================================
        # Part 1: 前回のおさらい
        # ============================================================
        subtitle1 = Text("前回のおさらい", font_size=28, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)

        recap_intro = Text(
            "主成分分析は以下の最適化問題に帰着できた",
            color=WHITE, font_size=26,
        )
        recap_intro.shift(UP * 1.8)
        self.play(Write(recap_intro), run_time=0.7)
        self.wait(0.5)

        # 最適化問題
        optimization_problem = VGroup(
            MathTex(
                r"\text{maximize}\quad f(\boldsymbol{w}) = \frac{1}{N}(X\boldsymbol{w})^{\top}(X\boldsymbol{w})",
                color=YELLOW,
                font_size=36,
            ),
            MathTex(
                r"\text{subject to}\quad g(\boldsymbol{w}) = \boldsymbol{w}^{\top}\boldsymbol{w} - 1 = 0",
                color=ORANGE,
                font_size=36,
            ),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        optimization_problem.shift(UP * 0.5)

        self.play(Write(optimization_problem[0]), run_time=0.8)
        self.wait(0.4)
        self.play(Write(optimization_problem[1]), run_time=0.8)
        self.wait(0.5)

        problem_note = VGroup(
            Text("f(w)：新しい軸での分散（最大化したい）", color=YELLOW, font_size=24),
            Text("制約条件：新軸は正規化されノルム１", color=ORANGE, font_size=24),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        problem_note.shift(DOWN * 1.2)

        for line in problem_note:
            self.play(Write(line), run_time=0.5)
            self.wait(0.2)

        question = Text(
            "この制約付き最適化問題をどう解く？",
            color=GREEN, font_size=26, weight=BOLD,
        )
        question.shift(DOWN * 2.3)
        self.play(Write(question), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(recap_intro), FadeOut(optimization_problem),
            FadeOut(problem_note), FadeOut(question), FadeOut(subtitle1),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: 最適性の幾何学的直観
        # ============================================================
        subtitle2 = Text("最適解の幾何学的イメージ（二次元で可視化）", font_size=28, color=GOLD)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2), run_time=0.6)

        # geometry_intro = Text(
        #     "2次元の空間で目的関数と制約条件を可視化する",
        #     color=WHITE, font_size=26,
        # )
        # geometry_intro.shift(UP * 2.2)
        # self.play(Write(geometry_intro), run_time=0.7)
        # self.wait(0.5)

        # 2次元平面上に等高線と制約曲線を描画
        axes = Axes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            x_length=5,
            y_length=5,
            axis_config={"color": GREY, "include_tip": False},
        ).scale(0.7)
        axes.shift(DOWN * 0.3 + LEFT * 3.5)

        # 円の中心と半径を計算（スケール後の座標系で）
        circle_center = axes.c2p(0, 0)
        point_on_circle = axes.c2p(1, 0)
        circle_radius_pixels = np.linalg.norm(point_on_circle - circle_center)

        # 制約条件 g(w) = w^T w - 1 = 0（単位円）
        constraint_circle = Circle(radius=circle_radius_pixels, color=ORANGE, stroke_width=4)
        constraint_circle.move_to(circle_center)
        constraint_label = MathTex(r"g(\boldsymbol{w})=0", color=ORANGE, font_size=32)
        constraint_label.next_to(constraint_circle, UP + LEFT, buff=0.1)

        # 目的関数の等高線（楕円状）
        contours = VGroup()
        for i, scale in enumerate([0.5, 0.8, 1.1, 1.4]):
            ellipse = Ellipse(
                width=circle_radius_pixels * scale * 2.5,
                height=circle_radius_pixels * scale * 1.5,
                color=BLUE,
                stroke_width=2,
                stroke_opacity=0.6,
            ).rotate(PI / 6)
            ellipse.move_to(circle_center)
            contours.add(ellipse)

        contour_label = MathTex(r"f(\boldsymbol{w})=\text{const}", color=BLUE, font_size=32)
        contour_label.next_to(contours[-1], RIGHT+DOWN, buff=0.1)

        self.play(Create(axes), run_time=0.5)
        self.play(Create(constraint_circle), Write(constraint_label), run_time=0.6)
        self.play(Create(contours), Write(contour_label), run_time=0.7)
        self.wait(0.8)

        # 最適点（制約の円上に確実に配置）
        optimal_angle = PI / 6  # 楕円の回転角と同じ
        optimal_point = circle_center + circle_radius_pixels * np.array([np.cos(optimal_angle), np.sin(optimal_angle), 0])
        optimal_dot = Dot(optimal_point, color=YELLOW, radius=0.08)
        optimal_label = MathTex(r"\boldsymbol{w}^*", color=YELLOW, font_size=30)
        optimal_label.next_to(optimal_dot, LEFT+DOWN, buff=0.15)

        self.play(Create(optimal_dot), Write(optimal_label), run_time=0.6)
        self.wait(0.5)

        # 説明文（右側）
        explanation1 = VGroup(
            Text("最適解w*では何が成り立つか", color=YELLOW, font_size=28, weight=BOLD),
        )
        explanation1.shift(RIGHT * 2.5 + UP * 1.5)
        self.play(Write(explanation1), run_time=0.6)
        self.wait(0.5)

        # 制約gの勾配と接線方向
        grad_g = Arrow(
            optimal_point,
            optimal_point + np.array([np.cos(optimal_angle), np.sin(optimal_angle), 0]) * 0.8,
            buff=0, color=RED, stroke_width=4,
        )
        grad_g_label = MathTex(r"\nabla_{\boldsymbol{w}} g", color=RED, font_size=30)
        grad_g_label.next_to(grad_g.get_end(), UP, buff=0.1)

        tangent_angle = optimal_angle + PI / 2
        tangent_vec = np.array([np.cos(tangent_angle), np.sin(tangent_angle), 0]) * 0.8
        tangent_arrow = Arrow(
            optimal_point - tangent_vec * 0.5,
            optimal_point + tangent_vec * 0.5,
            buff=0, color=TEAL, stroke_width=3,
        )
        tangent_label = MathTex(r"\boldsymbol{d}", color=TEAL, font_size=30)
        tangent_label.next_to(tangent_arrow.get_end(), UP + LEFT, buff=0.1)

        explanation2 = VGroup(
            Text("制約gの勾配∇gは制約曲線に垂直", color=RED, font_size=26),
            Text("接線方向dに進んでも制約は満たされる", color=TEAL, font_size=26),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        explanation2.next_to(explanation1, DOWN, buff=0.3, aligned_edge=LEFT)

        self.play(Create(grad_g), Write(grad_g_label), run_time=0.6)
        self.play(Write(explanation2[0]), run_time=0.5)
        self.wait(0.4)
        self.play(Create(tangent_arrow), Write(tangent_label), run_time=0.6)
        self.play(Write(explanation2[1]), run_time=0.5)
        self.wait(0.8)

        # 目的関数の勾配（最大化問題なので中心から外側へ）
        grad_f_angle = optimal_angle  # 最適点では勾配が制約の勾配と平行（同じ方向）
        grad_f = Arrow(
            optimal_point,
            optimal_point + np.array([np.cos(grad_f_angle), np.sin(grad_f_angle), 0]) * 0.6,
            buff=0, color=GREEN, stroke_width=4,
        )
        grad_f_label = MathTex(r"\nabla_{\boldsymbol{w}} f", color=GREEN, font_size=30)
        grad_f_label.next_to(grad_f.get_end(), DOWN + RIGHT, buff=0.1)

        explanation3 = VGroup(
            Text("ここで、もし∇fとdが直交していなければ…", color=WHITE, font_size=26),
            Text("→ d方向に進んでfをさらに大きくできる", color=YELLOW, font_size=24),
            Text("→ これは矛盾！よって∇fもdと直交する", color=GREEN, font_size=26),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        explanation3.next_to(explanation2, DOWN, buff=0.3, aligned_edge=LEFT)

        self.play(Create(grad_f), Write(grad_f_label), run_time=0.6)
        for line in explanation3:
            self.play(Write(line), run_time=0.5)
            self.wait(0.2)
        self.wait(0.8)

        conclusion_geometry = Text(
            "結論： ∇fと∇gは平行（最適性の必要条件）",
            color=YELLOW, font_size=28, weight=BOLD,
        )
        conclusion_geometry.shift(DOWN * 2.8)
        self.play(Write(conclusion_geometry), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(axes), FadeOut(constraint_circle),
            FadeOut(constraint_label), FadeOut(contours), FadeOut(contour_label),
            FadeOut(optimal_dot), FadeOut(optimal_label),
            FadeOut(grad_g), FadeOut(grad_g_label),
            FadeOut(tangent_arrow), FadeOut(tangent_label),
            FadeOut(grad_f), FadeOut(grad_f_label),
            FadeOut(explanation1), FadeOut(explanation2), FadeOut(explanation3),
            FadeOut(conclusion_geometry), FadeOut(subtitle2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: 最適性の1次の必要条件
        # ============================================================
        subtitle3 = Text("最適性の1次の必要条件", font_size=28, color=TEAL)
        subtitle3.next_to(title, DOWN)
        self.play(Write(subtitle3), run_time=0.6)

        condition_intro = Text(
            "2つの勾配が平行 ⇔ ある定数λで結べる",
            color=WHITE, font_size=26,
        )
        condition_intro.shift(UP * 1.8)
        self.play(Write(condition_intro), run_time=0.7)
        self.wait(0.5)

        # 必要条件の式
        necessary_condition = MathTex(
            r"\nabla_{\boldsymbol{w}} f(\boldsymbol{w}^*) - \lambda \nabla_{\boldsymbol{w}} g(\boldsymbol{w}^*) = \boldsymbol{0}",
            color=YELLOW,
            font_size=42,
        )
        necessary_condition.shift(UP * 0.8)
        necessary_box = SurroundingRectangle(necessary_condition, color=YELLOW, buff=0.2)

        self.play(Write(necessary_condition), run_time=0.8)
        self.play(Create(necessary_box), run_time=0.4)
        self.wait(0.7)
        
        name_note = Text(
            "これを「等式制約付き最適化問題における最適性の1次の必要条件」と呼ぶ",
            color=BLUE, font_size=24,
        )
        name_note.shift(DOWN * 0.5)
        self.play(Write(name_note), run_time=0.7)
        
        # 連立方程式
        system_intro = Text(
            "これと元の等式制約条件を連立して解けば,最適解w*とλが同時に求まる",
            color=WHITE, font_size=26,
        )
        system_intro.shift(DOWN * 1.3)
        self.play(Write(system_intro), run_time=0.6)
        self.wait(0.5)

        # system_equations = VGroup(
        #     MathTex(
        #         r"\nabla_{\boldsymbol{w}} f(\boldsymbol{w}^*) - \lambda \nabla_{\boldsymbol{w}} g(\boldsymbol{w}^*) = \boldsymbol{0}",
        #         color=GREEN,
        #         font_size=32,
        #     ),
        #     MathTex(
        #         r"g(\boldsymbol{w}^*) = 0",
        #         color=ORANGE,
        #         font_size=32,
        #     ),
        # ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        # system_equations.shift(DOWN * 2.5)

        # for eq in system_equations:
        #     self.play(Write(eq), run_time=0.6)
        #     self.wait(0.2)


        self.wait(1.5)

        self.play(
            FadeOut(condition_intro), FadeOut(necessary_condition), FadeOut(necessary_box),
            FadeOut(system_intro),  FadeOut(name_note), #FadeOut(system_equations),
            FadeOut(subtitle3),
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: ラグランジュの未定乗数法
        # ============================================================
        subtitle4 = Text("ラグランジュの未定乗数法", font_size=28, color=BLUE)
        subtitle4.next_to(title, DOWN)
        self.play(Write(subtitle4), run_time=0.6)

        lagrange_intro = Text(
            "以上の方法を一般化・体系化する",
            color=WHITE, font_size=26,
        )
        lagrange_intro.shift(UP * 2.0)
        self.play(Write(lagrange_intro), run_time=0.7)
        self.wait(0.5)

        # ラグラジアンの定義
        lagrangian_def = MathTex(
            r"L(\boldsymbol{w}, \boldsymbol{\lambda}) = f(\boldsymbol{w}) + \sum_{i=1}^{m} \lambda_i g_i(\boldsymbol{w})",
            color=YELLOW,
            font_size=38,
        )
        lagrangian_def.shift(UP * 0.9)
        lagrangian_label = Text("：ラグラジアン", color=YELLOW, font_size=24)
        lagrangian_label.next_to(lagrangian_def, RIGHT, buff=0.5)

        self.play(Write(lagrangian_def), run_time=0.8)
        self.play(Write(lagrangian_label), run_time=0.5)
        self.wait(0.6)

        # 最適性条件
        optimality_conditions = VGroup(
            MathTex(r"\nabla_{\boldsymbol{w}} L = \boldsymbol{0}", color=GREEN, font_size=36),
            MathTex(r"\nabla_{\boldsymbol{\lambda}} L = \boldsymbol{0}", color=ORANGE, font_size=36),
        ).arrange(DOWN, buff=0.3)
        optimality_conditions.shift(DOWN * 0.4)


        # λの名前
        lambda_name = VGroup(
            MathTex(r"\lambda_i", color=TEAL, font_size=32),
            Text("：ラグランジュ乗数", color=TEAL, font_size=26),
        ).arrange(RIGHT, buff=0.2)
        lambda_name.next_to(optimality_conditions, DOWN, buff=0.15)

        method_note = Text(
            "※ 複数の制約g₁, g₂, ...を許すため添字iを導入",
            color=GREY, font_size=22,
        )
        method_note.next_to(lambda_name, DOWN, buff=0.15)

        self.play(Write(lambda_name), run_time=0.6)
        self.play(Write(method_note), run_time=0.5)

        optimality_note = Text(
            "こうすると、所望の連立方程式が１つの目的関数を使って書き下せる",
            color=WHITE, font_size=24,
        )
        optimality_note.next_to(method_note, DOWN*2, buff=0.3)

        for eq in optimality_conditions:
            self.play(Write(eq), run_time=0.6)
            self.wait(0.2)
        self.play(Write(optimality_note), run_time=0.6)
        self.wait(0.7)

        self.wait(1.5)

        self.play(
            FadeOut(lagrange_intro), FadeOut(lagrangian_def), FadeOut(lagrangian_label),
            FadeOut(optimality_conditions), FadeOut(optimality_note),
            FadeOut(lambda_name), FadeOut(method_note), FadeOut(subtitle4),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: 主成分分析への適用（第一主成分）
        # ============================================================
        subtitle5 = Text("主成分分析の話に戻る", font_size=28, color=GOLD)
        subtitle5.next_to(title, DOWN)
        self.play(Write(subtitle5), run_time=0.6)

        pca_intro = Text(
            "第一主成分のラグラジアンを構成する",
            color=WHITE, font_size=26,
        )
        pca_intro.shift(UP * 2.0)
        self.play(Write(pca_intro), run_time=0.7)
        self.wait(0.5)

        # 第一主成分のラグラジアン
        L1_def = MathTex(
            r"L_1 = \frac{1}{N}(X\boldsymbol{w}_1)^{\top}(X\boldsymbol{w}_1) - \lambda_1(\boldsymbol{w}_1^{\top}\boldsymbol{w}_1 - 1)",
            color=YELLOW,
            font_size=36,
        )
        L1_def.shift(UP * 0.9)
        self.play(Write(L1_def), run_time=0.9)
        self.wait(0.6)

        # 微分して0
        derivative_note = Text(
            "これをw₁で微分して0とおく",
            color=WHITE, font_size=26,
        )
        derivative_note.shift(UP * 0.0)
        self.play(Write(derivative_note), run_time=0.6)
        self.wait(0.4)

        derivative_step = MathTex(
            r"\nabla_{\boldsymbol{w}_1} L_1 = \frac{2}{N}X^{\top}X\boldsymbol{w}_1 - 2\lambda_1\boldsymbol{w}_1 = \boldsymbol{0}",
            color=GREEN,
            font_size=34,
        )
        derivative_step.shift(DOWN * 0.8)
        self.play(Write(derivative_step), run_time=0.8)
        self.wait(0.6)

        # 式変形
        simplify_note = Text(
            "式を整理すると…",
            color=WHITE, font_size=26,
        )
        simplify_note.shift(DOWN * 1.6)
        self.play(Write(simplify_note), run_time=0.5)
        self.wait(0.3)

        eigen_eq1 = MathTex(
            r"\frac{1}{N}X^{\top}X\boldsymbol{w}_1 = \lambda_1\boldsymbol{w}_1",
            color=ORANGE,
            font_size=40,
        )
        eigen_eq1.shift(DOWN * 2.4)
        eigen_box1 = SurroundingRectangle(eigen_eq1, color=ORANGE, buff=0.2)

        self.play(Write(eigen_eq1), run_time=0.8)
        self.play(Create(eigen_box1), run_time=0.4)
        self.wait(0.5)

        eigen_note = Text(
            "固有値問題が自然に出現！",
            color=ORANGE, font_size=28, weight=BOLD,
        )
        eigen_note.shift(DOWN * 3.3)
        self.play(Write(eigen_note), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(subtitle5),
            FadeOut(pca_intro), FadeOut(L1_def), FadeOut(derivative_note),
            FadeOut(derivative_step), FadeOut(simplify_note),
            FadeOut(eigen_eq1), FadeOut(eigen_box1), FadeOut(eigen_note),
        )
        self.wait(0.3)

        # ============================================================
        # Part 6: 第二主成分
        # ============================================================
        subtitle6 = Text("第二主成分の導出", font_size=28, color=TEAL)
        subtitle6.next_to(title, DOWN)
        self.play(Write(subtitle6), run_time=0.6)

        pc2_intro = Text(
            "第二軸は第一軸に直交するという条件を追加",
            color=WHITE, font_size=26,
        )
        pc2_intro.shift(UP * 2.0)
        self.play(Write(pc2_intro), run_time=0.7)
        self.wait(0.5)

        # 第二主成分のラグラジアン
        L2_def = MathTex(
            r"L_2 = \frac{1}{N}(X\boldsymbol{w}_2)^{\top}(X\boldsymbol{w}_2) - \lambda_2(\boldsymbol{w}_2^{\top}\boldsymbol{w}_2 - 1) - \mu_2\boldsymbol{w}_1^{\top}\boldsymbol{w}_2",
            color=YELLOW,
            font_size=40,
        )
        L2_def.shift(UP * 0.8)
        self.play(Write(L2_def), run_time=1.0)
        self.wait(0.6)

        orthogonal_note = VGroup(
            MathTex(r"\boldsymbol{w}_1^{\top}\boldsymbol{w}_2 = 0", color=TEAL, font_size=28),
            Text("：軸同士の直交条件", color=TEAL, font_size=24),
        ).arrange(RIGHT, buff=0.2)
        orthogonal_note.shift(DOWN * 0.1)
        self.play(Write(orthogonal_note), run_time=0.6)
        self.wait(0.7)

        # 同様に展開
        expansion_note = Text(
            "同様にw₂で微分して式を展開すると…",
            color=WHITE, font_size=26,
        )
        expansion_note.shift(DOWN * 0.9)
        self.play(Write(expansion_note), run_time=0.6)
        self.wait(0.4)

        eigen_eq2 = MathTex(
            r"\frac{1}{N}X^{\top}X\boldsymbol{w}_2 = \lambda_2\boldsymbol{w}_2",
            color=ORANGE,
            font_size=44,
        )
        eigen_eq2.shift(DOWN * 1.8)
        eigen_box2 = SurroundingRectangle(eigen_eq2, color=ORANGE, buff=0.2)

        self.play(Write(eigen_eq2), run_time=0.8)
        self.play(Create(eigen_box2), run_time=0.4)
        self.wait(0.6)

        same_form = Text(
            "結局、同じ形の固有値問題に帰着される",
            color=GREEN, font_size=26,
        )
        same_form.shift(DOWN * 2.8)
        self.play(Write(same_form), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(pc2_intro), FadeOut(L2_def), FadeOut(orthogonal_note),
            FadeOut(expansion_note), FadeOut(eigen_eq2), FadeOut(eigen_box2),
            FadeOut(same_form), FadeOut(subtitle6),# FadeOut(subtitle5),
        )
        self.wait(0.3)

        # ============================================================
        # Part 7: 固有値の性質（実数性・非負性）
        # ============================================================
        subtitle7 = Text("固有値の性質", font_size=28, color=BLUE)
        subtitle7.next_to(title, DOWN)
        self.play(Write(subtitle7), run_time=0.6)

        concern_intro = Text(
            "ここで疑問：虚数や負の固有値が出ないか？",
            color=YELLOW, font_size=26, weight=BOLD,
        )
        concern_intro.shift(UP * 2.0)
        self.play(Write(concern_intro), run_time=0.7)
        self.wait(0.6)

        # 固有値が分散に対応
        variance_link = Text(
            "固有値λはデータの分散に対応するため、実数・非負であってほしい",
            color=WHITE, font_size=24,
        )
        variance_link.shift(UP * 1.3)
        self.play(Write(variance_link), run_time=0.7)
        self.wait(0.5)

        # 対称行列の性質
        property1_title = Text(
            "性質1：対称行列の固有値は必ず実数",
            color=TEAL, font_size=26, weight=BOLD,
        )
        property1_title.shift(UP * 0.5)
        self.play(Write(property1_title), run_time=0.6)
        self.wait(0.3)

        property1_detail = VGroup(
            MathTex(r"X^{\top}X", color=GREEN, font_size=32),
            Text("は対称行列", color=GREEN, font_size=24),
            MathTex(r"\Rightarrow", color=WHITE, font_size=28),
            Text("固有値は実数", color=GREEN, font_size=24),
        ).arrange(RIGHT, buff=0.2)
        property1_detail.shift(DOWN * 0.1)
        self.play(Write(property1_detail), run_time=0.7)
        self.wait(0.7)

        # 半正定値行列の性質
        property2_title = Text(
            "性質2：半正定値行列の固有値は非負",
            color=ORANGE, font_size=26, weight=BOLD,
        )
        property2_title.shift(DOWN * 0.9)
        self.play(Write(property2_title), run_time=0.6)
        self.wait(0.3)

        property2_detail = VGroup(
            MathTex(r"X^{\top}X", color=YELLOW, font_size=32),
            Text("は半正定値行列", color=YELLOW, font_size=24),
            MathTex(r"\Rightarrow", color=WHITE, font_size=28),
            Text("固有値≥0", color=YELLOW, font_size=24),
        ).arrange(RIGHT, buff=0.2)
        property2_detail.shift(DOWN * 1.5)
        self.play(Write(property2_detail), run_time=0.7)
        self.wait(0.7)

        # 結論
        conclusion_eigenvalue = Text(
            "よって、虚数や負の固有値は現れない！",
            color=GREEN, font_size=28, weight=BOLD,
        )
        conclusion_eigenvalue.shift(DOWN * 2.5)
        self.play(Write(conclusion_eigenvalue), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(concern_intro), FadeOut(variance_link),
            FadeOut(property1_title), FadeOut(property1_detail),
            FadeOut(property2_title), FadeOut(property2_detail),
            FadeOut(conclusion_eigenvalue), FadeOut(subtitle7),
        )
        self.wait(0.3)

        # ============================================================
        # Part 8: まとめ
        # ============================================================
        subtitle_end = Text("まとめ", font_size=36, color=GOLD, weight=BOLD)
        subtitle_end.next_to(title, DOWN)
        self.play(Write(subtitle_end), run_time=0.7)

        summary = VGroup(
            Text("1. 最適解では目的関数と制約の勾配が平行", color=WHITE, font_size=28),
            Text("2. ラグランジュの未定乗数法で制約付き最適化を解ける", color=WHITE, font_size=28),
            Text("3. 第一主成分：ラグラジアンを微分→固有値問題に帰着", color=WHITE, font_size=28),
            Text("4. 第二主成分以降：直交条件を追加→同様の固有値問題に", color=WHITE, font_size=28),
            Text("5. XᵀXの線形代数的な性質により固有値は実数・非負", color=YELLOW, font_size=28),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        summary.scale(0.90)
        summary.shift(DOWN * 0.4)

        for row in summary:
            self.play(Write(row), run_time=0.6)
            self.wait(0.15)

        self.wait(2)
        self.play(FadeOut(VGroup(title, subtitle_end, summary)), run_time=1.0)
        self.wait(0.5)
