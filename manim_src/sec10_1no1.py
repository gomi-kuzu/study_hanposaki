from manim import *
import numpy as np

class OrthogonalBasisPolynomials(Scene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"
        
        # タイトル
        title = Text("多項式空間の直交基底", font_size=40, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)
        
        # === イントロ: 前回の振り返り ===
        intro_text = VGroup(
            Text("前回までで多項式空間の内積を定義できた", color=WHITE, font_size=28, weight=BOLD),
            MathTex(
                r"\langle f_1 | f_2 \rangle = \int_{-\infty}^{\infty} f_1(x) \cdot f_2(x) \cdot e^{-x^2} \, dx",
                color=ORANGE, font_size=30
            ),
            Text("内積やノルムが計算できるようになった！", color=YELLOW, font_size=28),
        ).arrange(DOWN, buff=0.4)
        intro_text.shift(DOWN * 0.5)
        
        self.play(Write(intro_text), run_time=1.2)
        self.wait(1.5)
        
        self.play(FadeOut(intro_text))
        self.wait(0.3)
        
        # === パート1: 単項式基底で内積を調べてみる ===
        subtitle1 = Text("単項式基底で直交性を調べる", font_size=32, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.5)
        
        # 基底の表示
        basis_label = Text("単項式の基底:", color=YELLOW, font_size=26, weight=BOLD)
        basis_label.shift(UP * 2.0 + LEFT * 4.5)
        basis_formula = MathTex(
            r"\{|1\rangle, \, |x\rangle, \, |x^2\rangle, \, |x^3\rangle, \, \ldots \}",
            color=YELLOW, font_size=28
        )
        basis_formula.next_to(basis_label, RIGHT, buff=0.3)
        
        self.play(Write(basis_label), Write(basis_formula), run_time=0.7)
        self.wait(0.5)
        
        # 直交しているか調べよう
        question = Text("これらは互いに直交しているだろうか？", color=WHITE, font_size=26, slant=ITALIC)
        question.shift(UP * 1.2)
        self.play(Write(question), run_time=0.7)
        self.wait(0.6)
        
        # 内積の定義再掲（コンパクト）
        def_recall = MathTex(
            r"\langle x^m | x^n \rangle = \int_{-\infty}^{\infty} x^{m+n} \, e^{-x^2} \, dx",
            color=GRAY, font_size=24
        )
        def_recall.shift(UP * 0.5)
        self.play(Write(def_recall), run_time=0.6)
        self.wait(0.4)
        
        # 直交している例: <x|x^2>
        calc_ortho_label = Text("直交する組:", color=GREEN, font_size=24, weight=BOLD)
        calc_ortho_label.shift(DOWN * 0.2 + LEFT * 5.5)
        self.play(Write(calc_ortho_label), run_time=0.4)
        self.wait(0.2)
        
        calc_ortho1 = MathTex(
            r"\langle 1 | x \rangle = \int_{-\infty}^{\infty} x \, e^{-x^2} dx = 0",
            color=GREEN, font_size=26
        )
        calc_ortho1.next_to(calc_ortho_label, DOWN, buff=0.25, aligned_edge=LEFT)
        calc_ortho1_note = Text("(奇関数)", color=GRAY, font_size=16)
        calc_ortho1_note.next_to(calc_ortho1, RIGHT, buff=0.2)
        self.play(Write(calc_ortho1), Write(calc_ortho1_note), run_time=0.6)
        self.wait(0.3)
        
        calc_ortho2 = MathTex(
            r"\langle x | x^2 \rangle = \int_{-\infty}^{\infty} x^3 \, e^{-x^2} dx = 0",
            color=GREEN, font_size=26
        )
        calc_ortho2.next_to(calc_ortho1, DOWN, buff=0.25, aligned_edge=LEFT)
        calc_ortho2_note = Text("(奇関数)", color=GRAY, font_size=16)
        calc_ortho2_note.next_to(calc_ortho2, RIGHT, buff=0.2)
        self.play(Write(calc_ortho2), Write(calc_ortho2_note), run_time=0.6)
        self.wait(0.3)
        
        # 直交チェック
        check1 = MathTex(r"\checkmark", color=GREEN, font_size=28)
        check1.next_to(calc_ortho1_note, RIGHT, buff=0.2)
        check2 = MathTex(r"\checkmark", color=GREEN, font_size=28)
        check2.next_to(calc_ortho2_note, RIGHT, buff=0.2)
        self.play(Write(check1), Write(check2), run_time=0.3)
        self.wait(0.5)
        
        # 直交していない例: <x|x^3>
        calc_not_label = Text("直交しない組:", color=RED, font_size=24, weight=BOLD)
        calc_not_label.next_to(calc_ortho2, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(Write(calc_not_label), run_time=0.4)
        self.wait(0.2)
        
        calc_not1 = MathTex(
            r"\langle x | x^3 \rangle = \int_{-\infty}^{\infty} x^4 \, e^{-x^2} dx = \frac{3\sqrt{\pi}}{4} \neq 0",
            color=RED, font_size=26
        )
        calc_not1.next_to(calc_not_label, DOWN, buff=0.25, aligned_edge=LEFT)
        self.play(Write(calc_not1), run_time=0.7)
        self.wait(0.3)
        
        cross1 = MathTex(r"\times", color=RED, font_size=28)
        cross1.next_to(calc_not1, RIGHT, buff=0.2)
        self.play(Write(cross1), run_time=0.3)
        self.wait(0.3)
        
        calc_not2 = MathTex(
            r"\langle 1 | x^2 \rangle = \int_{-\infty}^{\infty} x^2 \, e^{-x^2} dx = \frac{\sqrt{\pi}}{2} \neq 0",
            color=RED, font_size=26
        )
        calc_not2.next_to(calc_not1, DOWN, buff=0.25, aligned_edge=LEFT)
        self.play(Write(calc_not2), run_time=0.7)
        self.wait(0.3)
        
        cross2 = MathTex(r"\times", color=RED, font_size=28)
        cross2.next_to(calc_not2, RIGHT, buff=0.2)
        self.play(Write(cross2), run_time=0.3)
        self.wait(0.8)
        
        # 結論
        conclusion1 = Text(
            "単項式基底は直交基底ではない！",
            color=RED, font_size=26, weight=BOLD
        )
        conclusion1.shift(DOWN * 3.0)
        conclusion1_box = SurroundingRectangle(conclusion1, color=RED, buff=0.15)
        self.play(Write(conclusion1), Create(conclusion1_box), run_time=0.8)
        self.wait(1.2)
        
        # フェードアウト
        self.play(
            FadeOut(basis_label), FadeOut(basis_formula),
            FadeOut(question), FadeOut(def_recall),
            FadeOut(calc_ortho_label), FadeOut(calc_ortho1), FadeOut(calc_ortho1_note),
            FadeOut(calc_ortho2), FadeOut(calc_ortho2_note),
            FadeOut(check1), FadeOut(check2),
            FadeOut(calc_not_label), FadeOut(calc_not1), FadeOut(cross1),
            FadeOut(calc_not2), FadeOut(cross2),
            FadeOut(conclusion1), FadeOut(conclusion1_box),
            FadeOut(subtitle1)
        )
        self.wait(0.3)
        
        # === パート2: 直交基底の便利さを復習 ===
        subtitle2 = Text("直交基底がほしい理由", font_size=32, color=GREEN)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)
        
        # sec4の復習
        review_intro = Text(
            "4話で学んだ直交基底の便利さ",
            color=WHITE, font_size=26, slant=ITALIC
        )
        review_intro.shift(UP * 2.0)
        self.play(Write(review_intro), run_time=0.7)
        self.wait(0.5)
        
        # 直交基底のメリット
        merits = VGroup(
            VGroup(
                Text("•", color=YELLOW, font_size=28),
                Text("座標（係数）が内積だけで求まる", color=YELLOW, font_size=26, weight=BOLD),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("", color=WHITE, font_size=26),
                MathTex(
                    r"c_i = \frac{\langle e_i | v \rangle}{\langle e_i | e_i \rangle}",
                    color=WHITE, font_size=28
                ),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("•", color=YELLOW, font_size=28),
                Text("他の基底の影響が消える", color=YELLOW, font_size=26, weight=BOLD),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("•", color=YELLOW, font_size=28),
                Text("次元が大きくなるほど利点が顕著", color=YELLOW, font_size=26, weight=BOLD),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        merits.shift(DOWN * 0.2)
        
        for merit in merits:
            self.play(Write(merit), run_time=0.6)
            self.wait(0.3)
        
        self.wait(0.5)
        
        want_text = Text(
            "多項式空間でも直交基底がとれないだろうか？",
            color=GREEN, font_size=28, weight=BOLD
        )
        want_text.shift(DOWN * 2.2)
        want_box = SurroundingRectangle(want_text, color=GREEN, buff=0.15)
        self.play(Write(want_text), Create(want_box), run_time=0.8)
        self.wait(1.2)
        
        # フェードアウト
        self.play(
            FadeOut(review_intro), FadeOut(merits),
            FadeOut(want_text), FadeOut(want_box),
            FadeOut(subtitle2)
        )
        self.wait(0.3)
        
        # === パート3: エルミート多項式が直交基底 ===
        subtitle3 = Text("実はエルミート多項式が答え", font_size=32, color=PURPLE)
        subtitle3.next_to(title, DOWN)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.5)
        
        # エルミート多項式の登場
        hermite_intro = VGroup(
            Text("ここ数回で何度も登場したエルミート多項式", color=WHITE, font_size=26),
            Text("実は直交基底になっている！", color=YELLOW, font_size=28, weight=BOLD),
        ).arrange(DOWN, buff=0.3)
        hermite_intro.shift(UP * 2.0)
        self.play(Write(hermite_intro), run_time=0.9)
        self.wait(0.8)
        
        # エルミート多項式の一覧
        hermite_list = VGroup(
            MathTex(r"H_0(x) = 1", color=BLUE, font_size=28),
            MathTex(r"H_1(x) = 2x", color=BLUE, font_size=28),
            MathTex(r"H_2(x) = 4x^2 - 2", color=BLUE, font_size=28),
            MathTex(r"H_3(x) = 8x^3 - 12x", color=BLUE, font_size=28),
            MathTex(r"H_4(x) = 16x^4 - 48x^2 + 12", color=BLUE, font_size=28),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        hermite_list.shift(DOWN * 0.3 + LEFT * 2)
        
        for h in hermite_list:
            self.play(Write(h), run_time=0.4)
            self.wait(0.2)
        
        self.wait(0.8)
        
        # フェードアウト
        self.play(
            FadeOut(hermite_intro), FadeOut(hermite_list),
            FadeOut(subtitle3)
        )
        self.wait(0.3)
        
        # === パート4: 直交性の公式 ===
        subtitle4 = Text("エルミート多項式の直交性", font_size=32, color=ORANGE)
        subtitle4.next_to(title, DOWN)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.5)
        
        # 公式の表示
        formula_label = Text("内積の公式:", color=YELLOW, font_size=28, weight=BOLD)
        formula_label.shift(UP * 1.8)
        self.play(Write(formula_label), run_time=0.5)
        self.wait(0.3)
        
        main_formula = MathTex(
            r"\langle H_n | H_m \rangle = \int_{-\infty}^{\infty} H_n(x) \, H_m(x) \, e^{-x^2} dx = 2^n \, n! \, \sqrt{\pi} \; \delta_{nm}",
            color=ORANGE, font_size=28
        )
        main_formula.shift(UP * 1.0)
        main_box = SurroundingRectangle(main_formula, color=ORANGE, buff=0.2)
        
        self.play(Write(main_formula), Create(main_box), run_time=1.0)
        self.wait(1.0)
        
        # クロネッカーのデルタの説明
        delta_label = Text("クロネッカーのデルタ:", color=YELLOW, font_size=24, weight=BOLD)
        delta_label.shift(UP * 0.0 + LEFT * 4)
        self.play(Write(delta_label), run_time=0.5)
        self.wait(0.3)
        
        delta_def = MathTex(
            r"\delta_{nm} = \begin{cases} 1 & (n = m) \\ 0 & (n \neq m) \end{cases}",
            color=WHITE, font_size=28
        )
        delta_def.next_to(delta_label, RIGHT, buff=0.3)
        self.play(Write(delta_def), run_time=0.8)
        self.wait(0.8)
        
        # 意味の説明
        meaning = VGroup(
            VGroup(
                MathTex(r"n = m", color=GREEN, font_size=26),
                Text("のとき：", color=WHITE, font_size=24),
                MathTex(r"\langle H_n | H_n \rangle = 2^n \, n! \, \sqrt{\pi}", color=GREEN, font_size=26),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                MathTex(r"n \neq m", color=RED, font_size=26),
                Text("のとき：", color=WHITE, font_size=24),
                MathTex(r"\langle H_n | H_m \rangle = 0", color=RED, font_size=26),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        meaning.shift(DOWN * 1.2)
        
        for m in meaning:
            self.play(Write(m), run_time=0.7)
            self.wait(0.4)
        
        self.wait(1.0)
        
        # フェードアウト
        self.play(
            FadeOut(formula_label), FadeOut(main_formula), FadeOut(main_box),
            FadeOut(delta_label), FadeOut(delta_def),
            FadeOut(meaning), FadeOut(subtitle4)
        )
        self.wait(0.3)
        
        # === パート5: 具体例で直交性を確認 ===
        subtitle5 = Text("具体例で直交性を確認", font_size=32, color=BLUE)
        subtitle5.next_to(title, DOWN)
        self.play(Write(subtitle5), run_time=0.6)
        self.wait(0.5)
        
        # n ≠ m のケース
        diff_label = Text("異なる基底同士 (n ≠ m) の内積:", color=RED, font_size=24, weight=BOLD)
        diff_label.shift(UP * 2.0 + LEFT * 3)
        self.play(Write(diff_label), run_time=0.5)
        self.wait(0.3)
        
        diff_calcs = VGroup(
            MathTex(
                r"\langle H_0 | H_1 \rangle = \int_{-\infty}^{\infty} 1 \cdot 2x \cdot e^{-x^2} dx = 0",
                color=RED, font_size=24
            ),
            MathTex(
                r"\langle H_0 | H_2 \rangle = \int_{-\infty}^{\infty} 1 \cdot (4x^2-2) \cdot e^{-x^2} dx = 0",
                color=RED, font_size=24
            ),
            MathTex(
                r"\langle H_1 | H_2 \rangle = \int_{-\infty}^{\infty} 2x \cdot (4x^2-2) \cdot e^{-x^2} dx = 0",
                color=RED, font_size=24
            ),
            MathTex(
                r"\langle H_1 | H_3 \rangle = \int_{-\infty}^{\infty} 2x \cdot (8x^3-12x) \cdot e^{-x^2} dx = 0",
                color=RED, font_size=24
            ),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        diff_calcs.next_to(diff_label, DOWN, buff=0.3, aligned_edge=LEFT)
        
        for calc in diff_calcs:
            self.play(Write(calc), run_time=0.6)
            self.wait(0.3)
        
        self.wait(0.5)
        
        # 全て0であることを強調
        all_zero = Text("全て 0 ！", color=RED, font_size=28, weight=BOLD)
        all_zero.next_to(diff_calcs, RIGHT, buff=0.5).shift(UP * 0.5)
        all_zero_box = SurroundingRectangle(all_zero, color=RED, buff=0.15)
        self.play(Write(all_zero), Create(all_zero_box), run_time=0.6)
        self.wait(0.8)
        
        # フェードアウト
        self.play(
            FadeOut(diff_label), FadeOut(diff_calcs),FadeOut(subtitle5),
            FadeOut(all_zero), FadeOut(all_zero_box),
        )
        self.wait(0.2)
        
        # n = m のケース
        # same_label = Text("同じ基底同士 (n = m) の内積:", color=GREEN, font_size=24, weight=BOLD)
        # same_label.shift(UP * 2.0 + LEFT * 4)
        # self.play(Write(same_label), run_time=0.5)
        # self.wait(0.3)
        
        # same_calcs = VGroup(
        #     MathTex(
        #         r"\langle H_0 | H_0 \rangle = \sqrt{\pi}",
        #         color=GREEN, font_size=26
        #     ),
        #     MathTex(
        #         r"\langle H_1 | H_1 \rangle = 2\sqrt{\pi}",
        #         color=GREEN, font_size=26
        #     ),
        #     MathTex(
        #         r"\langle H_2 | H_2 \rangle = 8\sqrt{\pi}",
        #         color=GREEN, font_size=26
        #     ),
        #     MathTex(
        #         r"\langle H_3 | H_3 \rangle = 48\sqrt{\pi}",
        #         color=GREEN, font_size=26
        #     ),
        # ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        # same_calcs.shift(UP * 0.5 + LEFT * 3)
        
        # # 右側に公式の値を並べる
        # formula_checks = VGroup(
        #     MathTex(r"= 2^0 \cdot 0! \cdot \sqrt{\pi}", color=WHITE, font_size=24),
        #     MathTex(r"= 2^1 \cdot 1! \cdot \sqrt{\pi}", color=WHITE, font_size=24),
        #     MathTex(r"= 2^2 \cdot 2! \cdot \sqrt{\pi}", color=WHITE, font_size=24),
        #     MathTex(r"= 2^3 \cdot 3! \cdot \sqrt{\pi}", color=WHITE, font_size=24),
        # )
        
        # for i, (calc, fcheck) in enumerate(zip(same_calcs, formula_checks)):
        #     self.play(Write(calc), run_time=0.5)
        #     fcheck.next_to(calc, RIGHT, buff=0.3)
        #     self.play(Write(fcheck), run_time=0.4)
        #     self.wait(0.2)
        
        # # チェックマーク
        # check_text = Text("✓ 公式と一致！", color=GREEN, font_size=24, weight=BOLD)
        # check_text.next_to(formula_checks, RIGHT, buff=0.5).shift(UP * 0.3)
        # self.play(Write(check_text), run_time=0.5)
        # self.wait(0.8)
        
        # # フェードアウト
        # self.play(
        #     FadeOut(same_label), FadeOut(same_calcs),
        #     FadeOut(formula_checks), FadeOut(check_text),
        #     FadeOut(subtitle5)
        # )
        # self.wait(0.3)
        
        # === パート6: 直交性の意味をまとめる ===
        subtitle6 = Text("直交基底がとれている！", font_size=32, color=GREEN)
        subtitle6.next_to(title, DOWN)
        self.play(Write(subtitle6), run_time=0.6)
        self.wait(0.5)
        
        # 内積行列のイメージ
        matrix_label = Text("基底同士の内積を行列で並べると:", color=YELLOW, font_size=24, weight=BOLD)
        matrix_label.shift(UP * 1.8)
        self.play(Write(matrix_label), run_time=0.6)
        self.wait(0.3)
        
        # 単項式の場合
        mono_matrix_label = Text("単項式基底", color=RED, font_size=24, weight=BOLD)
        mono_matrix_label.shift(UP * 1.0 + LEFT * 3.5)
        
        mono_matrix = MathTex(
            r"\begin{pmatrix}"
            r"\sqrt{\pi} & 0 & \frac{\sqrt{\pi}}{2} \\"
            r"0 & \frac{\sqrt{\pi}}{2} & 0 \\"
            r"\frac{\sqrt{\pi}}{2} & 0 & \frac{3\sqrt{\pi}}{4}"
            r"\end{pmatrix}",
            color=RED, font_size=24
        )
        mono_matrix.next_to(mono_matrix_label, DOWN, buff=0.3)
        
        # 非対角成分をハイライトしたい → 非ゼロ要素がある
        mono_note = Text("非対角成分に 0 でない値", color=RED, font_size=20)
        mono_note.next_to(mono_matrix, DOWN, buff=0.2)
        
        self.play(Write(mono_matrix_label), run_time=0.4)
        self.play(Write(mono_matrix), run_time=0.8)
        self.play(Write(mono_note), run_time=0.5)
        self.wait(0.5)
        
        # エルミート多項式の場合
        herm_matrix_label = Text("エルミート基底", color=GREEN, font_size=24, weight=BOLD)
        herm_matrix_label.shift(UP * 1.0 + RIGHT * 3.5)
        
        herm_matrix = MathTex(
            r"\begin{pmatrix}"
            r"\sqrt{\pi} & 0 & 0 \\"
            r"0 & 2\sqrt{\pi} & 0 \\"
            r"0 & 0 & 8\sqrt{\pi}"
            r"\end{pmatrix}",
            color=GREEN, font_size=24
        )
        herm_matrix.next_to(herm_matrix_label, DOWN, buff=0.3)
        
        herm_note = Text("対角行列！（直交基底の証）", color=GREEN, font_size=20, weight=BOLD)
        herm_note.next_to(herm_matrix, DOWN, buff=0.2)
        
        self.play(Write(herm_matrix_label), run_time=0.4)
        self.play(Write(herm_matrix), run_time=0.8)
        self.play(Write(herm_note), run_time=0.5)
        self.wait(1.0)
        
        # 矢印
        arrow = Arrow(LEFT * 0.8, RIGHT * 0.8, color=YELLOW, stroke_width=4)
        arrow.shift(DOWN * 0.5)
        arrow_label = Text("基底を変えるだけ！", color=YELLOW, font_size=22, weight=BOLD)
        arrow_label.next_to(arrow, DOWN, buff=0.1)
        self.play(Create(arrow), Write(arrow_label), run_time=0.6)
        self.wait(0.5)
        
        # 強調
        orthogonal_text = Text(
            "異なる基底同士の内積が全て 0 ＝ 直交基底",
            color=GREEN, font_size=26, weight=BOLD
        )
        orthogonal_text.shift(DOWN * 2.2)
        orthogonal_box = SurroundingRectangle(orthogonal_text, color=GREEN, buff=0.15)
        self.play(Write(orthogonal_text), Create(orthogonal_box), run_time=0.9)
        self.wait(1.2)
        
        # フェードアウト
        self.play(
            FadeOut(matrix_label),
            FadeOut(mono_matrix_label), FadeOut(mono_matrix), FadeOut(mono_note),
            FadeOut(herm_matrix_label), FadeOut(herm_matrix), FadeOut(herm_note),
            FadeOut(arrow), FadeOut(arrow_label),
            FadeOut(orthogonal_text), FadeOut(orthogonal_box),
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
                    Text("単項式基底 {1, x, x², ...} は", color=WHITE, font_size=24),
                    Text("（前回の内積定義だと）直交基底ではない", color=RED, font_size=24, weight=BOLD),
                ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("2.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("直交基底は計算上とても便利", color=WHITE, font_size=24),
                    Text("（座標が内積で求まる）", color=YELLOW, font_size=24, weight=BOLD),
                ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("3.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("エルミート多項式は直交基底をなす", color=WHITE, font_size=24),
                    MathTex(
                        r"\langle H_n | H_m \rangle = 2^n \, n! \, \sqrt{\pi} \; \delta_{nm}",
                        color=GREEN, font_size=24
                    ),
                ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("4.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("ノルムも積分なしで公式から求まる", color=WHITE, font_size=24),
                    Text("重み関数とのセットが鍵", color=ORANGE, font_size=24, weight=BOLD),
                ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        ).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        summary.scale(0.9)
        summary.shift(UP * 0.2)
        
        for point in summary:
            self.play(Write(point), run_time=0.8)
            self.wait(0.5)
        
        self.wait(1.0)
        
        # フェードアウト
        all_final = VGroup(
            summary, subtitle_end, title
        )
        self.play(FadeOut(all_final), run_time=1.0)
        self.wait(0.5)
