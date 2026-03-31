from manim import *
import numpy as np

class BasisChangeRepresentation(Scene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"

        # タイトル
        title = Text("基底が変われば表現行列も変わる", font_size=34, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)

        # === Part 1: 前回の復習 ===
        subtitle1 = Text("前回の復習: 単項式基底での微分", font_size=30, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.5)

        # 前回の基底
        prev_basis = VGroup(
            Text("基底:", color=ORANGE, font_size=24, weight=BOLD),
            MathTex(r"|1\rangle,\; |x\rangle,\; |x^2\rangle", color=ORANGE, font_size=26),
        ).arrange(RIGHT, buff=0.3)
        prev_basis.shift(UP * 1.6)
        self.play(Write(prev_basis), run_time=0.6)
        self.wait(0.3)

        # 前回の表現行列
        prev_matrix = MathTex(
            r"L_{\text{mono}} = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix}",
            color=YELLOW, font_size=28
        )
        prev_matrix.shift(UP * 0.4)
        prev_matrix_box = SurroundingRectangle(prev_matrix, color=YELLOW, buff=0.15)
        self.play(Write(prev_matrix), Create(prev_matrix_box), run_time=0.7)
        self.wait(0.5)

        # 説明
        prev_note = Text("微分作用素の表現行列（単項式基底）", color=WHITE, font_size=20, slant=ITALIC)
        prev_note.next_to(prev_matrix_box, DOWN, buff=0.2)
        self.play(Write(prev_note), run_time=0.5)
        self.wait(0.6)

        # 問いかけ
        question = VGroup(
            Text("基底を変えたらどうなる？", color=RED, font_size=26, weight=BOLD),
        )
        question.shift(DOWN * 1.5)
        q_box = SurroundingRectangle(question, color=RED, buff=0.2)
        self.play(Write(question), Create(q_box), run_time=0.7)
        self.wait(1.0)

        self.play(
            FadeOut(prev_basis), FadeOut(prev_matrix), FadeOut(prev_matrix_box),
            FadeOut(prev_note), FadeOut(question), FadeOut(q_box),
            FadeOut(subtitle1)
        )
        self.wait(0.3)

        # === Part 2: エルミート多項式基底の導入 ===
        subtitle2 = Text("新しい基底: エルミート多項式", font_size=30, color=PURPLE)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)

        # エルミート多項式の定義
        hermite_title = Text("エルミート多項式（次数2まで）:", color=ORANGE, font_size=24, weight=BOLD)
        hermite_title.shift(UP * 1.6)
        self.play(Write(hermite_title), run_time=0.5)
        self.wait(0.3)

        hermite_defs = VGroup(
            MathTex(r"H_0(x) = 1", color=WHITE, font_size=26),
            MathTex(r"H_1(x) = 2x", color=WHITE, font_size=26),
            MathTex(r"H_2(x) = 4x^2 - 2", color=WHITE, font_size=26),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        hermite_defs.shift(UP * 0.6)
        
        for hd in hermite_defs:
            self.play(Write(hd), run_time=0.5)
            self.wait(0.2)
        self.wait(0.5)

        # 新しい基底
        new_basis = VGroup(
            Text("新しい基底:", color=TEAL, font_size=24, weight=BOLD),
            MathTex(r"|H_0\rangle,\; |H_1\rangle,\; |H_2\rangle", color=TEAL, font_size=26),
        ).arrange(RIGHT, buff=0.3)
        new_basis.shift(DOWN * 0.8)
        new_basis_box = SurroundingRectangle(new_basis, color=TEAL, buff=0.15)
        self.play(Write(new_basis), Create(new_basis_box), run_time=0.7)
        self.wait(0.5)

        # 微分の結果
        diff_title = Text("これらを微分すると:", color=YELLOW, font_size=26, weight=BOLD)
        diff_title.shift(DOWN * 1.8 + LEFT * 4)
        self.play(Write(diff_title), run_time=0.4)

        diff_results = VGroup(
            MathTex(r"\frac{d}{dx}H_0 = 0", color=GREEN, font_size=28),
            MathTex(r"\frac{d}{dx}H_1 = 2 = 2H_0", color=GREEN, font_size=28),
            MathTex(r"\frac{d}{dx}H_2 = 8x = 4H_1", color=GREEN, font_size=28),
        ).arrange(RIGHT, buff=0.5)
        diff_results.shift(DOWN * 2.5)
        
        for dr in diff_results:
            self.play(Write(dr), run_time=0.5)
            self.wait(0.15)
        self.wait(0.8)

        self.play(
            FadeOut(hermite_title), FadeOut(hermite_defs),
            FadeOut(new_basis), FadeOut(new_basis_box),
            FadeOut(diff_title), FadeOut(diff_results),
            FadeOut(subtitle2)
        )
        self.wait(0.3)

        # === Part 3: h_1(x)の表現 ===
        subtitle3 = Text("関数の展開: 2つの基底で表す", font_size=30, color=GREEN)
        subtitle3.next_to(title, DOWN)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.5)

        # 同じ関数を2通りで表現
        same_func = Text("同じ多項式 h₁(x) を2つの基底で表す", color=YELLOW, font_size=24, weight=BOLD)
        same_func.shift(UP * 1.7)
        self.play(Write(same_func), run_time=0.6)
        self.wait(0.4)

        # 単項式基底での展開
        mono_label = Text("単項式基底:", color=BLUE, font_size=26, weight=BOLD)
        mono_label.shift(UP * 1.0 + LEFT * 5)
        self.play(Write(mono_label), run_time=0.4)

        h1_mono = MathTex(
            r"h_1(x) = c_{1,0}|1\rangle + c_{1,1}|x\rangle + c_{1,2}|x^2\rangle",
            color=BLUE, font_size=30
        )
        h1_mono.shift(UP * 0.4)
        self.play(Write(h1_mono), run_time=0.7)
        self.wait(0.3)

        # エルミート基底での展開
        herm_label = Text("エルミート基底:", color=PURPLE, font_size=26, weight=BOLD)
        herm_label.shift(DOWN * 0.3 + LEFT * 4.8)
        self.play(Write(herm_label), run_time=0.4)

        h1_herm = MathTex(
            r"h_1(x) = \tilde{c}_{1,0}|H_0\rangle + \tilde{c}_{1,1}|H_1\rangle + \tilde{c}_{1,2}|H_2\rangle",
            color=PURPLE, font_size=30
        )
        h1_herm.shift(DOWN * 0.9)
        self.play(Write(h1_herm), run_time=0.7)
        self.wait(0.5)

        # 係数の関係
        coeff_rel_title = Text("係数の関係:", color=ORANGE, font_size=26, weight=BOLD)
        coeff_rel_title.shift(DOWN * 1.7 + LEFT * 5)
        self.play(Write(coeff_rel_title), run_time=0.4)

        # H_0=1, H_1=2x, H_2=4x^2-2 を代入して比較
        coeff_rel = MathTex(
            r"\tilde{c}_{1,0} - 2\tilde{c}_{1,2} = c_{1,0}, \quad "
            r"2\tilde{c}_{1,1} = c_{1,1}, \quad "
            r"4\tilde{c}_{1,2} = c_{1,2}",
            color=WHITE, font_size=30
        )
        coeff_rel.shift(DOWN * 2.4)
        self.play(Write(coeff_rel), run_time=0.9)
        self.wait(1.0)

        self.play(
            FadeOut(same_func), FadeOut(mono_label), FadeOut(h1_mono),
            FadeOut(herm_label), FadeOut(h1_herm),
            FadeOut(coeff_rel_title), FadeOut(coeff_rel),
            FadeOut(subtitle3)
        )
        self.wait(0.3)

        # === Part 4: 微分後の h_2(x) の表現 ===
        subtitle4 = Text("微分後の関数も2つの基底で表す", font_size=30, color=TEAL)
        subtitle4.next_to(title, DOWN)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.5)

        # h_2 = L h_1
        h2_def = MathTex(
            r"h_2(x) = \mathcal{L} h_1(x) = \frac{d}{dx} h_1(x)",
            color=YELLOW, font_size=30
        )
        h2_def.shift(UP * 1.6)
        self.play(Write(h2_def), run_time=0.6)
        self.wait(0.4)

        # 単項式基底での h_2
        h2_mono_label = Text("単項式基底:", color=BLUE, font_size=26, weight=BOLD)
        h2_mono_label.shift(UP * 0.9 + LEFT * 5)
        self.play(Write(h2_mono_label), run_time=0.4)

        h2_mono = MathTex(
            r"h_2(x) = c_{1,1}|1\rangle + 2c_{1,2}|x\rangle + 0|x^2\rangle",
            color=BLUE, font_size=30
        )
        h2_mono.shift(UP * 0.3)
        self.play(Write(h2_mono), run_time=0.7)
        self.wait(0.3)

        # エルミート基底での h_2
        h2_herm_label = Text("エルミート基底:", color=PURPLE, font_size=26, weight=BOLD)
        h2_herm_label.shift(DOWN * 0.4 + LEFT * 4.8)
        self.play(Write(h2_herm_label), run_time=0.4)

        h2_herm = MathTex(
            r"h_2(x) = \tilde{c}_{2,0}|H_0\rangle + \tilde{c}_{2,1}|H_1\rangle + \tilde{c}_{2,2}|H_2\rangle",
            color=PURPLE, font_size=30
        )
        h2_herm.shift(DOWN * 1.0)
        self.play(Write(h2_herm), run_time=0.7)
        self.wait(0.5)

        # 係数の関係（h_2）
        coeff_rel2_title = Text("係数の関係:", color=ORANGE, font_size=26, weight=BOLD)
        coeff_rel2_title.shift(DOWN * 1.8 + LEFT * 5)
        self.play(Write(coeff_rel2_title), run_time=0.4)

        coeff_rel2 = MathTex(
            r"\tilde{c}_{2,0} - 2\tilde{c}_{2,2} = c_{1,1}, \quad "
            r"2\tilde{c}_{2,1} = 2c_{1,2}, \quad "
            r"4\tilde{c}_{2,2} = 0",
            color=WHITE, font_size=30
        )
        coeff_rel2.shift(DOWN * 2.5)
        self.play(Write(coeff_rel2), run_time=0.9)
        self.wait(1.0)

        self.play(
            FadeOut(h2_def), FadeOut(h2_mono_label), FadeOut(h2_mono),
            FadeOut(h2_herm_label), FadeOut(h2_herm),
            FadeOut(coeff_rel2_title), FadeOut(coeff_rel2),
            FadeOut(subtitle4)
        )
        self.wait(0.3)

        # === Part 5: 係数変換の導出 ===
        subtitle5 = Text("エルミート基底での係数変換", font_size=30, color=GOLD)
        subtitle5.next_to(title, DOWN)
        self.play(Write(subtitle5), run_time=0.6)
        self.wait(0.5)

        # 関係式から解く
        solve_title = Text("先ほどの関係式を整理すると:", color=YELLOW, font_size=24, weight=BOLD)
        solve_title.shift(UP * 1.6)
        self.play(Write(solve_title), run_time=0.5)
        self.wait(0.3)

        # h_2のエルミート係数を h_1のエルミート係数で表す
        solve_step1 = MathTex(
            r"\tilde{c}_{2,2} = 0",
            color=WHITE, font_size=32
        )
        solve_step1.shift(UP * 0.9)
        self.play(Write(solve_step1), run_time=0.5)
        self.wait(0.2)

        solve_step2 = MathTex(
            r"\tilde{c}_{2,1} = c_{1,2} = 4\tilde{c}_{1,2}",
            color=WHITE, font_size=32
        )
        solve_step2.shift(UP * 0.3)
        self.play(Write(solve_step2), run_time=0.5)
        self.wait(0.2)

        solve_step3 = MathTex(
            r"\tilde{c}_{2,0} = c_{1,1} = 2\tilde{c}_{1,1}",
            color=WHITE, font_size=32
        )
        solve_step3.shift(DOWN * 0.3)
        self.play(Write(solve_step3), run_time=0.5)
        self.wait(0.5)

        # ベクトル形式で
        vec_form_title = Text("ベクトル形式で書くと:", color=ORANGE, font_size=22, weight=BOLD)
        vec_form_title.shift(DOWN * 1.1 + LEFT * 4)
        self.play(Write(vec_form_title), run_time=0.4)

        vec_form = MathTex(
            r"\begin{pmatrix} \tilde{c}_{2,0} \\ \tilde{c}_{2,1} \\ \tilde{c}_{2,2} \end{pmatrix}"
            r"= \begin{pmatrix} 2\tilde{c}_{1,1} \\ 4\tilde{c}_{1,2} \\ 0 \end{pmatrix}",
            color=GREEN, font_size=32
        )
        vec_form.shift(DOWN * 2.3)
        vec_form_box = SurroundingRectangle(vec_form, color=GREEN, buff=0.15)
        self.play(Write(vec_form), Create(vec_form_box), run_time=0.8)
        self.wait(1.0)

        self.play(
            FadeOut(solve_title), FadeOut(solve_step1), FadeOut(solve_step2), FadeOut(solve_step3),
            FadeOut(vec_form_title), FadeOut(vec_form), FadeOut(vec_form_box),
            FadeOut(subtitle5)
        )
        self.wait(0.3)

        # === Part 6: 新しい表現行列 ===
        subtitle6 = Text("エルミート基底での表現行列", font_size=30, color=RED)
        subtitle6.next_to(title, DOWN)
        self.play(Write(subtitle6), run_time=0.6)
        self.wait(0.5)

        # この変換を行列で表す
        matrix_intro = Text("この係数変換を行列で表すと:", color=YELLOW, font_size=24, weight=BOLD)
        matrix_intro.shift(UP * 1.6)
        self.play(Write(matrix_intro), run_time=0.5)
        self.wait(0.3)

        # 行列方程式
        matrix_eq = MathTex(
            r"\begin{pmatrix} \tilde{c}_{2,0} \\ \tilde{c}_{2,1} \\ \tilde{c}_{2,2} \end{pmatrix}"
            r"= \begin{pmatrix} 0 & 2 & 0 \\ 0 & 0 & 4 \\ 0 & 0 & 0 \end{pmatrix}"
            r"\begin{pmatrix} \tilde{c}_{1,0} \\ \tilde{c}_{1,1} \\ \tilde{c}_{1,2} \end{pmatrix}",
            color=WHITE, font_size=26
        )
        matrix_eq.shift(UP * 0.5)
        self.play(Write(matrix_eq), run_time=0.9)
        self.wait(0.6)

        # 新しい表現行列
        new_matrix_title = Text("エルミート基底での微分の表現行列:", color=ORANGE, font_size=22, weight=BOLD)
        new_matrix_title.shift(DOWN * 0.7 + LEFT * 2.5)
        self.play(Write(new_matrix_title), run_time=0.5)

        new_matrix = MathTex(
            r"L_{\text{Hermite}} = \begin{pmatrix} 0 & 2 & 0 \\ 0 & 0 & 4 \\ 0 & 0 & 0 \end{pmatrix}",
            color=RED, font_size=32
        )
        new_matrix.shift(DOWN * 1.8)
        new_matrix_box = SurroundingRectangle(new_matrix, color=RED, buff=0.2)
        self.play(Write(new_matrix), Create(new_matrix_box), run_time=0.8)
        self.wait(1.0)

        self.play(
            FadeOut(matrix_intro), FadeOut(matrix_eq),
            FadeOut(new_matrix_title), FadeOut(new_matrix), FadeOut(new_matrix_box),
            FadeOut(subtitle6)
        )
        self.wait(0.3)

        # === Part 7: 2つの表現行列の比較 ===
        subtitle7 = Text("2つの表現行列の比較", font_size=30, color=GOLD)
        subtitle7.next_to(title, DOWN)
        self.play(Write(subtitle7), run_time=0.6)
        self.wait(0.5)

        # 並べて比較
        compare_title = Text("同じ微分作用素、異なる表現行列", color=YELLOW, font_size=26, weight=BOLD)
        compare_title.shift(UP * 1.6)
        self.play(Write(compare_title), run_time=0.6)
        self.wait(0.4)

        # 左: 単項式基底
        mono_side = VGroup(
            Text("単項式基底", color=BLUE, font_size=26, weight=BOLD),
            MathTex(r"|1\rangle, |x\rangle, |x^2\rangle", color=BLUE, font_size=28),
            MathTex(
                r"L_{\text{mono}} = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix}",
                color=YELLOW, font_size=32
            ),
        ).arrange(DOWN, buff=0.3)
        mono_side.shift(LEFT * 3.5 + DOWN * 0.3)

        # 右: エルミート基底
        herm_side = VGroup(
            Text("エルミート基底", color=PURPLE, font_size=26, weight=BOLD),
            MathTex(r"|H_0\rangle, |H_1\rangle, |H_2\rangle", color=PURPLE, font_size=28),
            MathTex(
                r"L_{\text{Hermite}} = \begin{pmatrix} 0 & 2 & 0 \\ 0 & 0 & 4 \\ 0 & 0 & 0 \end{pmatrix}",
                color=RED, font_size=32
            ),
        ).arrange(DOWN, buff=0.3)
        herm_side.shift(RIGHT * 3.5 + DOWN * 0.3)

        # 仕切り線
        divider = DashedLine(
            UP * 1.0, DOWN * 2.0,
            color=GRAY, stroke_width=2
        )

        self.play(Write(mono_side), run_time=0.8)
        self.play(Create(divider), run_time=0.3)
        self.play(Write(herm_side), run_time=0.8)
        self.wait(0.6)

        # 不等号
        neq_symbol = MathTex(r"\neq", color=RED, font_size=40)
        neq_symbol.shift(DOWN * 1.5)
        self.play(Write(neq_symbol), run_time=0.5)
        self.wait(0.5)

        # 強調
        diff_note = Text("行列の成分が異なる！", color=RED, font_size=24, weight=BOLD)
        diff_note.shift(DOWN * 2.5)
        self.play(Write(diff_note), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(compare_title), FadeOut(mono_side), FadeOut(herm_side),
            FadeOut(divider), FadeOut(neq_symbol), FadeOut(diff_note),
            FadeOut(subtitle7)
        )
        self.wait(0.3)

        # === Part 8: 本質は変わらない ===
        subtitle8 = Text("しかし、本質は変わらない！", font_size=30, color=GREEN)
        subtitle8.next_to(title, DOWN)
        self.play(Write(subtitle8), run_time=0.6)
        self.wait(0.5)

        # 本質の強調
        essence_box_content = VGroup(
            Text("どちらの行列も", color=WHITE, font_size=26),
            Text("「微分」", color=YELLOW, font_size=32, weight=BOLD),
            Text("という同じ操作を表している", color=WHITE, font_size=26),
        ).arrange(DOWN, buff=0.3)
        essence_box_content.shift(UP * 0.8)
        essence_box = SurroundingRectangle(essence_box_content, color=GREEN, buff=0.3)
        self.play(Write(essence_box_content), Create(essence_box), run_time=0.9)
        self.wait(0.8)

        # 比喩
        analogy = VGroup(
            Text("同じ人を", color=WHITE, font_size=24),
            Text("日本語で「山田太郎」", color=BLUE, font_size=24),
            Text("英語で \"Taro Yamada\"", color=PURPLE, font_size=24),
            Text("と呼ぶようなもの", color=WHITE, font_size=24),
        ).arrange(DOWN, buff=0.2)
        analogy.shift(DOWN * 1.5)
        self.play(Write(analogy), run_time=0.8)
        self.wait(0.8)

        # 結論
        conclusion = VGroup(
            Text("表現（行列）が変わっても", color=WHITE, font_size=24),
            Text("操作の本質（微分）は不変", color=YELLOW, font_size=26, weight=BOLD),
        ).arrange(DOWN, buff=0.2)
        conclusion.shift(DOWN * 3.0)
        concl_box = SurroundingRectangle(conclusion, color=YELLOW, buff=0.15)
        self.play(Write(conclusion), Create(concl_box), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(essence_box_content), FadeOut(essence_box),
            FadeOut(analogy), FadeOut(conclusion), FadeOut(concl_box),
            FadeOut(subtitle8)
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
                    Text("同じ微分作用素でも基底によって表現行列が異なる", color=WHITE, font_size=29),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("2.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("単項式基底:", color=BLUE, font_size=29),
                    MathTex(r"L = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix}", color=BLUE, font_size=29),
                ).arrange(RIGHT, buff=0.2),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("3.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("エルミート基底:", color=PURPLE, font_size=29),
                    MathTex(r"L = \begin{pmatrix} 0 & 2 & 0 \\ 0 & 0 & 4 \\ 0 & 0 & 0 \end{pmatrix}", color=PURPLE, font_size=29),
                ).arrange(RIGHT, buff=0.2),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("4.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("行列は違っても操作の本質は同じ", color=WHITE, font_size=29),
                    Text("→ これが「表現」の意味", color=YELLOW, font_size=29, weight=BOLD),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        summary.scale(0.9)
        summary.shift(UP * 0.2)

        for point in summary:
            self.play(Write(point), run_time=0.7)
            self.wait(0.4)

        self.wait(1.5)

        all_final = VGroup(summary, subtitle_end, title)
        self.play(FadeOut(all_final), run_time=1.0)
        self.wait(0.5)
