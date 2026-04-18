from manim import *

class AbstractVectorSpace(Scene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"
        
        # タイトル
        title = Text("抽象的なものの集合を考える", font_size=40, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)
        
        # === イントロ ===
        intro_text = VGroup(
            Text("多項式（関数）もベクトルとして扱える", color=WHITE, font_size=32, weight=BOLD),
            Text("係数を取り出すことで、ベクトル化", color=YELLOW, font_size=26),
        ).arrange(DOWN, buff=0.4)
        intro_text.shift(DOWN * 0.5)
        
        self.play(Write(intro_text), run_time=1.2)
        self.wait(1.5)
        
        self.play(FadeOut(intro_text))
        self.wait(0.3)
        
        # === パート1: 1次多項式のベクトル化 ===
        subtitle1 = Text("例1: 1次多項式を2次元ベクトルに", font_size=32, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.5)
        
        # 多項式f_1の表示
        f1_text = MathTex(r"f_1(x) = -2 + 2x", color=BLUE, font_size=40)
        f1_text.shift(UP * 2)
        self.play(Write(f1_text), run_time=0.8)
        self.wait(0.8)
        
        # 係数の取り出し
        coeff_explanation = Text("係数を取り出すと...", color=YELLOW, font_size=28)
        coeff_explanation.next_to(f1_text, DOWN, buff=0.5)
        self.play(Write(coeff_explanation), run_time=0.6)
        self.wait(0.5)
        
        # 矢印
        arrow1 = Arrow(coeff_explanation.get_bottom(), coeff_explanation.get_bottom() + DOWN * 0.8, 
                      color=YELLOW, buff=0.1)
        self.play(Create(arrow1), run_time=0.5)
        self.wait(0.3)
        
        # ベクトル表示
        vector_f1 = MathTex(r"\begin{bmatrix} -2 \\ 2 \end{bmatrix}", color=RED, font_size=44)
        vector_f1.next_to(arrow1, DOWN, buff=0.3)
        self.play(Write(vector_f1), run_time=0.8)
        self.wait(0.8)
        
        # 2次元平面での視覚化
        axes_2d = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=4,
            y_length=4,
            axis_config={"color": GRAY, "stroke_width": 2}
        )
        axes_2d.to_corner(DR).shift(UP * 0.5)
        
        axis_labels_2d = VGroup(
            MathTex("const.", font_size=24).next_to(axes_2d.get_x_axis().get_end(), DOWN),
            MathTex("x", font_size=24).next_to(axes_2d.get_y_axis().get_end(), LEFT),
        )
        
        self.play(Create(axes_2d), Write(axis_labels_2d), run_time=0.8)
        self.wait(0.5)
        
        # ベクトルの矢印
        vector_arrow_2d = Arrow(
            axes_2d.c2p(0, 0),
            axes_2d.c2p(-2, 2),
            buff=0,
            color=RED,
            stroke_width=6
        )
        vector_label_2d = MathTex(r"\begin{bmatrix} -2 \\ 2 \end{bmatrix}", 
                                 color=RED, font_size=28)
        vector_label_2d.next_to(axes_2d.c2p(-2, 2), LEFT, buff=0.2)
        
        self.play(Create(vector_arrow_2d), Write(vector_label_2d), run_time=0.9)
        self.wait(1.2)
        
        # フェードアウト
        self.play(
            FadeOut(f1_text), FadeOut(coeff_explanation), FadeOut(arrow1),
            FadeOut(vector_f1), FadeOut(axes_2d), FadeOut(axis_labels_2d),
            FadeOut(vector_arrow_2d), FadeOut(vector_label_2d),
            FadeOut(subtitle1)
        )
        self.wait(0.3)
        
        # === パート2: 2次多項式のベクトル化 ===
        subtitle2 = Text("例2: 2次多項式を3次元ベクトルに", font_size=32, color=GREEN)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)
        
        # 多項式f_2の表示
        f2_text = MathTex(r"f_2(x) = 3 - 2x + x^2", color=GREEN, font_size=40)
        f2_text.shift(UP * 1.5 + LEFT * 1.5)
        self.play(Write(f2_text), run_time=0.8)
        self.wait(0.8)
        
        # 係数の取り出し
        coeff_explanation2 = Text("係数を取り出すと...", color=YELLOW, font_size=26)
        coeff_explanation2.next_to(f2_text, DOWN, buff=0.4)
        self.play(Write(coeff_explanation2), run_time=0.6)
        self.wait(0.5)
        
        # 矢印
        arrow2 = Arrow(coeff_explanation2.get_bottom(), coeff_explanation2.get_bottom() + DOWN * 0.6, 
                      color=YELLOW, buff=0.1)
        self.play(Create(arrow2), run_time=0.5)
        self.wait(0.3)
        
        # ベクトル表示
        vector_f2 = MathTex(r"\begin{bmatrix} 3 \\ -2 \\ 1 \end{bmatrix}", 
                          color=PURPLE, font_size=40)
        vector_f2.next_to(arrow2, DOWN, buff=0.3)
        self.play(Write(vector_f2), run_time=0.8)
        self.wait(0.8)
        
        # 3次元空間での視覚化
        # 新しいシーンに切り替えるため、一時的に3Dシーンを埋め込む
        axes_3d_group = VGroup()
        
        # 3D風の座標軸を2Dで表現
        # 簡易的な3D表現
        origin_3d = RIGHT * 3 + DOWN * 1.5
        x_axis_3d = Line(origin_3d, origin_3d + RIGHT * 2.5, color=GRAY)
        y_axis_3d = Line(origin_3d, origin_3d + LEFT * 1.5 + UP * 0.75, color=GRAY)
        z_axis_3d = Line(origin_3d, origin_3d + UP * 2.5, color=GRAY)
        
        x_label_3d = MathTex("const.", font_size=22).next_to(x_axis_3d.get_end(), DOWN)
        y_label_3d = MathTex("x", font_size=22).next_to(y_axis_3d.get_end(), LEFT)
        z_label_3d = MathTex("x^2", font_size=22).next_to(z_axis_3d.get_end(), UP)
        
        axes_3d_group.add(x_axis_3d, y_axis_3d, z_axis_3d, x_label_3d, y_label_3d, z_label_3d)
        
        self.play(Create(axes_3d_group), run_time=0.8)
        self.wait(0.5)
        
        # ベクトルの矢印（3D風に）
        # 3, -2, 1 → x方向に3、y方向に-2、z方向に1
        vector_end_3d = origin_3d + RIGHT * 2.0 + LEFT * 1.0 + UP * 0.5 + UP * 0.8
        vector_arrow_3d = Arrow(
            origin_3d,
            vector_end_3d,
            buff=0,
            color=PURPLE,
            stroke_width=6
        )
        vector_label_3d = MathTex(r"\begin{bmatrix} 3 \\ -2 \\ 1 \end{bmatrix}", 
                                 color=PURPLE, font_size=26)
        vector_label_3d.next_to(vector_end_3d, RIGHT, buff=0.2)
        
        self.play(Create(vector_arrow_3d), Write(vector_label_3d), run_time=0.9)
        self.wait(1.2)
        
        # フェードアウト
        self.play(
            FadeOut(f2_text), FadeOut(coeff_explanation2), FadeOut(arrow2),
            FadeOut(vector_f2), FadeOut(axes_3d_group),
            FadeOut(vector_arrow_3d), FadeOut(vector_label_3d),
            FadeOut(subtitle2)
        )
        self.wait(0.3)
        
        # === パート3: 関数の操作と行列演算 ===
        subtitle3 = Text("関数の操作 → 行列演算", font_size=36, color=ORANGE, weight=BOLD)
        subtitle3.next_to(title, DOWN)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.5)
        
        explanation = Text(
            "線形性を満たせば、抽象的な操作も行列で表現可能!",
            color=YELLOW, font_size=26, weight=BOLD
        )
        explanation.next_to(subtitle3, DOWN, buff=0.3)
        self.play(Write(explanation), run_time=0.9)
        self.wait(1.0)
        
        self.play(FadeOut(explanation))
        self.wait(0.3)
        
        # 上段：関数の関係
        function_level_label = Text("関数レベル:", color=WHITE, font_size=24, weight=BOLD)
        function_level_label.to_edge(LEFT).shift(UP * 1.5)
        self.play(Write(function_level_label), run_time=0.5)
        self.wait(0.3)
        
        f2_func = MathTex(r"f_2(x) = 3 - 2x + x^2", color=GREEN, font_size=32)
        f2_func.shift(UP * 1.5 + LEFT * 1)
        
        f1_func = MathTex(r"f_1(x) = -2 + 2x", color=BLUE, font_size=32)
        f1_func.shift(UP * 1.5 + RIGHT * 2.5)
        
        # 微分の矢印
        diff_arrow = Arrow(f2_func.get_right(), f1_func.get_left(), 
                          color=YELLOW, buff=0.2, stroke_width=6)
        diff_label = Text("微分", color=YELLOW, font_size=24, weight=BOLD)
        diff_label.next_to(diff_arrow, UP, buff=0.1)
        
        self.play(Write(f2_func), run_time=0.7)
        self.wait(0.4)
        self.play(Create(diff_arrow), Write(diff_label), run_time=0.7)
        self.wait(0.4)
        self.play(Write(f1_func), run_time=0.7)
        self.wait(1.0)
        
        # 下段：ベクトルの関係
        vector_level_label = Text("ベクトルレベル:", color=WHITE, font_size=24, weight=BOLD)
        vector_level_label.to_edge(LEFT).shift(DOWN * 1.2)
        self.play(Write(vector_level_label), run_time=0.5)
        self.wait(0.3)
        
        vec_f2 = MathTex(r"\begin{bmatrix} 3 \\ -2 \\ 1 \end{bmatrix}", 
                        color=PURPLE, font_size=36)
        vec_f2.shift(DOWN * 1.2 + LEFT * 1.5)
        
        vec_f1 = MathTex(r"\begin{bmatrix} -2 \\ 2 \end{bmatrix}", 
                        color=RED, font_size=36)
        vec_f1.shift(DOWN * 1.2 + RIGHT * 2.8)
        
        # 行列演算の矢印
        matrix_arrow = Arrow(vec_f2.get_right(), vec_f1.get_left(), 
                           color=ORANGE, buff=0.3, stroke_width=6)
        
        self.play(Write(vec_f2), run_time=0.7)
        self.wait(0.4)
        self.play(Create(matrix_arrow), run_time=0.7)
        self.wait(0.4)
        self.play(Write(vec_f1), run_time=0.7)
        self.wait(1.0)
        
        # 「行列演算が存在」を強調
        matrix_exists = Text("行列演算が存在!", color=ORANGE, font_size=28, weight=BOLD)
        matrix_exists.next_to(matrix_arrow, DOWN, buff=0.3)
        matrix_box = SurroundingRectangle(matrix_exists, color=ORANGE, buff=0.15)
        
        self.play(Write(matrix_exists), Create(matrix_box), run_time=0.8)
        self.wait(1.2)
        
        # 具体的な行列の表示
        matrix_detail = MathTex(
            r"\begin{bmatrix} 0 & -2 & 0 \\ 0 & 0 & 2 \end{bmatrix}",
            color=ORANGE, font_size=28
        )
        matrix_detail.next_to(matrix_arrow, UP, buff=0.1)
        
        self.play(Write(matrix_detail), run_time=0.9)
        self.wait(1.5)
        
        # 対応関係を強調する四角形
        func_box = SurroundingRectangle(
            VGroup(f2_func, diff_arrow, diff_label, f1_func),
            color=YELLOW, buff=0.2, stroke_width=3
        )
        vec_box = SurroundingRectangle(
            VGroup(vec_f2, matrix_arrow, vec_f1, matrix_detail),
            color=ORANGE, buff=0.2, stroke_width=3
        )
        
        self.play(Create(func_box), Create(vec_box), run_time=0.8)
        self.wait(1.5)
        
        self.play(
            FadeOut(function_level_label), FadeOut(f2_func), FadeOut(f1_func),
            FadeOut(diff_arrow), FadeOut(diff_label),
            FadeOut(vector_level_label), FadeOut(vec_f2), FadeOut(vec_f1),
            FadeOut(matrix_arrow), FadeOut(matrix_exists), FadeOut(matrix_box),
            FadeOut(matrix_detail), FadeOut(func_box), FadeOut(vec_box),
            FadeOut(subtitle3)
        )
        self.wait(0.3)
        
        # === まとめ ===
        summary_subtitle = Text("まとめ", font_size=36, color=GOLD, weight=BOLD)
        summary_subtitle.next_to(title, DOWN)
        self.play(Write(summary_subtitle), run_time=0.6)
        self.wait(0.5)
        
        # まとめのポイント
        summary_points = VGroup(
            VGroup(
                Text("1.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("多項式（関数）は係数を取り出すことで", color=WHITE, font_size=24),
                    Text("ベクトルとして表現できる", color=YELLOW, font_size=24, weight=BOLD),
                ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            
            VGroup(
                Text("2.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("線形性を満たす操作は", color=WHITE, font_size=24),
                    Text("行列演算として表現可能", color=ORANGE, font_size=24, weight=BOLD),
                ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            
            VGroup(
                Text("3.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("微分などの抽象的な操作も", color=WHITE, font_size=24),
                    Text("具体的な行列で計算できる!", color=GREEN, font_size=24, weight=BOLD),
                ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        ).arrange(DOWN, buff=0.6, aligned_edge=LEFT)
        summary_points.shift(UP * 0.2)
        
        for point in summary_points:
            self.play(Write(point), run_time=0.9)
            self.wait(0.6)
        
        self.wait(1.5)
        
        # 最終メッセージ
        final_message = Text(
            "抽象 → 具体（ベクトル・行列）で計算可能!",
            color=YELLOW, font_size=30, weight=BOLD, slant=ITALIC
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
