from manim import *
import numpy as np

class OrthogonalityAdvantage(Scene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"

        # タイトル
        title = Text("直交基底の威力: 積分が係数の積和に化ける", font_size=34, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)

        # === イントロ ===
        intro_subtitle = Text("直交性が計算を劇的に簡単にする", font_size=30, color=YELLOW)
        intro_subtitle.next_to(title, DOWN)
        self.play(Write(intro_subtitle), run_time=0.6)
        self.wait(0.4)

        intro_group = VGroup(
            Text("関数 f₁, f₂ を直交基底で展開したとき...", color=WHITE, font_size=26, slant=ITALIC),
            MathTex(
                r"\langle f_1 | f_2 \rangle = \int_{-\infty}^{\infty} f_1(x)\,f_2(x)\,\rho(x)\,dx",
                color=ORANGE, font_size=28
            ),
            Text("この積分が --- 係数の掛け算と足し算だけで求まる！", color=YELLOW, font_size=26, weight=BOLD),
        ).arrange(DOWN, buff=0.4)
        intro_group.shift(DOWN * 0.3)

        self.play(Write(intro_group), run_time=1.2)
        self.wait(1.5)

        self.play(FadeOut(intro_group), FadeOut(intro_subtitle))
        self.wait(0.3)

        # === Part 1: 問題設定 ===
        subtitle1 = Text("問題設定", font_size=32, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.5)

        # 直交基底 g_0, g_1, g_2 がある
        basis_box_text = VGroup(
            Text("直交基底:", color=ORANGE, font_size=26, weight=BOLD),
            MathTex(r"g_0(x),\; g_1(x),\; g_2(x)", color=ORANGE, font_size=30),
        ).arrange(RIGHT, buff=0.3)
        basis_box_text.shift(UP * 1.8)
        basis_surr = SurroundingRectangle(basis_box_text, color=ORANGE, buff=0.1)
        self.play(Write(basis_box_text), Create(basis_surr), run_time=0.7)
        self.wait(0.4)

        # 直交性の条件
        orth_cond = MathTex(
            r"\langle g_i | g_j \rangle = 0 \quad (i \neq j)",
            color=ORANGE, font_size=28
        )
        orth_cond.next_to(basis_surr, DOWN, buff=0.2)
        self.play(Write(orth_cond), run_time=0.6)
        self.wait(0.4)

        # f_1, f_2 の展開
        f_expand = VGroup(
            MathTex(
                r"f_1(x) = c_{1,0}\,g_0 + c_{1,1}\,g_1 + c_{1,2}\,g_2",
                color=BLUE, font_size=30
            ),
            MathTex(
                r"f_2(x) = c_{2,0}\,g_0 + c_{2,1}\,g_1 + c_{2,2}\,g_2",
                color=GREEN, font_size=30
            ),
        ).arrange(DOWN, buff=0.3)
        f_expand.shift(DOWN * 0.2)
        self.play(Write(f_expand), run_time=0.9)
        self.wait(0.6)

        # 問: 内積を求めよ
        question = VGroup(
            Text("問:", color=YELLOW, font_size=28, weight=BOLD),
            MathTex(r"\langle f_1 | f_2 \rangle = \; ?", color=YELLOW, font_size=30),
        ).arrange(RIGHT, buff=0.3)
        question.shift(DOWN * 1.8)
        q_box = SurroundingRectangle(question, color=YELLOW, buff=0.15)
        self.play(Write(question), Create(q_box), run_time=0.7)
        self.wait(1.0)

        self.play(
            FadeOut(basis_box_text), FadeOut(basis_surr),
            FadeOut(orth_cond), FadeOut(f_expand),
            FadeOut(question), FadeOut(q_box),
            FadeOut(subtitle1)
        )
        self.wait(0.3)

        # === Part 2: 内積を展開すると ===
        subtitle2 = Text("内積を展開すると", font_size=32, color=GREEN)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)

        # 一般式
        linearity_note = Text("内積の線形性を使って展開:", color=YELLOW, font_size=24, weight=BOLD)
        linearity_note.shift(UP * 1.8)
        self.play(Write(linearity_note), run_time=0.5)
        self.wait(0.3)

        general_expand = MathTex(
            r"\langle f_1 | f_2 \rangle"
            r"= \sum_{i=0}^{2}\sum_{j=0}^{2} c_{1,i}\,c_{2,j}\,"
            r"\langle g_i | g_j \rangle",
            color=WHITE, font_size=26
        )
        general_expand.shift(UP * 1.1)
        self.play(Write(general_expand), run_time=0.8)
        self.wait(0.5)

        # 展開すると9項
        nine_label = Text("全部展開すると 3×3 = 9 項:", color=ORANGE, font_size=22, weight=BOLD)
        nine_label.shift(UP * 0.3 + LEFT * 2)
        self.play(Write(nine_label), run_time=0.5)
        self.wait(0.3)

        # 対角: GREEN, 非対角: RED
        fs = 24  # font_size for terms

        row0 = VGroup(
            MathTex(r"c_{1,0}c_{2,0}\langle g_0|g_0\rangle", color=GREEN, font_size=fs),
            MathTex(r"+\;c_{1,0}c_{2,1}\langle g_0|g_1\rangle", color=RED, font_size=fs),
            MathTex(r"+\;c_{1,0}c_{2,2}\langle g_0|g_2\rangle", color=RED, font_size=fs),
        ).arrange(RIGHT, buff=0.15)

        row1 = VGroup(
            MathTex(r"+\;c_{1,1}c_{2,0}\langle g_1|g_0\rangle", color=RED, font_size=fs),
            MathTex(r"+\;c_{1,1}c_{2,1}\langle g_1|g_1\rangle", color=GREEN, font_size=fs),
            MathTex(r"+\;c_{1,1}c_{2,2}\langle g_1|g_2\rangle", color=RED, font_size=fs),
        ).arrange(RIGHT, buff=0.15)

        row2 = VGroup(
            MathTex(r"+\;c_{1,2}c_{2,0}\langle g_2|g_0\rangle", color=RED, font_size=fs),
            MathTex(r"+\;c_{1,2}c_{2,1}\langle g_2|g_1\rangle", color=RED, font_size=fs),
            MathTex(r"+\;c_{1,2}c_{2,2}\langle g_2|g_2\rangle", color=GREEN, font_size=fs),
        ).arrange(RIGHT, buff=0.15)

        all_terms = VGroup(row0, row1, row2).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        all_terms.shift(DOWN * 0.8)

        for row in all_terms:
            self.play(Write(row), run_time=0.5)
            self.wait(0.15)

        self.wait(0.8)

        # 凡例
        legend = VGroup(
            VGroup(
                MathTex(r"\bullet", color=GREEN, font_size=24),
                Text(": i=j (対角項)", color=GREEN, font_size=16),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                MathTex(r"\bullet", color=RED, font_size=24),
                Text(": i≠j (交差項)", color=RED, font_size=16),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        legend.shift(DOWN * 2.6 + RIGHT * 4.5)
        self.play(FadeIn(legend), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(linearity_note), FadeOut(general_expand),
            FadeOut(nine_label), FadeOut(all_terms),
            FadeOut(legend), FadeOut(subtitle2)
        )
        self.wait(0.3)

        # === Part 3: 直交性による消去 ===
        subtitle3 = Text("直交性が交差項を全て 0 にする！", font_size=30, color=RED)
        subtitle3.next_to(title, DOWN)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.5)

        # 直交基底の条件
        orth_eq = MathTex(
            r"\langle g_i | g_j \rangle = 0 \quad (i \neq j)",
            color=ORANGE, font_size=30
        )
        orth_eq.shift(UP * 1.6)
        orth_eq_box = SurroundingRectangle(orth_eq, color=ORANGE, buff=0.2)
        self.play(Write(orth_eq), Create(orth_eq_box), run_time=0.7)
        self.wait(0.5)

        # 交差項の例
        cross_examples = VGroup(
            MathTex(r"\langle g_0|g_1\rangle = 0", color=RED, font_size=28),
            MathTex(r"\langle g_0|g_2\rangle = 0", color=RED, font_size=28),
            MathTex(r"\langle g_1|g_2\rangle = 0", color=RED, font_size=28),
        ).arrange(RIGHT, buff=0.6)
        cross_examples.shift(UP * 0.6)

        cross_note = Text("↑ すべてゼロ！", color=RED, font_size=24, weight=BOLD)
        cross_note.next_to(cross_examples, DOWN, buff=0.15)

        self.play(Write(cross_examples), run_time=0.7)
        self.play(Write(cross_note), run_time=0.4)
        self.wait(0.6)

        # 残るのは対角項のみ
        remains_label = Text("残るのは対角項のみ!", color=GREEN, font_size=26, weight=BOLD)
        remains_label.shift(DOWN * 0.1 + LEFT * 3.5)
        self.play(Write(remains_label), run_time=0.5)
        self.wait(0.3)

        simplified = MathTex(
            r"\langle f_1 | f_2 \rangle"
            r"= c_{1,0}c_{2,0}\langle g_0|g_0\rangle"
            r"+ c_{1,1}c_{2,1}\langle g_1|g_1\rangle"
            r"+ c_{1,2}c_{2,2}\langle g_2|g_2\rangle",
            color=GREEN, font_size=28
        )
        simplified.shift(DOWN * 0.9)
        simp_box = SurroundingRectangle(simplified, color=GREEN, buff=0.15)
        self.play(Write(simplified), Create(simp_box), run_time=0.9)
        self.wait(0.5)

        # コメント
        simp_note = VGroup(
            Text("9項 → 3項に削減！", color=YELLOW, font_size=24, weight=BOLD),
            Text("各 ⟨g_k|g_k⟩ は事前に 1 度計算すれば OK", color=WHITE, font_size=22),
        ).arrange(DOWN, buff=0.2)
        simp_note.shift(DOWN * 2.4)
        self.play(Write(simp_note), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(orth_eq), FadeOut(orth_eq_box),
            FadeOut(cross_examples), FadeOut(cross_note),
            FadeOut(remains_label), FadeOut(simplified), FadeOut(simp_box),
            FadeOut(simp_note), FadeOut(subtitle3)
        )
        self.wait(0.3)

        # === Part 4: エルミート多項式基底への適用 ===
        subtitle4 = Text("エルミート多項式基底への適用", font_size=30, color=PURPLE)
        subtitle4.next_to(title, DOWN)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.5)

        # 設定: g_k = H_k(x), ρ(x) = e^{-x²}
        setting_text = VGroup(
            VGroup(
                Text("基底:", color=WHITE, font_size=24),
                MathTex(r"g_k(x) = H_k(x)", color=BLUE, font_size=24),
                Text("(エルミート多項式)", color=BLUE, font_size=20),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("重み関数:", color=WHITE, font_size=24),
                MathTex(r"\rho(x) = e^{-x^2}", color=GREEN, font_size=24),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("内積:", color=WHITE, font_size=24),
                MathTex(
                    r"\langle f|g\rangle = \int_{-\infty}^{\infty} f(x)\,g(x)\,e^{-x^2}\,dx",
                    color=ORANGE, font_size=22
                ),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        setting_text.shift(UP * 1.4)
        self.play(Write(setting_text), run_time=0.9)
        self.wait(0.5)

        # 9話の結果: ノルム公式
        prev_label = Text("前回(9話)の結果:", color=YELLOW, font_size=24, weight=BOLD)
        prev_label.shift(DOWN * 0.3 + LEFT * 4)
        self.play(Write(prev_label), run_time=0.5)
        self.wait(0.3)

        norm_formula_big = MathTex(
            r"\langle H_n | H_n \rangle = 2^n \, n! \, \sqrt{\pi}",
            color=YELLOW, font_size=28
        )
        norm_formula_big.shift(DOWN * 1.0)
        nfb_box = SurroundingRectangle(norm_formula_big, color=YELLOW, buff=0.15)
        self.play(Write(norm_formula_big), Create(nfb_box), run_time=0.7)
        self.wait(0.5)

        # 具体値の一覧
        norm_specific = VGroup(
            MathTex(r"\langle H_0|H_0\rangle = \sqrt{\pi}", color=GREEN, font_size=24),
            MathTex(r"\langle H_1|H_1\rangle = 2\sqrt{\pi}", color=GREEN, font_size=24),
            MathTex(r"\langle H_2|H_2\rangle = 8\sqrt{\pi}", color=GREEN, font_size=24),
        ).arrange(RIGHT, buff=0.6)
        norm_specific.shift(DOWN * 1.9)

        for ns in norm_specific:
            self.play(Write(ns), run_time=0.4)
            self.wait(0.15)

        self.wait(0.6)

        # 最終的な公式
        final_hermite = MathTex(
            r"\therefore \quad \langle f_1 | f_2 \rangle"
            r"= c_{1,0}c_{2,0}\sqrt{\pi}"
            r"+ c_{1,1}c_{2,1}\cdot 2\sqrt{\pi}"
            r"+ c_{1,2}c_{2,2}\cdot 8\sqrt{\pi}",
            color=WHITE, font_size=26
        )
        final_hermite.shift(DOWN * 2.8)
        fh_box = SurroundingRectangle(final_hermite, color=WHITE, buff=0.12)
        self.play(Write(final_hermite), Create(fh_box), run_time=0.9)
        self.wait(1.2)

        self.play(
            FadeOut(setting_text), FadeOut(prev_label),
            FadeOut(norm_formula_big), FadeOut(nfb_box),
            FadeOut(norm_specific), FadeOut(final_hermite), FadeOut(fh_box),
            FadeOut(subtitle4)
        )
        self.wait(0.3)

        # === Part 5: 具体例 ===
        subtitle5 = Text("具体例: 数値で確かめよう", font_size=32, color=TEAL)
        subtitle5.next_to(title, DOWN)
        self.play(Write(subtitle5), run_time=0.6)
        self.wait(0.5)

        # 具体的な関数
        eg_label = Text("例:", color=YELLOW, font_size=26, weight=BOLD)
        eg_label.shift(UP * 1.8 + LEFT * 5.5)
        self.play(Write(eg_label), run_time=0.4)

        eg_f1 = MathTex(
            r"f_1(x) = 1 \cdot H_0 + 2 \cdot H_1 + 3 \cdot H_2",
            color=BLUE, font_size=26
        )
        eg_f1.shift(UP * 1.8 + LEFT * 0.5)

        eg_f2 = MathTex(
            r"f_2(x) = 1 \cdot H_0 + (-1) \cdot H_1 + 2 \cdot H_2",
            color=GREEN, font_size=26
        )
        eg_f2.next_to(eg_f1, DOWN, buff=0.25)

        self.play(Write(eg_f1), run_time=0.6)
        self.play(Write(eg_f2), run_time=0.6)
        self.wait(0.5)

        # 係数ベクトル
        coeff_label = Text("係数:", color=ORANGE, font_size=24, weight=BOLD)
        coeff_label.shift(UP * 0.6 + LEFT * 5)

        coeff_c1 = MathTex(
            r"\vec{c}_1 = (1,\; 2,\; 3)",
            color=BLUE, font_size=26
        )
        coeff_c1.shift(UP * 0.6 + LEFT * 0.5)

        coeff_c2 = MathTex(
            r"\vec{c}_2 = (1,\; -1,\; 2)",
            color=GREEN, font_size=26
        )
        coeff_c2.next_to(coeff_c1, RIGHT, buff=1.0)

        self.play(Write(coeff_label), Write(coeff_c1), Write(coeff_c2), run_time=0.7)
        self.wait(0.5)

        # 計算ステップ
        calc_title = Text("計算:", color=YELLOW, font_size=24, weight=BOLD)
        calc_title.shift(DOWN * 0.1 + LEFT * 5.5)
        self.play(Write(calc_title), run_time=0.4)

        step1 = MathTex(
            r"\langle f_1 | f_2 \rangle"
            r"= (1 \cdot 1)\,\sqrt{\pi}"
            r"+ \bigl(2 \cdot (-1)\bigr)\cdot 2\sqrt{\pi}"
            r"+ (3 \cdot 2)\cdot 8\sqrt{\pi}",
            color=WHITE, font_size=26
        )
        step1.shift(DOWN * 0.8)
        self.play(Write(step1), run_time=0.9)
        self.wait(0.4)

        step2 = MathTex(
            r"= \sqrt{\pi} - 4\sqrt{\pi} + 48\sqrt{\pi}",
            color=WHITE, font_size=26
        )
        step2.shift(DOWN * 1.6)
        self.play(Write(step2), run_time=0.7)
        self.wait(0.4)

        final_ans = MathTex(
            r"= 45\sqrt{\pi}",
            color=YELLOW, font_size=34
        )
        final_ans.shift(DOWN * 2.3)
        ans_box = SurroundingRectangle(final_ans, color=YELLOW, buff=0.2)
        self.play(Write(final_ans), Create(ans_box), run_time=0.7)
        self.wait(0.5)

        # 一言コメント
        no_int_comment = Text(
            "積分計算は一切なし！ 四則演算だけで内積が求まった",
            color=GREEN, font_size=22, weight=BOLD, slant=ITALIC
        )
        no_int_comment.shift(DOWN * 3.1)
        self.play(Write(no_int_comment), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(eg_label), FadeOut(eg_f1), FadeOut(eg_f2),
            FadeOut(coeff_label), FadeOut(coeff_c1), FadeOut(coeff_c2),
            FadeOut(calc_title), FadeOut(step1), FadeOut(step2),
            FadeOut(final_ans), FadeOut(ans_box),
            FadeOut(no_int_comment), FadeOut(subtitle5)
        )
        self.wait(0.3)

        # === Part 6: 行列表示との対応 ===
        subtitle6 = Text("行列表示との対応", font_size=32, color=GOLD)
        subtitle6.next_to(title, DOWN)
        self.play(Write(subtitle6), run_time=0.6)
        self.wait(0.5)

        # ベクトルの内積との類比
        analogy_label = Text("通常の実ベクトルの内積と比べると:", color=WHITE, font_size=24, weight=BOLD)
        analogy_label.shift(UP * 1.8)
        self.play(Write(analogy_label), run_time=0.5)
        self.wait(0.3)

        # 左: 通常ベクトル内積
        vec_label = Text("実ベクトル", color=BLUE, font_size=24, weight=BOLD)
        vec_label.shift(UP * 1.0 + LEFT * 3.5)

        vec_formula = MathTex(
            r"\vec{a} \cdot \vec{b} = \sum_k a_k b_k",
            color=BLUE, font_size=26
        )
        vec_formula.next_to(vec_label, DOWN, buff=0.3)

        # 右: 直交基底での関数内積
        func_label = Text("直交基底での関数", color=GREEN, font_size=24, weight=BOLD)
        func_label.shift(UP * 1.0 + RIGHT * 2.5)

        func_formula = MathTex(
            r"\langle f_1|f_2\rangle = \sum_k c_{1,k}\,c_{2,k}\,\langle g_k|g_k\rangle",
            color=GREEN, font_size=26
        )
        func_formula.next_to(func_label, DOWN, buff=0.3)

        # 仕切り線
        divider = DashedLine(
            UP * 1.3 + ORIGIN, DOWN * 0.4 + ORIGIN,
            color=GRAY, stroke_width=2
        )

        self.play(
            Write(vec_label), Write(func_label),
            Create(divider),
            run_time=0.7
        )
        self.wait(0.3)
        self.play(Write(vec_formula), Write(func_formula), run_time=0.8)
        self.wait(0.8)

        # 対角行列表示
        matrix_label = Text("対角行列を使って書くと:", color=YELLOW, font_size=24, weight=BOLD)
        matrix_label.shift(DOWN * 0.9 + LEFT * 3)
        self.play(Write(matrix_label), run_time=0.5)
        self.wait(0.3)

        matrix_form = MathTex(
            r"\langle f_1 | f_2 \rangle"
            r"= \vec{c}_1^{\,T} \, D \, \vec{c}_2",
            color=WHITE, font_size=28
        )
        matrix_form.shift(DOWN * 1.6)

        D_def = MathTex(
            r"D = \mathrm{diag}\!\left(\langle g_0|g_0\rangle,\;"
            r"\langle g_1|g_1\rangle,\;"
            r"\langle g_2|g_2\rangle\right)",
            color=GRAY, font_size=26
        )
        D_def.next_to(matrix_form, DOWN, buff=0.25)

        mf_box = SurroundingRectangle(matrix_form, color=WHITE, buff=0.15)
        self.play(Write(matrix_form), Create(mf_box), run_time=0.7)
        self.play(Write(D_def), run_time=0.6)
        self.wait(0.8)

        # 特に正規直交基底の場合
        onb_note = VGroup(
            Text("特に正規直交基底 (", color=WHITE, font_size=24),
            MathTex(r"\langle g_k|g_k\rangle = 1", color=WHITE, font_size=24),
            Text(") の場合:", color=WHITE, font_size=24),
            MathTex(
                r"D = I \;\Rightarrow\; \langle f_1|f_2\rangle = \vec{c}_1 \cdot \vec{c}_2",
                color=YELLOW, font_size=24
            ),
        ).arrange(RIGHT, buff=0.1)
        onb_note.shift(DOWN * 2.8)
        self.play(Write(onb_note), run_time=0.8)
        self.wait(1.2)

        self.play(
            FadeOut(analogy_label),
            FadeOut(vec_label), FadeOut(vec_formula),
            FadeOut(func_label), FadeOut(func_formula),
            FadeOut(divider),
            FadeOut(matrix_label), FadeOut(matrix_form), FadeOut(mf_box),
            FadeOut(D_def), FadeOut(onb_note),
            FadeOut(subtitle6)
        )
        self.wait(0.3)

        # === まとめ ===
        subtitle_end = Text("まとめ", font_size=36, color=GOLD, weight=BOLD)
        subtitle_end.next_to(title, DOWN)
        self.play(Write(subtitle_end), run_time=0.7)
        self.wait(0.5)

        summary = VGroup(
            VGroup(
                Text("1.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("関数を直交基底で展開すると", color=WHITE, font_size=24),
                    Text("内積の「交差項」はすべてゼロになる", color=YELLOW, font_size=22, weight=BOLD),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("2.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("残るのは対角項のみ:", color=WHITE, font_size=24),
                    MathTex(
                        r"\langle f_1|f_2\rangle = \sum_k c_{1,k}\,c_{2,k}\,\langle g_k|g_k\rangle",
                        color=GREEN, font_size=24
                    ),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("3.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("エルミート多項式なら ⟨H_n|H_n⟩ は公式で既知", color=WHITE, font_size=24),
                    Text("→ 積分なしで内積が計算できる！", color=ORANGE, font_size=24, weight=BOLD),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("4.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("これは実ベクトルの内積計算と全く同じ形！", color=WHITE, font_size=24),
                    Text("関数空間とベクトル空間の深いつながり", color=GREEN, font_size=22, weight=BOLD),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        summary.scale(0.9)
        summary.shift(UP * 0.3)

        for point in summary:
            self.play(Write(point), run_time=0.7)
            self.wait(0.4)

        self.wait(1.5)

        all_final = VGroup(summary, subtitle_end, title)
        self.play(FadeOut(all_final), run_time=1.0)
        self.wait(0.5)
