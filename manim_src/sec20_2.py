from manim import *
import numpy as np


class MatrixExponentialComputation(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        title = Text("行列の指数関数の計算方法", font_size=36, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.7)

        # ============================================================
        # Part 1: 前回のおさらい
        # ============================================================
        subtitle1 = Text("前回のおさらい", font_size=28, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.4)

        review1_text = Text(
            "前回、行列の指数関数を次のように定義した",
            color=WHITE, font_size=26,
        )
        review1_text.shift(UP * 1.8)
        self.play(Write(review1_text), run_time=0.7)
        self.wait(0.4)

        review1_eq = MathTex(
            r"e^A = I + A + \frac{1}{2!}A^2 + \frac{1}{3!}A^3 + \cdots",
            color=YELLOW,
            font_size=38,
        )
        review1_eq.shift(UP * 0.8)
        review1_box = SurroundingRectangle(review1_eq, color=YELLOW, buff=0.25)
        self.play(Write(review1_eq), Create(review1_box), run_time=0.8)
        self.wait(0.6)

        review2_text = Text(
            "または、無限和の形で",
            color=WHITE, font_size=26,
        )
        review2_text.shift(DOWN * 0.3)
        self.play(Write(review2_text), run_time=0.6)
        self.wait(0.4)

        review2_eq = MathTex(
            r"e^A = \sum_{n=0}^{\infty} \frac{1}{n!}A^n",
            color=YELLOW,
            font_size=38,
        )
        review2_eq.shift(DOWN * 1.1)
        self.play(Write(review2_eq), run_time=0.8)
        self.wait(0.8)

        question = Text(
            "しかし、A^nの極限をどう計算するのか？",
            color=ORANGE, font_size=28, weight=BOLD,
        )
        question.shift(DOWN * 2.2)
        self.play(Write(question), run_time=0.8)
        self.wait(0.6)

        answer = Text(
            "→ 固有値・固有ベクトルを使った対角化が鍵！",
            color=GREEN, font_size=28, weight=BOLD,
        )
        answer.shift(DOWN * 3.0)
        self.play(Write(answer), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(review1_text), FadeOut(review1_eq), FadeOut(review1_box),
            FadeOut(review2_text), FadeOut(review2_eq),
            FadeOut(question), FadeOut(answer),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: 対角化可能な行列
        # ============================================================
        subtitle2 = Text("対角化可能な行列", font_size=28, color=GOLD)
        subtitle2.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle2), run_time=0.5)
        self.wait(0.4)

        diag_text = Text(
            "行列Aが線形独立な固有ベクトルを持つとき",
            color=WHITE, font_size=26,
        )
        diag_text.shift(UP * 2.2)
        self.play(Write(diag_text), run_time=0.7)
        self.wait(0.5)

        diag_explanation = Text(
            "固有ベクトルを並べた行列Pで対角化できる",
            color=WHITE, font_size=26,
        )
        diag_explanation.shift(UP * 1.6)
        self.play(Write(diag_explanation), run_time=0.7)
        self.wait(0.5)

        diag_eq1 = MathTex(
            r"\Lambda = P^{-1}AP",
            color=YELLOW,
            font_size=40,
        )
        diag_eq1.shift(UP * 0.7)
        self.play(Write(diag_eq1), run_time=0.8)
        self.wait(0.6)

        lambda_note = Text(
            "Λは対角成分に固有値を並べた行列",
            color=TEAL, font_size=24,
        )
        lambda_note.shift(UP * 0.0)
        self.play(Write(lambda_note), run_time=0.6)
        self.wait(0.5)

        # 対角行列の例
        lambda_example = MathTex(
            r"\Lambda = \begin{bmatrix} \lambda_1 & 0 & \cdots & 0 \\ 0 & \lambda_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & \lambda_N \end{bmatrix}",
            color=BLUE,
            font_size=32,
        )
        lambda_example.shift(DOWN * 1.0)
        self.play(Write(lambda_example), run_time=0.9)
        self.wait(0.8)

        transform_text = Text(
            "この式を変形すると…",
            color=ORANGE, font_size=26,
        )
        transform_text.shift(DOWN * 2.3)
        self.play(Write(transform_text), run_time=0.7)
        self.wait(0.5)

        diag_eq2 = MathTex(
            r"A = P\Lambda P^{-1}",
            color=GREEN,
            font_size=40,
        )
        diag_eq2.shift(DOWN * 3.0)
        diag_eq2_box = SurroundingRectangle(diag_eq2, color=GREEN, buff=0.25)
        self.play(Write(diag_eq2), Create(diag_eq2_box), run_time=0.8)
        self.wait(1.2)

        self.play(
            FadeOut(diag_text), FadeOut(diag_explanation),
            FadeOut(lambda_note), FadeOut(lambda_example),
            FadeOut(transform_text),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: 行列指数関数への適用
        # ============================================================
        subtitle3 = Text("行列指数関数に適用", font_size=28, color=TEAL)
        subtitle3.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle3), run_time=0.5)
        self.wait(0.4)

        # diag_eq1とdiag_eq2を上に移動
        self.play(
            diag_eq1.animate.shift(UP * 1.5).scale(0.75),
            diag_eq2.animate.shift(UP * 4.2).scale(0.75),
            diag_eq2_box.animate.shift(UP * 4.2).scale(0.75),
            run_time=0.6
        )
        self.wait(0.3)

        apply_text = Text(
            "A = PΛP⁻¹ を指数関数の定義に代入すると",
            color=WHITE, font_size=26,
        )
        apply_text.shift(UP * 1.2)
        self.play(Write(apply_text), run_time=0.7)
        self.wait(0.5)

        apply_eq1 = MathTex(
            r"e^A = \sum_{n=0}^{\infty} \frac{1}{n!}A^n = \sum_{n=0}^{\infty} \frac{1}{n!}(P\Lambda P^{-1})^n",
            color=YELLOW,
            font_size=32,
        )
        apply_eq1.shift(UP * 0.4)
        self.play(Write(apply_eq1), run_time=0.9)
        self.wait(0.7)

        key_point = Text(
            "重要：(PΛP⁻¹)ⁿ = PΛⁿP⁻¹（途中のP⁻¹Pが消える）",
            color=ORANGE, font_size=24, weight=BOLD,
        )
        key_point.shift(DOWN * 0.5)
        self.play(Write(key_point), run_time=0.8)
        self.wait(0.8)

        # 具体例を示す
        example_power = MathTex(
            r"(P\Lambda P^{-1})^2 = P\Lambda P^{-1}P\Lambda P^{-1} = P\Lambda^2 P^{-1}",
            color=BLUE,
            font_size=28,
        )
        example_power.shift(DOWN * 1.3)
        self.play(Write(example_power), run_time=0.9)
        self.wait(0.8)

        arrow1 = MathTex(r"\Downarrow", color=WHITE, font_size=36)
        arrow1.shift(DOWN * 2.0)
        self.play(Write(arrow1), run_time=0.4)
        self.wait(0.3)

        apply_eq2 = MathTex(
            r"e^A = \sum_{n=0}^{\infty} \frac{1}{n!}P\Lambda^n P^{-1}",
            color=YELLOW,
            font_size=36,
        )
        apply_eq2.shift(DOWN * 2.7)
        self.play(Write(apply_eq2), run_time=0.9)
        self.wait(0.8)

        self.play(
            FadeOut(diag_eq1), FadeOut(apply_text),
            FadeOut(apply_eq1), FadeOut(key_point),
            FadeOut(example_power), FadeOut(arrow1),
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: PとP^{-1}の相殺
        # ============================================================
        subtitle4 = Text("和の外にPを出す", font_size=28, color=BLUE)
        subtitle4.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle4), run_time=0.5)
        self.wait(0.4)

        # apply_eq2を上に移動
        self.play(
            diag_eq2.animate.shift(UP * 0.5).scale(0.9),
            diag_eq2_box.animate.shift(UP * 0.5).scale(0.9),
            apply_eq2.animate.shift(UP * 3.9).scale(0.85),
            run_time=0.6
        )
        self.wait(0.3)

        factor_text = Text(
            "PとP⁻¹は和の各項に共通なので外に出せる",
            color=WHITE, font_size=26,
        )
        factor_text.shift(UP * 1.2)
        self.play(Write(factor_text), run_time=0.7)
        self.wait(0.5)

        arrow2 = MathTex(r"\Downarrow", color=WHITE, font_size=36)
        arrow2.shift(UP * 0.5)
        self.play(Write(arrow2), run_time=0.4)
        self.wait(0.3)

        factor_eq = MathTex(
            r"e^A = P\left(\sum_{n=0}^{\infty} \frac{1}{n!}\Lambda^n\right) P^{-1}",
            color=GREEN,
            font_size=36,
        )
        factor_eq.shift(DOWN * 0.3)
        factor_box = SurroundingRectangle(factor_eq, color=GREEN, buff=0.25)
        self.play(Write(factor_eq), Create(factor_box), run_time=0.9)
        self.wait(0.8)

        notice_text = Text(
            "真ん中の部分は対角行列Λの指数関数",
            color=TEAL, font_size=24,
        )
        notice_text.shift(DOWN * 1.3)
        self.play(Write(notice_text), run_time=0.7)
        self.wait(0.6)

        final_eq = MathTex(
            r"e^A = Pe^{\Lambda}P^{-1}",
            color=YELLOW,
            font_size=44,
        )
        final_eq.shift(DOWN * 2.3)
        final_box = SurroundingRectangle(final_eq, color=YELLOW, buff=0.3)
        self.play(Write(final_eq), Create(final_box), run_time=0.9)
        self.wait(1.2)

        self.play(
            FadeOut(diag_eq2), FadeOut(diag_eq2_box),
            FadeOut(apply_eq2), FadeOut(factor_text),
            FadeOut(arrow2), FadeOut(factor_eq),
            FadeOut(factor_box), FadeOut(notice_text),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: 対角行列の指数関数
        # ============================================================
        subtitle5 = Text("対角行列の指数関数", font_size=28, color=GOLD)
        subtitle5.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle5), run_time=0.5)
        self.wait(0.4)

        # final_eqを上に移動
        self.play(
            final_eq.animate.shift(UP * 3.5).scale(0.75),
            final_box.animate.shift(UP * 3.5).scale(0.75),
            run_time=0.6
        )
        self.wait(0.3)

        diagonal_text = Text(
            "対角行列Λの指数関数は成分ごとに計算できる",
            color=WHITE, font_size=26,
        )
        diagonal_text.shift(UP * 1.5)
        self.play(Write(diagonal_text), run_time=0.7)
        self.wait(0.5)

        diagonal_eq1 = MathTex(
            r"e^{\Lambda} = \sum_{n=0}^{\infty} \frac{1}{n!}\Lambda^n",
            color=BLUE,
            font_size=34,
        )
        diagonal_eq1.shift(UP * 0.7)
        self.play(Write(diagonal_eq1), run_time=0.8)
        self.wait(0.6)

        converge_text = Text(
            "対角行列の冪乗は対角成分の冪乗なので",
            color=WHITE, font_size=24,
        )
        converge_text.shift(DOWN * 0.1)
        self.play(Write(converge_text), run_time=0.7)
        self.wait(0.5)

        diagonal_eq2 = MathTex(
            r"e^{\Lambda} = \begin{bmatrix} e^{\lambda_1} & 0 & \cdots & 0 \\ 0 & e^{\lambda_2} & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & e^{\lambda_N} \end{bmatrix}",
            color=GREEN,
            font_size=32,
        )
        diagonal_eq2.shift(DOWN * 1.5)
        diagonal_box = SurroundingRectangle(diagonal_eq2, color=GREEN, buff=0.2)
        self.play(Write(diagonal_eq2), Create(diagonal_box), run_time=1.0)
        self.wait(0.8)

        result_text = Text(
            "各対角成分がスカラの指数関数に収束する",
            color=TEAL, font_size=24,
        )
        result_text.shift(DOWN * 3.0)
        self.play(Write(result_text), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(diagonal_text), FadeOut(diagonal_eq1),
            FadeOut(converge_text), FadeOut(result_text),
        )
        self.wait(0.3)

        # ============================================================
        # Part 6: 計算結果のまとめ
        # ============================================================
        subtitle6 = Text("計算結果のまとめ", font_size=28, color=TEAL)
        subtitle6.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle6), run_time=0.5)
        self.wait(0.4)

        # final_eqとdiagonal_eq2を配置
        self.play(
            final_eq.animate.shift(DOWN * 1.8).scale(1.1),
            final_box.animate.shift(DOWN * 1.8).scale(1.1),
            diagonal_eq2.animate.shift(UP * 2.8).scale(0.9),
            diagonal_box.animate.shift(UP * 2.8).scale(0.9),
            run_time=0.6
        )
        self.wait(0.3)

        summary_text = Text(
            "対角化可能な行列Aに対して",
            color=WHITE, font_size=26, weight=BOLD,
        )
        summary_text.shift(UP * 1.8)
        self.play(Write(summary_text), run_time=0.7)
        self.wait(0.8)

        steps_text = Text(
            "① Aを対角化：Λ = P⁻¹AP",
            color=BLUE, font_size=24,
        )
        steps_text.shift(UP * 0.3)
        self.play(Write(steps_text), run_time=0.6)
        self.wait(0.5)

        steps_text2 = Text(
            "② e^Λを計算：対角成分にe^λᵢを配置",
            color=BLUE, font_size=24,
        )
        steps_text2.shift(DOWN * 0.1)
        self.play(Write(steps_text2), run_time=0.6)
        self.wait(0.5)

        steps_text3 = Text(
            "③ e^A = Pe^ΛP⁻¹を計算",
            color=BLUE, font_size=24,
        )
        steps_text3.shift(DOWN * 0.5)
        self.play(Write(steps_text3), run_time=0.6)
        self.wait(1.0)

        conclusion = Text(
            "→ これで行列の指数関数が具体的に計算できた！",
            color=GREEN, font_size=26, weight=BOLD,
        )
        conclusion.shift(DOWN * 2.9)
        self.play(Write(conclusion), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(diagonal_eq2), FadeOut(diagonal_box),
            FadeOut(summary_text), FadeOut(steps_text),
            FadeOut(steps_text2), FadeOut(steps_text3),
            FadeOut(conclusion),
        )
        self.wait(0.3)

        # ============================================================
        # Part 7: 複素固有値の場合
        # ============================================================
        subtitle7 = Text("複素固有値の場合", font_size=28, color=BLUE)
        subtitle7.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle7), run_time=0.5)
        self.wait(0.4)

        # final_eqを上に移動
        self.play(
            final_eq.animate.shift(UP * 2.3).scale(0.85),
            final_box.animate.shift(UP * 2.3).scale(0.85),
            run_time=0.6
        )
        self.wait(0.3)

        complex_text = Text(
            "注意：Aが実数行列でも固有値に複素数が混じることがある",
            color=ORANGE, font_size=26, weight=BOLD,
        )
        complex_text.shift(UP * 1.2)
        self.play(Write(complex_text), run_time=0.8)
        self.wait(0.6)

        complex_example = Text(
            "例：回転行列の固有値は e^{±iθ}",
            color=WHITE, font_size=24,
        )
        complex_example.shift(UP * 0.5)
        self.play(Write(complex_example), run_time=0.7)
        self.wait(0.6)

        complex_lambda = MathTex(
            r"\Lambda = \begin{bmatrix} e^{\alpha + j\beta} & 0 \\ 0 & e^{\alpha - j\beta} \end{bmatrix}",
            color=BLUE,
            font_size=34,
        )
        complex_lambda.shift(DOWN * 0.5)
        self.play(Write(complex_lambda), run_time=0.8)
        self.wait(0.7)

        note_j = Text(
            "（jは虚数単位）",
            color=TEAL, font_size=22,
        )
        note_j.shift(DOWN * 1.3)
        self.play(Write(note_j), run_time=0.5)
        self.wait(0.5)

        complex_result = Text(
            "しかし、PやP⁻¹にも虚数単位jが含まれるため",
            color=WHITE, font_size=24,
        )
        complex_result.shift(DOWN * 2.0)
        self.play(Write(complex_result), run_time=0.7)
        self.wait(0.5)

        complex_conclusion = Text(
            "最終的なe^Aは実数行列になる（らしい）",
            color=GREEN, font_size=26, weight=BOLD,
        )
        complex_conclusion.shift(DOWN * 2.7)
        self.play(Write(complex_conclusion), run_time=0.8)
        self.wait(0.6)

        challenge = Text(
            "※ 余裕のある人はぜひ計算して確かめてみてください",
            color=YELLOW, font_size=22,
        )
        challenge.shift(DOWN * 3.4)
        self.play(Write(challenge), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(complex_text), FadeOut(complex_example),
            FadeOut(complex_lambda), FadeOut(note_j),
            FadeOut(complex_result), FadeOut(complex_conclusion),
            FadeOut(challenge),
        )
        self.wait(0.3)

        # ============================================================
        # Part 8: 対角化できない場合（ジョルダン標準形）
        # ============================================================
        subtitle8 = Text("対角化できない場合", font_size=28, color=RED)
        subtitle8.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle8), run_time=0.5)
        self.wait(0.4)

        # final_eqを少し上に移動
        self.play(
            final_eq.animate.shift(UP * 0.5).scale(0.9),
            final_box.animate.shift(UP * 0.5).scale(0.9),
            run_time=0.6
        )
        self.wait(0.3)

        jordan_intro = Text(
            "対角化できない場合でも計算可能！",
            color=ORANGE, font_size=26, weight=BOLD,
        )
        jordan_intro.shift(UP * 1.2)
        self.play(Write(jordan_intro), run_time=0.7)
        self.wait(0.6)

        jordan_text = Text(
            "ジョルダン標準形を使う",
            color=WHITE, font_size=26,
        )
        jordan_text.shift(UP * 0.5)
        self.play(Write(jordan_text), run_time=0.7)
        self.wait(0.5)

        jordan_def = Text(
            "ジョルダン標準形：対角成分の1つ上に1が入った行列",
            color=TEAL, font_size=24,
        )
        jordan_def.shift(DOWN * 0.2)
        self.play(Write(jordan_def), run_time=0.8)
        self.wait(0.6)

        # ジョルダン標準形の例
        jordan_example = MathTex(
            r"J = \begin{bmatrix} \lambda_i & 1 & 0 & \cdots \\ 0 & \lambda_i & 1 & \cdots \\ 0 & 0 & \lambda_i & \cdots \\ \vdots & \vdots & \vdots & \ddots \end{bmatrix}",
            color=BLUE,
            font_size=32,
        )
        jordan_example.shift(DOWN * 1.3)
        self.play(Write(jordan_example), run_time=0.9)
        self.wait(0.8)

        self.play(
            FadeOut(jordan_intro), FadeOut(jordan_text),
        )
        self.wait(0.3)

        # ============================================================
        # Part 9: ジョルダン標準形の分解
        # ============================================================
        subtitle9 = Text("ジョルダン標準形の分解", font_size=28, color=GOLD)
        subtitle9.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle9), run_time=0.5)
        self.wait(0.4)

        decompose_text = Text(
            "ジョルダン標準形を対角部分と上三角部分に分解",
            color=WHITE, font_size=26,
        )
        decompose_text.shift(UP * 0.8)
        self.play(Write(decompose_text), run_time=0.7)
        self.wait(0.5)

        # ジョルダン標準形を移動
        self.play(
            final_eq.animate.shift(UP * 0.7),
            final_box.animate.shift(UP * 0.7),
            jordan_def.animate.shift(UP * 1.7),
            jordan_example.animate.shift(UP * 1.7).scale(0.85),
            decompose_text.animate.shift(UP * 1.0),
            run_time=0.6
        )
        self.wait(0.3)

        decompose_eq = MathTex(
            r"J = \lambda_i I + H",
            color=YELLOW,
            font_size=38,
        )
        decompose_eq.shift(UP * 0.5)
        self.play(Write(decompose_eq), run_time=0.7)
        self.wait(0.6)

        # λ_iIとHの説明
        lambda_i_text = Text(
            "λᵢI: 対角行列,  H: 上三角行列",
            color=TEAL,
            font_size=26,
        )
        lambda_i_text.shift(DOWN * 0.2)
        self.play(Write(lambda_i_text), run_time=0.7)
        self.wait(0.6)

        # Hの例
        h_example = MathTex(
            r"H = \begin{bmatrix} 0 & 1 & 0 & \cdots \\ 0 & 0 & 1 & \cdots \\ 0 & 0 & 0 & \cdots \\ \vdots & \vdots & \vdots & \ddots \end{bmatrix}",
            color=BLUE,
            font_size=30,
        )
        h_example.shift(DOWN * 1.3)
        self.play(Write(h_example), run_time=0.8)
        self.wait(0.7)

        commute_notice = Text(
            "重要：λᵢIとHは可換（前回動画の可換性の条件）",
            color=ORANGE, font_size=24, weight=BOLD,
        )
        commute_notice.shift(DOWN * 2.4)
        self.play(Write(commute_notice), run_time=0.8)
        self.wait(1.0)

        self.play(
            FadeOut(final_eq), FadeOut(final_box),
            FadeOut(jordan_def), FadeOut(jordan_example),
            FadeOut(decompose_text), FadeOut(lambda_i_text),
            FadeOut(h_example),
        )
        self.wait(0.3)

        # ============================================================
        # Part 10: 指数関数の計算
        # ============================================================
        subtitle10 = Text("指数関数の計算", font_size=28, color=TEAL)
        subtitle10.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle10), run_time=0.5)
        self.wait(0.4)

        # decompose_eqを上に移動
        self.play(
            decompose_eq.animate.shift(UP * 2.0).scale(0.85),
            commute_notice.animate.shift(UP * 3.7).scale(0.85),
            run_time=0.6
        )
        self.wait(0.3)

        exponential_text = Text(
            "可換性から、指数関数を分解できる",
            color=WHITE, font_size=26,
        )
        exponential_text.shift(UP * 1.0)
        self.play(Write(exponential_text), run_time=0.7)
        self.wait(0.5)

        exponential_eq1 = MathTex(
            r"e^{J} = e^{\lambda_i I + H} = e^{\lambda_i I} e^{H}",
            color=YELLOW,
            font_size=38,
        )
        exponential_eq1.shift(UP * 0.2)
        exponential_box1 = SurroundingRectangle(exponential_eq1, color=YELLOW, buff=0.25)
        self.play(Write(exponential_eq1), Create(exponential_box1), run_time=0.9)
        self.wait(0.8)

        # e^{λ_iI}の計算
        lambda_exp_text = Text(
            "① e^{λᵢI}は対角化可能な場合と同様に計算",
            color=BLUE, font_size=24,
        )
        lambda_exp_text.shift(DOWN * 0.8)
        self.play(Write(lambda_exp_text), run_time=0.7)
        self.wait(0.5)

        lambda_exp_eq = MathTex(
            r"e^{\lambda_i I} = e^{\lambda_i} I",
            color=BLUE,
            font_size=32,
        )
        lambda_exp_eq.shift(DOWN * 1.5)
        self.play(Write(lambda_exp_eq), run_time=0.7)
        self.wait(0.6)

        # e^Hの計算
        h_exp_text = Text(
            "② e^Hはべき零行列なので有限項で打ち切れる",
            color=GREEN, font_size=24,
        )
        h_exp_text.shift(DOWN * 2.3)
        self.play(Write(h_exp_text), run_time=0.7)
        self.wait(0.6)

        h_exp_eq = MathTex(
            r"e^{H} = I + H + \frac{1}{2!}H^2 + \cdots + \frac{1}{(n-1)!}H^{n-1}",
            color=GREEN,
            font_size=28,
        )
        h_exp_eq.shift(DOWN * 3.0)
        self.play(Write(h_exp_eq), run_time=0.9)
        self.wait(0.8)

        nilpotent_note = Text(
            "（Hⁿ = 0 となるため）",
            color=TEAL, font_size=20,
        )
        nilpotent_note.shift(DOWN * 3.6)
        self.play(Write(nilpotent_note), run_time=0.6)
        self.wait(1.0)

        self.play(
            FadeOut(decompose_eq), FadeOut(commute_notice),
            FadeOut(exponential_text), FadeOut(lambda_exp_text),
            FadeOut(lambda_exp_eq), FadeOut(h_exp_text),
            FadeOut(h_exp_eq), FadeOut(nilpotent_note),
        )
        self.wait(0.3)

        # ============================================================
        # Part 11: ジョルダン標準形の結果
        # ============================================================
        subtitle11 = Text("ジョルダン標準形の結果", font_size=28, color=BLUE)
        subtitle11.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle11), run_time=0.5)
        self.wait(0.4)

        # exponential_eq1を上に移動
        self.play(
            exponential_eq1.animate.shift(UP * 1.8).scale(0.9),
            exponential_box1.animate.shift(UP * 1.8).scale(0.9),
            run_time=0.6
        )
        self.wait(0.3)

        jordan_result_text = Text(
            "両方とも計算可能なので、e^Jが求まる",
            color=WHITE, font_size=26,
        )
        jordan_result_text.shift(UP * 0.8)
        self.play(Write(jordan_result_text), run_time=0.7)
        self.wait(0.6)

        jordan_final = MathTex(
            r"e^{J} = e^{\lambda_i} \left( I + H + \frac{1}{2!}H^2 + \cdots \right)",
            color=GREEN,
            font_size=34,
        )
        jordan_final.shift(UP * 0.0)
        jordan_final_box = SurroundingRectangle(jordan_final, color=GREEN, buff=0.25)
        self.play(Write(jordan_final), Create(jordan_final_box), run_time=0.9)
        self.wait(0.8)

        general_form = Text(
            "一般の行列Aに対しても",
            color=WHITE, font_size=24,
        )
        general_form.shift(DOWN * 1.0)
        self.play(Write(general_form), run_time=0.7)
        self.wait(0.5)

        general_eq = MathTex(
            r"e^{A} = Pe^{J}P^{-1}",
            color=YELLOW,
            font_size=40,
        )
        general_eq.shift(DOWN * 1.8)
        general_box = SurroundingRectangle(general_eq, color=YELLOW, buff=0.3)
        self.play(Write(general_eq), Create(general_box), run_time=0.9)
        self.wait(0.8)

        conclusion2 = Text(
            "→ 対角化できない場合でもe^Aを計算できた！",
            color=GREEN, font_size=26, weight=BOLD,
        )
        conclusion2.shift(DOWN * 2.8)
        self.play(Write(conclusion2), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(exponential_eq1), FadeOut(exponential_box1),
            FadeOut(jordan_result_text), FadeOut(jordan_final),
            FadeOut(jordan_final_box), FadeOut(general_form),
            FadeOut(general_eq), FadeOut(general_box),
            FadeOut(conclusion2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 12: まとめ
        # ============================================================
        subtitle12 = Text("まとめ", font_size=36, color=GOLD)
        subtitle12.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle12), run_time=0.6)
        self.wait(0.4)

        summary = VGroup(
            Text("• 対角化可能な場合：e^A = Pe^ΛP⁻¹", color=WHITE, font_size=26),
            Text("  - e^Λは対角成分にe^λᵢを配置", color=WHITE, font_size=24),
            Text("• 複素固有値を持つ場合でも最終結果は実数", color=WHITE, font_size=26),
            Text("• 対角化不可能な場合：ジョルダン標準形を使用", color=WHITE, font_size=26),
            Text("  - e^J = e^{λᵢI}e^H で計算", color=WHITE, font_size=24),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        summary.shift(UP * 0.5)
        
        for row in summary:
            self.play(Write(row), run_time=0.6)
            self.wait(0.3)
        
        self.wait(0.8)

        next_topic = Text(
            "→ 次回は、これを使って微分方程式を解く！",
            color=GREEN, font_size=28, weight=BOLD,
        )
        next_topic.shift(DOWN * 2.3)
        self.play(Write(next_topic), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(
                title, subtitle1, summary,
                next_topic
            )),
            run_time=1.0
        )
        self.wait(0.5)
