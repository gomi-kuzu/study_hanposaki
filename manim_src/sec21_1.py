from manim import *
import numpy as np


class MatrixDifferentialEquation(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        title = Text("行列を使った微分方程式の解法", font_size=36, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.7)

        # ============================================================
        # Part 1: おさらい
        # ============================================================
        subtitle1 = Text("おさらい", font_size=28, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.4)

        review_text = Text(
            "前回、行列の指数関数を次のように定義した",
            color=WHITE, font_size=26,
        )
        review_text.shift(UP * 1.8)
        self.play(Write(review_text), run_time=0.7)
        self.wait(0.4)

        review_eq = MathTex(
            r"e^A = \sum_{n=0}^{\infty} \frac{1}{n!}A^n",
            color=YELLOW,
            font_size=38,
        )
        review_eq.shift(UP * 0.8)
        self.play(Write(review_eq), run_time=0.8)
        self.wait(0.6)

        purpose_text = Text(
            "今回はこれを使って、行列の微分方程式の一般解を見ていく",
            color=GREEN, font_size=26, weight=BOLD,
        )
        purpose_text.shift(DOWN * 0.3)
        self.play(Write(purpose_text), run_time=0.8)
        self.wait(1.2)

        self.play(
            FadeOut(review_text), FadeOut(review_eq), FadeOut(purpose_text),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: 微分方程式の設定
        # ============================================================
        subtitle2 = Text("微分方程式の設定", font_size=28, color=GOLD)
        subtitle2.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle2), run_time=0.5)
        self.wait(0.4)

        setup_text = Text(
            "D次元の状態ベクトルを x⃗、時間発展を与える行列をLとおく",
            color=WHITE, font_size=26,
        )
        setup_text.shift(UP * 1.8)
        self.play(Write(setup_text), run_time=0.8)
        self.wait(0.5)

        diff_eq = MathTex(
            r"\frac{d}{dt}\mathbf{x} = L\mathbf{x}",
            color=YELLOW,
            font_size=42,
        )
        diff_eq.shift(UP * 0.8)
        diff_box = SurroundingRectangle(diff_eq, color=YELLOW, buff=0.25)
        self.play(Write(diff_eq), Create(diff_box), run_time=0.8)
        self.wait(0.7)

        solution_text = Text(
            "この微分方程式の解は",
            color=WHITE, font_size=26,
        )
        solution_text.shift(DOWN * 0.3)
        self.play(Write(solution_text), run_time=0.7)
        self.wait(0.4)

        solution_eq = MathTex(
            r"\mathbf{x}(t) = e^{Lt}\mathbf{x}(0)",
            color=GREEN,
            font_size=42,
        )
        solution_eq.shift(DOWN * 1.2)
        solution_box = SurroundingRectangle(solution_eq, color=GREEN, buff=0.25)
        self.play(Write(solution_eq), Create(solution_box), run_time=0.8)
        self.wait(0.6)

        initial_note = Text(
            "ここで、x⃗(0)は時刻t=0の状態",
            color=TEAL, font_size=24,
        )
        initial_note.shift(DOWN * 2.3)
        self.play(Write(initial_note), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(setup_text), FadeOut(solution_text), FadeOut(initial_note),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: 固有値・固有ベクトルによる展開
        # ============================================================
        subtitle3 = Text("固有値・固有ベクトルによる展開", font_size=28, color=TEAL)
        subtitle3.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle3), run_time=0.5)
        self.wait(0.4)

        # diff_eqとsolution_eqを上に移動
        self.play(
            diff_eq.animate.shift(UP * 2.5).scale(0.8),
            diff_box.animate.shift(UP * 2.5).scale(0.8),
            solution_eq.animate.shift(UP * 3.2).scale(0.8),
            solution_box.animate.shift(UP * 3.2).scale(0.8),
            run_time=0.6
        )
        self.wait(0.3)

        eigen_text = Text(
            "Lの固有値をλₐ、固有ベクトルをv⃗ₐとする",
            color=WHITE, font_size=26,
        )
        eigen_text.shift(UP * 1.2)
        self.play(Write(eigen_text), run_time=0.7)
        self.wait(0.5)

        assumption = Text(
            "簡単のため、Lは互いに異なるD個の固有値を持つとする",
            color=ORANGE, font_size=24,
        )
        assumption.shift(UP * 0.7)
        self.play(Write(assumption), run_time=0.7)
        self.wait(0.5)

        expansion_text = Text(
            "すると、x⃗(t)は固有ベクトルの線形結合で表せる",
            color=WHITE, font_size=26,
        )
        expansion_text.shift(DOWN * 0.0)
        self.play(Write(expansion_text), run_time=0.7)
        self.wait(0.5)

        expansion_eq = MathTex(
            r"\mathbf{x}(t) = c_1 e^{\lambda_1 t}\mathbf{v}_1 + c_2 e^{\lambda_2 t}\mathbf{v}_2 + \cdots + c_D e^{\lambda_D t}\mathbf{v}_D",
            color=YELLOW,
            font_size=30,
        )
        expansion_eq.shift(DOWN * 0.9)
        self.play(Write(expansion_eq), run_time=1.0)
        self.wait(0.7)

        expansion_eq_sum = MathTex(
            r"= \sum_{d=1}^{D} c_d e^{\lambda_d t}\mathbf{v}_d",
            color=YELLOW,
            font_size=36,
        )
        expansion_eq_sum.shift(DOWN * 1.7)
        expansion_box = SurroundingRectangle(expansion_eq_sum, color=YELLOW, buff=0.25)
        self.play(Write(expansion_eq_sum), Create(expansion_box), run_time=0.8)
        self.wait(1.0)

        self.play(
            FadeOut(eigen_text), FadeOut(assumption), 
            FadeOut(expansion_text), FadeOut(expansion_eq),
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: 係数の求め方
        # ============================================================
        subtitle4 = Text("係数の求め方", font_size=28, color=BLUE)
        subtitle4.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle4), run_time=0.5)
        self.wait(0.4)

        # expansion_eq_sumを上に移動
        self.play(
            expansion_eq_sum.animate.shift(UP * 3.8).scale(0.85),
            expansion_box.animate.shift(UP * 3.8).scale(0.85),
            diff_eq.animate.shift(LEFT * 1.8).scale(0.9),
            diff_box.animate.shift(LEFT * 1.8).scale(0.9),
            solution_eq.animate.shift(RIGHT * 1.5).scale(0.9),
            solution_box.animate.shift(RIGHT * 1.5).scale(0.9),
            run_time=0.6
        )
        self.wait(0.3)

        coeff_text = Text(
            "係数{cₐ}は、t=0を代入してx⃗(0)と等しいとおくことで求まる",
            color=WHITE, font_size=26,
        )
        coeff_text.shift(UP * 1.2)
        self.play(Write(coeff_text), run_time=0.8)
        self.wait(0.5)

        coeff_eq1 = MathTex(
            r"c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \cdots + c_D\mathbf{v}_D = \mathbf{x}(0)",
            color=BLUE,
            font_size=32,
        )
        coeff_eq1.shift(UP * 0.4)
        self.play(Write(coeff_eq1), run_time=0.8)
        self.wait(0.6)

        matrix_form = Text(
            "これは行列形式で書くと",
            color=WHITE, font_size=24,
        )
        matrix_form.shift(DOWN * 0.4)
        self.play(Write(matrix_form), run_time=0.6)
        self.wait(0.4)

        coeff_eq2 = MathTex(
            r"[\mathbf{v}_1 \cdots \mathbf{v}_D]\begin{bmatrix}c_1 \\ \vdots \\ c_D \end{bmatrix} = \mathbf{x}(0)",
            color=GREEN,
            font_size=36,
        )
        coeff_eq2.shift(DOWN * 1.3)
        coeff_box = SurroundingRectangle(coeff_eq2, color=GREEN, buff=0.25)
        self.play(Write(coeff_eq2), Create(coeff_box), run_time=0.8)
        self.wait(0.7)

        solve_text = Text(
            "この連立方程式を解けば係数が求まる",
            color=ORANGE, font_size=24, weight=BOLD,
        )
        solve_text.shift(DOWN * 2.4)
        self.play(Write(solve_text), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(coeff_text), FadeOut(coeff_eq1),
            FadeOut(matrix_form), FadeOut(solve_text),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: 対角化との等価性（前半）
        # ============================================================
        subtitle5 = Text("対角化との等価性", font_size=28, color=GOLD)
        subtitle5.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle5), run_time=0.5)
        self.wait(0.4)

        # coeff_eq2を右下に移動
        self.play(
            coeff_eq2.animate.shift(DOWN * 0.5 + RIGHT * 2.5).scale(0.8),
            coeff_box.animate.shift(DOWN * 0.5 + RIGHT * 2.5).scale(0.8),
            expansion_eq_sum.animate.shift(LEFT * 2.8).scale(0.95),
            expansion_box.animate.shift(LEFT * 2.8).scale(0.95),
            diff_eq.animate.shift(UP * 0.3),
            diff_box.animate.shift(UP * 0.3),
            solution_eq.animate.shift(UP * 0.3),
            solution_box.animate.shift(UP * 0.3),
            run_time=0.6
        )
        self.wait(0.3)

        equiv_text = Text(
            "実は、これは前回説明した対角化を使った計算と厳密に等しい",
            color=ORANGE, font_size=26, weight=BOLD,
        )
        equiv_text.shift(UP * 1.2)
        self.play(Write(equiv_text), run_time=0.8)
        self.wait(0.6)

        matrix_exp_text = Text(
            "行列の指数関数を書き下すと",
            color=WHITE, font_size=24,
        )
        matrix_exp_text.shift(UP * 0.6)
        self.play(Write(matrix_exp_text), run_time=0.6)
        self.wait(0.4)

        diag_form = MathTex(
            r"e^{Lt} = P \text{diag}(e^{\lambda_1 t}, \cdots, e^{\lambda_D t}) P^{-1}",
            color=BLUE,
            font_size=32,
        )
        diag_form.shift(DOWN * 0.1)
        self.play(Write(diag_form), run_time=0.9)
        self.wait(0.7)

        therefore = Text(
            "よって、",
            color=WHITE, font_size=24,
        )
        therefore.shift(DOWN * 0.8)
        self.play(Write(therefore), run_time=0.5)
        self.wait(0.3)

        step1 = MathTex(
            r"e^{Lt}\mathbf{x}(0) = P \text{diag}(e^{\lambda_1 t}, \cdots, e^{\lambda_D t}) P^{-1}\mathbf{x}(0)",
            color=YELLOW,
            font_size=28,
        )
        step1.shift(DOWN * 1.5)
        self.play(Write(step1), run_time=0.9)
        self.wait(0.8)

        self.play(
            FadeOut(equiv_text), FadeOut(matrix_exp_text), 
            FadeOut(diag_form), FadeOut(therefore),
            FadeOut(diff_eq), FadeOut(diff_box),
            FadeOut(solution_eq), FadeOut(solution_box),
        )
        self.wait(0.3)

        # ============================================================
        # Part 6: 対角化との等価性（後半）
        # ============================================================
        subtitle6 = Text("計算の展開", font_size=28, color=TEAL)
        subtitle6.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle6), run_time=0.5)
        self.wait(0.4)

        # step1を上に移動
        self.play(
            step1.animate.shift(UP * 3.2).scale(0.95),
            expansion_eq_sum.animate.shift(RIGHT * 2.8),
            expansion_box.animate.shift(RIGHT * 2.8),
            coeff_eq2.animate.shift(LEFT * 2.5),
            coeff_box.animate.shift(LEFT * 2.5),
            run_time=0.6
        )
        self.wait(0.3)

        define_c = Text(
            "ここで、P⁻¹x⃗(0) = c⃗ とおく",
            color=ORANGE, font_size=26,
        )
        define_c.shift(UP * 1.2)
        self.play(Write(define_c), run_time=0.7)
        self.wait(0.5)

        step2 = MathTex(
            r"= P \text{diag}(e^{\lambda_1 t}, \cdots, e^{\lambda_D t}) \mathbf{c}",
            color=YELLOW,
            font_size=32,
        )
        step2.shift(UP * 0.5)
        self.play(Write(step2), run_time=0.8)
        self.wait(0.6)

        calc_text = Text(
            "Pより右を計算して",
            color=WHITE, font_size=24,
        )
        calc_text.shift(DOWN * 0.2)
        self.play(Write(calc_text), run_time=0.6)
        self.wait(0.4)

        step3 = MathTex(
            r"= P \begin{bmatrix}c_1 e^{\lambda_1 t} \\ \vdots \\ c_D e^{\lambda_D t} \end{bmatrix}",
            color=BLUE,
            font_size=34,
        )
        step3.shift(DOWN * 1.1)
        self.play(Write(step3), run_time=0.8)
        self.wait(0.6)

        step4 = MathTex(
            r"= [\mathbf{v}_1 \cdots \mathbf{v}_D] \begin{bmatrix}c_1 e^{\lambda_1 t} \\ \vdots \\ c_D e^{\lambda_D t} \end{bmatrix}",
            color=BLUE,
            font_size=32,
        )
        step4.shift(DOWN * 2.1)
        self.play(Write(step4), run_time=0.9)
        self.wait(0.7)

        step5 = MathTex(
            r"= \sum_{d=1}^{D} c_d e^{\lambda_d t}\mathbf{v}_d",
            color=GREEN,
            font_size=36,
        )
        step5.shift(DOWN * 3.1)
        step5_box = SurroundingRectangle(step5, color=GREEN, buff=0.25)
        self.play(Write(step5), Create(step5_box), run_time=0.8)
        self.wait(0.8)

        conclusion1 = Text(
            "→ 線形結合の形と一致！",
            color=GREEN, font_size=24, weight=BOLD,
        )
        conclusion1.next_to(step5_box, RIGHT, buff=0.3)
        self.play(Write(conclusion1), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(step1), FadeOut(define_c), FadeOut(step2),
            FadeOut(calc_text), FadeOut(step3), FadeOut(step4),
            FadeOut(conclusion1),
        )
        self.wait(0.3)

        # ============================================================
        # Part 7: 係数の等価性
        # ============================================================
        subtitle7 = Text("係数の等価性", font_size=28, color=BLUE)
        subtitle7.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle7), run_time=0.5)
        self.wait(0.4)

        # step5を上に移動
        self.play(
            step5.animate.shift(UP * 4.8 + LEFT * 3.0).scale(0.8),
            step5_box.animate.shift(UP * 4.8 + LEFT * 3.0).scale(0.8),
            expansion_eq_sum.animate.shift(DOWN * 0.3 + RIGHT * 2.0).scale(0.95),
            expansion_box.animate.shift(DOWN * 0.3 + RIGHT * 2.0).scale(0.95),
            coeff_eq2.animate.shift(DOWN * 0.3).scale(1.05),
            coeff_box.animate.shift(DOWN * 0.3).scale(1.05),
            run_time=0.6
        )
        self.wait(0.3)

        also_text = Text(
            "また、P⁻¹x⃗(0) = c⃗ とおいたので",
            color=WHITE, font_size=26,
        )
        also_text.shift(UP * 0.8)
        self.play(Write(also_text), run_time=0.7)
        self.wait(0.5)

        multiply_p = Text(
            "両辺左からPをかけて",
            color=WHITE, font_size=24,
        )
        multiply_p.shift(UP * 0.3)
        self.play(Write(multiply_p), run_time=0.6)
        self.wait(0.4)

        equiv_coeff = MathTex(
            r"\mathbf{x}(0) = P\mathbf{c}",
            color=BLUE,
            font_size=38,
        )
        equiv_coeff.shift(DOWN * 0.6)
        self.play(Write(equiv_coeff), run_time=0.8)
        self.wait(0.6)

        expand_equiv = MathTex(
            r"= [\mathbf{v}_1 \cdots \mathbf{v}_D]\begin{bmatrix}c_1 \\ \vdots \\ c_D \end{bmatrix}",
            color=BLUE,
            font_size=36,
        )
        expand_equiv.shift(DOWN * 1.5)
        equiv_box2 = SurroundingRectangle(expand_equiv, color=BLUE, buff=0.25)
        self.play(Write(expand_equiv), Create(equiv_box2), run_time=0.8)
        self.wait(0.7)

        conclusion2 = Text(
            "→ これも先ほどの連立方程式と等しい！",
            color=GREEN, font_size=24, weight=BOLD,
        )
        conclusion2.shift(DOWN * 2.6)
        self.play(Write(conclusion2), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(step5), FadeOut(step5_box),
            FadeOut(expansion_eq_sum), FadeOut(expansion_box),
            FadeOut(coeff_eq2), FadeOut(coeff_box),
            FadeOut(also_text), FadeOut(multiply_p),
            FadeOut(equiv_coeff), FadeOut(expand_equiv),
            FadeOut(equiv_box2), FadeOut(conclusion2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 8: 具体例の導入
        # ============================================================
        subtitle8 = Text("具体例：バネマスダンパ系", font_size=28, color=GOLD)
        subtitle8.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle8), run_time=0.5)
        self.wait(0.4)

        example_intro = Text(
            "19話、20話で用いたバネマスダンパ系で実際に計算してみる",
            color=WHITE, font_size=26,
        )
        example_intro.shift(UP * 1.8)
        self.play(Write(example_intro), run_time=0.8)
        self.wait(0.6)

        param_text = Text(
            "パラメータ：m=1, k=3, γ=1/2",
            color=TEAL, font_size=26,
        )
        param_text.shift(UP * 1.2)
        self.play(Write(param_text), run_time=0.7)
        self.wait(0.5)

        matrix_l = MathTex(
            r"L = \begin{bmatrix} 0 & 1 \\ -3 & -\frac{1}{2} \end{bmatrix}",
            color=YELLOW,
            font_size=40,
        )
        matrix_l.shift(UP * 0.3)
        matrix_l_box = SurroundingRectangle(matrix_l, color=YELLOW, buff=0.25)
        self.play(Write(matrix_l), Create(matrix_l_box), run_time=0.8)
        self.wait(0.7)

        eigen_intro = Text(
            "この行列は2つの共役な複素数を固有値に持つ",
            color=WHITE, font_size=26,
        )
        eigen_intro.shift(DOWN * 0.7)
        self.play(Write(eigen_intro), run_time=0.8)
        self.wait(0.6)

        eigenvalues = MathTex(
            r"\lambda_1 = \frac{1}{4}(-1 + j\sqrt{47}), \quad \lambda_2 = \frac{1}{4}(-1 - j\sqrt{47})",
            color=BLUE,
            font_size=32,
        )
        eigenvalues.shift(DOWN * 1.5)
        self.play(Write(eigenvalues), run_time=1.0)
        self.wait(0.8)

        note_j = Text(
            "（jは虚数単位）",
            color=GRAY, font_size=22,
        )
        note_j.shift(DOWN * 2.1)
        self.play(Write(note_j), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(example_intro), FadeOut(param_text),
            FadeOut(eigen_intro),
        )
        self.wait(0.3)

        # ============================================================
        # Part 9: 時間発展式と減衰振動
        # ============================================================
        subtitle9 = Text("時間発展と減衰振動", font_size=28, color=TEAL)
        subtitle9.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle9), run_time=0.5)
        self.wait(0.4)

        # matrix_lとeigenvaluesを上に移動
        self.play(
            matrix_l.animate.shift(UP * 1.8).scale(0.8),
            matrix_l_box.animate.shift(UP * 1.8).scale(0.8),
            eigenvalues.animate.shift(UP * 2.8).scale(0.85),
            note_j.animate.shift(UP * 2.8),
            run_time=0.6
        )
        self.wait(0.3)

        evolution_text = Text(
            "このとき線形結合で表した時間発展式は",
            color=WHITE, font_size=26,
        )
        evolution_text.shift(UP * 0.8)
        self.play(Write(evolution_text), run_time=0.7)
        self.wait(0.5)

        evolution_eq = MathTex(
            r"\mathbf{x}(t) = c_1 e^{\frac{1}{4}(-1+j\sqrt{47})t}\mathbf{v}_1 + c_2 e^{\frac{1}{4}(-1-j\sqrt{47})t}\mathbf{v}_2",
            color=YELLOW,
            font_size=26,
        )
        evolution_eq.shift(UP * 0.1)
        self.play(Write(evolution_eq), run_time=1.0)
        self.wait(0.8)

        euler_text = Text(
            "虚部の指数関数はオイラーの公式により周期関数の成分を持つ",
            color=ORANGE, font_size=24,
        )
        euler_text.shift(DOWN * 0.7)
        self.play(Write(euler_text), run_time=0.8)
        self.wait(0.6)

        euler_formula = MathTex(
            r"e^{j\theta} = \cos\theta + j\sin\theta",
            color=BLUE,
            font_size=32,
        )
        euler_formula.shift(DOWN * 1.4)
        self.play(Write(euler_formula), run_time=0.8)
        self.wait(0.7)

        oscillation = Text(
            "→ これが振動として振る舞いに現れる",
            color=WHITE, font_size=24,
        )
        oscillation.shift(DOWN * 2.1)
        self.play(Write(oscillation), run_time=0.7)
        self.wait(0.6)

        decay = Text(
            "加えて、実部が負の指数関数e^{-t/4}で減衰する",
            color=GREEN, font_size=24, weight=BOLD,
        )
        decay.shift(DOWN * 2.7)
        self.play(Write(decay), run_time=0.8)
        self.wait(0.7)

        result = Text(
            "→ 全体としては減衰振動となる",
            color=GREEN, font_size=26, weight=BOLD,
        )
        result.shift(DOWN * 3.3)
        self.play(Write(result), run_time=0.8)
        self.wait(1.2)

        self.play(
            FadeOut(matrix_l), FadeOut(matrix_l_box),
            FadeOut(eigenvalues), FadeOut(note_j),
            FadeOut(evolution_text), FadeOut(evolution_eq),
            FadeOut(euler_text), FadeOut(euler_formula),
            FadeOut(oscillation), FadeOut(decay), FadeOut(result),
        )
        self.wait(0.3)

        # ============================================================
        # Part 10: 減衰振動のグラフ
        # ============================================================
        subtitle10 = Text("減衰振動のグラフ", font_size=28, color=BLUE)
        subtitle10.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle10), run_time=0.5)
        self.wait(0.4)

        # 実際の数値計算（m=1, k=3, gamma=0.5）
        # 固有値: lambda1 = (-1 + j*sqrt(47))/4, lambda2 = (-1 - j*sqrt(47))/4
        # 初期条件: x(0) = [1, 0] (位置1, 速度0)
        
        # グラフの作成
        axes1 = Axes(
            x_range=[0, 10, 2],
            y_range=[-1, 1, 0.5],
            x_length=5.5,
            y_length=3.5,
            axis_config={"color": WHITE, "include_numbers": True, "font_size": 20},
            tips=False,
        )
        axes1.shift(LEFT * 3 + DOWN * 0.3)
        
        axes1_labels = axes1.get_axis_labels(x_label="t", y_label="x")
        
        # 時間配列
        t_vals = np.linspace(0, 10, 300)
        
        # 固有値
        lambda1 = (-1 + 1j * np.sqrt(47)) / 4
        lambda2 = (-1 - 1j * np.sqrt(47)) / 4
        
        # 固有ベクトル（概算）
        v1 = np.array([1, lambda1])
        v2 = np.array([1, lambda2])
        
        # 初期条件 x(0) = [1, 0]
        x0 = np.array([1, 0])
        
        # 係数を求める（P c = x0）
        P = np.column_stack([v1, v2])
        c = np.linalg.solve(P, x0)
        
        # 位置の時間発展
        x_pos = np.real(c[0] * np.exp(lambda1 * t_vals) * v1[0] + c[1] * np.exp(lambda2 * t_vals) * v2[0])
        
        # 速度の時間発展
        x_vel = np.real(c[0] * np.exp(lambda1 * t_vals) * v1[1] + c[1] * np.exp(lambda2 * t_vals) * v2[1])
        
        # グラフのプロット
        graph1_pos = axes1.plot_line_graph(
            t_vals, x_pos,
            line_color=YELLOW,
            add_vertex_dots=False,
            stroke_width=3,
        )
        
        title1 = Text("位置 x", font_size=24, color=YELLOW)
        title1.next_to(axes1, UP, buff=0.2)
        
        # 速度のグラフ
        axes2 = Axes(
            x_range=[0, 10, 2],
            y_range=[-2, 2, 1],
            x_length=5.5,
            y_length=3.5,
            axis_config={"color": WHITE, "include_numbers": True, "font_size": 20},
            tips=False,
        )
        axes2.shift(RIGHT * 3 + DOWN * 0.3)
        
        axes2_labels = axes2.get_axis_labels(x_label="t", y_label="v")
        
        graph2_vel = axes2.plot_line_graph(
            t_vals, x_vel,
            line_color=GREEN,
            add_vertex_dots=False,
            stroke_width=3,
        )
        
        title2 = Text("速度 v", font_size=24, color=GREEN)
        title2.next_to(axes2, UP, buff=0.2)
        
        self.play(
            Create(axes1), Create(axes2),
            Write(axes1_labels), Write(axes2_labels),
            Write(title1), Write(title2),
            run_time=0.8
        )
        self.wait(0.5)
        
        self.play(
            Create(graph1_pos), Create(graph2_vel),
            run_time=2.0
        )
        self.wait(1.5)

        damping_note = Text(
            "実部が負なので振幅が時間とともに減衰する",
            color=ORANGE, font_size=24, weight=BOLD,
        )
        damping_note.to_edge(DOWN, buff=0.3)
        self.play(Write(damping_note), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(axes1), FadeOut(axes2),
            FadeOut(axes1_labels), FadeOut(axes2_labels),
            FadeOut(graph1_pos), FadeOut(graph2_vel),
            FadeOut(title1), FadeOut(title2),
            FadeOut(damping_note),
        )
        self.wait(0.3)

        # ============================================================
        # Part 11: 摩擦なしの場合
        # ============================================================
        subtitle11 = Text("摩擦なしの場合（γ=0）", font_size=28, color=GOLD)
        subtitle11.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle11), run_time=0.5)
        self.wait(0.4)

        no_friction_text = Text(
            "γ=0（摩擦なし）の場合を見てみよう",
            color=WHITE, font_size=26,
        )
        no_friction_text.shift(UP * 1.8)
        self.play(Write(no_friction_text), run_time=0.7)
        self.wait(0.5)

        matrix_l2 = MathTex(
            r"L = \begin{bmatrix} 0 & 1 \\ -3 & 0 \end{bmatrix}",
            color=YELLOW,
            font_size=40,
        )
        matrix_l2.shift(UP * 0.9)
        matrix_l2_box = SurroundingRectangle(matrix_l2, color=YELLOW, buff=0.25)
        self.play(Write(matrix_l2), Create(matrix_l2_box), run_time=0.8)
        self.wait(0.7)

        eigenvalues2 = MathTex(
            r"\lambda_1 = j\sqrt{3}, \quad \lambda_2 = -j\sqrt{3}",
            color=BLUE,
            font_size=36,
        )
        eigenvalues2.shift(UP * 0.0)
        self.play(Write(eigenvalues2), run_time=0.8)
        self.wait(0.7)

        pure_imaginary = Text(
            "実部が0のため、減衰しない無限振動となる",
            color=ORANGE, font_size=26, weight=BOLD,
        )
        pure_imaginary.shift(DOWN * 0.8)
        self.play(Write(pure_imaginary), run_time=0.8)
        self.wait(1.0)

        self.play(
            FadeOut(no_friction_text), FadeOut(matrix_l2),
            FadeOut(matrix_l2_box), FadeOut(eigenvalues2),
            FadeOut(pure_imaginary),
        )
        self.wait(0.3)

        # ============================================================
        # Part 12: 無限振動のグラフ
        # ============================================================
        subtitle12 = Text("無限振動のグラフ", font_size=28, color=TEAL)
        subtitle12.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle12), run_time=0.5)
        self.wait(0.4)

        # 固有値（γ=0の場合）
        lambda1_nf = 1j * np.sqrt(3)
        lambda2_nf = -1j * np.sqrt(3)
        
        # 固有ベクトル
        v1_nf = np.array([1, lambda1_nf])
        v2_nf = np.array([1, lambda2_nf])
        
        # 係数
        P_nf = np.column_stack([v1_nf, v2_nf])
        c_nf = np.linalg.solve(P_nf, x0)
        
        # 位置と速度
        x_pos_nf = np.real(c_nf[0] * np.exp(lambda1_nf * t_vals) * v1_nf[0] + c_nf[1] * np.exp(lambda2_nf * t_vals) * v2_nf[0])
        x_vel_nf = np.real(c_nf[0] * np.exp(lambda1_nf * t_vals) * v1_nf[1] + c_nf[1] * np.exp(lambda2_nf * t_vals) * v2_nf[1])
        
        # グラフ作成
        axes3 = Axes(
            x_range=[0, 10, 2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=5.5,
            y_length=3.5,
            axis_config={"color": WHITE, "include_numbers": True, "font_size": 20},
            tips=False,
        )
        axes3.shift(LEFT * 3 + DOWN * 0.3)
        
        axes3_labels = axes3.get_axis_labels(x_label="t", y_label="x")
        
        graph3_pos = axes3.plot_line_graph(
            t_vals, x_pos_nf,
            line_color=YELLOW,
            add_vertex_dots=False,
            stroke_width=3,
        )
        
        title3 = Text("位置 x", font_size=24, color=YELLOW)
        title3.next_to(axes3, UP, buff=0.2)
        
        axes4 = Axes(
            x_range=[0, 10, 2],
            y_range=[-2, 2, 1],
            x_length=5.5,
            y_length=3.5,
            axis_config={"color": WHITE, "include_numbers": True, "font_size": 20},
            tips=False,
        )
        axes4.shift(RIGHT * 3 + DOWN * 0.3)
        
        axes4_labels = axes4.get_axis_labels(x_label="t", y_label="v")
        
        graph4_vel = axes4.plot_line_graph(
            t_vals, x_vel_nf,
            line_color=GREEN,
            add_vertex_dots=False,
            stroke_width=3,
        )
        
        title4 = Text("速度 v", font_size=24, color=GREEN)
        title4.next_to(axes4, UP, buff=0.2)
        
        self.play(
            Create(axes3), Create(axes4),
            Write(axes3_labels), Write(axes4_labels),
            Write(title3), Write(title4),
            run_time=0.8
        )
        self.wait(0.5)
        
        self.play(
            Create(graph3_pos), Create(graph4_vel),
            run_time=2.0
        )
        self.wait(1.5)

        oscillation_note = Text(
            "実部が0なので振幅は減衰せず、永久に振動し続ける",
            color=ORANGE, font_size=24, weight=BOLD,
        )
        oscillation_note.to_edge(DOWN, buff=0.3)
        self.play(Write(oscillation_note), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(axes3), FadeOut(axes4),
            FadeOut(axes3_labels), FadeOut(axes4_labels),
            FadeOut(graph3_pos), FadeOut(graph4_vel),
            FadeOut(title3), FadeOut(title4),
            FadeOut(oscillation_note),
        )
        self.wait(0.3)

        # ============================================================
        # Part 13: まとめ
        # ============================================================
        subtitle13 = Text("まとめ", font_size=36, color=GOLD)
        subtitle13.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle13), run_time=0.6)
        self.wait(0.4)

        summary = VGroup(
            Text("• 行列の微分方程式の解：x⃗(t) = e^{Lt}x⃗(0)", color=WHITE, font_size=26),
            Text("• 固有ベクトルの線形結合で表現可能", color=WHITE, font_size=26),
            Text("• 対角化による計算と完全に等価", color=WHITE, font_size=26),
            Text("• 固有値の実部が減衰を、虚部が振動を決定", color=WHITE, font_size=26),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        summary.shift(UP * 0.2)
        
        for row in summary:
            self.play(Write(row), run_time=0.6)
            self.wait(0.3)
        
        self.wait(1.0)

        final_message = Text(
            "これで複数の状態量の時間発展を統一的に扱える！",
            color=GREEN, font_size=28, weight=BOLD,
        )
        final_message.shift(DOWN * 2.5)
        self.play(Write(final_message), run_time=0.8)
        self.wait(2.0)

        self.play(
            FadeOut(VGroup(
                title, subtitle1, summary, final_message
            )),
            run_time=1.0
        )
        self.wait(0.5)
