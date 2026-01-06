from manim import *

class MatrixTransformationProperties(ThreeDScene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"
        
        # タイトル
        title = Text("行列による線型変換の性質", font_size=40, color=WHITE)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)
        
        # === パート1: 線型性をもつ操作はすべて行列で書ける ===
        subtitle1 = Text("線型性をもつ操作と行列", font_size=32, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle1)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.5)
        
        # 線型性の定義
        linearity_title = Text("線型性の復習↓", color=YELLOW, font_size=28, weight=BOLD)
        linearity_title.shift(UP * 2.0)
        self.add_fixed_in_frame_mobjects(linearity_title)
        self.play(Write(linearity_title), run_time=0.6)
        self.wait(0.4)
        
        # 線型性の条件
        linearity_conditions = VGroup(
            MathTex(r"f(c\mathbf{v}) = c \cdot f(\mathbf{v})", color=WHITE, font_size=28),
            Text("(スカラー倍)", color=ORANGE, font_size=22),
        ).arrange(RIGHT, buff=0.3)
        linearity_conditions.shift(UP * 1.2)
        self.add_fixed_in_frame_mobjects(linearity_conditions)
        self.play(Write(linearity_conditions), run_time=0.7)
        self.wait(0.5)
        
        linearity_conditions2 = VGroup(
            MathTex(r"f(\mathbf{u} + \mathbf{v}) = f(\mathbf{u}) + f(\mathbf{v})", color=WHITE, font_size=28),
            Text("(加法性)", color=ORANGE, font_size=22),
        ).arrange(RIGHT, buff=0.3)
        linearity_conditions2.shift(UP * 0.4)
        self.add_fixed_in_frame_mobjects(linearity_conditions2)
        self.play(Write(linearity_conditions2), run_time=0.7)
        self.wait(0.8)
        
        # 重要な事実
        important_fact = Text(
            "この2つの性質を持つ変換はすべて行列で表現できる!",
            color=YELLOW, font_size=26, weight=BOLD
        )
        important_fact.shift(DOWN * 0.5)
        important_box = SurroundingRectangle(important_fact, color=YELLOW, buff=0.2)
        self.add_fixed_in_frame_mobjects(important_fact, important_box)
        self.play(Write(important_fact), Create(important_box), run_time=0.9)
        self.wait(1.2)
        
        # 例
        example_title = Text("例:", color=GREEN, font_size=26, weight=BOLD)
        example_title.shift(DOWN * 1.5 + LEFT * 4)
        example_list = VGroup(
            Text("• 回転変換", color=WHITE, font_size=22),
            Text("• 拡大・縮小", color=WHITE, font_size=22),
            Text("• 鏡映変換(対称)", color=WHITE, font_size=22),
            Text("• 射影(projection)", color=WHITE, font_size=22),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        example_list.next_to(example_title, DOWN, buff=0.3, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(example_title, example_list)
        self.play(Write(example_title), run_time=0.5)
        self.play(Write(example_list), run_time=0.9)
        self.wait(1.2)
        
        # フェードアウト
        self.play(
            FadeOut(linearity_title), FadeOut(linearity_conditions),
            FadeOut(linearity_conditions2), FadeOut(important_fact),
            FadeOut(important_box), FadeOut(example_title),
            FadeOut(example_list), FadeOut(subtitle1)
        )
        self.wait(0.3)
        
        # === パート2: 行列の積の非可換性 ===
        subtitle2 = Text("行列の積は順序が重要", font_size=32, color=PURPLE)
        subtitle2.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle2)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)
        
        # 説明テキスト
        explanation = Text(
            "回転してから鏡映 vs 鏡映してから回転",
            color=YELLOW, font_size=26
        )
        explanation.shift(DOWN * 3)
        self.add_fixed_in_frame_mobjects(explanation)
        self.play(Write(explanation), run_time=0.7)
        self.wait(0.6)
        
        # 2次元平面を設定
        self.set_camera_orientation(phi=0, theta=-90*DEGREES)
        
        # 元のベクトル
        original_vector = Arrow(
            ORIGIN, [2, 1.5, 0],
            buff=0,
            color=GREEN,
            stroke_width=6
        )
        original_label = MathTex(r"\mathbf{v}", color=GREEN, font_size=32)
        original_label.next_to(original_vector.get_end(), RIGHT, buff=0.2)
        
        # 座標軸
        axes = VGroup(
            Arrow(ORIGIN, [3, 0, 0], buff=0, color=GRAY, stroke_width=2),
            Arrow(ORIGIN, [0, 3, 0], buff=0, color=GRAY, stroke_width=2),
        )
        axis_labels = VGroup(
            MathTex("x", color=GRAY, font_size=24).move_to([3.2, 0, 0]),
            MathTex("y", color=GRAY, font_size=24).move_to([0, 3.2, 0]),
        )
        
        self.add(axes, axis_labels)
        self.play(Create(original_vector), Write(original_label), run_time=0.7)
        self.wait(0.8)
        
        # === ケース1: 回転 → 鏡映(x軸対称) ===
        case1_label = Text("ケース1: 回転 → x軸対称", color=BLUE, font_size=24)
        case1_label.to_edge(LEFT).shift(UP * 1.8)
        self.add_fixed_in_frame_mobjects(case1_label)
        self.play(Write(case1_label), run_time=0.6)
        self.wait(0.5)
        
        # 回転 (45度)
        angle = 45 * DEGREES
        rotated_vector = Arrow(
            ORIGIN,
            [2*np.cos(angle) - 1.5*np.sin(angle), 
             2*np.sin(angle) + 1.5*np.cos(angle), 0],
            buff=0,
            color=BLUE,
            stroke_width=6
        )
        rotated_label = MathTex(r"R\mathbf{v}", color=BLUE, font_size=28)
        rotated_label.next_to(rotated_vector.get_end(), UP, buff=0.2)
        
        rotation_note = Text("45°回転", color=BLUE, font_size=20)
        rotation_note.to_edge(LEFT).shift(UP * 1.3)
        self.add_fixed_in_frame_mobjects(rotation_note)
        
        # Transformアニメーション用のコピーを作成
        transform_vec1 = original_vector.copy()
        self.add(transform_vec1)
        
        self.play(
            Transform(transform_vec1, rotated_vector),
            Write(rotated_label),
            Write(rotation_note),
            run_time=1.0
        )
        self.wait(0.6)
        
        # 鏡映 (x軸対称)
        rotated_end = rotated_vector.get_end()
        reflected_vector1 = Arrow(
            ORIGIN,
            [rotated_end[0], -rotated_end[1], 0],
            buff=0,
            color=RED,
            stroke_width=6
        )
        reflected_label1 = MathTex(r"S(R\mathbf{v})", color=RED, font_size=28)
        reflected_label1.next_to(reflected_vector1.get_end(), DOWN+RIGHT, buff=0.2)
        
        reflection_note = Text("x軸対称", color=RED, font_size=20)
        reflection_note.to_edge(LEFT).shift(UP * 0.8)
        self.add_fixed_in_frame_mobjects(reflection_note)
        
        # 次の変換用のコピーを作成
        transform_vec2 = transform_vec1.copy()
        self.add(transform_vec2)
        
        self.play(
            Transform(transform_vec2, reflected_vector1),
            Write(reflected_label1),
            Write(reflection_note),
            run_time=1.0
        )
        self.wait(1.0)
        
        # 結果ベクトルの位置を記録
        result1_pos = reflected_vector1.get_end()
        
        # フェードアウト(transform_vec1とtransform_vec2も消す)
        self.play(
            FadeOut(transform_vec1), FadeOut(rotated_label),
            FadeOut(transform_vec2), FadeOut(reflected_label1),
            FadeOut(rotation_note), FadeOut(reflection_note)
        )
        self.wait(0.3)
        
        # === ケース2: 鏡映 → 回転 ===
        case2_label = Text("ケース2: x軸対称 → 回転", color=ORANGE, font_size=24)
        case2_label.to_edge(LEFT).shift(UP * 1.8)
        self.add_fixed_in_frame_mobjects(case2_label)
        self.play(
            FadeOut(case1_label),
            Write(case2_label),
            run_time=0.6
        )
        self.wait(0.5)
        
        # 鏡映 (x軸対称)
        reflected_first = Arrow(
            ORIGIN,
            [2, -1.5, 0],
            buff=0,
            color=BLUE,
            stroke_width=6
        )
        reflected_first_label = MathTex(r"S\mathbf{v}", color=BLUE, font_size=28)
        reflected_first_label.next_to(reflected_first.get_end(), DOWN+RIGHT, buff=0.2)
        
        reflection_note2 = Text("x軸対称", color=BLUE, font_size=20)
        reflection_note2.to_edge(LEFT).shift(UP * 1.3)
        self.add_fixed_in_frame_mobjects(reflection_note2)
        
        # Transformアニメーション用のコピーを作成
        transform_vec3 = original_vector.copy()
        self.add(transform_vec3)
        
        self.play(
            Transform(transform_vec3, reflected_first),
            Write(reflected_first_label),
            Write(reflection_note2),
            run_time=1.0
        )
        self.wait(0.6)
        
        # 回転 (45度)
        reflected_end = reflected_first.get_end()
        rotated_second = Arrow(
            ORIGIN,
            [reflected_end[0]*np.cos(angle) - reflected_end[1]*np.sin(angle),
             reflected_end[0]*np.sin(angle) + reflected_end[1]*np.cos(angle), 0],
            buff=0,
            color=ORANGE,
            stroke_width=6
        )
        rotated_second_label = MathTex(r"R(S\mathbf{v})", color=ORANGE, font_size=28)
        rotated_second_label.next_to(rotated_second.get_end(), RIGHT, buff=0.2)
        
        rotation_note2 = Text("45°回転", color=ORANGE, font_size=20)
        rotation_note2.to_edge(LEFT).shift(UP * 0.8)
        self.add_fixed_in_frame_mobjects(rotation_note2)
        
        # 次の変換用のコピーを作成
        transform_vec4 = transform_vec3.copy()
        self.add(transform_vec4)
        
        self.play(
            Transform(transform_vec4, rotated_second),
            Write(rotated_second_label),
            Write(rotation_note2),
            run_time=1.0
        )
        self.wait(1.0)
        
        # 結果の比較
        comparison = Text("2つの結果が異なる!", color=YELLOW, font_size=28, weight=BOLD)
        comparison.to_edge(LEFT).shift(UP * 0.2)
        comparison_box = SurroundingRectangle(comparison, color=YELLOW, buff=0.15)
        self.add_fixed_in_frame_mobjects(comparison, comparison_box)
        self.play(Write(comparison), Create(comparison_box), run_time=0.8)
        self.wait(1.2)
        
        # 行列の式
        matrix_equation = MathTex(r"SR \neq RS", color=YELLOW, font_size=36)
        matrix_equation.to_edge(LEFT).shift(DOWN * 0.7)
        matrix_box = SurroundingRectangle(matrix_equation, color=YELLOW, buff=0.2)
        self.add_fixed_in_frame_mobjects(matrix_equation, matrix_box)
        self.play(Write(matrix_equation), Create(matrix_box), run_time=0.8)
        self.wait(1.0)
        
        # 非可換性の説明
        noncommutative = Text(
            "行列の積は非可換",
            color=RED, font_size=26, weight=BOLD
        )
        noncommutative.to_edge(LEFT).shift(DOWN * 1.5)
        self.add_fixed_in_frame_mobjects(noncommutative)
        self.play(Write(noncommutative), run_time=0.7)
        self.wait(1.5)
        
        # フェードアウト(transform_vec3とtransform_vec4も消す)
        self.play(
            FadeOut(original_vector), FadeOut(original_label),
            FadeOut(transform_vec3), FadeOut(reflected_first_label),
            FadeOut(transform_vec4), FadeOut(rotated_second_label),
            FadeOut(axes), FadeOut(axis_labels),
            FadeOut(case2_label), FadeOut(reflection_note2),
            FadeOut(rotation_note2), FadeOut(comparison),
            FadeOut(comparison_box), FadeOut(matrix_equation),
            FadeOut(matrix_box), FadeOut(noncommutative),
            FadeOut(explanation), FadeOut(subtitle2),
        )
        self.wait(0.3)
        
        # === パート3: 基底の選択と表現行列 ===
        self.set_camera_orientation(phi=0, theta=0)
        
        subtitle3 = Text("基底が変わると表現行列も変わる", font_size=32, color=TEAL)
        subtitle3.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle3)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.5)
        
        # intro_text = Text(
        #     "同じ線型変換でも、基底によって異なる行列で表される",
        #     color=YELLOW, font_size=24
        # )
        # intro_text.shift(UP * 2.5)
        # self.add_fixed_in_frame_mobjects(intro_text)
        # self.play(Write(intro_text), run_time=0.8)
        # self.wait(0.8)
        
        # === 標準基底の場合 ===
        basis1_title = Text("基底1: 標準基底", font_size=28, color=BLUE, weight=BOLD)
        basis1_title.shift(UP * 1.8 + LEFT * 3.5)
        self.add_fixed_in_frame_mobjects(basis1_title)
        self.play(Write(basis1_title), run_time=0.6)
        self.wait(0.5)
        
        # 標準基底の定義
        standard_basis = MathTex(
            r"\mathbf{u}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \quad"
            r"\mathbf{u}_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}",
            color=BLUE, font_size=26
        )
        standard_basis.shift(UP * 1.2 + LEFT * 3.5)
        self.add_fixed_in_frame_mobjects(standard_basis)
        self.play(Write(standard_basis), run_time=0.8)
        self.wait(0.6)
        
        # u1方向成分抽出の説明
        projection_desc1 = Text(
            "u₁方向の成分を抽出する変換:",
            color=WHITE, font_size=22
        )
        projection_desc1.shift(UP * 0.5 + LEFT * 3.5)
        self.add_fixed_in_frame_mobjects(projection_desc1)
        self.play(Write(projection_desc1), run_time=0.6)
        self.wait(0.4)
        
        # 標準基底での表現行列
        matrix1 = MathTex(
            r"P_1 = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}",
            color=BLUE, font_size=30
        )
        matrix1.shift(DOWN * 0.2 + LEFT * 3.5)
        matrix1_box = SurroundingRectangle(matrix1, color=BLUE, buff=0.15)
        self.add_fixed_in_frame_mobjects(matrix1, matrix1_box)
        self.play(Write(matrix1), Create(matrix1_box), run_time=0.8)
        self.wait(0.8)
        
        # 検証
        # verification1 = VGroup(
        #     MathTex(r"P_1 \mathbf{u}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}", 
        #            color=GREEN, font_size=20),
        #     MathTex(r"P_1 \mathbf{u}_2 = \begin{bmatrix} 0 \\ 0 \end{bmatrix}", 
        #            color=GREEN, font_size=20),
        # ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        # verification1.shift(DOWN * 1.2 + LEFT * 3.5)
        # self.add_fixed_in_frame_mobjects(verification1)
        # self.play(Write(verification1), run_time=0.7)
        # self.wait(0.8)
        
        # === 別の基底の場合 ===
        basis2_title = Text("基底2: 別の基底", font_size=28, color=ORANGE, weight=BOLD)
        basis2_title.shift(UP * 1.8 + RIGHT * 3.5)
        self.add_fixed_in_frame_mobjects(basis2_title)
        self.play(Write(basis2_title), run_time=0.6)
        self.wait(0.5)
        
        # 別の基底の定義
        alt_basis = MathTex(
            r"\mathbf{a}_1 = \begin{bmatrix} -1 \\ 0 \end{bmatrix}, \quad"
            r"\mathbf{a}_2 = \begin{bmatrix} -1 \\ -1 \end{bmatrix}",
            color=ORANGE, font_size=26
        )
        alt_basis.shift(UP * 1.2 + RIGHT * 3.5)
        self.add_fixed_in_frame_mobjects(alt_basis)
        self.play(Write(alt_basis), run_time=0.8)
        self.wait(0.6)
        
        # u1方向成分抽出の説明
        projection_desc2 = Text(
            "u₁方向の成分を抽出する変換:",
            color=WHITE, font_size=22
        )
        projection_desc2.shift(UP * 0.5 + RIGHT * 3.5)
        self.add_fixed_in_frame_mobjects(projection_desc2)
        self.play(Write(projection_desc2), run_time=0.6)
        self.wait(0.4)
        
        # 別基底での表現行列 (標準基底で表現)
        matrix2 = MathTex(
            r"P_2 = \begin{bmatrix} -1 & -1 \\ 0 & 0 \end{bmatrix}",
            color=ORANGE, font_size=30
        )
        matrix2.shift(DOWN *0.2 + RIGHT * 3.5)
        matrix2_box = SurroundingRectangle(matrix2, color=ORANGE, buff=0.15)
        self.add_fixed_in_frame_mobjects(matrix2, matrix2_box)
        self.play(Write(matrix2), Create(matrix2_box), run_time=0.8)
        self.wait(0.8)
        
        # 検証
        # verification2 = VGroup(
        #     MathTex(r"P_2 \mathbf{a}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix} = -\mathbf{a}_1", 
        #            color=GREEN, font_size=18),
        #     MathTex(r"P_2 \mathbf{a}_2 = \begin{bmatrix} 0 \\ 0 \end{bmatrix}", 
        #            color=GREEN, font_size=18),
        # ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        # verification2.shift(DOWN * 1.4 + RIGHT * 3.5)
        # self.add_fixed_in_frame_mobjects(verification2)
        # self.play(Write(verification2), run_time=0.7)
        # self.wait(1.0)
        
        # 重要なポイント
        key_point = VGroup(
            Text("重要:", color=YELLOW, font_size=26, weight=BOLD),
            Text("同じ「方向成分を抽出する」操作でも", color=WHITE, font_size=22),
            Text("基底が違えば表現行列も異なる!", color=YELLOW, font_size=22),
        ).arrange(DOWN, buff=0.3)
        key_point.shift(DOWN * 2)
        key_box = SurroundingRectangle(key_point, color=YELLOW, buff=0.2)
        self.add_fixed_in_frame_mobjects(key_point, key_box)
        self.play(Write(key_point), Create(key_box), run_time=1.0)
        self.wait(1.5)
        
        # フェードアウト
        self.play(
            # FadeOut(intro_text),
            FadeOut(basis1_title), FadeOut(standard_basis),
            FadeOut(projection_desc1), FadeOut(matrix1),
            FadeOut(matrix1_box),
            FadeOut(basis2_title), FadeOut(alt_basis),
            FadeOut(projection_desc2),
            FadeOut(matrix2), FadeOut(matrix2_box),
            FadeOut(key_point),
            FadeOut(key_box), FadeOut(subtitle3)
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
                Text("線型性をもつ変換はすべて行列で表現できる", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("2.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("行列の積は非可換: ", color=WHITE, font_size=24),
                    MathTex(r"AB \neq BA", color=YELLOW, font_size=24),
                ).arrange(RIGHT, buff=0.2),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("3.", color=WHITE, font_size=26, weight=BOLD),
                Text("基底が異なると同じ変換でも表現行列が変わる", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        summary_points.shift(UP * 0.5)
        self.add_fixed_in_frame_mobjects(summary_points)
        
        for point in summary_points:
            self.play(Write(point), run_time=0.7)
            self.wait(0.5)
        
        self.wait(1.0)
        
        # フェードアウト
        all_objects = VGroup(title, summary_subtitle, summary_points)
        self.play(FadeOut(all_objects), run_time=1.0)
        self.wait(0.5)
