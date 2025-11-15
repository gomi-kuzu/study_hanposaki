from manim import *

class VectorCombinations(Scene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"
        
        # タイトル
        title = Text("良い矢印、余分な矢印はどれか？", font_size=32, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)
        
        # === パート1: ベクトルの設定と表示 ===
        # 2D座標軸を設定
        axes = Axes(
            x_range=[-3, 6, 1],
            y_range=[-2, 5, 1],
            x_length=8,
            y_length=6,
            axis_config={"color": GRAY}
        )
        axes.shift(LEFT * 2.5)
        
        # 座標軸ラベル
        x_label = Text("X", color=RED, font_size=20)
        y_label = Text("Y", color=GREEN, font_size=20)
        x_label.next_to(axes.get_x_axis().get_end(), DOWN)
        y_label.next_to(axes.get_y_axis().get_end(), LEFT)
        
        self.play(Create(axes), Write(x_label), Write(y_label), run_time=0.8)
        self.wait(0.5)
        
        # 目標ベクトル x = [2, 4] (左側、白)
        x_vector = Vector(
            axes.c2p(2, 4) - axes.c2p(0, 0),
            color=WHITE,
            stroke_width=6
        ).shift(axes.c2p(0, 0))
        x_label_vec = MathTex(r"\mathbf{x} = \begin{bmatrix} 2 \\ 4 \end{bmatrix}", 
                             color=WHITE, font_size=24)
        x_label_vec.move_to(axes.c2p(-1, 0.5))
        
        self.play(Create(x_vector), Write(x_label_vec), run_time=0.7)
        self.wait(0.5)
        
        # 候補ベクトル群 (中央から右側、緑)
        a_vectors = []
        a_labels = []
        a_coords = [[0, 1], [1, 0], [0, -1], [1, 2], [-1, 2]]
        a_names = [r"\mathbf{a}_1", r"\mathbf{a}_2", r"\mathbf{a}_3", r"\mathbf{a}_4", r"\mathbf{a}_5"]
        a_positions = [
            axes.c2p(2.5, 0),  # a1の開始位置
            axes.c2p(4, 0),    # a2の開始位置  
            axes.c2p(3.5, -1), # a3の開始位置
            axes.c2p(1, 0),    # a4の開始位置
            axes.c2p(5, 0)     # a5の開始位置
        ]
        
        for i, (coord, name, pos) in enumerate(zip(a_coords, a_names, a_positions)):
            vector = Vector(
                axes.c2p(coord[0], coord[1]) - axes.c2p(0, 0),
                color=GREEN,
                stroke_width=4
            ).shift(pos)
            
            label = MathTex(f"{name} = \\begin{{bmatrix}} {coord[0]} \\\\ {coord[1]} \\end{{bmatrix}}", 
                           color=GREEN, font_size=20)
            label.next_to(vector.get_end(), UP, buff=0.2)
            
            a_vectors.append(vector)
            a_labels.append(label)
        
        # ベクトル群を順番に表示
        for vector, label in zip(a_vectors, a_labels):
            self.play(Create(vector), Write(label), run_time=0.5)
            self.wait(0.2)
        
        self.wait(0.8)
        
        # === パート2: 第1の組み合わせ x = 2a_4 ===        
        subtitle2 = Text("組み合わせ1: x = 2a₄", font_size=28, color=YELLOW)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.4)
        
        # 右側に式を表示
        eq1 = MathTex(
            r"\mathbf{x} = 2\mathbf{a}_4",
            color=WHITE,
            font_size=32
        )
        eq1.to_edge(RIGHT).shift(UP * 2)
        self.play(Write(eq1), run_time=0.6)
        self.wait(0.4)
        
        # 計算過程
        calc1 = MathTex(
            r"= 2\begin{bmatrix} 1 \\ 2 \end{bmatrix} = \begin{bmatrix} 2 \\ 4 \end{bmatrix}",
            color=WHITE,
            font_size=28
        )
        calc1.next_to(eq1, DOWN, buff=0.3, aligned_edge=RIGHT)
        self.play(Write(calc1), run_time=0.6)
        self.wait(0.4)
        
        # 2a_4を可視化 (原点から)
        scaled_a4 = Vector(
            axes.c2p(2, 4) - axes.c2p(0, 0),
            color=BLUE,
            stroke_width=5
        ).shift(axes.c2p(0, 0))
        
        scaled_label = MathTex(r"2\mathbf{a}_4", color=BLUE, font_size=24)
        scaled_label.next_to(scaled_a4.get_end(), RIGHT, buff=0.3)
        
        # a_4を強調
        self.play(a_vectors[3].animate.set_color(YELLOW), a_labels[3].animate.set_color(YELLOW), run_time=0.4)
        self.wait(0.3)
        
        self.play(Create(scaled_a4), Write(scaled_label), run_time=0.7)
        self.wait(0.8)
        
        # 一致を強調
        match_text1 = Text("一致！", color=YELLOW, font_size=24)
        match_text1.next_to(scaled_label, DOWN)
        self.play(Write(match_text1), run_time=0.5)
        self.wait(0.8)
        
        # クリーンアップ
        self.play(
            FadeOut(scaled_a4), FadeOut(scaled_label), FadeOut(match_text1),
            FadeOut(eq1), FadeOut(calc1), FadeOut(subtitle2)
        )
        self.play(a_vectors[3].animate.set_color(GREEN), a_labels[3].animate.set_color(GREEN))
        
        # === パート3: 第2の組み合わせ x = 2a_5 + 4a_2 ===
        subtitle3 = Text("組み合わせ2: x = 2a₅ + 4a₂", font_size=28, color=YELLOW)
        subtitle3.next_to(title, DOWN)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.4)
        
        # 右側に式を表示
        eq2 = MathTex(
            r"\mathbf{x} = 2\mathbf{a}_5 + 4\mathbf{a}_2",
            color=WHITE,
            font_size=28
        )
        eq2.to_edge(RIGHT).shift(UP * 2)
        self.play(Write(eq2), run_time=0.6)
        self.wait(0.4)
        
        # 計算過程
        calc2a = MathTex(
            r"= 2\begin{bmatrix} -1 \\ 2 \end{bmatrix} + 4\begin{bmatrix} 1 \\ 0 \end{bmatrix}",
            color=WHITE,
            font_size=24
        )
        calc2a.next_to(eq2, DOWN, buff=0.3, aligned_edge=RIGHT)
        self.play(Write(calc2a), run_time=0.6)
        self.wait(0.4)
        
        calc2b = MathTex(
            r"= \begin{bmatrix} -2 \\ 4 \end{bmatrix} + \begin{bmatrix} 4 \\ 0 \end{bmatrix} = \begin{bmatrix} 2 \\ 4 \end{bmatrix}",
            color=WHITE,
            font_size=24
        )
        calc2b.next_to(calc2a, DOWN, buff=0.3, aligned_edge=RIGHT)
        self.play(Write(calc2b), run_time=0.6)
        self.wait(0.4)
        
        # a_5とa_2を強調
        self.play(
            a_vectors[4].animate.set_color(YELLOW), a_labels[4].animate.set_color(YELLOW),
            a_vectors[1].animate.set_color(YELLOW), a_labels[1].animate.set_color(YELLOW),
            run_time=0.4
        )
        self.wait(0.3)
        
        # 2a_5を原点から描画
        scaled_a5 = Vector(
            axes.c2p(-2, 4) - axes.c2p(0, 0),
            color=PURPLE,
            stroke_width=5
        ).shift(axes.c2p(0, 0))
        
        scaled_a5_label = MathTex(r"2\mathbf{a}_5", color=PURPLE, font_size=20)
        scaled_a5_label.next_to(scaled_a5.get_end(), UP + LEFT, buff=0.2)
        
        self.play(Create(scaled_a5), Write(scaled_a5_label), run_time=0.6)
        self.wait(0.4)
        
        # 4a_2を2a_5の先端から描画
        scaled_a2 = Vector(
            axes.c2p(4, 0) - axes.c2p(0, 0),
            color=ORANGE,
            stroke_width=5
        ).shift(axes.c2p(-2, 4))
        
        scaled_a2_label = MathTex(r"4\mathbf{a}_2", color=ORANGE, font_size=20)
        scaled_a2_label.next_to(scaled_a2.get_end(), RIGHT, buff=0.2)
        
        self.play(Create(scaled_a2), Write(scaled_a2_label), run_time=0.6)
        self.wait(0.4)
        
        # 結果ベクトル
        result_vector2 = Vector(
            axes.c2p(2, 4) - axes.c2p(0, 0),
            color=RED,
            stroke_width=6
        ).shift(axes.c2p(0, 0))
        
        result_label2 = MathTex(r"2\mathbf{a}_5 + 4\mathbf{a}_2", color=RED, font_size=20)
        result_label2.next_to(result_vector2.get_end(), UP + RIGHT, buff=0.2)
        
        self.play(Create(result_vector2), Write(result_label2), run_time=0.6)
        self.wait(0.4)
        
        # 一致を強調
        match_text2 = Text("一致！", color=YELLOW, font_size=24)
        match_text2.next_to(result_label2, DOWN)
        self.play(Write(match_text2), run_time=0.5)
        self.wait(0.8)
        
        # クリーンアップ
        self.play(
            FadeOut(scaled_a5), FadeOut(scaled_a5_label),
            FadeOut(scaled_a2), FadeOut(scaled_a2_label),
            FadeOut(result_vector2), FadeOut(result_label2), FadeOut(match_text2),
            FadeOut(eq2), FadeOut(calc2a), FadeOut(calc2b), FadeOut(subtitle3)
        )
        self.play(
            a_vectors[4].animate.set_color(GREEN), a_labels[4].animate.set_color(GREEN),
            a_vectors[1].animate.set_color(GREEN), a_labels[1].animate.set_color(GREEN)
        )
        
        # === パート4: 第3の組み合わせ x = 4a_1 + 2a_2 ===
        subtitle4 = Text("組み合わせ3: x = 4a₁ + 2a₂", font_size=28, color=YELLOW)
        subtitle4.next_to(title, DOWN)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.4)
        
        # 右側に式を表示
        eq3 = MathTex(
            r"\mathbf{x} = 4\mathbf{a}_1 + 2\mathbf{a}_2",
            color=WHITE,
            font_size=28
        )
        eq3.to_edge(RIGHT).shift(UP * 2)
        self.play(Write(eq3), run_time=0.6)
        self.wait(0.4)
        
        # 計算過程
        calc3a = MathTex(
            r"= 4\begin{bmatrix} 0 \\ 1 \end{bmatrix} + 2\begin{bmatrix} 1 \\ 0 \end{bmatrix}",
            color=WHITE,
            font_size=24
        )
        calc3a.next_to(eq3, DOWN, buff=0.3, aligned_edge=RIGHT)
        self.play(Write(calc3a), run_time=0.6)
        self.wait(0.4)
        
        calc3b = MathTex(
            r"= \begin{bmatrix} 0 \\ 4 \end{bmatrix} + \begin{bmatrix} 2 \\ 0 \end{bmatrix} = \begin{bmatrix} 2 \\ 4 \end{bmatrix}",
            color=WHITE,
            font_size=24
        )
        calc3b.next_to(calc3a, DOWN, buff=0.3, aligned_edge=RIGHT)
        self.play(Write(calc3b), run_time=0.6)
        self.wait(0.4)
        
        # a_1とa_2を強調
        self.play(
            a_vectors[0].animate.set_color(YELLOW), a_labels[0].animate.set_color(YELLOW),
            a_vectors[1].animate.set_color(YELLOW), a_labels[1].animate.set_color(YELLOW),
            run_time=0.4
        )
        self.wait(0.3)
        
        # 4a_1を原点から描画
        scaled_a1 = Vector(
            axes.c2p(0, 4) - axes.c2p(0, 0),
            color=PURPLE,
            stroke_width=5
        ).shift(axes.c2p(0, 0))
        
        scaled_a1_label = MathTex(r"4\mathbf{a}_1", color=PURPLE, font_size=20)
        scaled_a1_label.next_to(scaled_a1.get_end(), LEFT, buff=0.2)
        
        self.play(Create(scaled_a1), Write(scaled_a1_label), run_time=0.6)
        self.wait(0.4)
        
        # 2a_2を4a_1の先端から描画
        scaled_a2_v2 = Vector(
            axes.c2p(2, 0) - axes.c2p(0, 0),
            color=ORANGE,
            stroke_width=5
        ).shift(axes.c2p(0, 4))
        
        scaled_a2_v2_label = MathTex(r"2\mathbf{a}_2", color=ORANGE, font_size=20)
        scaled_a2_v2_label.next_to(scaled_a2_v2.get_end(), UP, buff=0.2)
        
        self.play(Create(scaled_a2_v2), Write(scaled_a2_v2_label), run_time=0.6)
        self.wait(0.4)
        
        # 結果ベクトル
        result_vector3 = Vector(
            axes.c2p(2, 4) - axes.c2p(0, 0),
            color=RED,
            stroke_width=6
        ).shift(axes.c2p(0, 0))
        
        result_label3 = MathTex(r"4\mathbf{a}_1 + 2\mathbf{a}_2", color=RED, font_size=18)
        result_label3.next_to(result_vector3.get_end(), DOWN + RIGHT, buff=0.2)
        
        self.play(Create(result_vector3), Write(result_label3), run_time=0.6)
        self.wait(0.4)
        
        # 一致を強調
        match_text3 = Text("一致！", color=YELLOW, font_size=24)
        match_text3.next_to(result_label3, DOWN)
        self.play(Write(match_text3), run_time=0.5)
        self.wait(0.8)
        
        # クリーンアップ
        self.play(
            FadeOut(scaled_a1), FadeOut(scaled_a1_label),
            FadeOut(scaled_a2_v2), FadeOut(scaled_a2_v2_label),
            FadeOut(result_vector3), FadeOut(result_label3), FadeOut(match_text3),
            FadeOut(eq3), FadeOut(calc3a), FadeOut(calc3b), FadeOut(subtitle4)
        )
        self.play(
            a_vectors[0].animate.set_color(GREEN), a_labels[0].animate.set_color(GREEN),
            a_vectors[1].animate.set_color(GREEN), a_labels[1].animate.set_color(GREEN)
        )
        
        # === パート4-2: 冗長な組み合わせ1 x = 6a_1 + 2a_2 + 2a_3 ===
        subtitle4b = Text("組み合わせ4: x = 6a₁ + 2a₂ + 2a₃ (少し遠回り)", font_size=26, color=YELLOW)
        subtitle4b.next_to(title, DOWN)
        self.play(Write(subtitle4b), run_time=0.6)
        self.wait(0.4)
        
        # 右側に式を表示
        eq4 = MathTex(
            r"\mathbf{x} = 6\mathbf{a}_1 + 2\mathbf{a}_2 + 2\mathbf{a}_3",
            color=WHITE,
            font_size=26
        )
        eq4.to_edge(RIGHT).shift(UP * 2)
        self.play(Write(eq4), run_time=0.6)
        self.wait(0.4)
        
        # 計算過程
        calc4a = MathTex(
            r"= 6\begin{bmatrix} 0 \\ 1 \end{bmatrix} + 2\begin{bmatrix} 1 \\ 0 \end{bmatrix} + 2\begin{bmatrix} 0 \\ -1 \end{bmatrix}",
            color=WHITE,
            font_size=22
        )
        calc4a.next_to(eq4, DOWN, buff=0.3, aligned_edge=RIGHT)
        self.play(Write(calc4a), run_time=0.6)
        self.wait(0.4)
        
        calc4b = MathTex(
            r"= \begin{bmatrix} 0 \\ 6 \end{bmatrix} + \begin{bmatrix} 2 \\ 0 \end{bmatrix} + \begin{bmatrix} 0 \\ -2 \end{bmatrix}",
            color=WHITE,
            font_size=22
        )
        calc4b.next_to(calc4a, DOWN, buff=0.3, aligned_edge=RIGHT)
        self.play(Write(calc4b), run_time=0.6)
        self.wait(0.4)
        
        calc4c = MathTex(
            r"= \begin{bmatrix} 2 \\ 8 \end{bmatrix} \neq \mathbf{x}",
            color=RED,
            font_size=24
        )
        calc4c.next_to(calc4b, DOWN, buff=0.3, aligned_edge=RIGHT)
        
        calc4c_correct = MathTex(
            r"= \begin{bmatrix} 2 \\ 4 \end{bmatrix}",
            color=WHITE,
            font_size=24
        )
        calc4c_correct.next_to(calc4b, DOWN, buff=0.3, aligned_edge=RIGHT)
        self.play(Write(calc4c_correct), run_time=0.6)
        self.wait(0.4)
        
        # a_1, a_2, a_3を強調
        self.play(
            a_vectors[0].animate.set_color(YELLOW), a_labels[0].animate.set_color(YELLOW),
            a_vectors[1].animate.set_color(YELLOW), a_labels[1].animate.set_color(YELLOW),
            a_vectors[2].animate.set_color(YELLOW), a_labels[2].animate.set_color(YELLOW),
            run_time=0.4
        )
        self.wait(0.3)
        
        # 6a_1を原点から描画
        scaled_a1_v2 = Vector(
            axes.c2p(0, 6) - axes.c2p(0, 0),
            color=PURPLE,
            stroke_width=5
        ).shift(axes.c2p(0, 0))
        
        scaled_a1_v2_label = MathTex(r"6\mathbf{a}_1", color=PURPLE, font_size=20)
        scaled_a1_v2_label.next_to(scaled_a1_v2.get_end(), LEFT, buff=0.2)
        
        self.play(Create(scaled_a1_v2), Write(scaled_a1_v2_label), run_time=0.6)
        self.wait(0.4)
        
        # 2a_2を6a_1の先端から描画
        scaled_a2_v3 = Vector(
            axes.c2p(2, 0) - axes.c2p(0, 0),
            color=ORANGE,
            stroke_width=5
        ).shift(axes.c2p(0, 6))
        
        scaled_a2_v3_label = MathTex(r"2\mathbf{a}_2", color=ORANGE, font_size=20)
        scaled_a2_v3_label.next_to(scaled_a2_v3.get_end(), UP, buff=0.2)
        
        self.play(Create(scaled_a2_v3), Write(scaled_a2_v3_label), run_time=0.6)
        self.wait(0.4)
        
        # 2a_3を(2,6)の先端から描画
        scaled_a3 = Vector(
            axes.c2p(0, -2) - axes.c2p(0, 0),
            color=PINK,
            stroke_width=5
        ).shift(axes.c2p(2, 6))

        scaled_a3_label = MathTex(r"2\mathbf{a}_3", color=PINK, font_size=20)
        scaled_a3_label.next_to(scaled_a3.get_end(), RIGHT, buff=0.2)
        
        self.play(Create(scaled_a3), Write(scaled_a3_label), run_time=0.6)
        self.wait(0.4)
        
        # 結果ベクトル
        result_vector4 = Vector(
            axes.c2p(2, 4) - axes.c2p(0, 0),
            color=RED,
            stroke_width=6
        ).shift(axes.c2p(0, 0))

        result_label4 = MathTex(r"6\mathbf{a}_1 + 2\mathbf{a}_2 + 2\mathbf{a}_3", color=RED, font_size=16)
        result_label4.next_to(result_vector4.get_end(), LEFT, buff=0.2)
        
        self.play(Create(result_vector4), Write(result_label4), run_time=0.6)
        self.wait(0.4)
        
        # 一致を強調
        redundant_note = Text("一致！", color=RED, font_size=22)
        redundant_note.next_to(calc4c_correct, DOWN, buff=0.3)
        self.play(Write(redundant_note), run_time=0.5)
        self.wait(0.8)
        
        # クリーンアップ
        self.play(
            FadeOut(scaled_a1_v2), FadeOut(scaled_a1_v2_label),
            FadeOut(scaled_a2_v3), FadeOut(scaled_a2_v3_label),
            FadeOut(scaled_a3), FadeOut(scaled_a3_label),
            FadeOut(result_vector4), FadeOut(result_label4), FadeOut(redundant_note),
            FadeOut(eq4), FadeOut(calc4a), FadeOut(calc4b), FadeOut(calc4c_correct), FadeOut(subtitle4b)
        )
        self.play(
            a_vectors[0].animate.set_color(GREEN), a_labels[0].animate.set_color(GREEN),
            a_vectors[1].animate.set_color(GREEN), a_labels[1].animate.set_color(GREEN),
            a_vectors[2].animate.set_color(GREEN), a_labels[2].animate.set_color(GREEN)
        )
        
        
        # === パート5: まとめ ===
        subtitle5 = Text("結論: どのベクトルが必要か？", font_size=28, color=GREEN)
        subtitle5.next_to(title, DOWN)
        self.play(Write(subtitle5), run_time=0.6)
        self.wait(0.5)
        
        # 結論
        conclusion = VGroup(
            MathTex(r"\mathbf{x} = 2\mathbf{a}_4", color=GREEN, font_size=22),
            MathTex(r"\mathbf{x} = 2\mathbf{a}_5 + 4\mathbf{a}_2", color=YELLOW, font_size=22),
            MathTex(r"\mathbf{x} = 4\mathbf{a}_1 + 2\mathbf{a}_2", color=GREEN, font_size=22),
            MathTex(r"\mathbf{x} = 6\mathbf{a}_1 + 2\mathbf{a}_2 + 2\mathbf{a}_3", color=RED, font_size=22),
        ).arrange(DOWN, buff=0.2)
        conclusion.to_edge(RIGHT).shift(LEFT * 1.5 + UP * 0.5)
        
        self.play(Write(conclusion), run_time=0.8)
        self.wait(0.5)
        
        # 重要なベクトルを強調
        important_text = Text("必要: a₁とa₂だけで十分", color=YELLOW, font_size=20)
        important_text.next_to(conclusion, DOWN, buff=0.5)
        self.play(Write(important_text), run_time=0.6)
        
        # a₁, a₂を強調
        self.play(
            a_vectors[0].animate.set_color(YELLOW), a_labels[0].animate.set_color(YELLOW),
            a_vectors[1].animate.set_color(YELLOW), a_labels[1].animate.set_color(YELLOW),
            run_time=0.5
        )
        self.wait(0.5)
        
        # 余分なベクトルをフェードアウト
        redundant_text = Text("a₃, a₄, a₅はa₁とa₂の組み合わせで作れる！", color=RED, font_size=21)
        redundant_text.next_to(important_text, DOWN, buff=0.3)
        self.play(Write(redundant_text), run_time=0.7)
        
        self.play(
            a_vectors[2].animate.set_opacity(0.3), a_labels[2].animate.set_opacity(0.3),
            a_vectors[3].animate.set_opacity(0.3), a_labels[3].animate.set_opacity(0.3),
            a_vectors[4].animate.set_opacity(0.3), a_labels[4].animate.set_opacity(0.3),
            run_time=0.6
        )
        