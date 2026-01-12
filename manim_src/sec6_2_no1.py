from manim import *

class NormalizedVectorProjection(ThreeDScene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"
        
        # タイトル
        title = Text("正規化ベクトルとの内積による射影", font_size=40, color=WHITE)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)
        
        # === イントロ: 内積の幾何学的意味 ===
        intro_subtitle = Text("内積の幾何学的意味", font_size=32, color=YELLOW)
        intro_subtitle.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(intro_subtitle)
        self.play(Write(intro_subtitle), run_time=0.6)
        self.wait(0.5)
        
        intro_text = VGroup(
            Text("内積で「影の長さ」を測ることができる", color=WHITE, font_size=26, weight=BOLD),
            # MathTex(r"\langle \mathbf{u}_1 | \mathbf{x} \rangle = \|\mathbf{u}_1\| \|\mathbf{x}\| \cos\theta",
            #        color=YELLOW, font_size=30),
            # Text("特に ||u₁|| = 1 のとき、内積 = 影の長さ", color=GREEN, font_size=24),
        ).arrange(DOWN, buff=0.4)
        intro_text.shift(DOWN * 0.5)
        self.add_fixed_in_frame_mobjects(intro_text)
        
        self.play(Write(intro_text), run_time=1.2)
        self.wait(1.5)
        
        self.play(FadeOut(intro_text), FadeOut(intro_subtitle))
        self.wait(0.3)
        
        # === パート1: 2次元平面でのベクトル設定 ===
        # subtitle1 = Text("2次元平面でのベクトル", font_size=32, color=BLUE)
        # subtitle1.next_to(title, DOWN)
        # self.add_fixed_in_frame_mobjects(subtitle1)
        # self.play(Write(subtitle1), run_time=0.6)
        # self.wait(0.5)
        
        # 2D座標軸を作成
        axes = Axes(
            x_range=[-0.5, 4, 1],
            y_range=[-0.5, 3.5, 1],
            x_length=6,
            y_length=5,
            axis_config={"color": GRAY, "stroke_width": 2},
        )
        axes.shift(LEFT * 2.5)
        
        axis_labels = VGroup(
            MathTex("x", font_size=24).next_to(axes.get_x_axis().get_end(), DOWN),
            MathTex("y", font_size=24).next_to(axes.get_y_axis().get_end(), LEFT),
        )
        
        self.play(Create(axes), Write(axis_labels), run_time=1.0)
        self.wait(0.8)
        
        # 正規化ベクトル u_1（ノルムが1）
        u1_coords = np.array([1, 0])
        u1_vector = Arrow(
            axes.c2p(0, 0),
            axes.c2p(1, 0),  # ノルムが1なので座標軸1目盛り分
            buff=0,
            color=RED,
            stroke_width=6
        )
        u1_label = MathTex(r"\mathbf{u}_1", color=RED, font_size=32)
        u1_label.next_to(axes.c2p(1, 0), DOWN, buff=0.3)
        
        self.play(Create(u1_vector), Write(u1_label), run_time=0.8)
        self.wait(0.6)
        
        # 正規化の説明
        norm_text = MathTex(r"\|\mathbf{u}_1\| = 1", color=RED, font_size=28)
        norm_text.to_corner(UL).shift(DOWN * 6.2 + RIGHT * 0.3)
        self.add_fixed_in_frame_mobjects(norm_text)
        self.play(Write(norm_text), run_time=0.6)
        self.wait(0.8)
        
        # 任意のベクトル x
        x_coords = np.array([2.5, 2.0])
        x_vector = Arrow(
            axes.c2p(0, 0),
            axes.c2p(x_coords[0], x_coords[1]),
            buff=0,
            color=BLUE,
            stroke_width=6
        )
        x_label = MathTex(r"\mathbf{x}", color=BLUE, font_size=32)
        x_label.next_to(axes.c2p(x_coords[0], x_coords[1]), UP+RIGHT, buff=0.2)
        
        self.play(Create(x_vector), Write(x_label), run_time=0.8)
        self.wait(0.8)
        
        # 角度θの表示
        # u1とxの間の角度を計算
        u1_normalized = u1_coords / np.linalg.norm(u1_coords)
        x_normalized = x_coords / np.linalg.norm(x_coords)
        cos_theta = np.dot(u1_normalized, x_normalized)
        theta_angle = np.arccos(np.clip(cos_theta, -1, 1))
        
        angle_arc = Arc(
            radius=0.6,
            start_angle=0,
            angle=theta_angle,
            color=YELLOW,
            stroke_width=4,
            arc_center=axes.c2p(0, 0)
        )
        
        angle_label = MathTex(r"\theta", color=YELLOW, font_size=28)
        angle_label.move_to(axes.c2p(0.5, 0.3))
        
        self.play(Create(angle_arc), Write(angle_label), run_time=0.7)
        self.wait(1.0)
        
        # self.play(
        #     FadeOut(subtitle1),
        # )
        # self.wait(0.3)
        
        # === パート2: 射影の視覚化 ===
        subtitle2 = Text("u₁方向への射影の可視化", font_size=32, color=PURPLE)
        subtitle2.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle2)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)
        
        # xから射影への垂線（u1方向への射影であることを明示）
        # u_1方向への射影: (x・u_1)u_1
        projection_length = np.dot(x_coords, u1_coords)
        projection_coords = projection_length * u1_coords
        perpendicular_line = DashedLine(
            axes.c2p(x_coords[0], x_coords[1]),
            axes.c2p(projection_coords[0], projection_coords[1]),
            color=ORANGE,
            stroke_width=4,
            dash_length=0.15
        )
        
        # 垂線のラベル
        perp_label = Text("u₁に垂直", color=ORANGE, font_size=22)
        perp_mid_x = (x_coords[0] + projection_coords[0]) / 2
        perp_mid_y = (x_coords[1] + projection_coords[1]) / 2
        perp_label.next_to(axes.c2p(perp_mid_x, perp_mid_y), RIGHT, buff=0.3)
        
        self.play(Create(perpendicular_line), Write(perp_label), run_time=0.9)
        self.wait(1.0)
        
        # 影（射影）を作成     
        projection_vector = Arrow(
            axes.c2p(0, 0),
            axes.c2p(projection_coords[0], projection_coords[1]),
            buff=0,
            color=GREEN,
            stroke_width=8
        )
        projection_label = Text("射影（影）", color=GREEN, font_size=26)
        projection_label.next_to(axes.c2p(projection_coords[0], projection_coords[1]), DOWN, buff=0.4)
        
        # 射影点
        shadow_dot = Dot(axes.c2p(projection_coords[0], projection_coords[1]), 
                        color=GREEN, radius=0.1)
        
        self.play(
            Create(projection_vector),
            Create(shadow_dot),
            Write(projection_label),
            run_time=0.9
        )
        self.wait(1.0)
        
        # 影の長さを強調
        shadow_length_brace = Brace(
            Line(axes.c2p(0, 0), axes.c2p(projection_coords[0], projection_coords[1])),
            direction=DOWN,
            color=GREEN,
            buff=0.2
        )
        shadow_length_label = Text("影の長さ", color=GREEN, font_size=24)
        shadow_length_label.next_to(shadow_length_brace, DOWN, buff=0.1)
        
        self.play(
            Create(shadow_length_brace),
            Write(shadow_length_label),
            run_time=0.7
        )
        self.wait(1.2)
        
        self.play(FadeOut(subtitle2))
        self.wait(0.3)
        
        # === パート3: 数式による説明 ===
        subtitle3 = Text("内積と影の長さの関係", font_size=32, color=TEAL)
        subtitle3.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle3)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.5)
        
        # 内積の公式
        formula_title = Text("内積の公式:", color=YELLOW, font_size=26, weight=BOLD)
        formula_title.to_corner(UR).shift(DOWN * 1.5 + LEFT * 2.0)
        self.add_fixed_in_frame_mobjects(formula_title)
        self.play(Write(formula_title), run_time=0.6)
        self.wait(0.4)
        
        inner_product_formula = MathTex(
            r"\langle \mathbf{u}_1 | \mathbf{x} \rangle = \|\mathbf{u}_1\| \|\mathbf{x}\| \cos\theta",
            color=WHITE, font_size=26
        )
        inner_product_formula.next_to(formula_title, DOWN, buff=0.3, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(inner_product_formula)
        self.play(Write(inner_product_formula), run_time=0.8)
        self.wait(0.8)
        
        # 正規化条件を代入
        substitution_arrow = MathTex(r"\Downarrow", color=YELLOW, font_size=30)
        substitution_arrow.next_to(inner_product_formula, DOWN, buff=0.2)
        substitution_text = MathTex(r"\|\mathbf{u}_1\| = 1", color=RED, font_size=22)
        substitution_text.next_to(substitution_arrow, RIGHT, buff=0.2)
        self.add_fixed_in_frame_mobjects(substitution_arrow, substitution_text)
        self.play(Write(substitution_arrow), Write(substitution_text), run_time=0.6)
        self.wait(0.6)
        
        # 簡略化された式
        simplified_formula = MathTex(
            r"\langle \mathbf{u}_1 | \mathbf{x} \rangle = \|\mathbf{x}\| \cos\theta",
            color=GREEN, font_size=28
        )
        simplified_formula.next_to(substitution_arrow, DOWN, buff=0.3, aligned_edge=LEFT)
        simplified_box = SurroundingRectangle(simplified_formula, color=GREEN, buff=0.15)
        self.add_fixed_in_frame_mobjects(simplified_formula, simplified_box)
        self.play(Write(simplified_formula), Create(simplified_box), run_time=0.8)
        self.wait(1.0)
        
        # 幾何学的解釈
        geometric_interpretation = VGroup(
            Text("幾何学的意味:", color=ORANGE, font_size=24, weight=BOLD),
            # MathTex(r"\|\mathbf{x}\| \cos\theta = \text{projection length}", 
            #        color=ORANGE, font_size=22),
            Text(
            "内積 = 影の長さ",
            color=ORANGE, font_size=28, weight=BOLD, slant=ITALIC)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        geometric_interpretation.next_to(simplified_formula, DOWN, buff=0.5, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(geometric_interpretation)
        self.play(Write(geometric_interpretation), run_time=0.9)
        self.wait(1.2)
        
        # 重要なポイント
        # key_point = Text(
        #     "||u₁|| = 1 ⇒ 内積 = 影の長さ",
        #     color=YELLOW, font_size=28, weight=BOLD, slant=ITALIC
        # )
        # key_point.to_edge(DOWN).shift(UP * 0.5)
        # key_box = SurroundingRectangle(key_point, color=YELLOW, buff=0.2)
        # self.add_fixed_in_frame_mobjects(key_point, key_box)
        # self.play(Write(key_point), Create(key_box), run_time=0.8)
        # self.wait(1.5)
        
        # カメラ回転は削除（2Dなので不要）
        
        self.play(
            FadeOut(formula_title), FadeOut(inner_product_formula),
            FadeOut(substitution_arrow), FadeOut(substitution_text),
            FadeOut(simplified_formula), FadeOut(simplified_box),
            FadeOut(geometric_interpretation),
            # FadeOut(key_point), FadeOut(key_box),
            FadeOut(subtitle3)
        )
        self.wait(0.3)
        
        # === パート4: 具体例での計算 ===
        subtitle4 = Text("具体的な計算例", font_size=32, color=ORANGE)
        subtitle4.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle4)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.5)
        
        # ベクトルの成分表示
        vector_components = VGroup(
            MathTex(r"\mathbf{u}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}", 
                   color=RED, font_size=26),
            MathTex(r"\mathbf{x} = \begin{bmatrix} 2.5 \\ 2.0 \end{bmatrix}", 
                   color=BLUE, font_size=26),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        vector_components.to_corner(DL).shift(UP * 1.5 + RIGHT * 0.3)
        self.add_fixed_in_frame_mobjects(vector_components)
        self.play(Write(vector_components), run_time=0.8)
        self.wait(0.8)
        
        # 内積の計算
        calculation_title = Text("内積を計算:", color=WHITE, font_size=24, weight=BOLD)
        calculation_title.to_corner(DR).shift(UP * 3.5 + LEFT * 3)
        self.add_fixed_in_frame_mobjects(calculation_title)
        self.play(Write(calculation_title), run_time=0.5)
        self.wait(0.3)
        
        calculation_steps = VGroup(
            MathTex(r"\langle \mathbf{u}_1 | \mathbf{x} \rangle", color=WHITE, font_size=24),
            MathTex(r"= 1 \times 2.5 + 0 \times 2.0", color=WHITE, font_size=22),
            MathTex(r"= 2.5", color=GREEN, font_size=26),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        calculation_steps.next_to(calculation_title, DOWN, buff=0.3, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(calculation_steps)
        
        for step in calculation_steps:
            self.play(Write(step), run_time=0.6)
            self.wait(0.4)
        
        self.wait(0.6)
        
        # 影の長さと一致
        match_text = VGroup(
            Text("これは影の長さと一致!", color=YELLOW, font_size=24, weight=BOLD),
            Text("影の長さ = 2.5", color=GREEN, font_size=24),
        ).arrange(DOWN, buff=0.3)
        match_text.next_to(calculation_steps, DOWN, buff=0.5, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(match_text)
        self.play(Write(match_text), run_time=0.8)
        self.wait(1.2)
        
        self.play(
            FadeOut(vector_components),
            FadeOut(calculation_title),
            FadeOut(calculation_steps),
            FadeOut(match_text),
            FadeOut(subtitle4)
        )
        self.wait(0.3)
        
        # 2Dオブジェクトをフェードアウト
        self.play(
            FadeOut(axes), FadeOut(axis_labels),
            FadeOut(u1_vector), FadeOut(u1_label),
            FadeOut(x_vector), FadeOut(x_label),
            FadeOut(angle_arc), FadeOut(angle_label),
            FadeOut(projection_vector),
            FadeOut(projection_label), FadeOut(shadow_dot),
            FadeOut(perpendicular_line), FadeOut(perp_label),
            FadeOut(shadow_length_brace), FadeOut(shadow_length_label),
            FadeOut(norm_text),
            run_time=0.8
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
                    Text("正規化ベクトルとの内積: ", color=WHITE, font_size=24),
                    MathTex(r"\langle \mathbf{u}_1 | \mathbf{x} \rangle = \|\mathbf{x}\| \cos\theta", 
                           color=WHITE, font_size=22),
                ).arrange(RIGHT, buff=0.2),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("2.", color=WHITE, font_size=26, weight=BOLD),
                Text("||u₁|| = 1 のとき、内積はu₁方向への影の長さ", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("3.", color=WHITE, font_size=26, weight=BOLD),
                Text("射影（projection）の幾何学的な意味を表す", color=YELLOW, font_size=24),
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
