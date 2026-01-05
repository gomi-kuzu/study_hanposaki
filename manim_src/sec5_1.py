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
            Text("例: 2×3 行列と 3×2 行列の積は2×2 行列", color=WHITE, font_size=24),
        ).arrange(DOWN, buff=0.4)
        intro_text.shift(DOWN * 0.5)
        self.add_fixed_in_frame_mobjects(intro_text)
        
        self.play(Write(intro_text), run_time=1.2)
        self.wait(1.5)
        
        self.play(FadeOut(intro_text), FadeOut(intro_subtitle))
        self.wait(0.3)
        
        # === パート1: 行列の積の形式 ===
        subtitle1 = Text("行列の積の成分表示", font_size=32, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle1)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.5)
        
        # 行列A, Bを成分表示
        matrix_A = MathTex(r"A = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1M} \\" 
                   r"a_{21} & a_{22} & \cdots & a_{2M} \\" 
                   r"\vdots & \vdots & \ddots & \vdots \\" 
                   r"a_{\ell 1} & a_{\ell 2} & \cdots & a_{\ell M} \\" 
                   r"\vdots & \vdots & \ddots & \vdots \\" 
                   r"a_{L1} & a_{L2} & \cdots & a_{LM} \end{bmatrix}",
                   color=RED, font_size=24)
        matrix_B = MathTex(r"B = \begin{bmatrix} b_{11} & \cdots & b_{1n} & \cdots & b_{1N} \\" 
                   r"b_{21} & \cdots & b_{2n} & \cdots & b_{2N} \\" 
                   r"\vdots & \ddots & \vdots & \ddots & \vdots \\" 
                   r"b_{M1} & \cdots & b_{Mn} & \cdots & b_{MN} \end{bmatrix}",
                   color=BLUE, font_size=24)
        
        matrix_form = VGroup(matrix_A, matrix_B).arrange(RIGHT, buff=0.8)
        matrix_form.shift(UP * 0.8)
        self.add_fixed_in_frame_mobjects(matrix_form)
        
        self.play(Write(matrix_A), run_time=0.8)
        self.wait(0.5)
        self.play(Write(matrix_B), run_time=0.8)
        self.wait(0.8)
        
        # 次元の説明
        dimension_note = VGroup(
            MathTex(r"(L \times M)", color=RED, font_size=24),
            MathTex(r"\times", color=WHITE, font_size=24),
            MathTex(r"(M \times N)", color=BLUE, font_size=24),
            MathTex(r"=", color=WHITE, font_size=24),
            MathTex(r"(L \times N)", color=GREEN, font_size=24),
        ).arrange(RIGHT, buff=0.3)
        dimension_note.shift(DOWN * 3.2)
        self.add_fixed_in_frame_mobjects(dimension_note)
        self.play(Write(dimension_note), run_time=0.8)
        self.wait(1.0)
        
        # Aのℓ行目を強調
        highlight_text = Text("Aのℓ行目とBのn列目に注目", color=YELLOW, font_size=26, weight=BOLD)
        highlight_text.shift(DOWN * 2.3)
        self.add_fixed_in_frame_mobjects(highlight_text)
        self.play(Write(highlight_text), run_time=0.7)
        self.wait(0.8)
        
        # Aのℓ行を抽出
        a_row = MathTex(r"[a_{\ell 1}, a_{\ell 2}, \cdots, a_{\ell M}]", 
                       color=RED, font_size=28)
        a_row.shift(LEFT * 2.5 + DOWN * 1.2)
        a_row_label = Text("Aのℓ行", color=RED, font_size=22)
        a_row_label.next_to(a_row, LEFT, buff=0.3)
        
        # Bのn列を抽出
        b_col = MathTex(r"\begin{bmatrix} b_{1n} \\ b_{2n} \\ \vdots \\ b_{Mn} \end{bmatrix}", 
                       color=BLUE, font_size=28)
        b_col.shift(RIGHT * 2.5 + DOWN * 1.2)
        b_col_label = Text("Bのn列", color=BLUE, font_size=22)
        b_col_label.next_to(b_col, RIGHT, buff=0.3)
        
        self.add_fixed_in_frame_mobjects(a_row, a_row_label, b_col, b_col_label)
        
        # 行と列を抽出するアニメーション
        self.play(
            TransformFromCopy(matrix_A, a_row),
            Write(a_row_label),
            run_time=0.8
        )
        self.wait(0.5)
        self.play(
            TransformFromCopy(matrix_B, b_col),
            Write(b_col_label),
            run_time=0.8
        )
        self.wait(1.0)
        
        # 内積の計算を示す
        dot_product_label = Text("内積を計算", color=ORANGE, font_size=24, weight=BOLD)
        dot_product_label.shift(DOWN * 0.3)
        self.add_fixed_in_frame_mobjects(dot_product_label)
        self.play(Write(dot_product_label), run_time=0.6)
        self.wait(0.5)
        
        # 内積の式
        dot_product = MathTex(
            r"a_{\ell 1} b_{1n} + a_{\ell 2} b_{2n} + \cdots + a_{\ell M} b_{Mn}",
            color=WHITE, font_size=26
        )
        dot_product.shift(DOWN * 0.1)
        self.add_fixed_in_frame_mobjects(dot_product)
        self.play(
            FadeOut(a_row), FadeOut(a_row_label),
            FadeOut(b_col), FadeOut(b_col_label),
            FadeOut(dot_product_label)
        )
        self.play(Write(dot_product), run_time=0.8)
        self.wait(0.8)
        
        # 結果を示す
        equals_c = MathTex(r"=", color=WHITE, font_size=26)
        equals_c.next_to(dot_product, DOWN, buff=0.3)
        c_element = MathTex(r"c_{\ell n}", color=GREEN, font_size=32)
        c_element.next_to(equals_c, DOWN, buff=0.3)
        
        result_label = Text("これがCのℓ行n列目の成分", color=GREEN, font_size=24)
        result_label.next_to(c_element, DOWN, buff=0.4)
        
        self.add_fixed_in_frame_mobjects(equals_c, c_element, result_label)
        self.play(Write(equals_c), run_time=0.3)
        self.wait(0.3)
        self.play(Write(c_element), run_time=0.6)
        self.wait(0.5)
        self.play(Write(result_label), run_time=0.7)
        self.wait(1.2)
        
        self.play(
            FadeOut(matrix_form), FadeOut(dimension_note), 
            FadeOut(highlight_text), FadeOut(dot_product),
            FadeOut(equals_c), FadeOut(c_element), FadeOut(result_label),
            FadeOut(subtitle1)
        )
        self.wait(0.3)
        
        # === パート2: 要素の計算を経路で理解 ===
        subtitle2 = VGroup(
            Text("要素 ", font_size=32, color=PURPLE),
            MathTex(r"c_{\ell n}", font_size=32, color=PURPLE),
            Text(" を経路の総和として理解", font_size=32, color=PURPLE),
        ).arrange(RIGHT, buff=0.1)
        subtitle2.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle2)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)
        
        # 重要な公式
        formula_title = Text("重要な公式:", color=YELLOW, font_size=26, weight=BOLD)
        formula_title.to_edge(LEFT).shift(UP * 2.2)
        self.add_fixed_in_frame_mobjects(formula_title)
        self.play(Write(formula_title), run_time=0.6)
        self.wait(0.3)
        
        key_formula = MathTex(
            r"c_{\ell n} = \sum_{m=1}^{M} a_{\ell m} \cdot b_{mn}",
            color=YELLOW, font_size=32
        )
        key_formula.next_to(formula_title, DOWN, buff=0.3, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(key_formula)
        self.play(Write(key_formula), run_time=0.8)
        self.wait(0.8)
        
        # 展開表示
        expanded_title = Text("展開すると:", color=WHITE, font_size=24)
        expanded_title.next_to(key_formula, DOWN, buff=0.4, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(expanded_title)
        self.play(Write(expanded_title), run_time=0.5)
        self.wait(0.3)
        
        expanded_formula = MathTex(
            r"c_{\ell n} = a_{\ell 1} b_{1n} + a_{\ell 2} b_{2n} + \cdots + a_{\ell M} b_{Mn}",
            color=WHITE, font_size=28
        )
        expanded_formula.next_to(expanded_title, DOWN, buff=0.3, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(expanded_formula)
        self.play(Write(expanded_formula), run_time=0.8)
        self.wait(1.0)
        
        # 経路としての解釈
        path_interpretation = Text(
            "これを「経路」として視覚化 →",
            color=ORANGE, font_size=26, weight=BOLD
        )
        path_interpretation.next_to(expanded_formula, DOWN, buff=0.5, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(path_interpretation)
        self.play(Write(path_interpretation), run_time=0.7)
        self.wait(0.8)
        
        # グラフ構造の描画（右側に配置）
        # 左端: Aのℓ行目
        left_node = Circle(radius=0.35, color=RED, fill_opacity=0.6)
        left_node.shift(RIGHT * 2 + UP * 0.3)
        left_label = MathTex(r"A_\ell", color=RED, font_size=28)
        left_label.next_to(left_node, LEFT, buff=0.25)
        self.add_fixed_in_frame_mobjects(left_node, left_label)
        
        # 右端: Bのn列目
        right_node = Circle(radius=0.35, color=BLUE, fill_opacity=0.6)
        right_node.shift(RIGHT * 6 + UP * 0.3)
        right_label = MathTex(r"B_n", color=BLUE, font_size=28)
        right_label.next_to(right_node, RIGHT, buff=0.25)
        self.add_fixed_in_frame_mobjects(right_node, right_label)
        
        # 中間点: m=1, 2, ..., M
        middle_nodes = VGroup()
        middle_labels = VGroup()
        middle_positions = [UP * 1.8, UP * 0.3, DOWN * 1.2]
        labels_text = ["m{=}1", "m{=}2", r"\vdots"]
        
        for i, (pos, label_tex) in enumerate(zip(middle_positions, labels_text)):
            if i < 2:  # 実際のノード
                node = Circle(radius=0.28, color=YELLOW, fill_opacity=0.4)
                node.shift(RIGHT * 4 + pos)
                label = MathTex(label_tex, color=YELLOW, font_size=22)
                label.next_to(node, UP, buff=0.15)
                middle_nodes.add(node)
                middle_labels.add(label)
            else:  # 省略記号
                dots = MathTex(r"\vdots", color=YELLOW, font_size=32)
                dots.shift(RIGHT * 4 + pos)
                middle_labels.add(dots)
        
        m_note = MathTex(r"m{=}M", color=YELLOW, font_size=20)
        m_note.shift(RIGHT * 4 + DOWN * 2)
        
        self.add_fixed_in_frame_mobjects(middle_nodes, middle_labels, m_note)
        
        self.play(
            Create(left_node), Write(left_label),
            Create(right_node), Write(right_label),
            run_time=0.8
        )
        self.wait(0.4)
        self.play(Create(middle_nodes), Write(middle_labels), Write(m_note), run_time=0.8)
        self.wait(0.6)
        
        # 経路を描画（最初の2つの経路のみ表示）
        paths = VGroup()
        path_labels = VGroup()
        
        for i in range(2):  # m=1, 2のみ
            middle_node = middle_nodes[i]
            # 左から中間へ
            left_arrow = Arrow(
                left_node.get_right(),
                middle_node.get_left(),
                buff=0.15,
                color=ORANGE,
                stroke_width=4
            )
            # 中間から右へ
            right_arrow = Arrow(
                middle_node.get_right(),
                right_node.get_left(),
                buff=0.15,
                color=ORANGE,
                stroke_width=4
            )
            
            # 経路の重みラベル
            a_weight = MathTex(f"a_{{\ell {i+1}}}", color=RED, font_size=20)
            a_weight.next_to(left_arrow, DOWN, buff=0.08)
            b_weight = MathTex(f"b_{{{i+1}n}}", color=BLUE, font_size=20)
            b_weight.next_to(right_arrow, DOWN, buff=0.08)
            
            paths.add(left_arrow, right_arrow)
            path_labels.add(a_weight, b_weight)
        
        self.add_fixed_in_frame_mobjects(paths, path_labels)
        
        # 経路を1つずつアニメーション
        for i in range(2):
            self.play(
                Create(paths[2*i]), Write(path_labels[2*i]),
                Create(paths[2*i+1]), Write(path_labels[2*i+1]),
                run_time=0.6
            )
            self.wait(0.4)
        
        self.wait(0.6)
        
        # 経路の説明
        path_explanation = VGroup(
            Text("各経路の重み:", color=ORANGE, font_size=24, weight=BOLD),
            MathTex(r"m{=}1: \quad a_{\ell 1} \times b_{1n}", 
                   color=WHITE, font_size=22),
            MathTex(r"m{=}2: \quad a_{\ell 2} \times b_{2n}", 
                   color=WHITE, font_size=22),
            MathTex(r"\vdots", color=WHITE, font_size=22),
            MathTex(r"m{=}M: \quad a_{\ell M} \times b_{Mn}", 
                   color=WHITE, font_size=22),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        path_explanation.to_corner(DL).shift(UP * 0.3 + RIGHT * 0.2)
        self.add_fixed_in_frame_mobjects(path_explanation)
        self.play(Write(path_explanation), run_time=1.0)
        self.wait(1.0)
        
        # 総和
        path_sum = MathTex(
            r"c_{\ell n} = \sum_{m=1}^{M} a_{\ell m} \times b_{mn}",
            color=GREEN, font_size=30
        )
        path_sum.shift(DOWN * 2.8)
        sum_box = SurroundingRectangle(path_sum, color=GREEN, buff=0.2)
        self.add_fixed_in_frame_mobjects(path_sum, sum_box)
        
        self.play(Write(path_sum), Create(sum_box), run_time=0.8)
        self.wait(1.0)
        
        interpretation = Text(
            "M個の経路の重みの総和",
            color=YELLOW, font_size=26, slant=ITALIC
        )
        interpretation.next_to(path_sum, DOWN, buff=0.3)
        self.add_fixed_in_frame_mobjects(interpretation)
        self.play(Write(interpretation), run_time=0.8)
        self.wait(1.5)
        
        # 重要なポイント
        key_point = Text(
            "経路の総和 = 行列の積の要素",
            color=YELLOW, font_size=28, weight=BOLD, slant=ITALIC
        )
        key_point.to_edge(UP).shift(DOWN * 1.2)
        self.add_fixed_in_frame_mobjects(key_point)
        self.play(Write(key_point), run_time=0.8)
        self.wait(1.5)
        
        self.play(
            FadeOut(path_interpretation), FadeOut(left_node), FadeOut(left_label),
            FadeOut(right_node), FadeOut(right_label),
            FadeOut(middle_nodes), FadeOut(middle_labels), FadeOut(m_note),
            FadeOut(paths), FadeOut(path_labels),
            FadeOut(path_explanation), FadeOut(path_sum),
            FadeOut(sum_box), FadeOut(key_point),
            FadeOut(formula_title), FadeOut(key_formula),
            FadeOut(expanded_title), FadeOut(expanded_formula),
            FadeOut(interpretation), FadeOut(subtitle2)
        )
        self.wait(0.3)
        
        # === パート3: 正規直交基底による行列の分解 ===
        # subtitle3 = Text("正規直交基底による行列の分解", font_size=32, color=PURPLE)
        # subtitle3.next_to(title, DOWN)
        # self.add_fixed_in_frame_mobjects(subtitle3)
        # self.play(Write(subtitle3), run_time=0.6)
        # self.wait(0.5)
        
        # # 正規直交基底の導入
        # basis_intro = VGroup(
        #     Text("２次元空間の正規直交基底:", color=WHITE, font_size=26, weight=BOLD),
        #     MathTex(r"|e_1\rangle = \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \quad"
        #            r"|e_2\rangle = \begin{bmatrix} 0 \\ 1 \end{bmatrix}",
        #            color=WHITE, font_size=30),
        # ).arrange(DOWN*2.5, buff=0.4)
        # basis_intro.shift(UP * 2)
        # self.add_fixed_in_frame_mobjects(basis_intro)
        # self.play(Write(basis_intro), run_time=0.9)
        # self.wait(0.8)
        
        # # 正規直交性の確認
        # orthonormal = VGroup(
        #     MathTex(r"\langle e_i | e_j \rangle = \delta_{ij}", color=ORANGE, font_size=26),
        #     Text("(正規直交基底)", color=ORANGE, font_size=22),
        # ).arrange(RIGHT, buff=0.3)
        # orthonormal.shift(UP * 1.0)
        # self.add_fixed_in_frame_mobjects(orthonormal)
        # self.play(Write(orthonormal), run_time=0.7)
        # self.wait(0.8)
        
        # # 行列Aの分解
        # decomp_title = Text("行列Aを基底で分解:", color=BLUE, font_size=26, weight=BOLD)
        # decomp_title.shift(UP * 0.2)
        # self.add_fixed_in_frame_mobjects(decomp_title)
        # self.play(Write(decomp_title), run_time=0.6)
        # self.wait(0.5)
        
        # # 外積展開の式
        # decomp_formula = MathTex(
        #     r"A = \sum_{i=1}^{2}   |e_i\rangle\langle a_{i}|",
        #     color=GREEN, font_size=32
        # )
        # decomp_formula.shift(DOWN * 0.5)
        # self.add_fixed_in_frame_mobjects(decomp_formula)
        # self.play(Write(decomp_formula), run_time=0.8)
        # self.wait(1.0)
        
        # 展開した形
        # expand_arrow = MathTex(r"\Downarrow", color=YELLOW, font_size=36)
        # expand_arrow.next_to(decomp_formula, DOWN, buff=0.3)
        # expand_text = Text("展開すると", color=YELLOW, font_size=22)
        # expand_text.next_to(expand_arrow, RIGHT, buff=0.3)
        # self.add_fixed_in_frame_mobjects(expand_arrow, expand_text)
        # self.play(Write(expand_arrow), Write(expand_text), run_time=0.6)
        # self.wait(0.5)
        
        # 完全に展開した式
        # expanded_decomp = MathTex(
        #     r"A = a_{11}|e_1\rangle\langle e_1| + a_{12}|e_1\rangle\langle e_2|",
        #     color=WHITE, font_size=28
        # )
        # expanded_decomp.shift(DOWN * 1.5)
        # expanded_decomp2 = MathTex(
        #     r"+ a_{21}|e_2\rangle\langle e_1| + a_{22}|e_2\rangle\langle e_2|",
        #     color=WHITE, font_size=28
        # )
        # expanded_decomp2.next_to(expanded_decomp, DOWN, buff=0.2)
        # self.add_fixed_in_frame_mobjects(expanded_decomp, expanded_decomp2)
        # self.play(Write(expanded_decomp), run_time=0.8)
        # self.wait(0.4)
        # self.play(Write(expanded_decomp2), run_time=0.8)
        # self.wait(1.0)
        
        # 外積の意味
        # outer_product_note = VGroup(
        #     Text("外積の意味:", color=ORANGE, font_size=24, weight=BOLD),
        #     MathTex(r"|e_i\rangle\langle e_j| = \text{projection operator}", 
        #            color=ORANGE, font_size=22),
        # ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        # outer_product_note.to_corner(DL).shift(UP * 0.5 + RIGHT * 0.3)
        # self.add_fixed_in_frame_mobjects(outer_product_note)
        # self.play(Write(outer_product_note), run_time=0.8)
        # self.wait(1.2)
        
        # # 重要なポイント
        # key_insight_decomp = Text(
        #     "行列 = 基底の外積の線形結合",
        #     color=YELLOW, font_size=28, weight=BOLD, slant=ITALIC
        # )
        # key_insight_decomp.to_edge(UP).shift(DOWN * 1.2)
        # self.add_fixed_in_frame_mobjects(key_insight_decomp)
        # self.play(Write(key_insight_decomp), run_time=0.8)
        # self.wait(1.5)
        
        # self.play(
        #     FadeOut(basis_intro), FadeOut(orthonormal),
        #     FadeOut(decomp_title), FadeOut(decomp_formula),
        #     FadeOut(expand_arrow), FadeOut(expand_text),
        #     FadeOut(expanded_decomp), FadeOut(expanded_decomp2),
        #     FadeOut(outer_product_note), FadeOut(key_insight_decomp),
        #     FadeOut(subtitle3)
        # )
        # self.wait(0.3)
        
        # === パート4: 観測ブラベクトルのベクトルとしての解釈 ===
        subtitle4 = Text("別の視点: 観測ブラベクトルのベクトル", font_size=32, color=TEAL)
        subtitle4.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle4)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.5)
        
        bra_intro = VGroup(
            Text("行列をブラベクトルを成分に持つ列ベクトルとして見る", 
                color=YELLOW, font_size=26, weight=BOLD),
            Text("例: 2×2 行列の場合", color=WHITE, font_size=24),
        ).arrange(DOWN, buff=0.3)
        bra_intro.shift(UP * 2.2)
        self.add_fixed_in_frame_mobjects(bra_intro)
        self.play(Write(bra_intro), run_time=0.8)
        self.wait(0.8)
        
        # 2×2行列を通常表記で表示
        matrix_normal = MathTex(
            r"A = \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix}",
            color=RED, font_size=32
        )
        matrix_normal.shift(UP * 1.2)
        self.add_fixed_in_frame_mobjects(matrix_normal)
        self.play(Write(matrix_normal), run_time=0.8)
        self.wait(0.8)
        
        # 矢印
        arrow_transform = MathTex(r"\Downarrow", color=YELLOW, font_size=40)
        arrow_transform.next_to(matrix_normal, DOWN, buff=0.3)
        transform_text = Text("ブラベクトルの列ベクトルとして表現", color=YELLOW, font_size=22)
        transform_text.next_to(arrow_transform, RIGHT, buff=0.3)
        self.add_fixed_in_frame_mobjects(arrow_transform, transform_text)
        self.play(Write(arrow_transform), Write(transform_text), run_time=0.7)
        self.wait(0.6)
        
        # ブラベクトル表記
        matrix_bra = MathTex(
            r"A = \begin{bmatrix} \langle a_1 | \\ \langle a_2 | \end{bmatrix}",
            color=RED, font_size=36
        )
        matrix_bra.shift(DOWN * 0.3)
        self.add_fixed_in_frame_mobjects(matrix_bra)
        self.play(Write(matrix_bra), run_time=0.8)
        self.wait(0.8)
        
        # ブラベクトルの詳細
        # bra_details = VGroup(
        #     MathTex(r"\langle a_1 | = [a_{11}, a_{12}]", color=ORANGE, font_size=28),
        #     MathTex(r"\langle a_2 | = [a_{21}, a_{22}]", color=ORANGE, font_size=28),
        # ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        # bra_details.shift(DOWN * 1.5 + LEFT * 2)
        # self.add_fixed_in_frame_mobjects(bra_details)
        # self.play(Write(bra_details), run_time=0.9)
        # self.wait(1.0)
        
        self.play(
            FadeOut(bra_intro), FadeOut(matrix_normal),
            FadeOut(arrow_transform), FadeOut(transform_text),
            # FadeOut(bra_details)
        )
        self.wait(0.3)
        
        # ケットベクトルとの積
        multiplication_title = Text("任意のケットベクトルとの積", color=BLUE, font_size=28, weight=BOLD)
        multiplication_title.shift(UP * 1.8)
        self.add_fixed_in_frame_mobjects(multiplication_title)
        self.play(Write(multiplication_title), run_time=0.6)
        self.wait(0.5)
        
        # ケットベクトルを定義
        ket_vector = MathTex(
            r"|x\rangle = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}",
            color=BLUE, font_size=32
        )
        ket_vector.shift(UP * 1.3 + RIGHT * 3)
        self.add_fixed_in_frame_mobjects(ket_vector)
        self.play(Write(ket_vector), run_time=0.7)
        self.wait(0.6)
        
        # 積を計算
        product_eq = MathTex(
            r"A|x\rangle = \begin{bmatrix} \langle a_1 | \\ \langle a_2 | \end{bmatrix} |x\rangle",
            color=WHITE, font_size=32
        )
        product_eq.shift(UP * 0.3)
        self.add_fixed_in_frame_mobjects(product_eq)
        self.play(
            TransformFromCopy(matrix_bra, product_eq),
            FadeOut(matrix_bra),
            run_time=0.8,
        )
        self.wait(0.8)
        
        # 式変形のステップ
        transform_arrow1 = MathTex(r"\Downarrow", color=YELLOW, font_size=36)
        transform_arrow1.next_to(product_eq, DOWN, buff=0.3)
        step1_text = Text("各ブラベクトルとケットベクトルの内積", color=YELLOW, font_size=22)
        step1_text.next_to(transform_arrow1, RIGHT, buff=0.3)
        self.add_fixed_in_frame_mobjects(transform_arrow1, step1_text)
        self.play(Write(transform_arrow1), Write(step1_text), run_time=0.7)
        self.wait(0.6)
        
        # 結果: 観測値ベクトル
        observation_vector = MathTex(
            r"= \begin{bmatrix} \langle a_1 | x \rangle \\ \langle a_2 | x \rangle \end{bmatrix}",
            color=GREEN, font_size=36
        )
        observation_vector.shift(DOWN * 1.5)
        self.add_fixed_in_frame_mobjects(observation_vector)
        self.play(Write(observation_vector), run_time=0.8)
        self.wait(1.0)
        
        # 観測値ベクトルの説明
        obs_label = Text("観測値ベクトル", color=GREEN, font_size=28, weight=BOLD)
        obs_label.next_to(observation_vector, DOWN *1.2, buff=0.4)
        self.add_fixed_in_frame_mobjects(obs_label)
        self.play(Write(obs_label), run_time=0.6)
        self.wait(0.8)
        
        # 詳細な展開
        # detailed_expansion = VGroup(
        #     MathTex(r"\langle a_1 | x \rangle = a_{11} x_1 + a_{12} x_2", 
        #            color=ORANGE, font_size=24),
        #     MathTex(r"\langle a_2 | x \rangle = a_{21} x_1 + a_{22} x_2", 
        #            color=ORANGE, font_size=24),
        # ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        # detailed_expansion.shift(DOWN * 2.3 + LEFT * 1.5)
        # self.add_fixed_in_frame_mobjects(detailed_expansion)
        # self.play(Write(detailed_expansion), run_time=0.9)
        # self.wait(1.2)
        
        # まとめのポイント
        key_insight = Text(
            "行列 = 観測ブラベクトルの集まり",
            color=YELLOW, font_size=28, weight=BOLD, slant=ITALIC
        )
        key_insight.to_edge(UP).shift(DOWN * 6.5)
        self.add_fixed_in_frame_mobjects(key_insight)
        self.play(Write(key_insight), run_time=0.8)
        self.wait(1.5)
        
        self.play(
            FadeOut(multiplication_title),
            FadeOut(ket_vector), FadeOut(product_eq),
            FadeOut(transform_arrow1), FadeOut(step1_text),
            FadeOut(observation_vector), FadeOut(obs_label),
            # FadeOut(detailed_expansion),
            FadeOut(key_insight),
            FadeOut(subtitle4)
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
                VGroup(
                    Text("行列の積 ", color=WHITE, font_size=24),
                    MathTex(r"c_{\ell n} = \sum_{m=1}^{M} a_{\ell m} b_{mn}", color=WHITE, font_size=22),
                ).arrange(RIGHT, buff=0.2),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("2.", color=WHITE, font_size=26, weight=BOLD),
                Text("経路の総和という視点", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("3.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("観測器による観測という視点: ", color=YELLOW, font_size=24),
                    MathTex(r"A|x\rangle = \begin{bmatrix} \langle a_1|x\rangle \\ \vdots \end{bmatrix}", 
                           color=YELLOW, font_size=22),
                ).arrange(RIGHT, buff=0.2),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        summary_points.shift(UP * 0.3)
        self.add_fixed_in_frame_mobjects(summary_points)
        
        for point in summary_points:
            self.play(Write(point), run_time=0.6)
            self.wait(0.4)
        
        self.wait(0.5)
                
        # フェードアウト
        all_objects = VGroup(
            title, summary_subtitle, summary_points,
            # final_message
        )
        self.play(FadeOut(all_objects), run_time=1.0)
        self.wait(0.5)
