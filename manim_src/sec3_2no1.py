from manim import *

class NormAndDistance(ThreeDScene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"
        
        # タイトル
        title = Text("内積から導かれるノルムと距離", font_size=40, color=WHITE)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)
        
        # === パート1: ノルムの導入 ===
        subtitle1 = Text("ベクトルの「大きさ」を測る", font_size=32, color=YELLOW)
        subtitle1.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle1)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.5)
        
        # 座標平面を作成
        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 4, 1],
            x_length=5,
            y_length=4,
            axis_config={"color": GRAY}
        )
        axes.shift(LEFT * 3.5 + DOWN * 0.5)
        self.add_fixed_in_frame_mobjects(axes)
        
        # 方眼を追加
        grid = NumberPlane(
            x_range=[-1, 5, 1],
            y_range=[-1, 4, 1],
            x_length=5,
            y_length=4,
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            },
            axis_config={"stroke_opacity": 0}
        )
        grid.shift(LEFT * 3.5 + DOWN * 0.5)
        self.add_fixed_in_frame_mobjects(grid)
        
        self.play(Create(grid), Create(axes), run_time=0.7)
        self.wait(0.4)
        
        # ベクトルを表示
        vec_a = Vector(
            axes.c2p(3, 2) - axes.c2p(0, 0),
            color=BLUE,
            stroke_width=6
        ).shift(axes.c2p(0, 0))
        self.add_fixed_in_frame_mobjects(vec_a)
        
        vec_a_label = MathTex(r"\mathbf{a}", color=BLUE, font_size=32)
        vec_a_label.next_to(vec_a.get_end(), RIGHT, buff=0.2)
        self.add_fixed_in_frame_mobjects(vec_a_label)
        
        self.play(Create(vec_a), Write(vec_a_label), run_time=0.7)
        self.wait(0.5)
        
        # 説明テキスト
        explanation1 = VGroup(
            Text("このベクトルの「大きさ」は？", color=WHITE, font_size=26),
            Text("長さをどう測ればいい？", color=YELLOW, font_size=26),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        explanation1.to_edge(RIGHT).shift(LEFT * 1.5 + UP * 1.5)
        self.add_fixed_in_frame_mobjects(explanation1)
        
        self.play(Write(explanation1), run_time=0.8)
        self.wait(1.0)
        
        # 内積を使った定義を紹介
        norm_intro = Text("内積を使って定義できます！", 
                         color=GREEN, font_size=28, weight=BOLD)
        norm_intro.to_edge(RIGHT).shift(LEFT * 1.5 + UP * 0.3)
        self.add_fixed_in_frame_mobjects(norm_intro)
        self.play(Write(norm_intro), run_time=0.7)
        self.wait(0.8)
        
        self.play(FadeOut(explanation1), FadeOut(norm_intro), FadeOut(subtitle1))
        self.wait(0.3)
        
        # === パート2: ノルムの定義 ===
        subtitle2 = Text("ノルム（Norm）の定義", font_size=32, color=BLUE)
        subtitle2.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle2)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)
        
        # ノルムの定義式
        norm_definition_text = Text("ベクトル自身との内積の平方根", 
                                   color=YELLOW, font_size=26)
        norm_definition_text.to_edge(RIGHT).shift(LEFT * 1.5 + UP * 1.8)
        self.add_fixed_in_frame_mobjects(norm_definition_text)
        self.play(Write(norm_definition_text), run_time=0.7)
        self.wait(0.5)
        
        # 数式で表示
        norm_eq = MathTex(
            r"\|\mathbf{a}\| = \sqrt{\mathbf{a} \cdot \mathbf{a}}",
            color=GREEN, font_size=36
        )
        norm_eq.to_edge(RIGHT).shift(LEFT * 1.5 + UP * 0.8)
        self.add_fixed_in_frame_mobjects(norm_eq)
        self.play(Write(norm_eq), run_time=0.8)
        self.wait(0.8)
        
        # より詳しい展開
        norm_expanded = MathTex(
            r"\|\mathbf{a}\| = \sqrt{a_1^2 + a_2^2 + \cdots + a_n^2}",
            color=GREEN, font_size=28
        )
        norm_expanded.to_edge(RIGHT).shift(LEFT * 1.5 + UP * 0.1)
        self.add_fixed_in_frame_mobjects(norm_expanded)
        self.play(Write(norm_expanded), run_time=0.8)
        self.wait(0.8)
        
        # 具体例
        concrete_example = Text("具体例：", color=ORANGE, font_size=26, weight=BOLD)
        concrete_example.to_edge(RIGHT).shift(LEFT * 1.5 + DOWN * 0.8)
        self.add_fixed_in_frame_mobjects(concrete_example)
        self.play(Write(concrete_example), run_time=0.6)
        self.wait(0.3)
        
        vec_value = MathTex(
            r"\mathbf{a} = \begin{bmatrix} 3 \\ 2 \end{bmatrix}",
            color=BLUE, font_size=28
        )
        vec_value.to_edge(RIGHT).shift(LEFT * 1.5 + DOWN * 1.5)
        self.add_fixed_in_frame_mobjects(vec_value)
        self.play(Write(vec_value), run_time=0.7)
        self.wait(0.5)
        
        norm_calculation = MathTex(
            r"\|\mathbf{a}\| = \sqrt{3^2 + 2^2} = \sqrt{13} \approx 3.61",
            color=GREEN, font_size=26
        )
        norm_calculation.to_edge(RIGHT).shift(LEFT * 1.5 + DOWN * 2.3)
        self.add_fixed_in_frame_mobjects(norm_calculation)
        self.play(Write(norm_calculation), run_time=0.8)
        self.wait(1.0)
        
        # ベクトルの長さを視覚的に強調
        length_line = DashedLine(
            axes.c2p(0, 0), axes.c2p(3, 2),
            color=YELLOW, stroke_width=4, dash_length=0.1
        )
        self.add_fixed_in_frame_mobjects(length_line)
        
        length_label = MathTex(r"\|\mathbf{a}\| \approx 3.61", 
                              color=YELLOW, font_size=24)
        length_label.move_to(axes.c2p(1.5, 1) + UP * 0.3)
        self.add_fixed_in_frame_mobjects(length_label)
        
        self.play(Create(length_line), Write(length_label), run_time=0.8)
        self.wait(1.2)
        
        self.play(
            FadeOut(norm_definition_text), FadeOut(norm_eq), 
            FadeOut(norm_expanded), FadeOut(concrete_example),
            FadeOut(vec_value), FadeOut(norm_calculation),
            FadeOut(length_line), FadeOut(length_label),
            FadeOut(subtitle2)
        )
        self.wait(0.3)
        
        # === パート3: ノルムの性質 ===
        subtitle3 = Text("ノルムの重要な性質", font_size=32, color=PURPLE)
        subtitle3.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle3)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.5)
        
        properties = VGroup(
            MathTex(r"1.\quad \|\mathbf{a}\| \geq 0", color=WHITE, font_size=28),
            MathTex(r"2.\quad \|\mathbf{a}\| = 0 \Leftrightarrow \mathbf{a} = \mathbf{0}", 
                   color=WHITE, font_size=28),
            MathTex(r"3.\quad \|c\mathbf{a}\| = |c| \cdot \|\mathbf{a}\|", 
                   color=WHITE, font_size=28),
            MathTex(r"4.\quad \|\mathbf{a} + \mathbf{b}\| \leq \|\mathbf{a}\| + \|\mathbf{b}\|", 
                   color=WHITE, font_size=28),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        properties.to_edge(RIGHT).shift(LEFT * 1.5 + UP * 0.2)
        self.add_fixed_in_frame_mobjects(properties)
        
        for prop in properties:
            self.play(Write(prop), run_time=0.7)
            self.wait(0.5)
        
        self.wait(0.8)
        
        # スカラー倍の視覚化
        vec_2a = Vector(
            axes.c2p(6, 4) - axes.c2p(0, 0),
            color=RED,
            stroke_width=6
        ).shift(axes.c2p(0, 0)).scale(0.5, about_point=axes.c2p(0, 0))
        self.add_fixed_in_frame_mobjects(vec_2a)
        
        vec_2a_label = MathTex(r"2\mathbf{a}", color=RED, font_size=28)
        vec_2a_label.next_to(vec_2a.get_end(), UP + RIGHT, buff=0.2)
        self.add_fixed_in_frame_mobjects(vec_2a_label)
        
        scalar_note = Text("スカラー倍すると長さも倍に", 
                          color=YELLOW, font_size=24)
        scalar_note.to_edge(RIGHT).shift(LEFT * 1.5 + DOWN * 2)
        self.add_fixed_in_frame_mobjects(scalar_note)
        
        self.play(
            TransformFromCopy(vec_a, vec_2a),
            Write(vec_2a_label),
            Write(scalar_note),
            run_time=1.0
        )
        self.wait(1.2)
        
        self.play(
            FadeOut(properties), FadeOut(vec_2a), 
            FadeOut(vec_2a_label), FadeOut(scalar_note),
            FadeOut(subtitle3)
        )
        self.wait(0.3)
        
        # === パート4: 距離の定義 ===
        subtitle4 = Text("ベクトル間の距離", font_size=32, color=ORANGE)
        subtitle4.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle4)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.5)
        
        # 2つ目のベクトルを追加
        vec_b = Vector(
            axes.c2p(4, 3) - axes.c2p(0, 0),
            color=RED,
            stroke_width=6
        ).shift(axes.c2p(0, 0))
        self.add_fixed_in_frame_mobjects(vec_b)
        
        vec_b_label = MathTex(r"\mathbf{b}", color=RED, font_size=32)
        vec_b_label.next_to(vec_b.get_end(), RIGHT, buff=0.2)
        self.add_fixed_in_frame_mobjects(vec_b_label)
        
        self.play(Create(vec_b), Write(vec_b_label), run_time=0.7)
        self.wait(0.5)
        
        # 距離の疑問
        distance_question = VGroup(
            Text("2つのベクトルの間の", color=WHITE, font_size=26),
            Text("「距離」はどう測る？", color=YELLOW, font_size=26),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        distance_question.to_edge(RIGHT).shift(LEFT * 1.5 + UP * 1.5)
        self.add_fixed_in_frame_mobjects(distance_question)
        
        self.play(Write(distance_question), run_time=0.8)
        self.wait(1.0)
        
        # 答え：差のノルム
        distance_answer = Text("答え：差のノルムを取る！", 
                              color=GREEN, font_size=28, weight=BOLD)
        distance_answer.to_edge(RIGHT).shift(LEFT * 1.5 + UP * 0.3)
        self.add_fixed_in_frame_mobjects(distance_answer)
        self.play(Write(distance_answer), run_time=0.7)
        self.wait(0.8)
        
        self.play(FadeOut(distance_question), FadeOut(distance_answer))
        self.wait(0.3)
        
        # === パート5: 距離の定義式 ===
        subtitle5 = Text("距離の定義", font_size=32, color=GREEN)
        subtitle5.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle5)
        self.play(Transform(subtitle4, subtitle5), run_time=0.5)
        self.wait(0.5)
        
        # 距離の定義式
        distance_def = MathTex(
            r"d(\mathbf{a}, \mathbf{b}) = \|\mathbf{a} - \mathbf{b}\|",
            color=GREEN, font_size=36
        )
        distance_def.to_edge(RIGHT).shift(LEFT * 1.5 + UP * 1.5)
        self.add_fixed_in_frame_mobjects(distance_def)
        self.play(Write(distance_def), run_time=0.8)
        self.wait(0.8)
        
        # 展開した式
        distance_expanded = MathTex(
            r"= \sqrt{(a_1 - b_1)^2 + (a_2 - b_2)^2 + \cdots}",
            color=GREEN, font_size=28
        )
        distance_expanded.to_edge(RIGHT).shift(LEFT * 1.5 + UP * 0.7)
        self.add_fixed_in_frame_mobjects(distance_expanded)
        self.play(Write(distance_expanded), run_time=0.8)
        self.wait(0.8)
        
        # 差ベクトルを視覚化
        vec_diff = Vector(
            axes.c2p(1, 1) - axes.c2p(0, 0),
            color=YELLOW,
            stroke_width=6
        ).shift(axes.c2p(3, 2))
        self.add_fixed_in_frame_mobjects(vec_diff)
        
        vec_diff_label = MathTex(r"\mathbf{b} - \mathbf{a}", 
                                color=YELLOW, font_size=28)
        vec_diff_label.next_to(vec_diff.get_center(), UP, buff=0.2)
        self.add_fixed_in_frame_mobjects(vec_diff_label)
        
        # 差ベクトルの説明
        diff_explanation = Text("終点から終点へのベクトル", 
                               color=YELLOW, font_size=24)
        diff_explanation.to_edge(RIGHT).shift(LEFT * 1.5 + DOWN * 0.3)
        self.add_fixed_in_frame_mobjects(diff_explanation)
        
        self.play(
            Create(vec_diff), 
            Write(vec_diff_label),
            Write(diff_explanation),
            run_time=1.0
        )
        self.wait(1.0)
        
        # 具体的な計算例
        calc_title = Text("具体例：", color=ORANGE, font_size=26, weight=BOLD)
        calc_title.to_edge(RIGHT).shift(LEFT * 1.5 + DOWN * 1.2)
        self.add_fixed_in_frame_mobjects(calc_title)
        self.play(Write(calc_title), run_time=0.6)
        self.wait(0.3)
        
        vec_values = MathTex(
            r"\mathbf{a} = \begin{bmatrix} 3 \\ 2 \end{bmatrix}, \quad "
            r"\mathbf{b} = \begin{bmatrix} 4 \\ 3 \end{bmatrix}",
            color=WHITE, font_size=24
        )
        vec_values.to_edge(RIGHT).shift(LEFT * 1.5 + DOWN * 1.8)
        self.add_fixed_in_frame_mobjects(vec_values)
        self.play(Write(vec_values), run_time=0.7)
        self.wait(0.5)
        
        distance_calc = MathTex(
            r"d = \sqrt{(4-3)^2 + (3-2)^2} = \sqrt{2} \approx 1.41",
            color=GREEN, font_size=24
        )
        distance_calc.to_edge(RIGHT).shift(LEFT * 1.5 + DOWN * 2.5)
        self.add_fixed_in_frame_mobjects(distance_calc)
        self.play(Write(distance_calc), run_time=0.8)
        self.wait(1.0)
        
        # 距離を視覚的に強調
        distance_line = DashedLine(
            axes.c2p(3, 2), axes.c2p(4, 3),
            color=ORANGE, stroke_width=5, dash_length=0.15
        )
        self.add_fixed_in_frame_mobjects(distance_line)
        
        distance_label = MathTex(r"d \approx 1.41", 
                                color=ORANGE, font_size=26)
        distance_label.move_to(axes.c2p(3.5, 2.5) + RIGHT * 0.5)
        self.add_fixed_in_frame_mobjects(distance_label)
        
        self.play(
            Create(distance_line), 
            Write(distance_label),
            run_time=0.8
        )
        self.wait(1.5)
        
        self.play(
            FadeOut(distance_def), FadeOut(distance_expanded),
            FadeOut(vec_diff), FadeOut(vec_diff_label),
            FadeOut(diff_explanation), FadeOut(calc_title),
            FadeOut(vec_values), FadeOut(distance_calc),
            FadeOut(distance_line), FadeOut(distance_label),
            FadeOut(subtitle4) , FadeOut(subtitle5)
        )
        self.wait(0.3)
        
        # === パート6: 距離の性質 ===
        subtitle6 = Text("距離の重要な性質", font_size=32, color=PURPLE)
        subtitle6.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle6)
        self.play(Write(subtitle6), run_time=0.6)
        self.wait(0.5)
        
        distance_properties = VGroup(
            MathTex(r"1.\quad d(\mathbf{a}, \mathbf{b}) \geq 0", 
                   color=WHITE, font_size=26),
            MathTex(r"2.\quad d(\mathbf{a}, \mathbf{b}) = 0 \Leftrightarrow \mathbf{a} = \mathbf{b}", 
                   color=WHITE, font_size=26),
            MathTex(r"3.\quad d(\mathbf{a}, \mathbf{b}) = d(\mathbf{b}, \mathbf{a})", 
                   color=WHITE, font_size=26),
            Text("(対称性)", color=YELLOW, font_size=22),
            MathTex(r"4.\quad d(\mathbf{a}, \mathbf{c}) \leq d(\mathbf{a}, \mathbf{b}) + d(\mathbf{b}, \mathbf{c})", 
                   color=WHITE, font_size=24),
            Text("(三角不等式)", color=YELLOW, font_size=22),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        distance_properties.to_edge(RIGHT).shift(LEFT * 1.5 + UP * 0.8)
        self.add_fixed_in_frame_mobjects(distance_properties)
        
        for i, prop in enumerate(distance_properties):
            self.play(Write(prop), run_time=0.6)
            self.wait(0.4)
        
        self.wait(1.2)
        
        # 三角不等式の視覚化
        vec_c = Vector(
            axes.c2p(1, 3.5) - axes.c2p(0, 0),
            color=GREEN,
            stroke_width=6
        ).shift(axes.c2p(0, 0))
        self.add_fixed_in_frame_mobjects(vec_c)
        
        vec_c_label = MathTex(r"\mathbf{c}", color=GREEN, font_size=28)
        vec_c_label.next_to(vec_c.get_end(), LEFT, buff=0.2)
        self.add_fixed_in_frame_mobjects(vec_c_label)
        
        # 3つの距離を示す
        dist_ab = DashedLine(axes.c2p(3, 2), axes.c2p(4, 3), 
                            color=ORANGE, stroke_width=3, dash_length=0.1)
        dist_bc = DashedLine(axes.c2p(4, 3), axes.c2p(1, 3.5), 
                            color=PINK, stroke_width=3, dash_length=0.1)
        dist_ac = DashedLine(axes.c2p(3, 2), axes.c2p(1, 3.5), 
                            color=PURPLE, stroke_width=3, dash_length=0.1)
        
        self.add_fixed_in_frame_mobjects(dist_ab, dist_bc, dist_ac)
        
        triangle_note = Text("遠回りすると距離は長くなる", 
                           color=YELLOW, font_size=22)
        triangle_note.to_edge(RIGHT).shift(LEFT * 1.5 + DOWN * 2.8)
        self.add_fixed_in_frame_mobjects(triangle_note)
        
        self.play(
            Create(vec_c), Write(vec_c_label),
            Create(dist_ab), Create(dist_bc), Create(dist_ac),
            Write(triangle_note),
            run_time=1.2
        )
        self.wait(1.5)
        
        self.play(
            FadeOut(distance_properties),
            FadeOut(vec_c), FadeOut(vec_c_label),
            FadeOut(dist_ab), FadeOut(dist_bc), FadeOut(dist_ac),
            FadeOut(triangle_note),
            FadeOut(subtitle6)
        )
        self.wait(0.3)
        
        # === まとめ ===
        summary = Text("まとめ", font_size=36, color=GOLD, weight=BOLD)
        summary.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(summary)
        self.play(Write(summary), run_time=0.6)
        self.wait(0.5)
        
        summary_points = VGroup(
            Text("✓ ノルム：ベクトル自身との内積から", color=WHITE, font_size=24),
            MathTex(r"\|\mathbf{a}\| = \sqrt{\mathbf{a} \cdot \mathbf{a}}", 
                   color=GREEN, font_size=28),
            Text("✓ 距離：2つのベクトルの差のノルム", color=WHITE, font_size=24),
            MathTex(r"d(\mathbf{a}, \mathbf{b}) = \|\mathbf{a} - \mathbf{b}\|", 
                   color=ORANGE, font_size=28),
            Text("✓ 内積から導かれる重要な概念", color=YELLOW, font_size=24),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        summary_points.to_edge(RIGHT).shift(LEFT * 1.8 + UP * 0.5)
        self.add_fixed_in_frame_mobjects(summary_points)
        
        for point in summary_points:
            self.play(Write(point), run_time=0.7)
            self.wait(0.5)
        
        self.wait(2.0)
        
        # フェードアウト
        all_objects = VGroup(
            title, summary, summary_points,
            grid, axes, vec_a, vec_a_label, vec_b, vec_b_label
        )
        self.play(FadeOut(all_objects), run_time=1.0)
        self.wait(0.5)
