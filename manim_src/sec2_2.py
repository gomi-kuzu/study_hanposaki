from manim import *

class BasisTransformation(ThreeDScene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"
        
        # タイトル
        title = Text("基底が変わると座標が変わる", font_size=44, color=WHITE)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)
        
        # === パート1: 同一ベクトルの導入 ===
        subtitle1 = Text("あるベクトルx = [2, 3]ᵀを考える", font_size=32, color=YELLOW)
        subtitle1.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle1)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.5)
        
        # 座標軸を設定（標準基底用）
        axes1 = Axes(
            x_range=[-1, 4, 1],
            y_range=[-1, 4, 1],
            x_length=4,
            y_length=4,
            axis_config={"color": GRAY}
        )
        axes1.shift(LEFT * 3.5)
        self.add_fixed_in_frame_mobjects(axes1)
        
        # 方眼を追加
        grid = NumberPlane(
            x_range=[-1, 4, 1],
            y_range=[-1, 4, 1],
            x_length=4,
            y_length=4,
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            },
            axis_config={"stroke_opacity": 0}  # 軸は非表示（axesで表示するため）
        )
        grid.shift(LEFT * 3.5)
        self.add_fixed_in_frame_mobjects(grid)
        
        # 座標軸ラベル
        x_label1 = Text("X", color=RED, font_size=22)
        y_label1 = Text("Y", color=GREEN, font_size=22)
        x_label1.next_to(axes1.get_x_axis().get_end(), DOWN)
        y_label1.next_to(axes1.get_y_axis().get_end(), LEFT)
        self.add_fixed_in_frame_mobjects(x_label1, y_label1)
        
        self.play(Create(grid), Create(axes1), Write(x_label1), Write(y_label1), run_time=0.7)
        self.wait(0.4)
        
        # 目標となる白いベクトル x = [2, 3]^T
        target_vector = Vector(
            axes1.c2p(2, 3) - axes1.c2p(0, 0),
            color=WHITE,
            stroke_width=6
        ).shift(axes1.c2p(0, 0))
        self.add_fixed_in_frame_mobjects(target_vector)
        
        target_label = MathTex(r"\mathbf{x} = \begin{bmatrix} 2 \\ 3 \end{bmatrix}", 
                              color=WHITE, font_size=28)
        target_label.next_to(target_vector.get_end(), RIGHT, buff=0.3)
        self.add_fixed_in_frame_mobjects(target_label)
        
        self.play(Create(target_vector), Write(target_label), run_time=0.8)
        self.wait(0.5)
        
        # 右側に説明
        explanation1 = VGroup(
            Text("このベクトルの座標は", color=WHITE, font_size=26),
            Text("基底の取り方で変わる！", color=YELLOW, font_size=26),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        explanation1.to_edge(RIGHT).shift(LEFT * 1.5 + UP * 1.5)
        self.add_fixed_in_frame_mobjects(explanation1)
        
        for item in explanation1:
            self.play(Write(item), run_time=0.6)
            self.wait(0.3)
        
        self.wait(0.8)
        self.play(FadeOut(explanation1), FadeOut(subtitle1))
        self.wait(0.3)
        
        # === パート2: 標準基底での表現 ===
        subtitle2 = Text("基底1: 標準基底", font_size=32, color=BLUE)
        subtitle2.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle2)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)
        
        # 標準基底ベクトル
        e1 = Vector(
            axes1.c2p(1, 0) - axes1.c2p(0, 0),
            color=BLUE,
            stroke_width=5
        ).shift(axes1.c2p(0, 0))
        self.add_fixed_in_frame_mobjects(e1)
        
        e1_label = MathTex(r"\mathbf{e}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}", 
                          color=BLUE, font_size=24)
        e1_label.next_to(e1.get_end(), DOWN, buff=0.2)
        self.add_fixed_in_frame_mobjects(e1_label)
        
        e2 = Vector(
            axes1.c2p(0, 1) - axes1.c2p(0, 0),
            color=GREEN,
            stroke_width=5
        ).shift(axes1.c2p(0, 0))
        self.add_fixed_in_frame_mobjects(e2)
        
        e2_label = MathTex(r"\mathbf{e}_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}", 
                          color=GREEN, font_size=24)
        e2_label.next_to(e2.get_end(), LEFT, buff=0.2)
        self.add_fixed_in_frame_mobjects(e2_label)
        
        self.play(
            Create(e1), Write(e1_label),
            Create(e2), Write(e2_label),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 右側に基底の説明
        basis1_explanation = VGroup(
            Text("基底:", color=WHITE, font_size=26),
            MathTex(r"\mathbf{e}_1, \mathbf{e}_2", color=YELLOW, font_size=30),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        basis1_explanation.to_edge(RIGHT).shift(LEFT * 1.5 + UP * 1.8)
        self.add_fixed_in_frame_mobjects(basis1_explanation)
        
        for item in basis1_explanation:
            if isinstance(item, MathTex) or (hasattr(item, 'text') and item.text != ""):
                self.play(Write(item), run_time=0.6)
                self.wait(0.3)
        
        # ベクトルの分解アニメーション
        decomp_text1 = MathTex(r"\mathbf{x} = 2\mathbf{e}_1 + 3\mathbf{e}_2", 
                              color=YELLOW, font_size=30)
        decomp_text1.to_edge(RIGHT).shift(LEFT * 1.5 + UP * 0.5)
        self.add_fixed_in_frame_mobjects(decomp_text1)
        self.play(Write(decomp_text1), run_time=0.7)
        self.wait(0.5)
        
        # 2*e1を表示（e1を2つ継ぎ足し）
        e1_clone1 = Vector(
            axes1.c2p(1, 0) - axes1.c2p(0, 0),
            color=BLUE,
            stroke_width=4,
            stroke_opacity=0.8
        ).shift(axes1.c2p(0, 0))
        self.add_fixed_in_frame_mobjects(e1_clone1)
        
        e1_clone2 = Vector(
            axes1.c2p(1, 0) - axes1.c2p(0, 0),
            color=BLUE,
            stroke_width=4,
            stroke_opacity=0.8
        ).shift(axes1.c2p(1, 0))
        self.add_fixed_in_frame_mobjects(e1_clone2)
        
        scaled_e1_label = MathTex(r"2\mathbf{e}_1", color=BLUE, font_size=22)
        scaled_e1_label.next_to(axes1.c2p(1, 0), DOWN, buff=0.1)
        self.add_fixed_in_frame_mobjects(scaled_e1_label)
        
        self.play(Create(e1_clone1), run_time=0.4)
        self.play(Create(e1_clone2), Write(scaled_e1_label), run_time=0.6)
        self.wait(0.4)
        
        # 3*e2を2*e1の先端から表示（e2を3つ継ぎ足し）
        e2_clone1 = Vector(
            axes1.c2p(0, 1) - axes1.c2p(0, 0),
            color=GREEN,
            stroke_width=4,
            stroke_opacity=0.8
        ).shift(axes1.c2p(2, 0))
        self.add_fixed_in_frame_mobjects(e2_clone1)
        
        e2_clone2 = Vector(
            axes1.c2p(0, 1) - axes1.c2p(0, 0),
            color=GREEN,
            stroke_width=4,
            stroke_opacity=0.8
        ).shift(axes1.c2p(2, 1))
        self.add_fixed_in_frame_mobjects(e2_clone2)
        
        e2_clone3 = Vector(
            axes1.c2p(0, 1) - axes1.c2p(0, 0),
            color=GREEN,
            stroke_width=4,
            stroke_opacity=0.8
        ).shift(axes1.c2p(2, 2))
        self.add_fixed_in_frame_mobjects(e2_clone3)
        
        scaled_e2_label = MathTex(r"3\mathbf{e}_2", color=GREEN, font_size=22)
        scaled_e2_label.next_to(axes1.c2p(2, 3), RIGHT, buff=0.1)
        self.add_fixed_in_frame_mobjects(scaled_e2_label)
        
        self.play(Create(e2_clone1), run_time=0.4)
        self.play(Create(e2_clone2), run_time=0.4)
        self.play(Create(e2_clone3), Write(scaled_e2_label), run_time=0.4)
        self.wait(0.5)
        
        # 座標の結論
        coord1_result  = VGroup(
            Text("座標：", color=ORANGE, font_size=26),MathTex(r"\begin{bmatrix} 2 \\ 3 \end{bmatrix}", 
                               color=ORANGE, font_size=30))

        for i, item in enumerate(coord1_result):
            item.to_edge(RIGHT).shift(LEFT * 1.2 *(2-i) + DOWN * 0.8)
            self.add_fixed_in_frame_mobjects(item)
            self.play(Write(item), run_time=0.7)
            self.wait(1.0)
        
        # クリーンアップ（標準基底関連）
        self.play(
            FadeOut(e1), FadeOut(e1_label),
            FadeOut(e2), FadeOut(e2_label),
            FadeOut(e1_clone1), FadeOut(e1_clone2), FadeOut(scaled_e1_label),
            FadeOut(e2_clone1), FadeOut(e2_clone2), FadeOut(e2_clone3), FadeOut(scaled_e2_label),
            FadeOut(basis1_explanation), FadeOut(decomp_text1), FadeOut(coord1_result),
            FadeOut(subtitle2)
        )
        self.wait(0.3)
        
        # === パート3: 別の基底での表現 ===
        subtitle3 = Text("基底2: 別の基底", font_size=32, color=PURPLE)
        subtitle3.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle3)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.5)
        
        # 別の基底ベクトル
        b1 = Vector(
            axes1.c2p(1, 1) - axes1.c2p(0, 0),
            color=PURPLE,
            stroke_width=5
        ).shift(axes1.c2p(0, 0))
        self.add_fixed_in_frame_mobjects(b1)
        
        b1_label = MathTex(r"\mathbf{b}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}", 
                          color=PURPLE, font_size=24)
        b1_label.next_to(b1.get_end(), RIGHT, buff=0.2)
        self.add_fixed_in_frame_mobjects(b1_label)
        
        b2 = Vector(
            axes1.c2p(1, -1) - axes1.c2p(0, 0),
            color=ORANGE,
            stroke_width=5
        ).shift(axes1.c2p(0, 0))
        self.add_fixed_in_frame_mobjects(b2)
        
        b2_label = MathTex(r"\mathbf{b}_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}", 
                          color=ORANGE, font_size=24)
        b2_label.next_to(b2.get_end(), RIGHT, buff=0.2)
        self.add_fixed_in_frame_mobjects(b2_label)
        
        self.play(
            Create(b1), Write(b1_label),
            Create(b2), Write(b2_label),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 右側に基底の説明
        basis2_explanation = VGroup(
            Text("新しい基底:", color=WHITE, font_size=26),
            MathTex(r"\mathbf{b}_1, \mathbf{b}_2", color=YELLOW, font_size=28),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        basis2_explanation.to_edge(RIGHT).shift(LEFT * 1.5 + UP * 1.8)
        self.add_fixed_in_frame_mobjects(basis2_explanation)
        
        for item in basis2_explanation:
            if isinstance(item, MathTex) or (hasattr(item, 'text') and item.text != ""):
                self.play(Write(item), run_time=0.6)
                self.wait(0.3)
        
        # 計算過程の説明
        calc_explanation = VGroup(
            Text("新たな基底を使うと…", color=WHITE, font_size=24),
            MathTex(r"\mathbf{x} = \frac{5}{2}\mathbf{b}_1 + \left(-\frac{1}{2}\right)\mathbf{b}_2", 
                   color=YELLOW, font_size=24),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        calc_explanation.to_edge(RIGHT).shift(LEFT * 1.5)
        self.add_fixed_in_frame_mobjects(calc_explanation)
        
        for item in calc_explanation:
            if isinstance(item, MathTex) or (hasattr(item, 'text') and item.text != ""):
                self.play(Write(item), run_time=0.7)
                self.wait(0.4)
        
        # アニメーションで分解を見せる
        # (5/2)*b1を表示（b1を2.5個分継ぎ足し - 近似的に2個 + 0.5個）
        b1_clone1 = Vector(
            axes1.c2p(1, 1) - axes1.c2p(0, 0),
            color=PURPLE,
            stroke_width=4,
            stroke_opacity=0.8
        ).shift(axes1.c2p(0, 0))
        self.add_fixed_in_frame_mobjects(b1_clone1)
        
        b1_clone2 = Vector(
            axes1.c2p(1, 1) - axes1.c2p(0, 0),
            color=PURPLE,
            stroke_width=4,
            stroke_opacity=0.8
        ).shift(axes1.c2p(1, 1))
        self.add_fixed_in_frame_mobjects(b1_clone2)
        
        # 0.5*b1を表示
        b1_half = Vector(
            axes1.c2p(0.5, 0.5) - axes1.c2p(0, 0),
            color=PURPLE,
            stroke_width=4,
            stroke_opacity=0.8
        ).shift(axes1.c2p(2, 2))
        self.add_fixed_in_frame_mobjects(b1_half)
        
        scaled_b1_label = MathTex(r"\frac{5}{2}\mathbf{b}_1", color=PURPLE, font_size=22)
        scaled_b1_label.next_to(axes1.c2p(1.25, 1.25), LEFT, buff=0.1)
        self.add_fixed_in_frame_mobjects(scaled_b1_label)
        
        self.play(Create(b1_clone1), run_time=0.4)
        self.play(Create(b1_clone2), run_time=0.4)
        self.play(Create(b1_half), Write(scaled_b1_label), run_time=0.5)
        self.wait(0.5)
        
        # (-1/2)*b2を(5/2)*b1の先端から表示
        b2_half_negative = Vector(
            axes1.c2p(-0.5, 0.5) - axes1.c2p(0, 0),
            color=ORANGE,
            stroke_width=4,
            stroke_opacity=0.8
        ).shift(axes1.c2p(2.5, 2.5))
        self.add_fixed_in_frame_mobjects(b2_half_negative)
        
        scaled_b2_label = MathTex(r"-\frac{1}{2}\mathbf{b}_2", color=ORANGE, font_size=22)
        scaled_b2_label.next_to(axes1.c2p(2, 3), DOWN, buff=0.1)
        self.add_fixed_in_frame_mobjects(scaled_b2_label)
        
        self.play(Create(b2_half_negative), Write(scaled_b2_label), run_time=0.7)
        self.wait(0.5)
        
        # 座標の結論
        coord2_result = VGroup(
            Text("座標：", color=ORANGE, font_size=26),MathTex(r"\begin{bmatrix} \frac{5}{2} \\ -\frac{1}{2} \end{bmatrix}", 
                               color=ORANGE, font_size=30))
        for i, item in enumerate(coord2_result):
            item.to_edge(RIGHT).shift(LEFT * 1.2*(2-i) + DOWN * 1.5)
            self.add_fixed_in_frame_mobjects(item)
            self.play(Write(item), run_time=0.7)
            self.wait(1.0)
        
        # 同じベクトルであることを強調
        same_vector_text = Text("同じベクトルなのに座標が違う！", color=RED, font_size=28, weight=BOLD)
        same_vector_text.to_edge(RIGHT).shift(LEFT * 1.5 + DOWN * 2.5)
        self.add_fixed_in_frame_mobjects(same_vector_text)
        self.play(Write(same_vector_text), run_time=0.6)
        
        # 白いベクトルを点滅させて強調
        self.play(
            target_vector.animate.set_stroke(color=YELLOW, width=8),
            run_time=0.3
        )
        self.play(
            target_vector.animate.set_stroke(color=WHITE, width=6),
            run_time=0.3
        )
        self.play(
            target_vector.animate.set_stroke(color=YELLOW, width=8),
            run_time=0.3
        )
        self.play(
            target_vector.animate.set_stroke(color=WHITE, width=6),
            run_time=0.3
        )
        
        self.wait(1.0)
        
        # クリーンアップ（別の基底関連）
        self.play(
            FadeOut(b1), FadeOut(b1_label),
            FadeOut(b2), FadeOut(b2_label),
            FadeOut(b1_clone1), FadeOut(b1_clone2), FadeOut(b1_half), FadeOut(scaled_b1_label),
            FadeOut(b2_half_negative), FadeOut(scaled_b2_label),
            FadeOut(basis2_explanation), FadeOut(calc_explanation), 
            FadeOut(coord2_result), FadeOut(same_vector_text),
            FadeOut(subtitle3)
        )
        self.wait(0.3)
        
        # === パート4: さらに別の基底 ===
        subtitle4 = Text("基底3: さらに別の基底", font_size=32, color=RED)
        subtitle4.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle4)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.5)
        
        # さらに別の基底ベクトル
        c1 = Vector(
            axes1.c2p(2, 0) - axes1.c2p(0, 0),
            color=RED,
            stroke_width=5
        ).shift(axes1.c2p(0, 0))
        self.add_fixed_in_frame_mobjects(c1)
        
        c1_label = MathTex(r"\mathbf{c}_1 = \begin{bmatrix} 2 \\ 0 \end{bmatrix}", 
                          color=RED, font_size=24)
        c1_label.next_to(c1.get_end(), DOWN, buff=0.2)
        self.add_fixed_in_frame_mobjects(c1_label)
        
        c2 = Vector(
            axes1.c2p(0, 3) - axes1.c2p(0, 0),
            color=PINK,
            stroke_width=5
        ).shift(axes1.c2p(0, 0))
        self.add_fixed_in_frame_mobjects(c2)
        
        c2_label = MathTex(r"\mathbf{c}_2 = \begin{bmatrix} 0 \\ 3 \end{bmatrix}", 
                          color=PINK, font_size=24)
        c2_label.next_to(c2.get_end(), LEFT, buff=0.2)
        self.add_fixed_in_frame_mobjects(c2_label)
        
        self.play(
            Create(c1), Write(c1_label),
            Create(c2), Write(c2_label),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 右側に基底の説明
        basis3_explanation = VGroup(
            Text("3つ目の基底:", color=WHITE, font_size=26),
            MathTex(r"\mathbf{c}_1, \mathbf{c}_2", color=YELLOW, font_size=28),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        basis3_explanation.to_edge(RIGHT).shift(LEFT * 1.5 + UP * 1.8)
        self.add_fixed_in_frame_mobjects(basis3_explanation)
        
        for item in basis3_explanation:
            if isinstance(item, MathTex) or (hasattr(item, 'text') and item.text != ""):
                self.play(Write(item), run_time=0.6)
                self.wait(0.3)
        
        # 分解の説明
        decomp_text3 = MathTex(r"\mathbf{x} = 1\mathbf{c}_1 + 1\mathbf{c}_2", 
                              color=YELLOW, font_size=28)
        decomp_text3.to_edge(RIGHT).shift(LEFT * 1.5 + UP * 0.5)
        self.add_fixed_in_frame_mobjects(decomp_text3)
        self.play(Write(decomp_text3), run_time=0.7)
        self.wait(0.5)
        
        # 1*c1を表示（そのまま）
        self.play(c1.animate.set_stroke(opacity=0.7), run_time=0.4)
        
        scaled_c1_label = MathTex(r"1\mathbf{c}_1", color=RED, font_size=22)
        scaled_c1_label.next_to(c1.get_center(), DOWN, buff=0.3)
        self.add_fixed_in_frame_mobjects(scaled_c1_label)
        self.play(Write(scaled_c1_label), run_time=0.5)
        self.wait(0.4)
        
        # 1*c2をc1の先端から表示（そのまま）
        scaled_c2 = Vector(
            axes1.c2p(0, 3) - axes1.c2p(0, 0),
            color=PINK,
            stroke_width=4,
            stroke_opacity=0.7
        ).shift(axes1.c2p(2, 0))
        self.add_fixed_in_frame_mobjects(scaled_c2)
        
        scaled_c2_label = MathTex(r"1\mathbf{c}_2", color=PINK, font_size=22)
        scaled_c2_label.next_to(scaled_c2.get_end(), RIGHT, buff=0.1)
        self.add_fixed_in_frame_mobjects(scaled_c2_label)
        
        self.play(Create(scaled_c2), Write(scaled_c2_label), run_time=0.6)
        self.wait(0.5)
        
        # 座標の結論
        coord3_result = VGroup(
            Text("座標：", color=ORANGE, font_size=26),MathTex(r"\begin{bmatrix} 1 \\ 1 \end{bmatrix}", 
                               color=ORANGE, font_size=30))
        for i, item in enumerate(coord3_result):
            item.to_edge(RIGHT).shift(LEFT * 1.2 * (2-i) + DOWN * 0.8)
            self.add_fixed_in_frame_mobjects(item)
            self.play(Write(item), run_time=0.7)
            self.wait(1.0)
        
        # クリーンアップ（3つ目の基底関連）
        self.play(
            FadeOut(c1), FadeOut(c1_label),
            FadeOut(c2), FadeOut(c2_label),
            FadeOut(scaled_c2), FadeOut(scaled_c1_label), FadeOut(scaled_c2_label),
            FadeOut(basis3_explanation), FadeOut(decomp_text3), FadeOut(coord3_result),
            FadeOut(subtitle4), FadeOut(target_vector), FadeOut(target_label),
            FadeOut(axes1), FadeOut(x_label1), FadeOut(y_label1), FadeOut(grid)
        )
        self.wait(0.5)
        
        # === パート5: まとめ ===
        subtitle5 = Text("重要なポイント", font_size=36, color=GREEN)
        subtitle5.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle5)
        self.play(Write(subtitle5), run_time=0.6)
        self.wait(0.5)
        
        summary = VGroup(
            Text("1. 同じベクトルでも基底により座標が変わる", color=WHITE, font_size=28),
            Text("2. 基底の取り方は無数にある", color=YELLOW, font_size=28),
            Text("3. 基底が決まれば座標は一意に決まる", color=GREEN, font_size=28, weight=BOLD),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        summary.shift(DOWN * 0.5)
        self.add_fixed_in_frame_mobjects(summary)
        
        for item in summary:
            self.play(Write(item), run_time=0.7)
            self.wait(0.5)
        
        self.wait(1.5)
        
        # # === パート6: 視覚的強調 ===
        # emphasis_text = Text("基底が決まると座標は一意！", 
        #                     font_size=36, color=RED, weight=BOLD)
        # emphasis_text.shift(DOWN * 2.5)
        # self.add_fixed_in_frame_mobjects(emphasis_text)
        
        # # アニメーション効果付きで強調
        # self.play(
        #     Write(emphasis_text),
        #     emphasis_text.animate.scale(1.2),
        #     run_time=1.0
        # )
        # self.play(
        #     emphasis_text.animate.scale(1.0),
        #     run_time=0.5
        # )
        # self.wait(1.0)
        
        # 最後のクリーンアップ
        # self.play(
        #     FadeOut(summary), FadeOut(subtitle5), FadeOut(emphasis_text), FadeOut(title)
        # )
        # self.wait(0.5)
