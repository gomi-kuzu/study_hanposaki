from manim import *

class MatrixMultiplicationVisualization(ThreeDScene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"
        
        # タイトル
        title = Text("行列の積の直感的理解", font_size=40, color=WHITE)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)
        
        # === イントロ: 行列の積とは ===
        intro_subtitle = Text("L×M 行列と M×N 行列の積", font_size=32, color=YELLOW)
        intro_subtitle.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(intro_subtitle)
        self.play(Write(intro_subtitle), run_time=0.6)
        self.wait(0.5)
        
        intro_text = VGroup(
            Text("行列の積の基本形:", color=WHITE, font_size=26),
            MathTex(r"A_{L \times M} \times B_{M \times N} = C_{L \times N}",
                   color=YELLOW, font_size=32),
            Text("例: 2×3 行列と 3×2 行列の積", color=WHITE, font_size=24),
        ).arrange(DOWN, buff=0.4)
        intro_text.shift(DOWN * 0.5)
        self.add_fixed_in_frame_mobjects(intro_text)
        
        self.play(Write(intro_text), run_time=1.2)
        self.wait(1.5)
        
        self.play(FadeOut(intro_text), FadeOut(intro_subtitle))
        self.wait(0.3)
        
        # === パート1: 具体例の提示 ===
        subtitle1 = Text("具体例: 行列の積を計算", font_size=32, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle1)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.5)
        
        # 行列A, B, Cを表示
        matrix_equation = VGroup(
            MathTex(r"A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}",
                   color=RED, font_size=28),
            MathTex(r"B = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}",
                   color=BLUE, font_size=28),
            MathTex(r"C = A \times B = \begin{bmatrix} 22 & 28 \\ 49 & 64 \end{bmatrix}",
                   color=GREEN, font_size=28),
        ).arrange(DOWN, buff=0.5)
        matrix_equation.shift(UP * 0.8)
        self.add_fixed_in_frame_mobjects(matrix_equation)
        
        self.play(Write(matrix_equation[0]), run_time=0.8)
        self.wait(0.5)
        self.play(Write(matrix_equation[1]), run_time=0.8)
        self.wait(0.5)
        self.play(Write(matrix_equation[2]), run_time=0.8)
        self.wait(1.0)
        
        # 次元の説明
        dimension_note = VGroup(
            MathTex(r"(2 \times 3)", color=RED, font_size=24),
            MathTex(r"\times", color=WHITE, font_size=24),
            MathTex(r"(3 \times 2)", color=BLUE, font_size=24),
            MathTex(r"=", color=WHITE, font_size=24),
            MathTex(r"(2 \times 2)", color=GREEN, font_size=24),
        ).arrange(RIGHT, buff=0.3)
        dimension_note.shift(DOWN * 2)
        self.add_fixed_in_frame_mobjects(dimension_note)
        self.play(Write(dimension_note), run_time=0.8)
        self.wait(1.2)
        
        self.play(FadeOut(matrix_equation), FadeOut(dimension_note), FadeOut(subtitle1))
        self.wait(0.3)
        
        # === パート2: 要素の計算方法 ===
        subtitle2 = VGroup(
            Text("要素 ", font_size=32, color=PURPLE),
            MathTex(r"c_{\ell n}", font_size=32, color=PURPLE),
            Text(" の計算方法", font_size=32, color=PURPLE),
        ).arrange(RIGHT, buff=0.1)
        subtitle2.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle2)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)
        
        # 重要な公式
        formula_title = Text("重要な公式:", color=YELLOW, font_size=26, weight=BOLD)
        formula_title.shift(UP * 2)
        self.add_fixed_in_frame_mobjects(formula_title)
        self.play(Write(formula_title), run_time=0.6)
        self.wait(0.3)
        
        key_formula = VGroup(
            MathTex(r"c_{\ell n} = ", color=YELLOW, font_size=30),
            Text("(Aのl行目)", color=YELLOW, font_size=24),
            MathTex(r"\cdot", color=YELLOW, font_size=30),
            Text("(Bのn列目)", color=YELLOW, font_size=24),
        ).arrange(RIGHT, buff=0.2)
        key_formula.next_to(formula_title, DOWN, buff=0.4)
        self.add_fixed_in_frame_mobjects(key_formula)
        self.play(Write(key_formula), run_time=0.8)
        self.wait(1.0)
        
        # 具体例: c_11を計算
        example_title = Text("例: c₁₁ を計算", color=ORANGE, font_size=26, weight=BOLD)
        example_title.shift(UP * 0.3)
        self.add_fixed_in_frame_mobjects(example_title)
        self.play(Write(example_title), run_time=0.6)
        self.wait(0.3)
        
        # Aの1行目とBの1列目を強調
        a_row1 = VGroup(
            Text("Aの1行目:", color=RED, font_size=24),
            MathTex(r"[1, 2, 3]", color=RED, font_size=26),
        ).arrange(RIGHT, buff=0.2)
        b_col1 = VGroup(
            Text("Bの1列目:", color=BLUE, font_size=24),
            MathTex(r"[1, 3, 5]^T", color=BLUE, font_size=26),
        ).arrange(RIGHT, buff=0.2)
        row_col = VGroup(a_row1, b_col1).arrange(DOWN, buff=0.3)
        row_col.shift(DOWN * 0.5)
        self.add_fixed_in_frame_mobjects(row_col)
        self.play(Write(row_col), run_time=0.8)
        self.wait(0.8)
        
        # 内積の計算
        dot_product_calc = MathTex(
            r"c_{11} = 1 \times 1 + 2 \times 3 + 3 \times 5",
            color=WHITE, font_size=28
        )
        dot_product_calc.shift(DOWN * 1.5)
        self.add_fixed_in_frame_mobjects(dot_product_calc)
        self.play(Write(dot_product_calc), run_time=0.8)
        self.wait(0.6)
        
        dot_product_result = MathTex(
            r"= 1 + 6 + 15 = 22",
            color=GREEN, font_size=28
        )
        dot_product_result.next_to(dot_product_calc, DOWN, buff=0.3)
        self.add_fixed_in_frame_mobjects(dot_product_result)
        self.play(Write(dot_product_result), run_time=0.8)
        self.wait(1.0)
        
        # 一般的な形
        general_form = MathTex(
            r"c_{\ell n} = \sum_{m=1}^{M} a_{\ell m} \cdot b_{mn}",
            color=YELLOW, font_size=28
        )
        general_form.shift(DOWN * 2.8)
        self.add_fixed_in_frame_mobjects(general_form)
        self.play(Write(general_form), run_time=0.8)
        self.wait(1.5)
        
        self.play(
            FadeOut(formula_title), FadeOut(key_formula),
            FadeOut(example_title), FadeOut(row_col),
            FadeOut(dot_product_calc), FadeOut(dot_product_result),
            FadeOut(general_form), FadeOut(subtitle2)
        )
        self.wait(0.3)
        
        # === パート3: 経路の総和としての解釈 ===
        subtitle3 = Text("別の視点: 経路の総和", font_size=32, color=TEAL)
        subtitle3.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle3)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.5)
        
        path_intro = VGroup(
            Text("行列の積を「経路」として理解する", color=YELLOW, font_size=26, weight=BOLD),
            Text("左端(Aの行) → 中間点(M個) → 右端(Bの列)", color=WHITE, font_size=24),
        ).arrange(DOWN, buff=0.3)
        path_intro.shift(UP * 2)
        self.add_fixed_in_frame_mobjects(path_intro)
        self.play(Write(path_intro), run_time=1.0)
        self.wait(1.0)
        
        # グラフ構造の描画
        # 左端: Aの1行目
        left_node = Circle(radius=0.3, color=RED, fill_opacity=0.5)
        left_node.shift(LEFT * 4 + UP * 0.5)
        left_label = MathTex(r"A_1", color=RED, font_size=24)
        left_label.next_to(left_node, LEFT, buff=0.2)
        self.add_fixed_in_frame_mobjects(left_node, left_label)
        
        # 右端: Bの1列目
        right_node = Circle(radius=0.3, color=BLUE, fill_opacity=0.5)
        right_node.shift(RIGHT * 4 + UP * 0.5)
        right_label = MathTex(r"B_1", color=BLUE, font_size=24)
        right_label.next_to(right_node, RIGHT, buff=0.2)
        self.add_fixed_in_frame_mobjects(right_node, right_label)
        
        # 中間点: m=1, 2, 3
        middle_nodes = VGroup()
        middle_labels = VGroup()
        middle_positions = [UP * 1.5, UP * 0.5, DOWN * 0.5]
        
        for i, pos in enumerate(middle_positions):
            node = Circle(radius=0.25, color=YELLOW, fill_opacity=0.3)
            node.shift(pos)
            label = MathTex(f"m={i+1}", color=YELLOW, font_size=20)
            label.next_to(node, UP, buff=0.1)
            middle_nodes.add(node)
            middle_labels.add(label)
        
        self.add_fixed_in_frame_mobjects(middle_nodes, middle_labels)
        
        self.play(
            Create(left_node), Write(left_label),
            Create(right_node), Write(right_label),
            run_time=0.8
        )
        self.wait(0.5)
        self.play(Create(middle_nodes), Write(middle_labels), run_time=0.8)
        self.wait(0.8)
        
        # 経路を描画
        paths = VGroup()
        path_labels = VGroup()
        
        for i, middle_node in enumerate(middle_nodes):
            # 左から中間へ
            left_arrow = Arrow(
                left_node.get_right(),
                middle_node.get_left(),
                buff=0.1,
                color=ORANGE,
                stroke_width=3
            )
            # 中間から右へ
            right_arrow = Arrow(
                middle_node.get_right(),
                right_node.get_left(),
                buff=0.1,
                color=ORANGE,
                stroke_width=3
            )
            
            # 経路の重みラベル
            a_weight = MathTex(f"a_{{1{i+1}}}", color=RED, font_size=18)
            a_weight.next_to(left_arrow, DOWN, buff=0.05)
            b_weight = MathTex(f"b_{{{i+1}1}}", color=BLUE, font_size=18)
            b_weight.next_to(right_arrow, DOWN, buff=0.05)
            
            paths.add(left_arrow, right_arrow)
            path_labels.add(a_weight, b_weight)
        
        self.add_fixed_in_frame_mobjects(paths, path_labels)
        
        # 経路を1つずつアニメーション
        for i in range(len(middle_nodes)):
            self.play(
                Create(paths[2*i]), Write(path_labels[2*i]),
                Create(paths[2*i+1]), Write(path_labels[2*i+1]),
                run_time=0.6
            )
            self.wait(0.4)
        
        self.wait(0.8)
        
        # 経路の説明
        path_explanation = VGroup(
            Text("各経路の重み:", color=ORANGE, font_size=24, weight=BOLD),
            MathTex(r"m=1: \quad a_{11} \times b_{11} = 1 \times 1 = 1", 
                   color=WHITE, font_size=22),
            MathTex(r"m=2: \quad a_{12} \times b_{21} = 2 \times 3 = 6", 
                   color=WHITE, font_size=22),
            MathTex(r"m=3: \quad a_{13} \times b_{31} = 3 \times 5 = 15", 
                   color=WHITE, font_size=22),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        path_explanation.to_corner(DL).shift(UP * 0.5)
        self.add_fixed_in_frame_mobjects(path_explanation)
        self.play(Write(path_explanation), run_time=1.2)
        self.wait(1.0)
        
        # 総和
        path_sum = MathTex(
            r"c_{11} = 1 + 6 + 15 = 22",
            color=GREEN, font_size=28
        )
        path_sum.shift(DOWN * 2.5)
        self.add_fixed_in_frame_mobjects(path_sum)
        
        sum_box = SurroundingRectangle(path_sum, color=GREEN, buff=0.2)
        self.add_fixed_in_frame_mobjects(sum_box)
        
        self.play(Write(path_sum), Create(sum_box), run_time=0.8)
        self.wait(1.5)
        
        # 重要なポイント
        key_point = Text(
            "経路の総和 = 行列の積の要素",
            color=YELLOW, font_size=26, weight=BOLD, slant=ITALIC
        )
        key_point.to_corner(UR).shift(DOWN * 2)
        self.add_fixed_in_frame_mobjects(key_point)
        self.play(Write(key_point), run_time=0.8)
        self.wait(1.5)
        
        self.play(
            FadeOut(path_intro), FadeOut(left_node), FadeOut(left_label),
            FadeOut(right_node), FadeOut(right_label),
            FadeOut(middle_nodes), FadeOut(middle_labels),
            FadeOut(paths), FadeOut(path_labels),
            FadeOut(path_explanation), FadeOut(path_sum),
            FadeOut(sum_box), FadeOut(key_point),
            FadeOut(subtitle3)
        )
        self.wait(0.3)
        
        # === パート4: より一般的な要素での経路 ===
        subtitle4 = VGroup(
            Text("一般の要素 ", font_size=32, color=GOLD),
            MathTex(r"c_{\ell n}", font_size=32, color=GOLD),
            Text(" での経路", font_size=32, color=GOLD),
        ).arrange(RIGHT, buff=0.1)
        subtitle4.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle4)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.5)
        
        general_path_text = VGroup(
            VGroup(
                Text("任意の要素 ", color=YELLOW, font_size=26, weight=BOLD),
                MathTex(r"c_{\ell n}", color=YELLOW, font_size=26),
                Text(" について:", color=YELLOW, font_size=26, weight=BOLD),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("左端: Aの", color=RED, font_size=24),
                MathTex(r"\ell", color=RED, font_size=24),
                Text("行目", color=RED, font_size=24),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("右端: Bの", color=BLUE, font_size=24),
                MathTex(r"n", color=BLUE, font_size=24),
                Text("列目", color=BLUE, font_size=24),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("中間:", color=YELLOW, font_size=24),
                MathTex(r"M", color=YELLOW, font_size=24),
                Text("個の経路", color=YELLOW, font_size=24),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        general_path_text.shift(UP * 1.2)
        self.add_fixed_in_frame_mobjects(general_path_text)
        self.play(Write(general_path_text), run_time=1.0)
        self.wait(1.0)
        
        # 一般的な図
        general_left = Circle(radius=0.3, color=RED, fill_opacity=0.5)
        general_left.shift(LEFT * 4)
        general_left_label = MathTex(r"A_\ell", color=RED, font_size=24)
        general_left_label.next_to(general_left, LEFT, buff=0.2)
        
        general_right = Circle(radius=0.3, color=BLUE, fill_opacity=0.5)
        general_right.shift(RIGHT * 4)
        general_right_label = MathTex(r"B_n", color=BLUE, font_size=24)
        general_right_label.next_to(general_right, RIGHT, buff=0.2)
        
        general_middle = VGroup()
        for i in range(3):
            node = Circle(radius=0.2, color=YELLOW, fill_opacity=0.3)
            node.shift(UP * (1 - i) * 0.8)
            general_middle.add(node)
        
        m_label = MathTex(r"m=1,2,...,M", color=YELLOW, font_size=20)
        m_label.next_to(general_middle, DOWN, buff=0.3)
        
        self.add_fixed_in_frame_mobjects(
            general_left, general_left_label,
            general_right, general_right_label,
            general_middle, m_label
        )
        
        self.play(
            Create(general_left), Write(general_left_label),
            Create(general_right), Write(general_right_label),
            Create(general_middle), Write(m_label),
            run_time=1.0
        )
        self.wait(0.8)
        
        # 一般的な経路の式
        general_formula = MathTex(
            r"c_{\ell n} = \sum_{m=1}^{M} a_{\ell m} \times b_{mn}",
            color=GREEN, font_size=30
        )
        general_formula.shift(DOWN * 2)
        general_formula_box = SurroundingRectangle(general_formula, color=GREEN, buff=0.2)
        self.add_fixed_in_frame_mobjects(general_formula, general_formula_box)
        self.play(Write(general_formula), Create(general_formula_box), run_time=0.8)
        self.wait(1.5)
        
        interpretation = Text(
            "M個の経路の重みの総和",
            color=YELLOW, font_size=26, slant=ITALIC
        )
        interpretation.next_to(general_formula, DOWN, buff=0.4)
        self.add_fixed_in_frame_mobjects(interpretation)
        self.play(Write(interpretation), run_time=0.8)
        self.wait(1.5)
        
        self.play(
            FadeOut(general_path_text),
            FadeOut(general_left), FadeOut(general_left_label),
            FadeOut(general_right), FadeOut(general_right_label),
            FadeOut(general_middle), FadeOut(m_label),
            FadeOut(general_formula), FadeOut(general_formula_box),
            FadeOut(interpretation), FadeOut(subtitle4)
        )
        self.wait(0.3)
        
        # === まとめ ===
        summary_subtitle = Text("まとめ", font_size=36, color=GOLD, weight=BOLD)
        summary_subtitle.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(summary_subtitle)
        self.play(Write(summary_subtitle), run_time=0.6)
        self.wait(0.5)
        
        # まとめのポイント
        summary_points = VGroup(
            VGroup(
                Text("1.", color=WHITE, font_size=26, weight=BOLD),
                Text("行列の積: ", color=WHITE, font_size=24),
                MathTex(r"c_{\ell n}", color=WHITE, font_size=24),
                Text(" = Aのℓ行 · Bのn列", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.2, aligned_edge=UP),
            VGroup(
                Text("2.", color=WHITE, font_size=26, weight=BOLD),
                Text("内積として: 対応する要素の積の和", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("3.", color=WHITE, font_size=26, weight=BOLD),
                Text("経路として: M個の経路の重みの総和", color=YELLOW, font_size=24),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("※", color=GREEN, font_size=24, weight=BOLD),
                Text("2つの視点は本質的に同じもの", color=GREEN, font_size=24),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        summary_points.shift(UP * 0.3)
        self.add_fixed_in_frame_mobjects(summary_points)
        
        for point in summary_points:
            self.play(Write(point), run_time=0.6)
            self.wait(0.4)
        
        self.wait(0.5)
        
        # 最終メッセージ
        final_message = Text(
            "行列の積 = 経路の総和",
            color=YELLOW, font_size=32, weight=BOLD, slant=ITALIC
        )
        final_message.shift(DOWN * 2.5)
        self.add_fixed_in_frame_mobjects(final_message)
        self.play(Write(final_message), run_time=0.8)
        self.wait(1.5)
        
        self.wait(2.0)
        
        # フェードアウト
        all_objects = VGroup(
            title, summary_subtitle, summary_points, final_message
        )
        self.play(FadeOut(all_objects), run_time=1.0)
        self.wait(0.5)
