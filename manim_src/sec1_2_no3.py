from manim import *

class PlaneToVectors(ThreeDScene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"
        
        # タイトル
        title = Text("平面の方程式から空間の生成元へ", font_size=32, color=WHITE)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        self.wait(1)
        
        # === パート1: 平面の方程式を表示 ===
        subtitle1 = Text("平面の方程式", font_size=28, color=YELLOW)
        subtitle1.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle1)
        self.play(Write(subtitle1))
        self.wait(1)
        
        # 平面の方程式(右側の上部に配置)
        plane_eq = MathTex(
            r"2x + y + 2z = 0",
            color=WHITE,
            font_size=36
        )
        plane_eq.to_edge(RIGHT).shift(LEFT * 0.5 + UP * 2)
        self.add_fixed_in_frame_mobjects(plane_eq)
        self.play(Write(plane_eq))
        self.wait(1)
        
        # 3D座標軸を設定(左側に配置)
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-3, 3, 1],
            x_length=5,
            y_length=5,
            z_length=5,
            axis_config={"color": GRAY}
        )
        axes.shift(LEFT * (-3.5))
        
        # 座標軸のラベルを追加
        x_label = Text("X", color=RED, font_size=24)
        y_label = Text("Y", color=GREEN, font_size=24)
        z_label = Text("Z", color=BLUE, font_size=24)
        
        x_label.move_to(axes.c2p(3.5, 0, 0))
        y_label.move_to(axes.c2p(0, 3.5, 0))
        z_label.move_to(axes.c2p(0, 0, 3.5))
        
        # カメラの設定
        self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)
        self.play(Create(axes))
        self.add(x_label, y_label, z_label)
        self.wait(1)
        
        # 平面を描画 (2x + y + 2z = 0 => x = -0.5y - z)
        plane_surface = Surface(
            lambda u, v: axes.c2p(-0.5*u - v, u, v),
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=(20, 20),
            fill_opacity=0.5,
            checkerboard_colors=[BLUE_D, BLUE_E]
        )
        
        self.play(Create(plane_surface))
        self.wait(2)
        
        # カメラをZ軸中心に回転
        self.begin_ambient_camera_rotation(rate=0.2, about="theta")
        self.wait(3)
        self.stop_ambient_camera_rotation()
        
        # === パート2: 式変形 ===
        self.play(
            FadeOut(subtitle1),
            FadeOut(plane_surface, run_time=0.5)
        )
        
        subtitle2 = Text("式を変形してxについて解く", font_size=28, color=YELLOW)
        subtitle2.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle2)
        self.play(Write(subtitle2))
        self.wait(1)
        
        # 式変形のステップ(右側に縦に並べる)
        eq_step2 = MathTex(
            r"2x = -y - 2z",
            color=WHITE,
            font_size=32
        )
        eq_step2.next_to(plane_eq, DOWN, buff=0.4, aligned_edge=RIGHT)
        self.add_fixed_in_frame_mobjects(eq_step2)
        self.play(Write(eq_step2))
        self.wait(1)
        
        eq_step3 = MathTex(
            r"x = -\frac{1}{2}y - z",
            color=WHITE,
            font_size=32
        )
        eq_step3.next_to(eq_step2, DOWN, buff=0.4, aligned_edge=RIGHT)
        self.add_fixed_in_frame_mobjects(eq_step3)
        self.play(Write(eq_step3))
        self.wait(2)
        
        # y=r, z=s と置き換え
        eq_step4 = MathTex(
            r"y = r, \quad z = s",
            color=YELLOW,
            font_size=28
        )
        eq_step4.next_to(eq_step3, DOWN, buff=0.5, aligned_edge=RIGHT)
        self.add_fixed_in_frame_mobjects(eq_step4)
        self.play(Write(eq_step4))
        self.wait(1)
        
        eq_step5 = MathTex(
            r"x = -\frac{1}{2}r - s",
            color=WHITE,
            font_size=32
        )
        eq_step5.next_to(eq_step4, DOWN, buff=0.4, aligned_edge=RIGHT)
        self.add_fixed_in_frame_mobjects(eq_step5)
        self.play(Write(eq_step5))
        self.wait(2)
        
        # === パート3: ベクトル形式へ ===
        self.play(FadeOut(subtitle2))
        
        subtitle3 = Text("ベクトル形式で表現", font_size=28, color=YELLOW)
        subtitle3.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle3)
        self.play(Write(subtitle3))
        self.wait(1)
        
        # 前の式を消去
        self.play(FadeOut(plane_eq), FadeOut(eq_step2), FadeOut(eq_step3), FadeOut(eq_step4))
        
        # ベクトル形式(右側上部に再配置)
        vector_eq = MathTex(
            r"\begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} -\frac{1}{2}r - s \\ r \\ s \end{bmatrix}",
            color=WHITE,
            font_size=28
        )
        vector_eq.to_edge(RIGHT).shift(LEFT * 0.5 + UP * 2)
        self.add_fixed_in_frame_mobjects(vector_eq)
        self.play(Write(vector_eq))
        self.wait(2)
        

        
        # 線型結合の形に
        linear_comb_eq = MathTex(
            r"= r\begin{bmatrix} -\frac{1}{2} \\ 1 \\ 0 \end{bmatrix} + s\begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix}",
            color=WHITE,
            font_size=28
        )
        linear_comb_eq.next_to(vector_eq, DOWN, buff=0.5, aligned_edge=RIGHT)
        self.add_fixed_in_frame_mobjects(linear_comb_eq)
        self.play(Write(linear_comb_eq))
        self.wait(2)

        self.play(
            FadeOut(eq_step5),
            FadeOut(subtitle3)
        )
        
        # 生成元の強調
        generators = MathTex(
            r"\boldsymbol{v}_1 = \begin{bmatrix} -\frac{1}{2} \\ 1 \\ 0 \end{bmatrix}",
            color=BLUE,
            font_size=26
        )
        generators.next_to(linear_comb_eq, DOWN, buff=0.5, aligned_edge=RIGHT)
        self.add_fixed_in_frame_mobjects(generators)
        
        generators2 = MathTex(
            r"\boldsymbol{v}_2 = \begin{bmatrix} -1 \\ 0 \\ 1 \end{bmatrix}",
            color=GREEN,
            font_size=26
        )

        generators2.next_to(generators, DOWN, buff=0.3, aligned_edge=RIGHT)
        self.add_fixed_in_frame_mobjects(generators2)
        
        self.play(Write(generators), Write(generators2))
        self.wait(2)
        
        # === パート4: 3D空間でベクトルを表示 ===
        
        subtitle4 = Text("平面上の2つのベクトルが導かれる", font_size=28, color=YELLOW)
        subtitle4.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle4)
        self.play(Write(subtitle4))
        self.wait(1)
        
        # 平面を再表示
        self.play(Create(plane_surface))
        self.wait(1)
        
        # ベクトルv1を描画 (-0.5, 1, 0)
        v1_arrow = Arrow3D(
            start=axes.c2p(0, 0, 0),
            end=axes.c2p(-0.5, 1, 0),
            color=BLUE,
            thickness=0.02,
            height=0.3,
            base_radius=0.08
        )
        
        self.play(Create(v1_arrow))
        self.wait(1)
        
        # ベクトルv2を描画 (-1, 0, 1)
        v2_arrow = Arrow3D(
            start=axes.c2p(0, 0, 0),
            end=axes.c2p(-1, 0, 1),
            color=GREEN,
            thickness=0.02,
            height=0.3,
            base_radius=0.08
        )
        
        self.play(Create(v2_arrow))
        self.wait(2)
        
        # カメラをZ軸中心に逆方向に回転して関係を見せる
        self.begin_ambient_camera_rotation(rate=-0.3, about="theta")
        self.wait(4)
        self.stop_ambient_camera_rotation()
        
        # === パート5: 線形結合の例 ===
        self.play(FadeOut(subtitle4))
        
        subtitle5 = Text("このベクトルの線形結合で平面上の任意の点を表現", font_size=28, color=YELLOW)
        subtitle5.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle5)
        self.play(Write(subtitle5))
        self.wait(1)
        
        # 前の式を消去し、例を右側に表示
        self.play(
            FadeOut(vector_eq),
            FadeOut(linear_comb_eq),
            FadeOut(generators),
            FadeOut(generators2)
        )
        
        # 例: 2v1 + 1v2
        example_eq = MathTex(
            r"2\boldsymbol{v}_1 + 1\boldsymbol{v}_2",
            color=WHITE,
            font_size=32
        )
        example_eq.to_edge(RIGHT).shift(LEFT * 0.5 + UP * 2)
        self.add_fixed_in_frame_mobjects(example_eq)
        self.play(Write(example_eq))
        self.wait(1)
        
        # 2v1を描画 (2 * (-0.5, 1, 0) = (-1, 2, 0))
        v1_scaled = Arrow3D(
            start=axes.c2p(0, 0, 0),
            end=axes.c2p(-1, 2, 0),
            color=BLUE,
            thickness=0.02,
            height=0.3,
            base_radius=0.08
        )
        self.play(Create(v1_scaled))
        self.wait(1)
        
        # 1v2を2v1の先端から描画 ((-1, 0, 1))
        v2_shifted = Arrow3D(
            start=axes.c2p(-1, 2, 0),
            end=axes.c2p(-2, 2, 1),
            color=GREEN,
            thickness=0.02,
            height=0.3,
            base_radius=0.08
        )
        self.play(Create(v2_shifted))
        self.wait(1)
        
        # 結果のベクトル ((-2, 2, 1))
        result_arrow = Arrow3D(
            start=axes.c2p(0, 0, 0),
            end=axes.c2p(-2, 2, 1),
            color=YELLOW,
            thickness=0.025,
            height=0.3,
            base_radius=0.1
        )
        self.play(Create(result_arrow))
        self.wait(2)
        
        # カメラをZ軸中心に回転
        self.begin_ambient_camera_rotation(rate=0.2, about="theta")
        self.wait(3)
        self.stop_ambient_camera_rotation()
        
        # === パート6: まとめ ===
        self.play(
            FadeOut(v1_scaled),
            FadeOut(v2_shifted),
            FadeOut(result_arrow),
            FadeOut(example_eq),
            FadeOut(subtitle5)
        )
        
        subtitle6 = Text("つまり、平面は2つのベクトルで生成される", font_size=28, color=GREEN)
        subtitle6.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle6)
        self.play(Write(subtitle6))
        self.wait(1)
        
        summary = MathTex(
            r"r\boldsymbol{v}_1 + s\boldsymbol{v}_2",
            color=YELLOW,
            font_size=36
        )
        summary.to_edge(RIGHT).shift(LEFT * 0.5 + UP * 2)
        self.add_fixed_in_frame_mobjects(summary)
        self.play(Write(summary))
        self.wait(2)
