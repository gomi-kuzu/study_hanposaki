from manim import *

class LinearIndependence(Scene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"
        
        # タイトル
        title = Text("1次独立と1次従属", font_size=36, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)
        
        # === パート1: 1次独立の定義 ===
        subtitle1 = Text("ベクトルの1次独立とは？", font_size=28, color=YELLOW)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.5)
        
        # 定義を表示
        definition1 = VGroup(
            Text("1次独立 = 1次従属でない", color=WHITE, font_size=24),
            Text("↓", color=YELLOW, font_size=26),
            Text("互いに従属し合っていない", color=GREEN, font_size=26)
        ).arrange(DOWN, buff=0.3)
        definition1.shift(DOWN * 0.5)
        
        self.play(Write(definition1[0]), run_time=0.7)
        self.wait(0.6)
        self.play(Write(definition1[1]), run_time=0.4)
        self.wait(0.3)
        self.play(Write(definition1[2]), run_time=0.7)
        self.wait(1.0)
        
        self.play(FadeOut(definition1), FadeOut(subtitle1))
        self.wait(0.3)
        
        # === パート2: 1次従属の説明 ===
        subtitle2 = Text("1次従属はベクトルの”組”に対する概念", font_size=28, color=RED)
        subtitle2.next_to(title, DOWN*0.8)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)
        
        # 座標軸を設定
        axes = Axes(
            x_range=[-2, 5, 1],
            y_range=[-1, 4, 1],
            x_length=6,
            y_length=5,
            axis_config={"color": GRAY}
        )
        axes.shift(LEFT * 3)
        
        # 座標軸ラベル
        x_label = Text("X", color=RED, font_size=18)
        y_label = Text("Y", color=GREEN, font_size=18)
        x_label.next_to(axes.get_x_axis().get_end(), DOWN)
        y_label.next_to(axes.get_y_axis().get_end(), LEFT)
        
        self.play(Create(axes), Write(x_label), Write(y_label), run_time=0.7)
        self.wait(0.4)
        
        # === パート3: 従属の例1 - a₁とa₃は従属 ===
        # self.play(FadeOut(subtitle2))
        subtitle3 = Text("例1: a₁ = [0, 1], a₃ = [0, -1]", font_size=26, color=YELLOW)
        subtitle3.next_to(title, DOWN*2.5)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.4)
        
        # ベクトルa₁とa₃を表示
        a1_vec = Vector(
            axes.c2p(0, 1) - axes.c2p(0, 0),
            color=BLUE,
            stroke_width=5
        ).shift(axes.c2p(0, 0))
        
        a1_label = MathTex(r"\mathbf{a}_1", color=BLUE, font_size=24)
        a1_label.next_to(a1_vec.get_end(), LEFT, buff=0.2)
        
        a3_vec = Vector(
            axes.c2p(0, -1) - axes.c2p(0, 0),
            color=RED,
            stroke_width=5
        ).shift(axes.c2p(0, 0))
        
        a3_label = MathTex(r"\mathbf{a}_3", color=RED, font_size=24)
        a3_label.next_to(a3_vec.get_end(), RIGHT, buff=0.2)
        
        self.play(
            Create(a1_vec), Write(a1_label),
            Create(a3_vec), Write(a3_label),
            run_time=0.7
        )
        self.wait(0.5)
        
        # 右側に説明を表示
        explanation1 = VGroup(
            MathTex(r"\mathbf{a}_1 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}", color=BLUE, font_size=28),
            MathTex(r"\mathbf{a}_3 = \begin{bmatrix} 0 \\ -1 \end{bmatrix}", color=RED, font_size=28),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        explanation1.to_edge(RIGHT).shift(LEFT * 2.0 + UP * 1.5)
        
        self.play(Write(explanation1), run_time=0.7)
        self.wait(0.5)
        
        # a₁をa₃で表現
        relation1 = MathTex(
            r"\mathbf{a}_1 = -1 \cdot \mathbf{a}_3",
            color=YELLOW,
            font_size=30
        )
        relation1.next_to(explanation1, DOWN, buff=0.5)
        self.play(Write(relation1), run_time=0.7)
        self.wait(0.6)
        
        # 逆も成り立つ
        relation2 = MathTex(
            r"\mathbf{a}_3 = -1 \cdot \mathbf{a}_1",
            color=YELLOW,
            font_size=30
        )
        relation2.next_to(relation1, DOWN, buff=0.3)
        self.play(Write(relation2), run_time=0.7)
        self.wait(0.6)
        
        # 結論
        conclusion1 = Text("互いに従属し合っている！", color=GREEN, font_size=24)
        conclusion1.next_to(relation2, DOWN, buff=0.5)
        self.play(Write(conclusion1), run_time=0.6)
        self.wait(1.0)
        
        # クリーンアップ
        self.play(
            FadeOut(a1_vec), FadeOut(a1_label),
            FadeOut(a3_vec), FadeOut(a3_label),
            FadeOut(explanation1), FadeOut(relation1),
            FadeOut(relation2), FadeOut(conclusion1),
            FadeOut(subtitle3)
        )
        self.wait(0.3)
        
        # === パート4: 従属の例2 - a₄は従属 ===
        subtitle4 = Text("例2: a₁ = [0, 1], a₂ = [1, 0], a₄ = [1, 2]", font_size=26, color=YELLOW)
        subtitle4.next_to(title, DOWN*2.5)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.4)
        
        # ベクトルa₄とa₅を表示
        a1_vec = Vector(
            axes.c2p(0, 1) - axes.c2p(0, 0),
            color=BLUE,
            stroke_width=5
        ).shift(axes.c2p(0, 0))
        
        a1_label = MathTex(r"\mathbf{a}_1", color=BLUE, font_size=24)
        a1_label.next_to(a1_vec.get_end(), LEFT, buff=0.2)
        
        a2_vec = Vector(
            axes.c2p(1, 0) - axes.c2p(0, 0),
            color=GREEN,
            stroke_width=5
        ).shift(axes.c2p(0, 0))

        a2_label = MathTex(r"\mathbf{a}_2", color=GREEN, font_size=24)
        a2_label.next_to(a2_vec.get_end(), DOWN, buff=0.2)


        a4_vec = Vector(
            axes.c2p(1, 2) - axes.c2p(0, 0),
            color=PURPLE,
            stroke_width=5
        ).shift(axes.c2p(0, 0))
        
        a4_label = MathTex(r"\mathbf{a}_4", color=PURPLE, font_size=24)
        a4_label.next_to(a4_vec.get_end(), RIGHT, buff=0.2)
        
        
        self.play(
            Create(a1_vec), Write(a1_label),
            Create(a2_vec), Write(a2_label),
            Create(a4_vec), Write(a4_label),
            run_time=0.7
        )
        self.wait(0.5)
        
        # 右側に説明を表示
        explanation2 = VGroup(
            MathTex(r"\mathbf{a}_1 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}", color=BLUE, font_size=28),
            MathTex(r"\mathbf{a}_2 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}", color=GREEN, font_size=28),
            MathTex(r"\mathbf{a}_4 = \begin{bmatrix} 1 \\ 2 \end{bmatrix}", color=PURPLE, font_size=28),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        explanation2.to_edge(RIGHT).shift(LEFT * 2.0 + UP * 1.5)
        
        self.play(Write(explanation2), run_time=0.7)
        self.wait(0.5)
        
        # これらも「組」として従属関係がある
        relation3_label = Text("これらの組は1次従属？", color=YELLOW, font_size=24)
        relation3_label.next_to(explanation2, DOWN, buff=0.5)
        self.play(Write(relation3_label), run_time=0.6)
        self.wait(0.5)
        
        # a₄をa₁とa₂で表現
        relation3 = MathTex(
            r"\mathbf{a}_4 = 2\mathbf{a}_1 + \mathbf{a}_2",
            color=YELLOW,
            font_size=28
        )
        relation3.next_to(relation3_label, DOWN, buff=0.3)
        self.play(Write(relation3), run_time=0.7)
        self.wait(0.6)
        
        
        # 結論
        conclusion2 = Text("a₁, a₂でa₄が表現できる", color=GREEN, font_size=24)
        conclusion2_2 = Text("→右左辺間の移項でお互い言えること!", color=RED, font_size=24)
        conclusion2_group = VGroup(conclusion2, conclusion2_2).arrange(DOWN, buff=0.2)
        conclusion2_group.next_to(relation3, DOWN, buff=0.5)
        self.play(Write(conclusion2), run_time=0.6)
        self.wait(0.4)
        self.play(Write(conclusion2_2), run_time=0.6)
        self.wait(1.0)
        
        # クリーンアップ
        self.play(
            FadeOut(a4_vec), FadeOut(a4_label),
            FadeOut(a1_vec), FadeOut(a1_label),
            FadeOut(a2_vec), FadeOut(a2_label),
            FadeOut(explanation2), FadeOut(relation3_label),
            FadeOut(relation3), 
            FadeOut(conclusion2_group),
            FadeOut(subtitle4)
        )
        self.wait(0.3)
        
        # === パート5: 1次独立の例 ===
        subtitle5 = Text("例3: a₁ = [0, 1], a₂ = [1, 0]", font_size=26, color=YELLOW)
        subtitle5.next_to(title, DOWN*2.5)
        self.play(Write(subtitle5), run_time=0.6)
        self.wait(0.4)
        
        # ベクトルa₁とa₂を表示
        a1_vec3 = Vector(
            axes.c2p(0, 1) - axes.c2p(0, 0),
            color=BLUE,
            stroke_width=5
        ).shift(axes.c2p(0, 0))
        
        a1_label3 = MathTex(r"\mathbf{a}_1", color=BLUE, font_size=24)
        a1_label3.next_to(a1_vec3.get_end(), LEFT, buff=0.2)
        
        a2_vec2 = Vector(
            axes.c2p(1, 0) - axes.c2p(0, 0),
            color=GREEN,
            stroke_width=5
        ).shift(axes.c2p(0, 0))
        
        a2_label2 = MathTex(r"\mathbf{a}_2", color=GREEN, font_size=24)
        a2_label2.next_to(a2_vec2.get_end(), DOWN, buff=0.2)
        
        self.play(
            Create(a1_vec3), Write(a1_label3),
            Create(a2_vec2), Write(a2_label2),
            run_time=0.7
        )
        self.wait(0.5)
        
        # 右側に説明を表示
        explanation3 = VGroup(
            MathTex(r"\mathbf{a}_1 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}", color=BLUE, font_size=28),
            MathTex(r"\mathbf{a}_2 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}", color=GREEN, font_size=28),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        explanation3.to_edge(RIGHT).shift(LEFT * 2.0 + UP * 1.5)
        
        self.play(Write(explanation3), run_time=0.7)
        self.wait(0.5)
        
        # 互いに表現できない
        question1 = MathTex(
            r"\mathbf{a}_1 = c \cdot \mathbf{a}_2 \text{ ?}",
            color=YELLOW,
            font_size=28
        )
        question1.next_to(explanation3, DOWN, buff=0.5)
        self.play(Write(question1), run_time=0.7)
        self.wait(0.5)
        
        answer1 = MathTex(
            r"\begin{bmatrix} 0 \\ 1 \end{bmatrix} = c \begin{bmatrix} 1 \\ 0 \end{bmatrix}",
            color=WHITE,
            font_size=26
        )
        answer1.next_to(question1, DOWN, buff=0.3)
        self.play(Write(answer1), run_time=0.7)
        self.wait(0.5)
        
        result1 = Text("不可能！", color=RED, font_size=30, weight=BOLD)
        result1.next_to(answer1, DOWN, buff=0.4)
        self.play(Write(result1), run_time=0.6)
        self.wait(0.8)
        
        # 結論
        conclusion3 = VGroup(
            Text("互いに表現できない", color=GREEN, font_size=24),
            Text("↓", color=YELLOW, font_size=22),
            Text("1次独立！", color=GREEN, font_size=28, weight=BOLD)
        ).arrange(DOWN, buff=0.2)
        conclusion3.next_to(result1, DOWN, buff=0.5)
        
        self.play(Write(conclusion3[0]), run_time=0.6)
        self.wait(0.4)
        self.play(Write(conclusion3[1]), run_time=0.3)
        self.wait(0.3)
        self.play(Write(conclusion3[2]), run_time=0.7)
        self.wait(1.2)
        
        # クリーンアップ
        self.play(
            FadeOut(subtitle2),
            FadeOut(a1_vec3), FadeOut(a1_label3),
            FadeOut(a2_vec2), FadeOut(a2_label2),
            FadeOut(explanation3), FadeOut(question1),
            FadeOut(answer1), FadeOut(result1),
            FadeOut(conclusion3), FadeOut(subtitle5),
            FadeOut(axes), FadeOut(x_label), FadeOut(y_label),
        )
        # === パート6: まとめ ===
        subtitle6 = Text("まとめ", font_size=36, color=GREEN)
        subtitle6.next_to(title, DOWN)
        self.play(Write(subtitle6), run_time=0.6)
        self.wait(0.5)
        
        summary = VGroup(
            Text("1. 1次従属はベクトルの「組」に対する概念", color=WHITE, font_size=30),
            Text("2. 互いに他のベクトルで表現できる", color=WHITE, font_size=30),
            Text("   → 1次従属", color=YELLOW, font_size=28),
            Text("3. 互いに他のベクトルで表現できない", color=WHITE, font_size=30),
            Text("   → 1次独立", color=GREEN, font_size=28),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        summary.shift(DOWN * 0.5)
        
        for item in summary:
            self.play(Write(item), run_time=0.6)
            self.wait(0.4)
        
        self.wait(1.5)
        

