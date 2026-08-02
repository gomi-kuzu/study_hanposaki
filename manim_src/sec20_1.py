from manim import *
import numpy as np


class MatrixExponentialDefinition(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        title = Text("行列の指数関数を定義する", font_size=36, color=WHITE)
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
            "１変数の微分方程式の解は指数関数で表せた",
            color=WHITE, font_size=26,
        )
        review1_text.shift(UP * 1.8)
        self.play(Write(review1_text), run_time=0.7)
        self.wait(0.4)

        review1_eq = MathTex(
            r"\frac{d}{dt}x(t) = -\alpha x(t) \quad \Rightarrow \quad x(t) = x(0)e^{-\alpha t}",
            color=YELLOW,
            font_size=36,
        )
        review1_eq.shift(UP * 1.0)
        self.play(Write(review1_eq), run_time=0.8)
        self.wait(0.6)

        review2_text = Text(
            "また、多変数の微分方程式は行列とベクトルで書けた",
            color=WHITE, font_size=26,
        )
        review2_text.shift(UP * 0.0)
        self.play(Write(review2_text), run_time=0.7)
        self.wait(0.4)

        review2_eq = MathTex(
            r"\frac{d}{dt}\boldsymbol{x}(t) = A\boldsymbol{x}(t)",
            color=YELLOW,
            font_size=36,
        )
        review2_eq.shift(DOWN * 0.8)
        self.play(Write(review2_eq), run_time=0.8)
        self.wait(0.8)

        question = Text(
            "この２つから…行列版の指数関数があれば解けるのでは？",
            color=ORANGE, font_size=28, weight=BOLD,
        )
        question.shift(DOWN * 1.8)
        self.play(Write(question), run_time=0.8)
        self.wait(0.6)

        answer = Text(
            "→ 実際に行列の指数関数を定義して、性質を紐解こう！",
            color=GREEN, font_size=28, weight=BOLD,
        )
        answer.shift(DOWN * 2.6)
        self.play(Write(answer), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(review1_text), FadeOut(review1_eq),
            FadeOut(review2_text), FadeOut(review2_eq),
            FadeOut(question), FadeOut(answer),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: 行列の指数関数の記法
        # ============================================================
        subtitle2 = Text("行列の指数関数の記法", font_size=28, color=GOLD)
        subtitle2.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle2), run_time=0.5)
        self.wait(0.4)

        notation_text = Text(
            "これ以降、行列Aを引数とする指数関数を次のように書く",
            color=WHITE, font_size=26,
        )
        notation_text.shift(UP * 1.5)
        self.play(Write(notation_text), run_time=0.7)
        self.wait(0.5)

        notation_eq = MathTex(
            r"e^A",
            color=YELLOW,
            font_size=48,
        )
        notation_eq.shift(UP * 0.3)
        notation_box = SurroundingRectangle(notation_eq, color=YELLOW, buff=0.3)
        self.play(Write(notation_eq), run_time=0.6)
        self.play(Create(notation_box), run_time=0.4)
        self.wait(0.6)

        condition_text = Text(
            "ただし、Aは正方行列とする",
            color=BLUE, font_size=26,
        )
        condition_text.shift(DOWN * 0.8)
        self.play(Write(condition_text), run_time=0.6)
        self.wait(0.5)

        reason_text = Text(
            "理由：微分方程式 d𝐱/dt = A𝐱 では、Aは同一次元空間の写像",
            color=TEAL, font_size=24,
        )
        reason_text.shift(DOWN * 1.5)
        self.play(Write(reason_text), run_time=0.7)
        self.wait(0.4)

        reason_text2 = Text(
            "（同じ次元に戻ってくる変換なので、行列は正方になる）",
            color=TEAL, font_size=22,
        )
        reason_text2.shift(DOWN * 2.1)
        self.play(Write(reason_text2), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(notation_text), FadeOut(notation_eq), FadeOut(notation_box),
            FadeOut(condition_text), FadeOut(reason_text), FadeOut(reason_text2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: スカラの指数関数のマクローリン展開
        # ============================================================
        subtitle3 = Text("まずスカラの指数関数を展開", font_size=28, color=TEAL)
        subtitle3.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle3), run_time=0.5)
        self.wait(0.4)

        maclaurin_text = Text(
            "スカラの指数関数をマクローリン展開してみる",
            color=WHITE, font_size=26,
        )
        maclaurin_text.shift(UP * 2.1)
        self.play(Write(maclaurin_text), run_time=0.7)
        self.wait(0.5)

        # マクローリン展開の一般式
        maclaurin_general = MathTex(
            r"f(x) = \sum_{n=0}^{\infty} \frac{1}{n!} \frac{d^n f}{dx^n}\bigg|_{x=0} x^n",
            color=BLUE,
            font_size=32,
        )
        maclaurin_general.shift(UP * 1.2)
        self.play(Write(maclaurin_general), run_time=0.9)
        self.wait(0.6)

        arrow1 = MathTex(r"\Downarrow", color=WHITE, font_size=36)
        arrow1.shift(UP * 0.4)
        apply_text = Text("この公式を指数関数 f(x) = eˣ に適用すると…", color=ORANGE, font_size=22)
        apply_text.next_to(arrow1, RIGHT, buff=0.3)
        self.play(Write(arrow1), Write(apply_text), run_time=0.6)
        self.wait(0.5)

        # 指数関数の微分は自分自身
        derivative_note = MathTex(
            r"\frac{d^n e^x}{dx^n}\bigg|_{x=0} = e^0 = 1",
            color=GREEN,
            font_size=30,
        )
        derivative_note.shift(DOWN * 0.5)
        self.play(Write(derivative_note), run_time=0.7)
        self.wait(0.6)

        explanation = Text(
            "（微分しても形が変わらず、x=0で1になる）",
            color=GREEN, font_size=22,
        )
        explanation.shift(DOWN * 1.1)
        self.play(Write(explanation), run_time=0.6)
        self.wait(0.7)

        self.play(
            FadeOut(maclaurin_text), FadeOut(apply_text), FadeOut(explanation),
        )
        self.wait(1.0)

        # 展開結果
        arrow2 = MathTex(r"\Downarrow", color=WHITE, font_size=36)
        # arrow2.shift(DOWN * 0.8)
        self.play(
            maclaurin_general.animate.shift(UP * 0.8).scale(0.85),
            derivative_note.animate.shift(UP *1.1).scale(0.85),
            arrow1.animate.shift(UP * 0.8).scale(0.85),
            Write(arrow2),
            run_time=0.6
        )
        self.wait(0.4)

        exp_expansion = MathTex(
            r"e^x = \sum_{n=0}^{\infty} \frac{1}{n!} x^n",
            color=YELLOW,
            font_size=36,
        )
        exp_expansion.shift(DOWN * 1.2)
        exp_box = SurroundingRectangle(exp_expansion, color=YELLOW, buff=0.25)
        self.play(Write(exp_expansion), run_time=0.8)
        self.play(Create(exp_box), run_time=0.4)
        self.wait(0.6)

        # 具体的に展開
        exp_explicit = MathTex(
            r"e^x = 1 + x + \frac{1}{2!}x^2 + \frac{1}{3!}x^3 + \cdots",
            color=YELLOW,
            font_size=36,
        )
        exp_explicit.shift(DOWN * 2.5)
        self.play(Write(exp_explicit), run_time=0.8)
        self.wait(1.2)

        self.play(
            FadeOut(maclaurin_general), FadeOut(derivative_note),
            FadeOut(arrow1), FadeOut(arrow2), 
            FadeOut(exp_expansion), FadeOut(exp_box)
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: 行列の指数関数の定義
        # ============================================================
        subtitle4 = Text("行列の指数関数を定義", font_size=28, color=BLUE)
        subtitle4.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle4), run_time=0.5)
        self.wait(0.4)

        # 展開式を上に移動
        self.play(
            # exp_expansion.animate.shift(UP * 3.8).scale(0.75),
            # exp_box.animate.shift(UP * 3.8).scale(0.75),
            exp_explicit.animate.shift(UP * 4.5).scale(0.75),
            run_time=0.6
        )
        self.wait(0.3)

        idea_text = Text(
            "ここで、xを行列Aにすり替える！",
            color=ORANGE, font_size=26, weight=BOLD,
        )
        idea_text.shift(UP * 1.4 + LEFT * 3.2)
        self.play(Write(idea_text), run_time=0.7)
        self.wait(0.6)

        arrow3 = MathTex(r"\Downarrow", color=WHITE, font_size=40)
        arrow3.shift(UP * 1.4)
        self.play(Write(arrow3), run_time=0.4)
        self.wait(0.3)

        # 行列の指数関数の定義
        matrix_exp_def = MathTex(
            r"e^A = I + A + \frac{1}{2!}A^2 + \frac{1}{3!}A^3 + \cdots",
            color=YELLOW,
            font_size=38,
        )
        matrix_exp_def.shift(UP * 0.5)
        matrix_exp_box = SurroundingRectangle(matrix_exp_def, color=YELLOW, buff=0.3)
        self.play(Write(matrix_exp_def), run_time=1.0)
        self.play(Create(matrix_exp_box), run_time=0.4)
        self.wait(0.8)

        identity_note = Text(
            "※Iは単位行列（スカラの1に対応）",
            color=GRAY, font_size=22,
        )
        identity_note.shift(DOWN * 0.5)
        self.play(Write(identity_note), run_time=0.6)
        self.wait(0.7)

        # 時間変数を導入
        time_intro = Text(
            "出したいのは微分方程式の解のため、時間変数tを導入すると…",
            color=WHITE, font_size=26,
        )
        time_intro.shift(DOWN * 1.2)
        self.play(Write(time_intro), run_time=0.7)
        self.wait(0.5)

        matrix_exp_time = MathTex(
            r"e^{At} = I + At + \frac{1}{2!}(At)^2 + \frac{1}{3!}(At)^3 + \cdots",
            color=GREEN,
            font_size=36,
        )
        matrix_exp_time.shift(DOWN * 1.9)
        self.play(Write(matrix_exp_time), run_time=0.9)
        self.wait(0.5)

        # Aとtの可換性
        commute_note = MathTex(
            r"= I + At + \frac{1}{2!}A^2t^2 + \frac{1}{3!}A^3t^3 + \cdots",
            color=GREEN,
            font_size=36,
        )
        commute_note.shift(DOWN * 2.75)
        commute_label = Text(
            "（tはスカラなので順序交換可）",
            color=TEAL, font_size=20,
        )
        commute_label.next_to(commute_note, RIGHT, buff=0.2)
        self.play(Write(commute_note), Write(commute_label), run_time=0.8)
        self.wait(1.5)

        self.play(
            # FadeOut(exp_expansion), FadeOut(exp_box), 
            FadeOut(exp_explicit),
            FadeOut(idea_text), FadeOut(arrow3), FadeOut(identity_note),
            FadeOut(time_intro), FadeOut(matrix_exp_time),
            FadeOut(commute_label),FadeOut(commute_note),
        )
        self.wait(0.3)

        # 定義のまとめ
        self.play(
            matrix_exp_def.animate.shift(UP),
            matrix_exp_box.animate.shift(UP),
            # commute_note.animate.shift(UP * 4.7).scale(0.9),
            run_time=0.6
        )
        self.wait(0.3)

        definition_label = Text(
            "これを行列の指数関数の定義とする",
            color=GREEN, font_size=26, weight=BOLD,
        )
        definition_label.shift(DOWN * 0.3)
        self.play(Write(definition_label), run_time=0.7)
        self.wait(0.6)

        note_computation = Text(
            "※ 具体的にA^nの極限を求める方法は次の動画で詳しく扱う",
            color=ORANGE, font_size=24,
        )
        note_computation.shift(DOWN * 1.1)
        self.play(Write(note_computation), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(matrix_exp_def), FadeOut(matrix_exp_box),
            FadeOut(definition_label),
            FadeOut(note_computation),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: 行列の指数関数の性質（可換性）
        # ============================================================
        subtitle5 = Text("行列の指数関数の性質", font_size=28, color=GOLD)
        subtitle5.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle5), run_time=0.5)
        self.wait(0.4)

        warning_text = Text(
            "注意：スカラとは異なる性質を持つ！",
            color=RED, font_size=28, weight=BOLD,
        )
        warning_text.shift(UP * 2)
        self.play(Write(warning_text), run_time=0.7)
        self.wait(0.6)

        # 可換性について
        commutative_title = Text(
            "【可換性について】",
            color=YELLOW, font_size=26, weight=BOLD,
        )
        commutative_title.shift(UP * 1.4)
        self.play(Write(commutative_title), run_time=0.6)
        self.wait(0.4)

        # ケース1：可換な行列
        case1_text = Text(
            "可換な行列A, B（AB = BA）の場合：",
            color=GREEN, font_size=24,
        )
        case1_text.shift(UP * 0.7)
        self.play(Write(case1_text), run_time=0.6)
        self.wait(0.4)

        case1_eq = MathTex(
            r"e^{A+B} = e^A e^B = e^B e^A = e^{B+A}",
            color=GREEN,
            font_size=36,
        )
        case1_eq.shift(UP * 0.1)
        case1_box = SurroundingRectangle(case1_eq, color=GREEN, buff=0.2)
        self.play(Write(case1_eq), run_time=0.8)
        self.play(Create(case1_box), run_time=0.4)
        self.wait(0.8)

        # ケース2：一般の場合
        case2_text = Text(
            "それ以外の一般の場合（AB ≠ BA）：",
            color=RED, font_size=24,
        )
        case2_text.shift(DOWN * 0.8)
        self.play(Write(case2_text), run_time=0.6)
        self.wait(0.4)

        case2_eq = MathTex(
            r"e^{A+B} \neq e^A e^B \neq e^B e^A \neq e^{B+A}",
            color=RED,
            font_size=36,
        )
        case2_eq.shift(DOWN * 1.5)
        case2_box = SurroundingRectangle(case2_eq, color=RED, buff=0.2)
        self.play(Write(case2_eq), run_time=0.8)
        self.play(Create(case2_box), run_time=0.4)
        self.wait(1.0)

        explanation_comm = Text(
            "行列は積の順序で結果が変わるため！",
            color=ORANGE, font_size=24,
        )
        explanation_comm.shift(DOWN * 2.7)
        self.play(Write(explanation_comm), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(warning_text), FadeOut(commutative_title),
            FadeOut(case1_text), FadeOut(case1_eq), FadeOut(case1_box),
            FadeOut(case2_text), FadeOut(case2_eq), FadeOut(case2_box),
            FadeOut(explanation_comm),
        )
        self.wait(0.3)

        # ============================================================
        # Part 6: 行列と自分自身の可換性
        # ============================================================
        subtitle6 = Text("行列は自分自身とは可換", font_size=28, color=TEAL)
        subtitle6.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle6), run_time=0.5)
        self.wait(0.4)

        self_commute_text = Text(
            "自明な性質↓",
            color=WHITE, font_size=26,
        )
        self_commute_text.shift(UP * 1.6)
        self.play(Write(self_commute_text), run_time=0.7)
        self.wait(0.5)

        self_commute_eq = MathTex(
            r"AA = A^2 = AA",
            color=BLUE,
            font_size=36,
        )
        self_commute_eq.shift(UP * 1.2)
        self.play(Write(self_commute_eq), run_time=0.6)
        self.wait(0.5)

        therefore = Text(
            "したがって、スカラt, t₁, t₂に対して：",
            color=WHITE, font_size=26,
        )
        therefore.shift(UP * 0.4)
        self.play(Write(therefore), run_time=0.7)
        self.wait(0.4)

        # 性質1
        prop1 = MathTex(
            r"e^{At_1 + At_2} = e^{At_1} e^{At_2} = e^{At_2 + At_1}",
            color=YELLOW,
            font_size=36,
        )
        prop1.shift(DOWN * 0.4)
        self.play(Write(prop1), run_time=0.8)
        self.wait(0.6)

        # 性質2
        prop2 = MathTex(
            r"e^{At} e^{-At} = e^{-At} e^{At} = e^{At - At} = I",
            color=YELLOW,
            font_size=36,
        )
        prop2.shift(DOWN * 1.2)
        self.play(Write(prop2), run_time=0.8)
        self.wait(0.6)

        # 性質3
        prop3 = MathTex(
            r"(e^{At})^{-1} = e^{-At}",
            color=GREEN,
            font_size=36,
        )
        prop3.shift(DOWN * 2.2)
        prop3_box = SurroundingRectangle(prop3, color=GREEN, buff=0.25)
        self.play(Write(prop3), run_time=0.7)
        self.play(Create(prop3_box), run_time=0.4)
        self.wait(0.5)

        inverse_note = Text(
            "（逆行列が簡単に求まる！）",
            color=GREEN, font_size=22,
        )
        inverse_note.shift(DOWN * 3.0)
        self.play(Write(inverse_note), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(self_commute_text), FadeOut(self_commute_eq),
            FadeOut(therefore), FadeOut(prop1), FadeOut(prop2),
            FadeOut(inverse_note),
            FadeOut(prop3), FadeOut(prop3_box),
        )
        self.wait(0.3)

        # ============================================================
        # Part 7: 微分の性質
        # ============================================================
        subtitle7 = Text("微分の性質", font_size=28, color=BLUE)
        subtitle7.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle7), run_time=0.5)
        self.wait(0.4)

        # # prop3を上に移動
        # self.play(
        #     prop3.animate.shift(UP * 3.8).scale(0.8),
        #     prop3_box.animate.shift(UP * 3.8).scale(0.8),
        #     run_time=0.6
        # )
        # self.wait(0.3)

        derivative_title = Text(
            "最後に、微分に関する性質",
            color=WHITE, font_size=26,
        )
        derivative_title.shift(UP * 1.5)
        self.play(Write(derivative_title), run_time=0.7)
        self.wait(0.5)

        derivative_prop = MathTex(
            r"\frac{d}{dt} e^{At} = A e^{At} = e^{At} A",
            color=YELLOW,
            font_size=42,
        )
        derivative_prop.shift(UP * 0.5)
        derivative_box = SurroundingRectangle(derivative_prop, color=YELLOW, buff=0.3)
        self.play(Write(derivative_prop), run_time=0.9)
        self.play(Create(derivative_box), run_time=0.4)
        self.wait(0.7)

        # 証明のヒント
        proof_hint = Text(
            "（定義式を項ごとに微分すれば確かめられる）",
            color=GRAY, font_size=24,
        )
        proof_hint.shift(DOWN * 0.5)
        self.play(Write(proof_hint), run_time=0.7)
        self.wait(0.5)

        # スカラとの比較
        comparison_text = Text(
            "スカラの場合：d/dt eᵅᵗ = α eᵅᵗ と同じ形",
            color=GREEN, font_size=24,
        )
        comparison_text.shift(DOWN * 1.3)
        self.play(Write(comparison_text), run_time=0.7)
        self.wait(0.8)

        importance = Text(
            "この性質により、微分方程式の解として使える！",
            color=ORANGE, font_size=26, weight=BOLD,
        )
        importance.shift(DOWN * 2.2)
        self.play(Write(importance), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(derivative_title), FadeOut(derivative_prop),
            FadeOut(derivative_box), FadeOut(proof_hint),
            FadeOut(comparison_text), FadeOut(importance),
        )
        self.wait(0.3)

        # ============================================================
        # Part 8: まとめと次回予告
        # ============================================================
        subtitle8 = Text("まとめ", font_size=36, color=GOLD)
        subtitle8.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle8), run_time=0.6)
        self.wait(0.4)

        summary = VGroup(
            Text("• スカラの指数関数をマクローリン展開", color=WHITE, font_size=26),
            Text("• 引数を行列に置き換えて行列の指数関数を定義", color=WHITE, font_size=26),
            Text("• 可換な行列に対しては積の分解が可能", color=WHITE, font_size=26),
            Text("• 微分の性質：d/dt eᴬᵗ = A eᴬᵗ", color=WHITE, font_size=26),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        summary.shift(UP * 0.8)
        
        for row in summary:
            self.play(Write(row), run_time=0.6)
            self.wait(0.3)
        
        self.wait(0.8)

        next_question = Text(
            "しかし、A^nの足し合わせの極限を具体的に計算する必要がある…",
            color=ORANGE, font_size=26, weight=BOLD,
        )
        next_question.shift(DOWN * 1.5)
        self.play(Write(next_question), run_time=0.7)
        self.wait(0.6)

        next_topic = Text(
            "→ 次の動画では、固有値・固有ベクトルを使った計算方法を見ていこう",
            color=GREEN, font_size=26, weight=BOLD,
        )
        next_topic.shift(DOWN * 2.1)
        self.play(Write(next_topic), run_time=0.8)
        self.wait(1.8)

        self.play(
            FadeOut(VGroup(
                title, subtitle1, summary,
                next_question, next_topic
            )),
            run_time=1.0
        )
        self.wait(0.5)
