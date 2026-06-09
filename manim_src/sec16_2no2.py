from manim import *
import numpy as np


class RegularizationForOverfitting(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        # タイトル
        title = Text("正則化による過学習の抑制", font_size=32, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)

        # ============================================================
        # Part 1: 導入
        # ============================================================
        subtitle1 = Text("学び過ぎを防ぐという発想", font_size=28, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.4)

        intro = VGroup(
            Text("過学習は、モデルがデータに合わせ過ぎることで起こる", color=WHITE, font_size=24),
            Text("特に、パラメータが多いと過度な調整が可能になりやすい", color=YELLOW, font_size=23),
            Text("そこで『パラメータに制限をかける』のが正則化の考え方", color=GREEN, font_size=23),
        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        intro.shift(UP * 0.8)

        self.play(Write(intro[0]), run_time=0.5)
        self.play(Write(intro[1]), run_time=0.5)
        self.play(Write(intro[2]), run_time=0.5)
        self.wait(0.5)

        methods = VGroup(
            Text("代表的な2つの方法", color=GOLD, font_size=26, weight=BOLD),
            VGroup(
                Text("① リッジ回帰（Ridge）", color=TEAL, font_size=25),
                Text("② ラッソ回帰（Lasso）", color=ORANGE, font_size=25),
            ).arrange(DOWN, buff=0.18, aligned_edge=LEFT),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        methods.shift(DOWN * 1.5)

        self.play(Write(methods[0]), run_time=0.4)
        self.play(Write(methods[1]), run_time=0.6)
        self.wait(1.2)

        self.play(FadeOut(intro), FadeOut(methods), FadeOut(subtitle1))
        self.wait(0.3)

        # ============================================================
        # Part 2: リッジ回帰
        # ============================================================
        subtitle2 = Text("① ある意味で学び過ぎを防ぐ方法：リッジ回帰", font_size=25, color=TEAL)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.4)

        ridge_idea = VGroup(
            Text("リッジ回帰では『重みは小さいほど望ましい』と決める", color=WHITE, font_size=24),
            Text("（※ただしこれは、" + "アート的に" + "決めたことであって、必ずしもそれがよいとは限らない）", color=GRAY, font_size=22),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        ridge_idea.shift(UP * 1.7)
        self.play(Write(ridge_idea), run_time=0.6)
        self.wait(0.3)

        ridge_cost = MathTex(
            r"J^{\mathrm{Ridge}}(\mathbf{w})"
            r"= (\mathbf{y}-X\mathbf{w})^\top(\mathbf{y}-X\mathbf{w})"
            r"+ \alpha\,\mathbf{w}^\top\mathbf{w}",
            color=YELLOW,
            font_size=34,
        )
        ridge_cost.shift(UP * 0.8)
        ridge_cost_box = SurroundingRectangle(ridge_cost, color=YELLOW, buff=0.18)

        alpha_note = VGroup(
            Text("正則化係数 ", color=WHITE, font_size=23),
            MathTex(r"\alpha", color=YELLOW, font_size=28),
            Text(" は正の実数（", color=WHITE, font_size=23),
            MathTex(r"\alpha > 0", color=YELLOW, font_size=28),
            Text("）", color=WHITE, font_size=23),
        ).arrange(RIGHT, buff=0.07)
        alpha_note.shift(DOWN * 0.05)

        self.play(Write(ridge_cost), Create(ridge_cost_box), run_time=0.8)
        self.play(Write(alpha_note), run_time=0.5)
        self.wait(0.4)

        ridge_sol_label = Text("このコストを最小化する解を最小二乗法で求めると：", color=WHITE, font_size=23)
        ridge_sol_label.shift(DOWN * 0.85 + LEFT * 3)
        ridge_sol = MathTex(
            r"\hat{\mathbf{w}} = (X^\top X + \alpha I)^{-1}X^\top\mathbf{y}",
            color=TEAL,
            font_size=36,
        )
        ridge_sol.shift(DOWN * 1.45)
        ridge_sol_box = SurroundingRectangle(ridge_sol, color=TEAL, buff=0.18)

        self.play(Write(ridge_sol_label), run_time=0.4)
        self.play(Write(ridge_sol), Create(ridge_sol_box), run_time=0.8)
        self.wait(0.8)

        self.play(
            FadeOut(ridge_idea), FadeOut(ridge_cost), FadeOut(ridge_cost_box),
            FadeOut(alpha_note), FadeOut(ridge_sol_label), FadeOut(ridge_sol), FadeOut(ridge_sol_box),
        )
        self.wait(0.2)

        # 行列成分での説明
        comp_title = Text("正則化の効果を線形代数的に考える", color=TEAL, font_size=25)
        comp_title.shift(UP * 1.8)
        self.play(Write(comp_title), run_time=0.5)
        self.wait(0.3)

        col_def = MathTex(
            r"X = [\tilde{\mathbf{x}}_1\;\tilde{\mathbf{x}}_2\;\cdots\;\tilde{\mathbf{x}}_D]",
            color=WHITE,
            font_size=31,
        )
        col_def.shift(UP * 1.2)

        comp_text = VGroup(
            MathTex(r"X^\top X + \alpha I", color=YELLOW, font_size=32),
            Text("を成分で書くと：", color=WHITE, font_size=24),
        ).arrange(RIGHT, buff=0.12)
        comp_text.shift(UP * 0.68)

        ridge_matrix = MathTex(
            r"\begin{bmatrix}"
            r"\tilde{\mathbf{x}}_1^\top\tilde{\mathbf{x}}_1+\alpha & \tilde{\mathbf{x}}_1^\top\tilde{\mathbf{x}}_2 & \cdots & \tilde{\mathbf{x}}_1^\top\tilde{\mathbf{x}}_D\\"
            r"\tilde{\mathbf{x}}_2^\top\tilde{\mathbf{x}}_1 & \tilde{\mathbf{x}}_2^\top\tilde{\mathbf{x}}_2+\alpha & \cdots & \tilde{\mathbf{x}}_2^\top\tilde{\mathbf{x}}_D\\"
            r"\vdots & \vdots & \ddots & \vdots\\"
            r"\tilde{\mathbf{x}}_D^\top\tilde{\mathbf{x}}_1 & \tilde{\mathbf{x}}_D^\top\tilde{\mathbf{x}}_2 & \cdots & \tilde{\mathbf{x}}_D^\top\tilde{\mathbf{x}}_D+\alpha"
            r"\end{bmatrix}",
            color=WHITE,
            font_size=30,
        )
        ridge_matrix.shift(DOWN * 0.55)

        indep_note_top = VGroup(
            MathTex(r"\tilde{\mathbf{x}}_1 = \tilde{\mathbf{x}}_2", color=ORANGE, font_size=32),
            Text("であっても、対角成分に", color=WHITE, font_size=26),
            MathTex(r"\alpha", color=YELLOW, font_size=32),
            Text("が加わるため、", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.08)
        indep_note_bottom = Text(
            "行・列の完全一致が崩れ、必ず逆行列を持つ（正定値行列になる）",
            color=GREEN,
            font_size=26,
        )
        indep_note = VGroup(indep_note_top, indep_note_bottom).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        indep_note.shift(DOWN * 2.0)
        indep_note.scale(0.9)

        self.play(Write(col_def), run_time=0.5)
        self.play(Write(comp_text), run_time=0.5)
        self.play(Write(ridge_matrix), run_time=0.9)
        self.play(Write(indep_note), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(comp_title), FadeOut(col_def), FadeOut(comp_text),
            FadeOut(ridge_matrix), FadeOut(indep_note), FadeOut(subtitle2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: ラッソ回帰
        # ============================================================
        subtitle3 = Text("② ある意味で本質を抜き出す方法：ラッソ回帰", font_size=25, color=ORANGE)
        subtitle3.next_to(title, DOWN)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.4)

        lasso_cost_label = Text("ラッソ回帰のコスト関数：", color=WHITE, font_size=24)
        lasso_cost_label.shift(UP * 1.65 + LEFT * 3.7)

        lasso_cost = MathTex(
            r"J^{\mathrm{Lasso}}(\mathbf{w})"
            r"= (\mathbf{y}-X\mathbf{w})^\top(\mathbf{y}-X\mathbf{w})"
            r"+ \alpha\sum_{d=1}^{D}|w_d|",
            color=YELLOW,
            font_size=33,
        )
        lasso_cost.shift(UP * 0.95)
        # lasso_box = SurroundingRectangle(lasso_cost, color=ORANGE, buff=0.18)

        self.play(Write(lasso_cost_label), run_time=0.4)
        self.play(Write(lasso_cost), run_time=0.8)
        self.wait(0.4)

        l1_explain = VGroup(
            Text("これは、ベクトルの各要素の絶対値の和を", color=WHITE, font_size=24),
            # MathTex(r"\|\mathbf{w}\|_1 = \sum_{d=1}^{D}|w_d|", color=ORANGE, font_size=30),
            Text(" を小さくするという気持ち", color=WHITE, font_size=24),
        ).arrange(RIGHT, buff=0.1)
        l1_explain.shift(UP * 0.1)

        lasso_points = VGroup(
            VGroup(
                Text("● ", color=GOLD, font_size=24),
                Text("重みの一部を 0 にしやすい（疎な解）", color=ORANGE, font_size=24),
            ).arrange(RIGHT, buff=0.05),
            VGroup(
                Text("● ", color=GOLD, font_size=24),
                Text("不要な特徴量をモデルから外す効果が期待できる", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.05),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        lasso_points.shift(DOWN * 1.35)

        self.play(Write(l1_explain), run_time=0.6)
        self.play(Write(lasso_points), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(lasso_cost_label), FadeOut(lasso_cost),
            FadeOut(l1_explain), FadeOut(lasso_points), FadeOut(subtitle3),
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: リッジ vs ラッソ（幾何学的説明）
        # ============================================================
        subtitle4 = Text("二次元重み空間で見る：等高線と制約", font_size=27, color=GOLD)
        subtitle4.next_to(title, DOWN)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.4)

        # 左: Ridge、右: Lasso
        ax_ridge = Axes(
            x_range=[-2.2, 2.2, 1], y_range=[-2.2, 2.2, 1],
            x_length=4.2, y_length=4.2,
            axis_config={"color": GRAY, "include_tip": True, "include_numbers": True},
        ).scale(0.84)
        ax_ridge.shift(LEFT * 3.25 + DOWN * 0.45)
        label_ridge = Text("Ridge（L2制約）", font_size=22, color=TEAL)
        label_ridge.next_to(ax_ridge, UP, buff=0.1)

        ax_lasso = Axes(
            x_range=[-2.2, 2.2, 1], y_range=[-2.2, 2.2, 1],
            x_length=4.2, y_length=4.2,
            axis_config={"color": GRAY, "include_tip": True, "include_numbers": True},
        ).scale(0.84)
        ax_lasso.shift(RIGHT * 2.65 + DOWN * 0.45)
        label_lasso = Text("Lasso（L1制約）", font_size=22, color=ORANGE)
        label_lasso.next_to(ax_lasso, UP, buff=0.1)

        ridge_xlab = MathTex(r"w_1", color=WHITE, font_size=20)
        ridge_xlab.next_to(ax_ridge.x_axis, RIGHT, buff=0.05)
        ridge_ylab = MathTex(r"w_2", color=WHITE, font_size=20)
        ridge_ylab.next_to(ax_ridge.y_axis, UP, buff=0.05)

        lasso_xlab = MathTex(r"w_1", color=WHITE, font_size=20)
        lasso_xlab.next_to(ax_lasso.x_axis, RIGHT, buff=0.05)
        lasso_ylab = MathTex(r"w_2", color=WHITE, font_size=20)
        lasso_ylab.next_to(ax_lasso.y_axis, UP, buff=0.05)

        self.play(
            Create(ax_ridge), Write(label_ridge), Write(ridge_xlab), Write(ridge_ylab),
            Create(ax_lasso), Write(label_lasso), Write(lasso_xlab), Write(lasso_ylab),
            run_time=0.8,
        )

        center = np.array([1.25, 1.15])

        def make_contour(ax, scale, color):
            return ParametricFunction(
                lambda t: ax.c2p(
                    center[0] + 1.05 * scale * np.cos(t),
                    center[1] + 0.65 * scale * np.sin(t),
                ),
                t_range=[0, TAU],
                color=color,
                stroke_width=2,
            )

        contours_ridge = VGroup(*[
            make_contour(ax_ridge, s, BLUE_B) for s in [0.7, 1.1, 1.5, 1.9]
        ])
        contours_lasso = VGroup(*[
            make_contour(ax_lasso, s, BLUE_B) for s in [0.7, 1.1, 1.5, 1.9]
        ])

        self.play(Create(contours_ridge), Create(contours_lasso), run_time=0.9)
        self.wait(0.3)

        # 制約集合
        r = 1.1
        ridge_constraint = ParametricFunction(
            lambda t: ax_ridge.c2p(r * np.cos(t), r * np.sin(t)),
            t_range=[0, TAU],
            color=TEAL,
            stroke_width=3,
        )
        ridge_constraint_label = MathTex(r"\|\mathbf{w}\|_2 \le c", color=TEAL, font_size=22)
        ridge_constraint_label.next_to(ax_ridge, DOWN, buff=0.08)

        lasso_constraint = Polygon(
            ax_lasso.c2p(0, r),
            ax_lasso.c2p(r, 0),
            ax_lasso.c2p(0, -r),
            ax_lasso.c2p(-r, 0),
            color=ORANGE,
            stroke_width=3,
        )
        lasso_constraint_label = MathTex(r"\|\mathbf{w}\|_1 \le c", color=ORANGE, font_size=22)
        lasso_constraint_label.next_to(ax_lasso, DOWN, buff=0.08)

        self.play(Create(ridge_constraint), Write(ridge_constraint_label), run_time=0.6)
        self.play(Create(lasso_constraint), Write(lasso_constraint_label), run_time=0.6)
        self.wait(0.4)

        ridge_dir = center / np.linalg.norm(center)
        ridge_opt = Dot(ax_ridge.c2p(r * ridge_dir[0], r * ridge_dir[1]), color=TEAL, radius=0.08)
        ridge_opt_label = MathTex(r"\hat{\mathbf{w}}_{\mathrm{ridge}}", color=TEAL, font_size=20)
        ridge_opt_label.next_to(ridge_opt, UR, buff=0.05)

        lasso_opt = Dot(ax_lasso.c2p(0.0, r), color=ORANGE, radius=0.08)
        lasso_opt_label = MathTex(r"\hat{\mathbf{w}}_{\mathrm{lasso}}", color=ORANGE, font_size=20)
        lasso_opt_label.next_to(lasso_opt, LEFT, buff=0.08)

        self.play(FadeIn(ridge_opt), Write(ridge_opt_label), run_time=0.5)
        self.play(FadeIn(lasso_opt), Write(lasso_opt_label), run_time=0.5)
        self.wait(0.4)

        geo_notes = VGroup(
            Text("ラッソの制約はひし形なので、等高線と軸上で接しやすい", color=ORANGE, font_size=23),
            Text("→ どれかの重みが 0 になりやすく、疎な解が生まれる", color=YELLOW, font_size=23),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        geo_notes.shift(DOWN * 2.95)

        self.play(Write(geo_notes), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(ax_ridge), FadeOut(label_ridge), FadeOut(ridge_xlab), FadeOut(ridge_ylab),
            FadeOut(ax_lasso), FadeOut(label_lasso), FadeOut(lasso_xlab), FadeOut(lasso_ylab),
            FadeOut(contours_ridge), FadeOut(contours_lasso),
            FadeOut(ridge_constraint), FadeOut(ridge_constraint_label),
            FadeOut(lasso_constraint), FadeOut(lasso_constraint_label),
            FadeOut(ridge_opt), FadeOut(ridge_opt_label),
            FadeOut(lasso_opt), FadeOut(lasso_opt_label),
            FadeOut(geo_notes), FadeOut(subtitle4),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: ラッソは本質を抜き出す
        # ============================================================
        subtitle5 = Text("ラッソが『本質を抜き出す』といえる理由", font_size=27, color=ORANGE)
        subtitle5.next_to(title, DOWN)
        self.play(Write(subtitle5), run_time=0.6)
        self.wait(0.4)

        sparse_explain = VGroup(
            Text("ラッソでは重みベクトルが疎（Sparse）になりがち", color=WHITE, font_size=25),
            MathTex(r"\hat{\mathbf{w}}_{\mathrm{lasso}} = [1.4,\;0,\;0.7,\;0,\;\ldots]^\top", color=ORANGE, font_size=32),
            Text("重み 0 の項は『最初からモデルに無かった』のと同じ", color=YELLOW, font_size=24),
            Text("=> 不要な特徴量を削ぎ落として、必要十分なモデルへ近づく", color=GREEN, font_size=24),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        sparse_explain.shift(DOWN * 0.2)

        self.play(Write(sparse_explain[0]), run_time=0.5)
        self.play(Write(sparse_explain[1]), run_time=0.6)
        self.play(Write(sparse_explain[2]), run_time=0.5)
        self.play(Write(sparse_explain[3]), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(sparse_explain), FadeOut(subtitle5))
        self.wait(0.3)

        # ============================================================
        # Part 6: まとめ
        # ============================================================
        subtitle_end = Text("まとめ", font_size=36, color=GOLD, weight=BOLD)
        subtitle_end.next_to(title, DOWN)
        self.play(Write(subtitle_end), run_time=0.7)
        self.wait(0.5)

        summary = VGroup(
            VGroup(
                Text("1.", color=GOLD, font_size=26, weight=BOLD),
                VGroup(
                    Text("リッジ回帰：", color=TEAL, font_size=28),
                    MathTex(
                        r"J^{\mathrm{Ridge}}(\mathbf{w})=(\mathbf{y}-X\mathbf{w})^\top(\mathbf{y}-X\mathbf{w})+\alpha\mathbf{w}^\top\mathbf{w}",
                        color=TEAL, font_size=30,
                    ),
                    Text("→ 重みを小さく抑えて過学習を和らげる", color=WHITE, font_size=26),
                ).arrange(DOWN, buff=0.06, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("2.", color=GOLD, font_size=26, weight=BOLD),
                VGroup(
                    Text("解は", color=WHITE, font_size=28),
                    MathTex(r"\hat{\mathbf{w}}=(X^\top X+\alpha I)^{-1}X^\top\mathbf{y}", color=TEAL, font_size=30),
                    Text("→ α>0 なら必ず正定値になり逆行列が存在する", color=WHITE, font_size=26),
                ).arrange(DOWN, buff=0.06, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("3.", color=GOLD, font_size=26, weight=BOLD),
                VGroup(
                    Text("ラッソ回帰：", color=ORANGE, font_size=28),
                    MathTex(
                        r"J^{\mathrm{Lasso}}(\mathbf{w})=(\mathbf{y}-X\mathbf{w})^\top(\mathbf{y}-X\mathbf{w})+\alpha\sum_{d=1}^{D}|w_d|",
                        color=ORANGE, font_size=30,
                    ),
                    Text("→ 重みが疎になり、本質的な特徴量を残しやすい", color=WHITE, font_size=28),
                ).arrange(DOWN, buff=0.06, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        summary.scale(0.9)
        summary.shift(DOWN * 0.45)

        for point in summary:
            self.play(Write(point), run_time=0.7)
            self.wait(0.25)

        self.wait(1.4)

        all_final = VGroup(summary, subtitle_end, title)
        self.play(FadeOut(all_final), run_time=1.0)
        self.wait(0.5)
