from manim import *

class VectorScalarMultiplication(Scene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"
        
        # 座標平面を作成
        plane = NumberPlane(
            x_range=[-1, 6],
            y_range=[-1, 5],
            x_length=10,
            y_length=8,
            axis_config={"color": GRAY},
            background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )
        plane.add_coordinates()
        self.add(plane)
        
        # タイトル
        title = Text("ベクトルはスカラ倍しても加算してもベクトル", font_size=32, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # === パート1: スカラ倍 ===
        subtitle1 = Text("スカラ倍しても新たな矢印", font_size=28, color=YELLOW)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1))
        self.wait(1)
        
        # 元のベクトル
        vec1 = Vector([1, 2], color=BLUE)
        vec1.put_start_and_end_on(plane.c2p(0, 0), plane.c2p(1, 2))
        vec1_label = MathTex(r"\boldsymbol{v} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}", color=BLUE)
        vec1_label.next_to(vec1.get_end(), RIGHT, buff=0.2)
        
        self.play(Create(vec1), Write(vec1_label))
        self.wait(1)
        
        # スカラ倍の式
        scalar_formula = MathTex(r"2 \times \boldsymbol{v} = 2 \times \begin{bmatrix} 1 \\ 2 \end{bmatrix}", color=WHITE)
        scalar_formula.to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(scalar_formula))
        self.wait(1)
        
        # スカラ倍の結果
        vec1_scaled = Vector([2, 4], color=RED)
        vec1_scaled.put_start_and_end_on(plane.c2p(0, 0), plane.c2p(2, 4))
        vec1_scaled_label = MathTex(r"2\boldsymbol{v} = \begin{bmatrix} 2 \\ 4 \end{bmatrix}", color=RED)
        vec1_scaled_label.next_to(vec1_scaled.get_end(), RIGHT, buff=0.2)
        
        result_formula = MathTex(r"= \begin{bmatrix} 2 \\ 4 \end{bmatrix}", color=RED)
        result_formula.next_to(scalar_formula, RIGHT)
        
        self.play(
            Create(vec1_scaled),
            Write(vec1_scaled_label),
            Write(result_formula)
        )
        self.wait(2)
        
        # クリア
        self.play(
            FadeOut(vec1), FadeOut(vec1_label),
            FadeOut(vec1_scaled), FadeOut(vec1_scaled_label),
            FadeOut(scalar_formula), FadeOut(result_formula),
            FadeOut(subtitle1)
        )
        self.wait(1)
        
        # === パート2: 加算 ===
        subtitle2 = Text("足しても新たな矢印", font_size=28, color=YELLOW)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2))
        self.wait(1)
        
        # 2つのベクトル
        vec_a = Vector([2, 1], color=BLUE)
        vec_a.put_start_and_end_on(plane.c2p(0, 0), plane.c2p(2, 1))
        vec_a_label = MathTex(r"\boldsymbol{a} = \begin{bmatrix} 2 \\ 1 \end{bmatrix}", color=BLUE)
        vec_a_label.next_to(vec_a.get_end(), DOWN, buff=0.2)
        
        vec_b = Vector([1, 2], color=GREEN)
        vec_b.put_start_and_end_on(plane.c2p(0, 0), plane.c2p(1, 2))
        vec_b_label = MathTex(r"\boldsymbol{b} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}", color=GREEN)
        vec_b_label.next_to(vec_b.get_end(), LEFT, buff=0.2)
        
        self.play(
            Create(vec_a), Write(vec_a_label),
            Create(vec_b), Write(vec_b_label)
        )
        self.wait(1)
        
        # 加算の式
        addition_formula = MathTex(
            r"\boldsymbol{a} + \boldsymbol{b} = \begin{bmatrix} 2 \\ 1 \end{bmatrix} + \begin{bmatrix} 1 \\ 2 \end{bmatrix}",
            color=WHITE
        )
        addition_formula.to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(addition_formula))
        self.wait(1)
        
        # ベクトルbをベクトルaの先端に移動
        vec_b_shifted = Vector([1, 2], color=GREEN)
        vec_b_shifted.put_start_and_end_on(plane.c2p(2, 1), plane.c2p(3, 3))
        vec_b_label_shifted = vec_b_label.copy()
        vec_b_label_shifted.next_to(vec_b_shifted.get_center(), RIGHT, buff=0.2)
        
        self.play(
            Transform(vec_b, vec_b_shifted),
            Transform(vec_b_label, vec_b_label_shifted)
        )
        self.wait(1)
        
        # 結果のベクトル
        result_vec = Vector([3, 3], color=YELLOW)
        result_vec.put_start_and_end_on(plane.c2p(0, 0), plane.c2p(3, 3))
        result_label = MathTex(r"\boldsymbol{a} + \boldsymbol{b} = \begin{bmatrix} 3 \\ 3 \end{bmatrix}", color=YELLOW)
        result_label.next_to(result_vec.get_center(), UP, buff=0.3)
        
        result_formula2 = MathTex(r"= \begin{bmatrix} 3 \\ 3 \end{bmatrix}", color=YELLOW)
        result_formula2.next_to(addition_formula, RIGHT)
        
        self.play(
            Create(result_vec),
            Write(result_label),
            Write(result_formula2)
        )
        self.wait(2)
        
        # 最終的な強調
        conclusion = Text("どちらも新しいベクトルが生成される！", font_size=24, color=YELLOW)
        conclusion.to_edge(DOWN)
        self.play(
            Indicate(result_vec),
            Indicate(result_formula2),
            run_time=2
        )
        self.play(Write(conclusion))
        self.wait(2)
        
        # クリア
        self.play(
            FadeOut(vec_a), FadeOut(vec_a_label),
            FadeOut(vec_b), FadeOut(vec_b_label),
            FadeOut(result_vec), FadeOut(result_label),
            FadeOut(addition_formula), FadeOut(result_formula2),
            FadeOut(subtitle2), FadeOut(conclusion)
        )
        self.wait(1)
        
        # === パート3: スカラ倍したもの同士の加算 ===
        subtitle3 = Text("スカラ倍したベクトル同士も足せる", font_size=28, color=YELLOW)
        subtitle3.next_to(title, DOWN)
        self.play(Write(subtitle3))
        self.wait(1)
        
        # 元のベクトル2つ
        vec_u = Vector([1, 1], color=BLUE)
        vec_u.put_start_and_end_on(plane.c2p(0, 0), plane.c2p(1, 1))
        vec_u_label = MathTex(r"\boldsymbol{u} = \begin{bmatrix} 1 \\ 1 \end{bmatrix}", color=BLUE)
        vec_u_label.next_to(vec_u.get_end(), UP + LEFT, buff=0.2)
        
        vec_w = Vector([2, 0], color=GREEN)
        vec_w.put_start_and_end_on(plane.c2p(0, 0), plane.c2p(2, 0))
        vec_w_label = MathTex(r"\boldsymbol{w} = \begin{bmatrix} 2 \\ 0 \end{bmatrix}", color=GREEN)
        vec_w_label.next_to(vec_w.get_end(), DOWN, buff=0.2)
        
        self.play(
            Create(vec_u), Write(vec_u_label),
            Create(vec_w), Write(vec_w_label)
        )
        self.wait(1)
        
        # スカラ倍の式
        combined_formula = MathTex(
            r"2\boldsymbol{u} + 1.5\boldsymbol{w} = 2\begin{bmatrix} 1 \\ 1 \end{bmatrix} + 1.5\begin{bmatrix} 2 \\ 0 \end{bmatrix}",
            color=WHITE,
            font_size=36
        )
        combined_formula.to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(combined_formula))
        self.wait(1)
        
        # 2u を計算
        vec_2u = Vector([2, 2], color=BLUE)
        vec_2u.put_start_and_end_on(plane.c2p(0, 0), plane.c2p(2, 2))
        vec_2u_label = MathTex(r"2\boldsymbol{u} = \begin{bmatrix} 2 \\ 2 \end{bmatrix}", color=BLUE)
        vec_2u_label.next_to(vec_2u.get_end(), UP + LEFT, buff=0.2)
        
        self.play(
            Transform(vec_u, vec_2u),
            Transform(vec_u_label, vec_2u_label)
        )
        self.wait(1)
        
        # 1.5w を計算
        vec_1p5w = Vector([3, 0], color=GREEN)
        vec_1p5w.put_start_and_end_on(plane.c2p(0, 0), plane.c2p(3, 0))
        vec_1p5w_label = MathTex(r"1.5\boldsymbol{w} = \begin{bmatrix} 3 \\ 0 \end{bmatrix}", color=GREEN)
        vec_1p5w_label.next_to(vec_1p5w.get_end(), DOWN, buff=0.2)
        
        self.play(
            Transform(vec_w, vec_1p5w),
            Transform(vec_w_label, vec_1p5w_label)
        )
        self.wait(1)
        
        # 計算結果を表示
        calc_result = MathTex(
            r"= \begin{bmatrix} 2 \\ 2 \end{bmatrix} + \begin{bmatrix} 3 \\ 0 \end{bmatrix}",
            color=WHITE,
            font_size=36
        )
        calc_result.next_to(combined_formula, DOWN, buff=0.3)
        self.play(Write(calc_result))
        self.wait(1)
        
        # 1.5wを2uの先端に移動
        vec_1p5w_shifted = Vector([3, 0], color=GREEN)
        vec_1p5w_shifted.put_start_and_end_on(plane.c2p(2, 2), plane.c2p(5, 2))
        vec_1p5w_label_shifted = vec_1p5w_label.copy()
        vec_1p5w_label_shifted.next_to(vec_1p5w_shifted.get_center(), UP, buff=0.2)
        
        self.play(
            Transform(vec_w, vec_1p5w_shifted),
            Transform(vec_w_label, vec_1p5w_label_shifted)
        )
        self.wait(1)
        
        # 結果のベクトル
        result_vec_final = Vector([5, 2], color=YELLOW)
        result_vec_final.put_start_and_end_on(plane.c2p(0, 0), plane.c2p(5, 2))
        result_label_final = MathTex(r"2\boldsymbol{u} + 1.5\boldsymbol{w} = \begin{bmatrix} 5 \\ 2 \end{bmatrix}", color=YELLOW)
        result_label_final.next_to(result_vec_final.get_center(), UP, buff=0.3)
        
        final_result = MathTex(
            r"= \begin{bmatrix} 5 \\ 2 \end{bmatrix}",
            color=YELLOW,
            font_size=36
        )
        final_result.next_to(calc_result, DOWN, buff=0.3)
        
        self.play(
            Create(result_vec_final),
            Write(result_label_final),
            Write(final_result)
        )
        self.wait(2)
        
        # 最終メッセージ
        final_message = Text("スカラ倍と加算を組み合わせても\n新しいベクトルが生まれる！", 
                            font_size=24, color=YELLOW, line_spacing=1.2)
        final_message.to_corner(DOWN + LEFT, buff=0.5)
        
        self.play(
            Indicate(result_vec_final),
            Indicate(final_result),
            run_time=2
        )
        self.play(Write(final_message))
        self.wait(3)
