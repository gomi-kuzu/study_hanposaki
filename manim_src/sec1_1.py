from manim import *

class VectorAsNumbers(Scene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"
        
        # 座標平面を作成
        plane = NumberPlane(
            x_range=[-1, 4],
            y_range=[-1, 3],
            x_length=8,
            y_length=6,
            axis_config={"color": GRAY},
            background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )
        plane.add_coordinates()  # 座標ラベルを追加
        self.add(plane)
        
        # タイトル
        title = Text("矢印（ベクトル）は数字の組で表現できる", font_size=32, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # ベクトルを描画（右に1、上に2）- スケールを座標系に合わせる
        vector = Vector([1, 2], color=BLUE)
        vector.put_start_and_end_on(plane.c2p(0, 0), plane.c2p(1, 2))
        self.play(Create(vector))
        self.wait(1)
        
        # 移動の説明
        explanation1 = Text("右に「1」", font_size=24, color=YELLOW)
        explanation1.move_to([2, -0.5, 0])
        
        explanation2 = Text("上に「2」", font_size=24, color=YELLOW)
        explanation2.move_to([-1, 1, 0])
        
        # 右方向の矢印とラベル - 座標系に合わせる
        right_arrow = Arrow(plane.c2p(0, 0), plane.c2p(1, 0), color=RED, buff=0)
        right_label = MathTex("1", color=RED).next_to(right_arrow, DOWN, buff=0.1)
        
        # 上方向の矢印とラベル - 座標系に合わせる
        up_arrow = Arrow(plane.c2p(1, 0), plane.c2p(1, 2), color=GREEN, buff=0)
        up_label = MathTex("2", color=GREEN).next_to(up_arrow, RIGHT, buff=0.1)
        
        self.play(
            Write(explanation1),
            Create(right_arrow),
            Write(right_label)
        )
        self.wait(1)
        
        self.play(
            Write(explanation2),
            Create(up_arrow),
            Write(up_label)
        )
        self.wait(1)
        
        # 数学的表記の導入
        math_explanation = Text("これを数字の組で表すと:", font_size=28, color=WHITE)
        math_explanation.move_to([0, -2, 0])
        self.play(Write(math_explanation))
        self.wait(1)
        
        # ベクトルの数学表記
        vector_notation = MathTex(
            r"\boldsymbol{y} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}",
            color=BLUE,
            font_size=48
        )
        vector_notation.move_to([0, -2.8, 0])
        
        self.play(Write(vector_notation))
        self.wait(1)
        
        # 説明テキスト
        # explanation_text = VGroup(
        #     Text("1番目の数字: 横方向の移動", font_size=20, color=RED),
        #     Text("2番目の数字: 縦方向の移動", font_size=20, color=GREEN)
        # ).arrange(DOWN, aligned_edge=LEFT)
        # explanation_text.move_to([2.5, -2.5, 0])
        
        # self.play(Write(explanation_text))
        # self.wait(2)
        
        # 最終的な強調
        self.play(
            Indicate(vector),
            Indicate(vector_notation),
            run_time=2
        )
        self.wait(2)
