from manim import *
import numpy as np
from numpy.polynomial.polynomial import Polynomial


class OverfittingAndRank(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        # タイトル
        title = Text("最小二乗法の諸問題", font_size=32, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)

        # ============================================================
        # Part 1: 過学習の視覚的デモ
        # ============================================================
        subtitle1 = Text("表現力が高いほどよいとは限らない", font_size=28, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.4)

        # トイデータ生成（端点が疎、中間が密の14点）
        np.random.seed(42)
        x_data = np.array([
            0.1, 0.5,
            1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8,
            3.5, 4.0
        ])
        y_true = 1.5 + 1.5 * np.sin(x_data * 1.2)
        y_data = y_true + np.random.normal(0, 0.15, len(x_data))

        # 4次・13次多項式フィット（数値安定な実装）
        poly4  = Polynomial.fit(x_data, y_data, 4)
        poly13 = Polynomial.fit(x_data, y_data, 13)

        # 左：4次多項式、右：13次多項式
        ax_l = Axes(
            x_range=[-0.1, 4.4, 1], y_range=[-0.5, 4.2, 1],
            x_length=4.8, y_length=3.5,
            axis_config={"color": GRAY, "include_tip": True},
        ).scale(0.82)
        ax_l.shift(LEFT * 3.2 + DOWN * 0.9)

        ax_r = Axes(
            x_range=[-0.1, 4.4, 1], y_range=[-0.5, 4.2, 1],
            x_length=4.8, y_length=3.5,
            axis_config={"color": GRAY, "include_tip": True},
        ).scale(0.82)
        ax_r.shift(RIGHT * 2.4 + DOWN * 0.9)

        label_l = Text("4次多項式モデル", font_size=21, color=YELLOW)
        label_l.next_to(ax_l, UP, buff=0.1)
        label_r = Text("13次多項式モデル", font_size=21, color=RED)
        label_r.next_to(ax_r, UP+RIGHT*0.02, buff=0.1)

        dots_l = VGroup(*[
            Dot(ax_l.c2p(x, y), color=ORANGE, radius=0.08)
            for x, y in zip(x_data, y_data)
        ])
        dots_r = VGroup(*[
            Dot(ax_r.c2p(x, y), color=ORANGE, radius=0.08)
            for x, y in zip(x_data, y_data)
        ])

        curve4 = ax_l.plot(
            lambda x: float(poly4(x)),
            x_range=[0.0, 4.1, 0.05], color=YELLOW, stroke_width=2.5
        )
        curve13 = ax_r.plot(
            lambda x: float(poly13(x)),
            x_range=[0.0, 4.0, 0.005], color=RED, stroke_width=2.5
        )

        self.play(Create(ax_l), Write(label_l), Create(ax_r), Write(label_r), run_time=0.7)
        self.play(FadeIn(dots_l), FadeIn(dots_r), run_time=0.5)
        self.wait(0.3)
        self.play(Create(curve4), run_time=0.8)
        self.wait(0.3)
        self.play(Create(curve13), run_time=0.9)
        self.wait(0.5)

        note4 = Text("データになめらかに\nフィットしている", color=YELLOW, font_size=19)
        note4.next_to(ax_l, DOWN, buff=0.1)
        note13 = Text("データが少ない区間で\n動きが激しい！", color=RED, font_size=19)
        note13.next_to(ax_r, DOWN, buff=0.1)
        self.play(Write(note4), Write(note13), run_time=0.5)
        self.wait(2.0)

        self.play(
            FadeOut(ax_l), FadeOut(label_l), FadeOut(dots_l), FadeOut(curve4), FadeOut(note4),
            FadeOut(ax_r), FadeOut(label_r), FadeOut(dots_r), FadeOut(curve13), FadeOut(note13),
            FadeOut(subtitle1),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: 過学習と汎化能力
        # ============================================================
        subtitle2 = Text("過学習（過適合）と汎化能力", font_size=28, color=ORANGE)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.4)

        overfit_lead = Text("訓練データに過度にフィッティングしてしまうことを", color=WHITE, font_size=25)
        overfit_lead.shift(UP * 1.8)
        self.play(Write(overfit_lead), run_time=0.5)

        overfit_terms = VGroup(
            Text("過学習", color=RED, font_size=34, weight=BOLD),
            Text("（overfitting）または", color=WHITE, font_size=26),
            Text("過適合", color=RED, font_size=34, weight=BOLD),
            Text("と呼ぶ", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.15)
        overfit_terms.shift(UP * 1.1)
        overfit_terms_box = SurroundingRectangle(overfit_terms, color=RED, buff=0.15)
        self.play(Write(overfit_terms), Create(overfit_terms_box), run_time=0.7)
        self.wait(0.4)

        gen_lead = Text("一方、未知のデータに対しても対応できる能力を", color=WHITE, font_size=25)
        gen_lead.shift(UP * 0.2)
        self.play(Write(gen_lead), run_time=0.5)

        gen_term = VGroup(
            Text("汎化能力", color=GREEN, font_size=34, weight=BOLD),
            Text("（generalization）と呼ぶ", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.15)
        gen_term.shift(DOWN * 0.5)
        gen_box = SurroundingRectangle(gen_term, color=GREEN, buff=0.15)
        self.play(Write(gen_term), Create(gen_box), run_time=0.6)
        self.wait(0.5)

        pts = VGroup(
            VGroup(
                Text("● ", color=GOLD, font_size=24),
                Text("汎化能力が高いほど実用上役に立つことが多い", color=WHITE, font_size=25),
            ).arrange(RIGHT, buff=0.05),
            VGroup(
                Text("● ", color=GOLD, font_size=24),
                Text("機械学習の学習手法を評価する大きな指標の一つ", color=YELLOW, font_size=25),
            ).arrange(RIGHT, buff=0.05),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        pts.shift(DOWN * 1.8)
        self.play(Write(pts), run_time=0.7)
        self.wait(2.0)

        self.play(
            FadeOut(overfit_lead), FadeOut(overfit_terms), FadeOut(overfit_terms_box),
            FadeOut(gen_lead), FadeOut(gen_term), FadeOut(gen_box),
            FadeOut(pts),
            FadeOut(subtitle2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: X^TXの逆行列問題
        # ============================================================
        subtitle3 = Text("もう一つの問題：逆行列が存在しない場合", font_size=28, color=TEAL)
        subtitle3.next_to(title, DOWN)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.4)

        recall_text = Text("前回求めた最小二乗解を思い出そう：", color=WHITE, font_size=24)
        recall_text.shift(UP * 1.6)
        self.play(Write(recall_text), run_time=0.5)
        self.wait(0.3)

        lsq_sol = MathTex(
            r"\hat{\mathbf{w}} = (X^\top X)^{-1} X^\top \mathbf{y}",
            color=YELLOW, font_size=38
        )
        lsq_sol.shift(UP * 0.8)
        lsq_box = SurroundingRectangle(lsq_sol, color=YELLOW, buff=0.2)
        self.play(Write(lsq_sol), Create(lsq_box), run_time=0.7)
        self.wait(0.4)

        prob_text = VGroup(
            Text("問題：", color=ORANGE, font_size=26, weight=BOLD),
            MathTex(r"X^\top X", color=TEAL, font_size=30),
            Text("は逆行列を", color=WHITE, font_size=26),
            Text("常に持つとは限らない！", color=RED, font_size=26, weight=BOLD),
        ).arrange(RIGHT, buff=0.12)
        prob_text.shift(DOWN * 0.1)
        self.play(Write(prob_text), run_time=0.6)
        self.wait(0.5)

        prob_highlight = SurroundingRectangle(prob_text[-1], color=RED, buff=0.1)
        self.play(Create(prob_highlight), run_time=0.4)
        self.wait(0.5)

        intro_rank = Text("逆行列の存在条件を理解するために", color=WHITE, font_size=25)
        intro_rank.shift(DOWN * 1.3)
        intro_rank2 = VGroup(
            Text("「行列のランク（階数）」", color=GREEN, font_size=28, weight=BOLD),
            Text("という概念を導入しよう", color=WHITE, font_size=25),
        ).arrange(RIGHT, buff=0.1)
        intro_rank2.shift(DOWN * 1.9)
        self.play(Write(intro_rank), run_time=0.5)
        self.play(Write(intro_rank2), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(recall_text), FadeOut(lsq_sol), FadeOut(lsq_box),
            FadeOut(prob_text), FadeOut(prob_highlight),
            FadeOut(intro_rank), FadeOut(intro_rank2),
            FadeOut(subtitle3),
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: 行列のランク（階数）
        # ============================================================
        subtitle4 = Text("行列のランク（階数）", font_size=28, color=GREEN)
        subtitle4.next_to(title, DOWN)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.4)

        rank_concept = VGroup(
            Text("ランク（階数）：", color=GREEN, font_size=26, weight=BOLD),
            Text("その行列が持つ「本質的な情報の数」", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.12)
        rank_concept.shift(UP * 1.8)
        self.play(Write(rank_concept), run_time=0.6)
        self.wait(0.3)

        rank_defs = VGroup(
            VGroup(
                Text("＝ ", color=GRAY, font_size=24),
                Text("行ごとの1次独立なベクトルの数", color=TEAL, font_size=25),
            ).arrange(RIGHT, buff=0.05),
            VGroup(
                Text("＝ ", color=GRAY, font_size=24),
                Text("列ごとの1次独立なベクトルの数", color=ORANGE, font_size=25),
            ).arrange(RIGHT, buff=0.05),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        rank_defs.shift(UP * 1.1)
        self.play(Write(rank_defs), run_time=0.7)
        self.wait(0.4)

        # 具体例：4×5行列
        example_label = Text("具体例（4×5 行列）：", color=WHITE, font_size=23)
        example_label.shift(UP * 0.2 + LEFT * 5.0)
        self.play(Write(example_label), run_time=0.4)

        mat_vals = [
            [1, 0, 2, 1, 3],
            [0, 1, 1, 2, 0],
            [1, 0, 2, 1, 3],   # ← 1行目と同じ
            [2, 1, 5, 4, 4],
        ]
        mat_mob = Matrix(
            mat_vals,
            element_to_mobject_config={"font_size": 28},
            h_buff=0.9,
        )
        mat_mob.scale(0.88)
        mat_mob.shift(DOWN * 0.8 + LEFT )
        self.play(Write(mat_mob), run_time=0.8)
        self.wait(0.3)

        # 1行目と3行目をハイライト
        rows = mat_mob.get_rows()
        row1_rect = SurroundingRectangle(rows[0], color=TEAL, buff=0.1)
        row3_rect = SurroundingRectangle(rows[2], color=TEAL, buff=0.1)
        self.play(Create(row1_rect), Create(row3_rect), run_time=0.5)
        self.wait(0.2)

        same_note = Text("1行目と3行目が同じ！\n→ 独立な情報は3行分しかない", color=TEAL, font_size=22)
        same_note.next_to(mat_mob, RIGHT, buff=0.5)
        self.play(Write(same_note), run_time=0.5)
        self.wait(0.4)

        rank_result = Text("独立な行は 1or3行目, 2行目, 4行目 の 合計3本", color=WHITE, font_size=24)
        rank_result.shift(DOWN * 2.5 + LEFT * 0.5)
        rank_result2 = VGroup(
            Text("→ この行列のランク ＝ ", color=WHITE, font_size=26),
            Text("3", color=GREEN, font_size=32, weight=BOLD),
            Text("（4 より小さい）", color=ORANGE, font_size=24),
        ).arrange(RIGHT, buff=0.1)
        rank_result2.next_to(rank_result, DOWN, buff=0.12)
        self.play(Write(rank_result), run_time=0.4)
        self.play(Write(rank_result2), run_time=0.5)
        self.wait(0.5)

        fullrank_stmt = VGroup(
            Text("m×m 行列はランクが m（", color=WHITE, font_size=25),
            Text("フルランク", color=GREEN, font_size=25, weight=BOLD),
            Text("）のとき、かつそのときに限り逆行列をもつ", color=WHITE, font_size=25),
        ).arrange(RIGHT, buff=0.08)
        fullrank_stmt.shift(DOWN * 3.5)
        fullrank_box = SurroundingRectangle(fullrank_stmt, color=GREEN, buff=0.12)
        self.play(Write(fullrank_stmt), Create(fullrank_box), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(rank_concept), FadeOut(rank_defs), FadeOut(example_label),
            FadeOut(mat_mob), FadeOut(row1_rect), FadeOut(row3_rect),
            FadeOut(same_note), FadeOut(rank_result), FadeOut(rank_result2),
            FadeOut(fullrank_stmt), FadeOut(fullrank_box),
            FadeOut(subtitle4),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: X^TX のランクと列フルランク
        # ============================================================
        subtitle5 = VGroup(
            MathTex(r"X^\top X", color=YELLOW, font_size=30),
            Text("のランクと X の列ベクトルの関係", color=YELLOW, font_size=27),
        ).arrange(RIGHT, buff=0.1)
        subtitle5.next_to(title, DOWN)
        self.play(Write(subtitle5), run_time=0.6)
        self.wait(0.4)

        # X を列ベクトルで書き直す
        x_col_text = Text("データ行列 X を列ベクトルで書き直すと：", color=WHITE, font_size=26)
        x_col_text.shift(UP * 1.7)
        self.play(Write(x_col_text), run_time=0.5)
        self.wait(0.2)

        x_col_def = MathTex(
            r"X = \bigl[\,\tilde{\mathbf{x}}_0 \;\; \tilde{\mathbf{x}}_1 \;\; \cdots \;\; \tilde{\mathbf{x}}_D\,\bigr]",
            color=TEAL, font_size=32
        )
        x_col_def.shift(UP * 0.9)
        self.play(Write(x_col_def), run_time=0.6)
        x_dim = VGroup(
            Text("ここで", color=WHITE, font_size=22),
            MathTex(r"X \in \mathbb{R}^{N \times (D+1)}", color=TEAL, font_size=28),
            Text("なので", color=WHITE, font_size=22),
            MathTex(r"X^\top X \in \mathbb{R}^{(D+1) \times (D+1)}", color=YELLOW, font_size=28),
        ).arrange(RIGHT, buff=0.12)
        x_dim.shift(UP * 0.5)
        self.play(Write(x_dim), run_time=0.6)
        self.wait(0.3)

        xtx_text = VGroup(
            MathTex(r"X^\top X", color=YELLOW, font_size=30),
            Text("の", color=WHITE, font_size=24),
            MathTex(r"(d, d')", color=YELLOW, font_size=30),
            Text("成分を書き下すと：", color=WHITE, font_size=24)
        ).arrange(RIGHT, buff=0.1)
        xtx_text.shift(DOWN * 0.05)
        self.play(Write(xtx_text), run_time=0.5)
        self.wait(0.2)

        xtx_matrix = MathTex(
            r"X^\top X = \begin{bmatrix}"
            r"\tilde{\mathbf{x}}_0^\top \tilde{\mathbf{x}}_0 & "
            r"\tilde{\mathbf{x}}_0^\top \tilde{\mathbf{x}}_1 & "
            r"\tilde{\mathbf{x}}_0^\top \tilde{\mathbf{x}}_2 & \cdots & "
            r"\tilde{\mathbf{x}}_0^\top \tilde{\mathbf{x}}_D \\"
            r"\tilde{\mathbf{x}}_1^\top \tilde{\mathbf{x}}_0 & "
            r"\tilde{\mathbf{x}}_1^\top \tilde{\mathbf{x}}_1 & "
            r"\tilde{\mathbf{x}}_1^\top \tilde{\mathbf{x}}_2 & \cdots & "
            r"\tilde{\mathbf{x}}_1^\top \tilde{\mathbf{x}}_D \\"
            r"\tilde{\mathbf{x}}_2^\top \tilde{\mathbf{x}}_0 & "
            r"\tilde{\mathbf{x}}_2^\top \tilde{\mathbf{x}}_1 & "
            r"\tilde{\mathbf{x}}_2^\top \tilde{\mathbf{x}}_2 & \cdots & "
            r"\tilde{\mathbf{x}}_2^\top \tilde{\mathbf{x}}_D \\"
            r"\vdots & \vdots & \vdots & \ddots & \vdots \\"
            r"\tilde{\mathbf{x}}_D^\top \tilde{\mathbf{x}}_0 & "
            r"\tilde{\mathbf{x}}_D^\top \tilde{\mathbf{x}}_1 & "
            r"\tilde{\mathbf{x}}_D^\top \tilde{\mathbf{x}}_2 & \cdots & "
            r"\tilde{\mathbf{x}}_D^\top \tilde{\mathbf{x}}_D"
            r"\end{bmatrix}",
            color=WHITE, font_size=30
        )
        xtx_matrix.shift(DOWN * 1.4)

        xtx_comp_label = Text("すなわち：", color=YELLOW, font_size=22)
        xtx_comp = MathTex(
            r"(X^\top X)_{d,\,d'} = \tilde{\mathbf{x}}_d^\top \tilde{\mathbf{x}}_{d'}",
            color=YELLOW, font_size=26
        )
        xtx_comp_group = VGroup(xtx_comp_label, xtx_comp).arrange(RIGHT, buff=0.15)
        xtx_comp_group.shift(DOWN * 2.9)

        self.play(Write(xtx_matrix), run_time=0.9)
        self.play(Write(xtx_comp_group), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(x_col_text), FadeOut(x_col_def),
            FadeOut(x_dim),
            FadeOut(xtx_text), FadeOut(xtx_matrix), FadeOut(xtx_comp_group),
        )
        self.wait(0.2)

        # 1次従属ケース
        dep_title = Text("列ベクトルが1次従属なときを考える", color=ORANGE, font_size=26)
        dep_title.shift(UP * 1.7)
        self.play(Write(dep_title), run_time=0.5)
        self.wait(0.3)

        # Case 1
        case1_label = Text("【ケース1】", color=TEAL, font_size=26, weight=BOLD)
        case1_label.shift(UP * 1.0 + LEFT * 4.5)
        case1_eq = MathTex(r"\tilde{\mathbf{x}}_1 = \tilde{\mathbf{x}}_2", color=TEAL, font_size=32)
        case1_eq.next_to(case1_label, RIGHT, buff=0.2)
        self.play(Write(case1_label), Write(case1_eq), run_time=0.5)
        self.wait(0.2)

        case1_result_tex = MathTex(
            r"(X^\top X)_{1,\,d'} = \tilde{\mathbf{x}}_1^\top \tilde{\mathbf{x}}_{d'}"
            r"= \tilde{\mathbf{x}}_2^\top \tilde{\mathbf{x}}_{d'}"
            r"= (X^\top X)_{2,\,d'}",
            color=TEAL, font_size=30
        )
        case1_result_tex.shift(UP * 0.2)
        self.play(Write(case1_result_tex), run_time=0.7)
        self.wait(0.3)

        case1_conclude = VGroup(
            MathTex(r"(X^\top X)",color=WHITE, font_size=26),
            Text("→ の2行目と3行目が完全一致", color=WHITE, font_size=24),
            Text("→ ランクが落ちて逆行列を持たない！", color=RED, font_size=24, weight=BOLD),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        case1_conclude.shift(DOWN * 0.7)
        self.play(Write(case1_conclude), run_time=0.5)
        self.wait(0.5)

        # Case 2
        case2_label = Text("【ケース2】", color=ORANGE, font_size=26, weight=BOLD)
        case2_label.shift(DOWN * 1.6 + LEFT * 4.5)
        case2_eq = MathTex(r"\tilde{\mathbf{x}}_1 = 4\,\tilde{\mathbf{x}}_2", color=ORANGE, font_size=32)
        case2_eq.next_to(case2_label, RIGHT, buff=0.2)
        self.play(Write(case2_label), Write(case2_eq), run_time=0.5)
        self.wait(0.2)

        case2_note = Text(
            "→ 1次従属なので、やはりランクが落ちて逆行列を持たない",
            color=ORANGE, font_size=24
        )
        case2_note.shift(DOWN * 2.2)
        self.play(Write(case2_note), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(dep_title),
            FadeOut(case1_label), FadeOut(case1_eq), FadeOut(case1_result_tex),
            FadeOut(case1_conclude),
            FadeOut(case2_label), FadeOut(case2_eq), FadeOut(case2_note),
        )
        self.wait(0.2)

        # 結論：列フルランク条件
        concl_title = Text("結論", color=GOLD, font_size=28, weight=BOLD)
        concl_title.shift(UP * 1.7)
        self.play(Write(concl_title), run_time=0.4)
        self.wait(0.2)

        concl_stmt = VGroup(
            MathTex(r"X^\top X", color=YELLOW, font_size=32),
            Text("がフルランク（逆行列をもつ）", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.12)
        concl_stmt.shift(UP * 1.0)
        self.play(Write(concl_stmt), run_time=0.5)
        self.wait(0.2)

        concl_cond = VGroup(
            Text("⟺ X の列ベクトル", color=WHITE, font_size=26),
            MathTex(
                r"\tilde{\mathbf{x}}_0,\,\tilde{\mathbf{x}}_1,\,\ldots,\,\tilde{\mathbf{x}}_D",
                color=TEAL, font_size=26
            ),
            Text("がすべて1次独立", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.1)
        concl_cond.shift(UP * 0.3)

        concl_term = VGroup(
            Text("（ ＝ ", color=WHITE, font_size=24),
            Text("X が列フルランク", color=GREEN, font_size=26, weight=BOLD),
            Text("）", color=WHITE, font_size=24),
        ).arrange(RIGHT, buff=0.08)
        concl_term.shift(DOWN * 0.3)

        concl_box = SurroundingRectangle(
            VGroup(concl_cond, concl_term), color=GREEN, buff=0.18
        )
        self.play(Write(concl_cond), run_time=0.5)
        self.play(Write(concl_term), Create(concl_box), run_time=0.6)
        self.wait(0.5)

        # 数値的不安定性への言及
        instab = VGroup(
            Text("● ", color=GRAY, font_size=24),
            Text("実際の計算では全く同じ列ベクトルが現れることは少ないが、", color=WHITE, font_size=23),
        ).arrange(RIGHT, buff=0.05)
        instab.shift(DOWN * 1.1)
        instab2 = VGroup(
            Text("    ", font_size=24),
            Text("似ているベクトルが存在するだけでも計算が不安定になる場合がある", color=YELLOW, font_size=24),
        ).arrange(RIGHT, buff=0.05)
        instab2.next_to(instab, DOWN, buff=0.08).align_to(instab, LEFT)
        self.play(Write(instab), run_time=0.5)
        self.play(Write(instab2), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(concl_title), FadeOut(concl_stmt),
            FadeOut(concl_cond), FadeOut(concl_term), FadeOut(concl_box),
            FadeOut(instab), FadeOut(instab2),
            FadeOut(subtitle5),
        )
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
                    Text("高次モデルが常によいとは限らない（過学習・過適合）", color=WHITE, font_size=28),
                    Text("→ 訓練データへの過度な適合は汎化能力を損なう", color=RED, font_size=28),
                ).arrange(DOWN, buff=0.08, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("2.", color=GOLD, font_size=26, weight=BOLD),
                VGroup(
                    Text("汎化能力：未知データへの対応力", color=WHITE, font_size=28),
                    Text("→ 機械学習の学習手法を評価する主要指標の一つ", color=GREEN, font_size=28),
                ).arrange(DOWN, buff=0.08, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("3.", color=GOLD, font_size=26, weight=BOLD),
                VGroup(
                    Text("行列のランク＝本質的な情報の数（1次独立な行／列の数）", color=WHITE, font_size=28),
                    Text("正方行列はフルランクのときのみ逆行列をもつ", color=TEAL, font_size=28),
                ).arrange(DOWN, buff=0.08, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("4.", color=GOLD, font_size=26, weight=BOLD),
                VGroup(
                    MathTex(r"X^\top X", color=YELLOW, font_size=28),
                    Text(
                        "が逆行列をもつ ⟺ X が列フルランク（列ベクトルが1次独立）",
                        color=WHITE, font_size=28
                    ),
                ).arrange(RIGHT, buff=0.08),
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
