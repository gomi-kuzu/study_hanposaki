from manim import *
import numpy as np

class VectorDifferentiation(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        # タイトル
        title = Text("ベクトルによる微分", font_size=34, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)

        # ============================================================
        # Part 1: 偏微分の復習
        # ============================================================
        subtitle1 = Text("偏微分の基本", font_size=30, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.5)

        partial_intro = VGroup(
            Text("偏微分とは", color=WHITE, font_size=26),
            Text("注目している変数以外を定数として扱う微分", color=YELLOW, font_size=26, weight=BOLD),
        ).arrange(DOWN, buff=0.15)
        partial_intro.shift(UP * 1.5)
        self.play(Write(partial_intro), run_time=0.7)
        self.wait(0.5)

        # 二変数関数の例
        func_example = MathTex(
            r"f(x_1, x_2) = x_1^2 + 3x_1 x_2 + x_2^2",
            color=WHITE, font_size=36
        )
        func_example.shift(UP * 0.6)
        func_box = SurroundingRectangle(func_example, color=TEAL, buff=0.18)
        self.play(Write(func_example), Create(func_box), run_time=0.7)
        self.wait(0.5)

        # x_1での偏微分
        partial_x_label = VGroup(
            MathTex(r"x_1", color=ORANGE, font_size=36),
            Text("で偏微分（", color=ORANGE, font_size=24),
            MathTex(r"x_2", color=ORANGE, font_size=36),
            Text("は定数として扱う）", color=ORANGE, font_size=24),
        ).arrange(RIGHT, buff=0.1)
        partial_x_label.shift(DOWN * 0.2)
        self.play(Write(partial_x_label), run_time=0.6)
        self.wait(1.0)

        partial_x = MathTex(
            r"\frac{\partial f}{\partial x_1} = 2x_1 + 3x_2",
            color=ORANGE, font_size=36
        )
        partial_x.shift(DOWN)
        self.play(Write(partial_x), run_time=0.7)
        self.wait(1.0)

        self.play(FadeOut(partial_x_label), FadeOut(partial_x))
        self.wait(0.2)

        # x_2での偏微分
        partial_y_label = VGroup(
            MathTex(r"x_2", color=GREEN, font_size=36),
            Text("で偏微分（", color=GREEN, font_size=24),
            MathTex(r"x_1", color=GREEN, font_size=36),
            Text("は定数として扱う）", color=GREEN, font_size=24),
        ).arrange(RIGHT, buff=0.1)
        partial_y_label.shift(DOWN * 0.2)
        self.play(Write(partial_y_label), run_time=0.6)
        self.wait(1)

        partial_y = MathTex(
            r"\frac{\partial f}{\partial x_2} = 3x_1 + 2x_2",
            color=GREEN, font_size=36
        )
        partial_y.shift(DOWN)
        self.play(Write(partial_y), run_time=0.7)
        self.wait(1.0)

        self.play(
            FadeOut(partial_intro), FadeOut(func_example), FadeOut(func_box),
            FadeOut(partial_y_label), FadeOut(partial_y),
            FadeOut(subtitle1),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: ベクトル表記への書き換え
        # ============================================================
        subtitle2 = Text("ベクトル表記で書き直す", font_size=30, color=PURPLE)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)

        vector_intro = Text("同じ関数をベクトルを引数に取る形で表現", color=WHITE, font_size=26)
        vector_intro.shift(UP * 1.5)
        self.play(Write(vector_intro), run_time=0.7)
        self.wait(0.5)

        # 元の関数
        original_func = MathTex(
            r"f(x_1, x_2) = x_1^2 + 3x_1 x_2 + x_2^2",
            color=WHITE, font_size=36
        )
        original_func.shift(UP * 0.7)
        self.play(Write(original_func), run_time=0.6)
        self.wait(0.4)

        # 矢印
        arrow_down = Arrow(UP * 0.3, DOWN * 0.1, color=TEAL, buff=0.05)
        rewrite_text = Text("書き換え", color=TEAL, font_size=24)
        rewrite_text.next_to(arrow_down, RIGHT, buff=0.15)
        self.play(Create(arrow_down), Write(rewrite_text), run_time=0.5)
        self.wait(0.3)

        # ベクトル表記
        vector_def = MathTex(
            r"\mathbf{x} = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix}",
            color=TEAL, font_size=36
        )
        vector_def.shift(DOWN * 0.8 + LEFT * 2.0)
        self.play(Write(vector_def), run_time=0.6)
        self.wait(0.3)

        vector_func = MathTex(
            r"f(\mathbf{x})",
            color=TEAL, font_size=36
        )
        vector_func.shift(DOWN * 0.8 + RIGHT * 1.5)
        vector_func_box = SurroundingRectangle(vector_func, color=TEAL, buff=0.15)
        self.play(Write(vector_func), Create(vector_func_box), run_time=0.7)
        self.wait(0.5)

        note_vector = Text("※列ベクトルとして定義", color=YELLOW, font_size=22, weight=BOLD)
        note_vector.shift(DOWN * 2)
        self.play(Write(note_vector), run_time=0.6)
        self.wait(1.0)

        self.play(
            FadeOut(vector_intro), FadeOut(original_func),
            FadeOut(arrow_down), FadeOut(rewrite_text),
            FadeOut(vector_def), FadeOut(vector_func), FadeOut(vector_func_box),
            FadeOut(note_vector), FadeOut(subtitle2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: ベクトルでの微分
        # ============================================================
        subtitle3 = Text("ベクトルでの微分", font_size=30, color=ORANGE)
        subtitle3.next_to(title, DOWN)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.5)

        diff_intro = VGroup(
            Text("ベクトルで微分する場合", color=WHITE, font_size=26),
            Text("成分ごとに偏微分して並べるだけ", color=YELLOW, font_size=26, weight=BOLD),
        ).arrange(DOWN, buff=0.15)
        diff_intro.shift(UP * 1.5)
        self.play(Write(diff_intro), run_time=0.7)
        self.wait(0.5)

        # 関数の再表示
        func_recall = MathTex(
            r"f(\mathbf{x}) = f(x_1, x_2) = x_1^2 + 3x_1 x_2 + x_2^2",
            color=WHITE, font_size=36
        )
        func_recall.shift(UP * 0.7)
        self.play(Write(func_recall), run_time=0.6)
        self.wait(0.4)

        # 微分の定義
        gradient_def = MathTex(
            r"\frac{\partial f}{\partial \mathbf{x}} = "
            r"\begin{pmatrix} \frac{\partial f}{\partial x_1} \\ \frac{\partial f}{\partial x_2} \end{pmatrix}",
            color=ORANGE, font_size=34
        )
        gradient_def.shift(DOWN * 0.5)
        # gradient_box = SurroundingRectangle(gradient_def, color=ORANGE, buff=0.18)
        self.play(Write(gradient_def), run_time=0.8)
        self.wait(0.6)

        # 計算結果
        gradient_result = MathTex(
            r"= \begin{pmatrix} 2x_1 + 3x_2 \\ 3x_1 + 2x_2 \end{pmatrix}",
            color=ORANGE, font_size=34
        )
        gradient_result.shift(DOWN * 1.5)
        self.play(Write(gradient_result), run_time=0.7)
        self.wait(0.6)

        # 重要な注意
        note_column = Text("結果も列ベクトル！", color=YELLOW, font_size=24, weight=BOLD)
        note_column.shift(DOWN * 2.7)
        note_box = SurroundingRectangle(note_column, color=YELLOW, buff=0.12)
        self.play(Write(note_column), Create(note_box), run_time=0.6)
        self.wait(1.2)

        self.play(
            FadeOut(diff_intro), FadeOut(func_recall),
            FadeOut(gradient_def), 
            FadeOut(gradient_result), FadeOut(note_column), FadeOut(note_box),
            FadeOut(subtitle3),
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: 線形形式の微分（注意点）
        # ============================================================
        subtitle4 = Text("よくある間違い", font_size=30, color=RED)
        subtitle4.next_to(title, DOWN)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.5)

        mistake_intro = VGroup(
            Text("次のような線形形式を考える", color=WHITE, font_size=26),
        )
        mistake_intro.shift(UP * 1.7)
        self.play(Write(mistake_intro), run_time=0.7)
        self.wait(0.5)

        # 線形形式の定義
        linear_form = MathTex(
            r"f(\mathbf{x}) = \mathbf{a}^{\top} \mathbf{x}",
            color=WHITE, font_size=36
        )
        linear_form.shift(UP * 1.0)
        linear_box = SurroundingRectangle(linear_form, color=TEAL, buff=0.15)
        self.play(Write(linear_form), Create(linear_box), run_time=0.7)
        self.wait(0.5)

        # ベクトルの定義
        vector_defs = MathTex(
            r"\mathbf{a} = \begin{pmatrix} a_1 \\ a_2 \end{pmatrix}, \quad "
            r"\mathbf{x} = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix}",
            color=WHITE, font_size=34
        )
        vector_defs.shift(DOWN * 0.3)
        self.play(Write(vector_defs), run_time=0.6)
        self.wait(0.4)

        # 展開形
        # expanded_form = MathTex(
        #     r"f(\mathbf{x}) = a_1 x_1 + a_2 x_2",
        #     color=WHITE, font_size=34
        # )
        # expanded_form.shift(DOWN * 1.0)
        # self.play(Write(expanded_form), run_time=0.6)
        # self.wait(0.5)

        # 問題提起
        question = Text("これをxで微分すると？", color=YELLOW, font_size=26, weight=BOLD)
        question.shift(DOWN * 1.2)
        self.play(Write(question), run_time=0.6)
        self.wait(0.6)

        self.play(FadeOut(question))
        self.wait(0.2)

        # 間違った答え
        wrong_answer_label = Text("❌ 間違い：", color=RED, font_size=24, weight=BOLD)
        wrong_answer_label.shift(DOWN * 1.2 + LEFT * 3.0)
        wrong_answer = MathTex(
            r"\mathbf{a}^{\top}",
            color=RED, font_size=34
        )
        wrong_answer.shift(DOWN * 1.2 + RIGHT * 0.5)
        wrong_box = SurroundingRectangle(
            VGroup(wrong_answer_label, wrong_answer), 
            color=RED, buff=0.15
        )
        self.play(
            Write(wrong_answer_label), Write(wrong_answer), 
            Create(wrong_box), run_time=0.7
        )
        self.wait(0.6)

        wrong_note = Text("係数をそのまま残してしまう", color=RED, font_size=20)
        wrong_note.shift(DOWN * 1.8)
        self.play(Write(wrong_note), run_time=0.6)
        self.wait(1.0)

        self.play(
            FadeOut(wrong_answer_label), FadeOut(wrong_answer), 
            FadeOut(wrong_box), FadeOut(wrong_note)
        )
        self.wait(0.3)

        # 正しい答え
        correct_answer_label = Text("✓ 正しい：", color=GREEN, font_size=24, weight=BOLD)
        correct_answer_label.shift(DOWN * 1.2 + LEFT * 3.0)
        correct_answer = MathTex(
            r"\mathbf{a}",
            color=GREEN, font_size=38
        )
        correct_answer.shift(DOWN * 1.2 + RIGHT * 0.5)
        correct_box = SurroundingRectangle(
            VGroup(correct_answer_label, correct_answer), 
            color=GREEN, buff=0.15
        )
        self.play(
            Write(correct_answer_label), Write(correct_answer), 
            Create(correct_box), run_time=0.7
        )
        self.wait(1.0)

        # 理由の説明
        reason = VGroup(
            Text("理由：列ベクトルで微分しているため", color=GREEN, font_size=22),
            Text("結果も列ベクトルになる", color=GREEN, font_size=22),
        ).arrange(DOWN, buff=0.1)
        reason.shift(DOWN * 2.0)
        self.play(Write(reason), run_time=0.7)
        self.wait(1.0)

        self.play(
            FadeOut(correct_answer_label), FadeOut(correct_answer),
            FadeOut(correct_box), FadeOut(reason)
        )
        self.wait(0.3)

        # 詳細な計算
        detail_label = Text("確認：", color=TEAL, font_size=24, weight=BOLD)
        detail_label.shift(DOWN* 1.2)
        self.play(Write(detail_label), run_time=0.6)
        self.wait(0.4)

        detail_calc = MathTex(
            r"\frac{\partial f}{\partial \mathbf{x}} = "
            r"\begin{pmatrix} \frac{\partial f}{\partial x_1} \\ \frac{\partial f}{\partial x_2} \end{pmatrix} = "
            r"\begin{pmatrix} a_1 \\ a_2 \end{pmatrix} = \mathbf{a}",
            color=TEAL, font_size=30
        )
        detail_calc.shift(DOWN * 2.0)
        self.play(Write(detail_calc), run_time=0.9)
        self.wait(1.5)

        self.play(
            FadeOut(mistake_intro), FadeOut(linear_form), FadeOut(linear_box),
            FadeOut(vector_defs),# FadeOut(expanded_form),
            FadeOut(detail_label), FadeOut(detail_calc),
            FadeOut(subtitle4),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: まとめ
        # ============================================================
        subtitle_end = Text("まとめ", font_size=36, color=GOLD, weight=BOLD)
        subtitle_end.next_to(title, DOWN)
        self.play(Write(subtitle_end), run_time=0.7)
        self.wait(0.5)

        summary = VGroup(
            VGroup(
                Text("1.", color=WHITE, font_size=24, weight=BOLD),
                VGroup(
                    Text("偏微分は他の変数を定数として扱う", color=WHITE, font_size=28),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("2.", color=WHITE, font_size=24, weight=BOLD),
                VGroup(
                    Text("スカラをベクトルで微分するときは成分ごとに偏微分して並べる", color=WHITE, font_size=28),
                    Text("列ベクトルで微分すれば結果も列ベクトル", color=ORANGE, font_size=26),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("3.", color=WHITE, font_size=24, weight=BOLD),
                VGroup(
                    MathTex(r"\mathbf{a}^{\top}\mathbf{x}", color=WHITE, font_size=32),
                    Text("を", color=WHITE, font_size=28),
                    MathTex(r"\mathbf{x}", color=WHITE, font_size=32),
                    Text("で微分すると", color=WHITE, font_size=28),
                    MathTex(r"\mathbf{a}^{\top}", color=GREEN, font_size=36),
                    Text("ではなく", color=WHITE, font_size=28),
                    MathTex(r"\mathbf{a}", color=GREEN, font_size=36)
                ).arrange(RIGHT, buff=0.15),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        summary.scale(0.9)
        summary.shift(DOWN * 0.0)

        for point in summary:
            self.play(Write(point), run_time=0.7)
            self.wait(0.4)

        self.wait(1.5)

        all_final = VGroup(summary, subtitle_end, title)
        self.play(FadeOut(all_final), run_time=1.0)
        self.wait(0.5)
