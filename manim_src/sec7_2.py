from manim import *

class PolynomialVectorSpace(Scene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"
        
        # タイトル
        title = Text("N次多項式の空間とベクトル空間", font_size=40, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)
        
        # === イントロ ===
        intro_text = VGroup(
            Text("N次多項式もベクトル空間を形成する", color=WHITE, font_size=32, weight=BOLD),
            Text("多項式 ⇔ (N+1)次元ベクトル", color=YELLOW, font_size=26),
        ).arrange(DOWN, buff=0.4)
        intro_text.shift(DOWN * 0.5)
        
        self.play(Write(intro_text), run_time=1.2)
        self.wait(1.5)
        
        self.play(FadeOut(intro_text))
        self.wait(0.3)
        
        # === パート1: 一般的なN次多項式の表現 ===
        subtitle1 = Text("一般的なN次多項式", font_size=32, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.5)
        
        # N次多項式の一般形
        poly_general = MathTex(
            r"f(x) = c_0 + c_1 x + c_2 x^2 + \cdots + c_N x^N",
            color=BLUE, font_size=36
        )
        poly_general.shift(UP * 1.5)
        self.play(Write(poly_general), run_time=1.0)
        self.wait(1.0)
        
        # 基底の説明
        basis_text = Text("基底:", color=YELLOW, font_size=28, weight=BOLD)
        basis_text.next_to(poly_general, DOWN, buff=0.6)
        self.play(Write(basis_text), run_time=0.5)
        self.wait(0.3)
        
        # 基底を視覚化
        basis_terms = MathTex(
            r"1, \quad x, \quad x^2, \quad \cdots, \quad x^N",
            color=GREEN, font_size=34
        )
        basis_terms.next_to(basis_text, DOWN, buff=0.3)
        self.play(Write(basis_terms), run_time=0.9)
        self.wait(0.8)
        
        # 各基底を別々の方向として説明
        direction_text = Text(
            "各項を別々の「方向」と考える",
            color=YELLOW, font_size=26, slant=ITALIC
        )
        direction_text.next_to(basis_terms, DOWN, buff=0.4)
        self.play(Write(direction_text), run_time=0.8)
        self.wait(1.0)
        
        self.play(
            FadeOut(poly_general), FadeOut(basis_text), 
            FadeOut(basis_terms), FadeOut(direction_text),
            FadeOut(subtitle1)
        )
        self.wait(0.3)
        
        # === パート2: ベクトル表現 ===
        subtitle2 = Text("ベクトル表現への変換", font_size=32, color=PURPLE)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)
        
        # 左側: 多項式
        poly_example = MathTex(
            r"f(x) = c_0 + c_1 x + c_2 x^2 + \cdots + c_N x^N",
            color=BLUE, font_size=32
        )
        poly_example.shift(LEFT * 2 + UP * 1.2)
        self.play(Write(poly_example), run_time=0.8)
        self.wait(0.5)
        
        # 係数の強調
        coeff_box1 = SurroundingRectangle(poly_example[0][4:6], color=RED, buff=0.08)  # c_0
        coeff_box2 = SurroundingRectangle(poly_example[0][7:9], color=RED, buff=0.08)  # c_1
        coeff_box3 = SurroundingRectangle(poly_example[0][11:13], color=RED, buff=0.08)  # c_2
        
        self.play(Create(coeff_box1), run_time=0.3)
        self.wait(0.2)
        self.play(Create(coeff_box2), run_time=0.3)
        self.wait(0.2)
        self.play(Create(coeff_box3), run_time=0.3)
        self.wait(0.6)
        
        # 矢印
        arrow_transform = Arrow(
            poly_example.get_right() + RIGHT * 0.3,
            poly_example.get_right() + RIGHT * 2.0,
            color=YELLOW, buff=0.1, stroke_width=6
        )
        arrow_label = Text("係数を抽出", color=YELLOW, font_size=22)
        arrow_label.next_to(arrow_transform, UP, buff=0.1)
        
        self.play(Create(arrow_transform), Write(arrow_label), run_time=0.7)
        self.wait(0.5)
        
        # 右側: ベクトル
        vector_rep = MathTex(
            r"\begin{bmatrix} c_0 \\ c_1 \\ c_2 \\ \vdots \\ c_N \end{bmatrix}",
            color=RED, font_size=38
        )
        vector_rep.shift(RIGHT * 3.5 + UP * 1.2)
        self.play(Write(vector_rep), run_time=0.9)
        self.wait(1.0)
        
        # (N+1)次元の説明
        dimension_text = Text(
            "(N+1)次元ベクトル",
            color=YELLOW, font_size=26
        )
        dimension_text.next_to(vector_rep, DOWN, buff=0.5)
        self.play(Write(dimension_text), run_time=0.7)
        self.wait(1.0)
        
        self.play(
            FadeOut(poly_example), FadeOut(coeff_box1), FadeOut(coeff_box2), 
            FadeOut(coeff_box3), FadeOut(arrow_transform), FadeOut(arrow_label),
            FadeOut(vector_rep), FadeOut(dimension_text), FadeOut(subtitle2)
        )
        self.wait(0.3)
        
        # === パート3: 具体例（2次多項式） ===
        subtitle3 = Text("具体例: 2次多項式の空間", font_size=32, color=GREEN)
        subtitle3.next_to(title, DOWN)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.5)
        
        # 3つの多項式の例
        example_label = Text("3つの2次多項式:", color=WHITE, font_size=26, weight=BOLD)
        example_label.shift(UP * 2 + LEFT * 4)
        self.play(Write(example_label), run_time=0.5)
        self.wait(0.3)
        
        poly1 = MathTex(r"f_1(x) = 1 + 2x - x^2", color=BLUE, font_size=28)
        poly1.next_to(example_label, DOWN, buff=0.3, aligned_edge=LEFT)
        
        poly2 = MathTex(r"f_2(x) = -1 + 3x^2", color=GREEN, font_size=28)
        poly2.next_to(poly1, DOWN, buff=0.2, aligned_edge=LEFT)
        
        poly3 = MathTex(r"f_3(x) = 4 - x + 2x^2", color=PURPLE, font_size=28)
        poly3.next_to(poly2, DOWN, buff=0.2, aligned_edge=LEFT)
        
        self.play(Write(poly1), run_time=0.6)
        self.wait(0.3)
        self.play(Write(poly2), run_time=0.6)
        self.wait(0.3)
        self.play(Write(poly3), run_time=0.6)
        self.wait(0.8)
        
        # ベクトル表現
        vec_label = Text("ベクトル表現:", color=WHITE, font_size=26, weight=BOLD)
        vec_label.shift(UP * 2 + RIGHT * 1.5)
        self.play(Write(vec_label), run_time=0.5)
        self.wait(0.3)
        
        vec1 = MathTex(r"\mathbf{v}_1 = \begin{bmatrix} 1 \\ 2 \\ -1 \end{bmatrix}", 
                      color=BLUE, font_size=28)
        vec1.next_to(vec_label, DOWN, buff=0.3, aligned_edge=LEFT)
        
        vec2 = MathTex(r"\mathbf{v}_2 = \begin{bmatrix} -1 \\ 0 \\ 3 \end{bmatrix}", 
                      color=GREEN, font_size=28)
        vec2.next_to(vec1, DOWN, buff=0.3, aligned_edge=LEFT)
        
        vec3 = MathTex(r"\mathbf{v}_3 = \begin{bmatrix} 4 \\ -1 \\ 2 \end{bmatrix}", 
                      color=PURPLE, font_size=28)
        vec3.next_to(vec2, DOWN, buff=0.3, aligned_edge=LEFT)
        
        self.play(Write(vec1), run_time=0.6)
        self.wait(0.3)
        self.play(Write(vec2), run_time=0.6)
        
        self.wait(0.3)
        self.play(Write(vec3), run_time=0.6)
        self.wait(1.0)
        
        # 3次元空間での可視化（簡易版）
        axes_label = Text("3次元空間での表現:", color=YELLOW, font_size=24, weight=BOLD)
        axes_label.shift(DOWN * 0.8+ LEFT * 2)
        self.play(Write(axes_label), run_time=0.5)
        self.wait(0.3)
        
        # 簡易的な3D座標軸
        origin_3d = DOWN * 2.5 + LEFT * 2
        x_axis_3d = Line(origin_3d + LEFT * 1.5, origin_3d + RIGHT * 1.5, color=GRAY)
        y_axis_3d = Line(origin_3d, origin_3d + LEFT * 0.8 + UP * 0.6, color=GRAY)
        z_axis_3d = Line(origin_3d, origin_3d + UP * 1.8, color=GRAY)
        
        x_label_3d = MathTex(r"c_0", font_size=20, color=YELLOW).next_to(x_axis_3d.get_right(), DOWN)
        y_label_3d = MathTex(r"c_1", font_size=20, color=YELLOW).next_to(y_axis_3d.get_end(), LEFT)
        z_label_3d = MathTex(r"c_2", font_size=20, color=YELLOW).next_to(z_axis_3d.get_end(), UP)
        
        axes_3d = VGroup(x_axis_3d, y_axis_3d, z_axis_3d, x_label_3d, y_label_3d, z_label_3d)
        self.play(Create(axes_3d), run_time=0.8)
        self.wait(0.5)
        
        # ベクトルを点として表示
        dot1 = Dot(origin_3d + RIGHT * 0.5 + LEFT * 0.3 + UP * 0.3 + DOWN * 0.2, 
                   color=BLUE, radius=0.08)
        label1 = MathTex(r"\mathbf{v}_1", color=BLUE, font_size=18).next_to(dot1, RIGHT, buff=0.1)
        
        dot2 = Dot(origin_3d + LEFT * 0.5 + UP * 0.5, 
                   color=GREEN, radius=0.08)
        label2 = MathTex(r"\mathbf{v}_2", color=GREEN, font_size=18).next_to(dot2, LEFT, buff=0.1)
        
        dot3 = Dot(origin_3d + RIGHT * 1.2 + LEFT * 0.15 + UP * 0.15 + UP * 0.3, 
                   color=PURPLE, radius=0.08)
        label3 = MathTex(r"\mathbf{v}_3", color=PURPLE, font_size=18).next_to(dot3, RIGHT, buff=0.1)
        
        self.play(Create(dot1), Write(label1), run_time=0.5)
        self.wait(0.3)
        self.play(Create(dot2), Write(label2), run_time=0.5)
        self.wait(0.3)
        self.play(Create(dot3), Write(label3), run_time=0.5)
        self.wait(1.0)
        
        self.play(
            FadeOut(example_label), FadeOut(poly1), FadeOut(poly2), FadeOut(poly3),
            FadeOut(vec_label), FadeOut(vec1), FadeOut(vec2), FadeOut(vec3),
            FadeOut(axes_label), FadeOut(axes_3d),
            FadeOut(dot1), FadeOut(dot2), FadeOut(dot3),
            FadeOut(label1), FadeOut(label2), FadeOut(label3),
            FadeOut(subtitle3)
        )
        self.wait(0.3)
        
        # === パート4: 線形性の確認 ===
        subtitle4 = Text("線形空間の条件: 和とスカラ倍", font_size=32, color=ORANGE)
        subtitle4.next_to(title, DOWN)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.5)
        
        # 条件1: 和に閉じている
        condition1_label = Text("条件1: 和に閉じている", color=YELLOW, font_size=28, weight=BOLD)
        condition1_label.shift(UP * 2)
        self.play(Write(condition1_label), run_time=0.6)
        self.wait(0.4)
        
        # 多項式の和
        poly_sum_text = MathTex(
            r"f_1(x) + f_2(x) &= (c_0 + c_1 x + \cdots + c_N x^N) \\",
            r"&\quad + (d_0 + d_1 x + \cdots + d_N x^N) \\",
            r"&= (c_0 + d_0) + (c_1 + d_1)x + \cdots \\",
            r"&\quad + (c_N + d_N) x^N",
            color=WHITE, font_size=32
        )
        poly_sum_text.shift(UP * 0.5)
        self.play(Write(poly_sum_text), run_time=1.5)
        self.wait(1.0)
        
        # 結論
        sum_conclusion = Text(
            "→ また N次多項式になる!",
            color=GREEN, font_size=26, weight=BOLD, slant=ITALIC
        )
        sum_conclusion.next_to(poly_sum_text, DOWN, buff=0.4)
        self.play(Write(sum_conclusion), run_time=0.7)
        self.wait(1.0)
        
        self.play(
            FadeOut(condition1_label), FadeOut(poly_sum_text), FadeOut(sum_conclusion)
        )
        self.wait(0.3)
        
        # 条件2: スカラ倍に閉じている
        condition2_label = Text("条件2: スカラ倍に閉じている", color=YELLOW, font_size=28, weight=BOLD)
        condition2_label.shift(UP * 2)
        self.play(Write(condition2_label), run_time=0.6)
        self.wait(0.4)
        
        # 多項式のスカラ倍
        poly_scalar_text = MathTex(
            r"k \cdot f(x) &= k(c_0 + c_1 x + \cdots + c_N x^N) \\",
            r"&= kc_0 + kc_1 x + \cdots + kc_N x^N",
            color=WHITE, font_size=32
        )
        poly_scalar_text.shift(UP * 0.5)
        self.play(Write(poly_scalar_text), run_time=1.2)
        self.wait(1.0)
        
        # 結論
        scalar_conclusion = Text(
            "→ また N次多項式になる!",
            color=GREEN, font_size=26, weight=BOLD, slant=ITALIC
        )
        scalar_conclusion.next_to(poly_scalar_text, DOWN, buff=0.4)
        self.play(Write(scalar_conclusion), run_time=0.7)
        self.wait(1.0)
        
        self.play(
            FadeOut(condition2_label), FadeOut(poly_scalar_text), FadeOut(scalar_conclusion)
        )
        self.wait(0.3)
        
        # 線形空間であることの確認
        linear_space_text = Text(
            "N次多項式の集合は線形空間（ベクトル空間）!",
            color=GOLD, font_size=30, weight=BOLD
        )
        linear_space_text.shift(UP * 0.5)
        linear_space_box = SurroundingRectangle(linear_space_text, color=GOLD, buff=0.25)
        
        self.play(Write(linear_space_text), Create(linear_space_box), run_time=1.0)
        self.wait(1.5)
        
        self.play(
            FadeOut(linear_space_text), FadeOut(linear_space_box), FadeOut(subtitle4)
        )
        self.wait(0.3)
        
        # === パート5: ベクトル演算との対応 ===
        subtitle5 = Text("ベクトル演算との対応", font_size=32, color=TEAL)
        subtitle5.next_to(title, DOWN)
        self.play(Write(subtitle5), run_time=0.6)
        self.wait(0.5)
        
        # 左側: 多項式の演算
        poly_side_label = Text("多項式:", color=WHITE, font_size=26, weight=BOLD)
        poly_side_label.to_edge(LEFT).shift(UP * 1)
        self.play(Write(poly_side_label), run_time=0.5)
        self.wait(0.3)
        
        poly_op1 = MathTex(r"f_1(x) = 1 + 2x", color=BLUE, font_size=28)
        poly_op1.shift(LEFT * 3.5 + UP * 0.3)
        
        poly_op2 = MathTex(r"f_2(x) = 3 - x", color=GREEN, font_size=28)
        poly_op2.next_to(poly_op1, DOWN, buff=0.2, aligned_edge=LEFT)
        
        self.play(Write(poly_op1), Write(poly_op2), run_time=0.8)
        self.wait(0.5)
        
        plus_sign_poly = MathTex(r"+", color=YELLOW, font_size=32)
        plus_sign_poly.move_to((poly_op1.get_left() + poly_op2.get_left()) / 2 + LEFT * 0.5)
        
        self.play(Write(plus_sign_poly), run_time=0.4)
        self.wait(0.3)
        
        line_poly = Line(
            poly_op2.get_left() + LEFT * 0.8 + DOWN * 0.2,
            poly_op2.get_right() + RIGHT * 0.2 + DOWN * 0.2,
            color=YELLOW
        )
        self.play(Create(line_poly), run_time=0.4)
        self.wait(0.3)
        
        poly_result = MathTex(r"f_1 + f_2 = 4 + x", color=YELLOW, font_size=28)
        poly_result.next_to(line_poly, DOWN, buff=0.3, aligned_edge=LEFT)
        poly_result.shift(RIGHT * 0.5)
        self.play(Write(poly_result), run_time=0.7)
        self.wait(0.8)
        
        # 右側: ベクトルの演算
        vec_side_label = Text("ベクトル:", color=WHITE, font_size=26, weight=BOLD)
        vec_side_label.to_edge(RIGHT).shift(LEFT * 3 + UP * 1)
        self.play(Write(vec_side_label), run_time=0.5)
        self.wait(0.3)
        
        vec_op1 = MathTex(r"\begin{bmatrix} 1 \\ 2 \end{bmatrix}", color=BLUE, font_size=28)
        vec_op1.shift(RIGHT * 2 + UP * 0.3)
        
        vec_op2 = MathTex(r"\begin{bmatrix} 3 \\ -1 \end{bmatrix}", color=GREEN, font_size=28)
        vec_op2.next_to(vec_op1, DOWN, buff=0.4, aligned_edge=LEFT)
        
        self.play(Write(vec_op1), Write(vec_op2), run_time=0.8)
        self.wait(0.5)
        
        plus_sign_vec = MathTex(r"+", color=YELLOW, font_size=32)
        plus_sign_vec.move_to((vec_op1.get_left() + vec_op2.get_left()) / 2 + LEFT * 0.4)
        
        self.play(Write(plus_sign_vec), run_time=0.4)
        self.wait(0.3)
        
        line_vec = Line(
            vec_op2.get_left() + LEFT * 0.6 + DOWN * 0.3,
            vec_op2.get_right() + RIGHT * 0.2 + DOWN * 0.3,
            color=YELLOW
        )
        self.play(Create(line_vec), run_time=0.4)
        self.wait(0.3)
        
        vec_result = MathTex(r"\begin{bmatrix} 4 \\ 1 \end{bmatrix}", color=YELLOW, font_size=28)
        vec_result.next_to(line_vec, DOWN, buff=0.4, aligned_edge=LEFT)
        vec_result.shift(RIGHT * 0.2)
        self.play(Write(vec_result), run_time=0.7)
        self.wait(0.8)
        
        # 対応を示す両矢印
        correspondence_arrow = DoubleArrow(
            poly_result.get_right() + RIGHT * 0.3,
            vec_result.get_left() + LEFT * 0.3,
            color=ORANGE, buff=0.1, stroke_width=5
        )
        correspondence_label = Text("同じ演算!", color=ORANGE, font_size=22, weight=BOLD)
        correspondence_label.next_to(correspondence_arrow, DOWN, buff=0.1)
        
        self.play(Create(correspondence_arrow), Write(correspondence_label), run_time=0.8)
        self.wait(1.5)
        
        self.play(
            FadeOut(poly_side_label), FadeOut(poly_op1), FadeOut(poly_op2),
            FadeOut(plus_sign_poly), FadeOut(line_poly), FadeOut(poly_result),
            FadeOut(vec_side_label), FadeOut(vec_op1), FadeOut(vec_op2),
            FadeOut(plus_sign_vec), FadeOut(line_vec), FadeOut(vec_result),
            FadeOut(correspondence_arrow), FadeOut(correspondence_label),
            FadeOut(subtitle5)
        )
        self.wait(0.3)
        
        # === まとめ ===
        summary_subtitle = Text("まとめ", font_size=32, color=GOLD, weight=BOLD)
        summary_subtitle.next_to(title, DOWN)
        self.play(Write(summary_subtitle), run_time=0.6)
        self.wait(0.5)
        
        # まとめのポイント
        summary_points = VGroup(
            VGroup(
                Text("1.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("N次多項式の各項 1, x, x², ..., x^N を", color=WHITE, font_size=24),
                    Text("別々の「方向」と考える", color=YELLOW, font_size=24, weight=BOLD),
                ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            
            VGroup(
                Text("2.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("係数を成分として (N+1)次元ベクトルで", color=WHITE, font_size=24),
                    Text("多項式空間の点を表現できる", color=GREEN, font_size=24, weight=BOLD),
                ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            
            VGroup(
                Text("3.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("多項式は和とスカラ倍に閉じているため", color=WHITE, font_size=24),
                    Text("線形空間（ベクトル空間）を形成する", color=ORANGE, font_size=24, weight=BOLD),
                ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            
            VGroup(
                Text("4.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("多項式の演算 ⇔ ベクトルの演算", color=WHITE, font_size=24),
                    Text("という対応が成り立つ!", color=TEAL, font_size=24, weight=BOLD),
                ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        summary_points.scale(0.95)
        summary_points.shift(UP * 0.1)
        
        for point in summary_points:
            self.play(Write(point), run_time=0.9)
            self.wait(0.6)
        
        self.wait(1.5)
        
        # 最終メッセージ
        final_message = Text(
            "抽象的な多項式も具体的なベクトルとして扱える!",
            color=YELLOW, font_size=28, weight=BOLD, slant=ITALIC
        )
        final_message.shift(DOWN * 2.5)
        final_box = SurroundingRectangle(final_message, color=YELLOW, buff=0.25)
        self.play(Write(final_message), Create(final_box), run_time=1.0)
        self.wait(2.0)
        
        # フェードアウト
        all_objects = VGroup(
            title, summary_subtitle, summary_points, 
            final_message, final_box
        )
        self.play(FadeOut(all_objects), run_time=1.0)
        self.wait(0.5)
