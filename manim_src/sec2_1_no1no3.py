from manim import *

class BasisConcept(ThreeDScene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"
        
        # タイトル
        title = Text("基底とは何か？", font_size=36, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)
        
        # === パート1: 基底の定義 ===
        subtitle1 = Text("基底の定義", font_size=28, color=YELLOW)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.5)
        
        # 定義を表示
        definition1 = VGroup(
            Text("基底 = 空間を表現するのに", color=WHITE, font_size=26),
            Text("過不足ないベクトルの組", color=WHITE, font_size=26),
            Text("↓", color=YELLOW, font_size=22),
            Text("ポイントは必要十分であること！", color=GREEN, font_size=28, weight=BOLD)
        ).arrange(DOWN, buff=0.3)
        definition1.shift(DOWN * 0.5)
        
        self.play(Write(definition1[0]), run_time=0.7)
        self.wait(0.4)
        self.play(Write(definition1[1]), run_time=0.7)
        self.wait(0.5)
        self.play(Write(definition1[2]), run_time=0.4)
        self.wait(0.3)
        self.play(Write(definition1[3]), run_time=0.7)
        self.wait(1.0)
        
        self.play(FadeOut(definition1), FadeOut(subtitle1))
        self.wait(0.3)
        
        # === パート2: 2次元空間の座標軸 ===
        subtitle2 = Text("2次元空間での例", font_size=28, color=YELLOW)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)
        
        # 座標軸を設定
        axes = Axes(
            x_range=[-1, 4, 1],
            y_range=[-1, 4, 1],
            x_length=5,
            y_length=5,
            axis_config={"color": GRAY}
        )
        axes.shift(LEFT * 3.5)
        
        # 座標軸ラベル
        x_label = Text("X", color=RED, font_size=18)
        y_label = Text("Y", color=GREEN, font_size=18)
        x_label.next_to(axes.get_x_axis().get_end(), DOWN)
        y_label.next_to(axes.get_y_axis().get_end(), LEFT)
        
        self.play(Create(axes), Write(x_label), Write(y_label), run_time=0.7)
        self.wait(0.4)
        
        # === パート3: 不足例1 - ベクトル1本のみ ===
        self.play(FadeOut(subtitle2))
        subtitle3 = Text("例1: 不足 (1本のみ)", font_size=26, color=RED)
        subtitle3.next_to(title, DOWN)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.4)
        
        # ベクトル1本
        v1 = Vector(
            axes.c2p(1, 2) - axes.c2p(0, 0),
            color=BLUE,
            stroke_width=5
        ).shift(axes.c2p(0, 0))
        
        v1_label = MathTex(r"\mathbf{v}_1", color=BLUE, font_size=24)
        v1_label.next_to(v1.get_end(), RIGHT, buff=0.2)
        
        self.play(Create(v1), Write(v1_label), run_time=0.7)
        self.wait(0.5)
        
        # 右側に説明
        explanation1_part1 = VGroup(
            Text("ベクトル: 1本", color=WHITE, font_size=24),
            Text("2次元空間には不足", color=RED, font_size=24),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        explanation1_part1.to_edge(RIGHT).shift(LEFT * 2.0 + UP * 1.5)
        
        explanation1_part2 = VGroup(
            Text("すべての点を", color=YELLOW, font_size=22),
            Text("表現できない", color=YELLOW, font_size=22),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        explanation1_part2.to_edge(RIGHT).shift(LEFT * 2.0 + DOWN * 0.5)
        
        for item in explanation1_part1:
            self.play(Write(item), run_time=0.6)
            self.wait(0.3)
        
        for item in explanation1_part2:
            self.play(Write(item), run_time=0.6)
            self.wait(0.3)
        
        self.wait(0.8)
        
        # クリーンアップ
        self.play(
            FadeOut(v1), FadeOut(v1_label),
            FadeOut(explanation1_part1), FadeOut(explanation1_part2), FadeOut(subtitle3)
        )
        self.wait(0.3)
        
        # === パート4: 不足例2 - 2本だが従属 ===
        subtitle4 = Text("例2: 不足 (2本だが1次従属)", font_size=26, color=RED)
        subtitle4.next_to(title, DOWN)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.4)
        
        # 従属な2本のベクトル
        v2 = Vector(
            axes.c2p(1, 2) - axes.c2p(0, 0),
            color=BLUE,
            stroke_width=5
        ).shift(axes.c2p(0, 0))
        
        v2_label = MathTex(r"\mathbf{v}_1", color=BLUE, font_size=24)
        v2_label.next_to(v2.get_end(), RIGHT, buff=0.2)
        
        v3 = Vector(
            axes.c2p(2, 4) - axes.c2p(0, 0),
            color=PURPLE,
            stroke_width=5
        ).shift(axes.c2p(0, 0))
        
        v3_label = MathTex(r"\mathbf{v}_2", color=PURPLE, font_size=24)
        v3_label.next_to(v3.get_end(), RIGHT, buff=0.2)
        
        self.play(
            Create(v2), Write(v2_label),
            Create(v3), Write(v3_label),
            run_time=0.7
        )
        self.wait(0.5)
        
        # 右側に説明
        explanation2_part1 = VGroup(
            Text("ベクトル: 2本", color=WHITE, font_size=24),
            MathTex(r"\mathbf{v}_2 = 2\mathbf{v}_1", color=YELLOW, font_size=26),
            Text("1次従属", color=RED, font_size=24),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        explanation2_part1.to_edge(RIGHT).shift(LEFT * 2.0 + UP * 1.5)
        
        explanation2_part2 = VGroup(
            Text("実質1本と同じ", color=YELLOW, font_size=22),
            Text("2次元空間には不足", color=RED, font_size=22),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        explanation2_part2.to_edge(RIGHT).shift(LEFT * 2.0 + DOWN * 0.5)
        
        for item in explanation2_part1:
            if isinstance(item, MathTex) or (hasattr(item, 'text') and item.text != ""):
                self.play(Write(item), run_time=0.6)
                self.wait(0.3)
        
        for item in explanation2_part2:
            self.play(Write(item), run_time=0.6)
            self.wait(0.3)
        
        self.wait(0.8)
        
        # クリーンアップ
        self.play(
            FadeOut(v2), FadeOut(v2_label),
            FadeOut(v3), FadeOut(v3_label),
            FadeOut(explanation2_part1), FadeOut(explanation2_part2), FadeOut(subtitle4)
        )
        self.wait(0.3)
        
        # === パート5: 過不足ない例 - 2本で独立 ===
        subtitle5 = Text("例3: 過不足ない (基底！)", font_size=26, color=GREEN)
        subtitle5.next_to(title, DOWN)
        self.play(Write(subtitle5), run_time=0.6)
        self.wait(0.4)
        
        # 独立な2本のベクトル
        e1 = Vector(
            axes.c2p(1, 0) - axes.c2p(0, 0),
            color=BLUE,
            stroke_width=6
        ).shift(axes.c2p(0, 0))
        
        e1_label = MathTex(r"\mathbf{e}_1", color=BLUE, font_size=26)
        e1_label.next_to(e1.get_end(), DOWN, buff=0.2)
        
        e2 = Vector(
            axes.c2p(0, 1) - axes.c2p(0, 0),
            color=GREEN,
            stroke_width=6
        ).shift(axes.c2p(0, 0))
        
        e2_label = MathTex(r"\mathbf{e}_2", color=GREEN, font_size=26)
        e2_label.next_to(e2.get_end(), LEFT, buff=0.2)
        
        self.play(
            Create(e1), Write(e1_label),
            Create(e2), Write(e2_label),
            run_time=0.7
        )
        self.wait(0.5)
        
        # 右側に説明
        explanation3_part1 = VGroup(
            Text("ベクトル: 2本", color=WHITE, font_size=24),
            Text("1次独立", color=GREEN, font_size=24),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        explanation3_part1.to_edge(RIGHT).shift(LEFT * 2.0 + UP * 1.8)
        
        explanation3_part2 = VGroup(
            Text("任意の点を表現可能", color=GREEN, font_size=22),
            MathTex(r"\mathbf{p} = a\mathbf{e}_1 + b\mathbf{e}_2", color=YELLOW, font_size=24),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        explanation3_part2.to_edge(RIGHT).shift(LEFT * 2.0 + UP * 0.2)
        
        explanation3_part3 = VGroup(
            Text("これが基底！", color=GREEN, font_size=28, weight=BOLD),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        explanation3_part3.to_edge(RIGHT).shift(LEFT * 2.0 + DOWN * 1.2)
        
        for item in explanation3_part1:
            self.play(Write(item), run_time=0.6)
            self.wait(0.3)
        
        for item in explanation3_part2:
            if isinstance(item, MathTex) or (hasattr(item, 'text') and item.text != ""):
                self.play(Write(item), run_time=0.6)
                self.wait(0.3)
        
        for item in explanation3_part3:
            self.play(Write(item), run_time=0.6)
            self.wait(0.3)
        
        # 任意の点を表現できることを示す
        test_point = Dot(axes.c2p(2, 3), color=YELLOW, radius=0.08)
        test_label = MathTex(r"\mathbf{p}", color=YELLOW, font_size=20)
        test_label.next_to(test_point, UP, buff=0.1)
        
        self.play(Create(test_point), Write(test_label), run_time=0.5)
        self.wait(0.5)
        
        # 2e1を描画
        scaled_e1 = Vector(
            axes.c2p(2, 0) - axes.c2p(0, 0),
            color=BLUE,
            stroke_width=4,
            stroke_opacity=0.6
        ).shift(axes.c2p(0, 0))
        
        # 3e2を2e1の先端から描画
        scaled_e2 = Vector(
            axes.c2p(0, 3) - axes.c2p(0, 0),
            color=GREEN,
            stroke_width=4,
            stroke_opacity=0.6
        ).shift(axes.c2p(2, 0))
        
        self.play(Create(scaled_e1), run_time=0.5)
        self.wait(0.3)
        self.play(Create(scaled_e2), run_time=0.5)
        self.wait(1.0)
        
        # クリーンアップ
        self.play(
            FadeOut(test_point), FadeOut(test_label),
            FadeOut(scaled_e1), FadeOut(scaled_e2)
        )
        self.wait(0.3)
        self.play(
            FadeOut(e1), FadeOut(e1_label),
            FadeOut(e2), FadeOut(e2_label),
            FadeOut(explanation3_part1), FadeOut(explanation3_part2), FadeOut(explanation3_part3), FadeOut(subtitle5)
        )
        self.wait(0.3)
        
        # === パート6: 過剰例 - 3本 ===
        subtitle6 = Text("例4: 過剰 (3本)", font_size=26, color=ORANGE)
        subtitle6.next_to(title, DOWN)
        self.play(Write(subtitle6), run_time=0.6)
        self.wait(0.4)
        
        # 3本のベクトル
        w1 = Vector(
            axes.c2p(1, 0) - axes.c2p(0, 0),
            color=BLUE,
            stroke_width=5
        ).shift(axes.c2p(0, 0))
        
        w1_label = MathTex(r"\mathbf{w}_1", color=BLUE, font_size=24)
        w1_label.next_to(w1.get_end(), DOWN, buff=0.2)
        
        w2 = Vector(
            axes.c2p(0, 1) - axes.c2p(0, 0),
            color=GREEN,
            stroke_width=5
        ).shift(axes.c2p(0, 0))
        
        w2_label = MathTex(r"\mathbf{w}_2", color=GREEN, font_size=24)
        w2_label.next_to(w2.get_end(), LEFT, buff=0.2)
        
        w3 = Vector(
            axes.c2p(1, 1) - axes.c2p(0, 0),
            color=ORANGE,
            stroke_width=5
        ).shift(axes.c2p(0, 0))
        
        w3_label = MathTex(r"\mathbf{w}_3", color=ORANGE, font_size=24)
        w3_label.next_to(w3.get_end(), RIGHT, buff=0.2)
        
        self.play(
            Create(w1), Write(w1_label),
            Create(w2), Write(w2_label),
            Create(w3), Write(w3_label),
            run_time=0.7
        )
        self.wait(0.5)
        
        # 右側に説明
        explanation4_part1 = VGroup(
            Text("ベクトル: 3本", color=WHITE, font_size=24),
            MathTex(r"\mathbf{w}_3 = \mathbf{w}_1 + \mathbf{w}_2", color=YELLOW, font_size=24),
            Text("1次従属", color=RED, font_size=24),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        explanation4_part1.to_edge(RIGHT).shift(LEFT * 2.0 + UP * 1.5)
        
        explanation4_part2 = VGroup(
            Text("2次元には過剰", color=ORANGE, font_size=22),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        explanation4_part2.to_edge(RIGHT).shift(LEFT * 2.0 + DOWN * 0.5)
        
        for item in explanation4_part1:
            if isinstance(item, MathTex) or (hasattr(item, 'text') and item.text != ""):
                self.play(Write(item), run_time=0.6)
                self.wait(0.3)
        
        for item in explanation4_part2:
            self.play(Write(item), run_time=0.6)
            self.wait(0.3)
        
        self.wait(0.8)
        
        # クリーンアップ
        self.play(
            FadeOut(w1), FadeOut(w1_label),
            FadeOut(w2), FadeOut(w2_label),
            FadeOut(w3), FadeOut(w3_label),
            FadeOut(explanation4_part1), FadeOut(explanation4_part2), FadeOut(subtitle6),
            FadeOut(axes), FadeOut(x_label), FadeOut(y_label)
        )
        self.wait(0.5)
        
        # === パート7: 次元が重要 ===
        subtitle7 = Text("重要: 空間の次元", font_size=32, color=YELLOW)
        subtitle7.next_to(title, DOWN)
        self.play(Write(subtitle7), run_time=0.6)
        self.wait(0.5)
        
        dimension_note_part1 = VGroup(
            Text("基底の本数 = 空間の次元", color=WHITE, font_size=26),
        ).arrange(DOWN, buff=0.5)
        dimension_note_part1.shift(UP * 0.8)
        
        dimension_note_part2 = VGroup(
            Text("2次元空間 → 基底は2本", color=GREEN, font_size=24),
            Text("3次元空間 → 基底は3本", color=GREEN, font_size=24),
        ).arrange(DOWN, buff=0.5)
        dimension_note_part2.shift(DOWN * 1.0)
        
        for item in dimension_note_part1:
            self.play(Write(item), run_time=0.7)
            self.wait(0.4)
        
        for item in dimension_note_part2:
            self.play(Write(item), run_time=0.7)
            self.wait(0.4)
        
        self.wait(1.0)
        self.play(FadeOut(dimension_note_part1), FadeOut(dimension_note_part2))
        self.wait(0.3)
        
        # === パート8: 3次元空間での部分空間の基底 ===
        # self.play(FadeOut(subtitle7))
        subtitle8 = Text("注目している空間の次元に注目", font_size=28, color=YELLOW)
        subtitle8.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle8)
        self.play(Write(subtitle8), run_time=0.6)
        self.wait(0.5)
        
        # 3D空間に切り替え(疑似3D表現)
        # 3次元座標軸
        axes_3d = ThreeDAxes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            z_range=[-2, 2, 1],
            x_length=5,
            y_length=5,
            z_length=5,
            axis_config={"color": GRAY}
        )
        axes_3d.shift(LEFT * -4.5 - DOWN * 0.8)
        
        # カメラの初期設定
        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)
        
        self.play(Create(axes_3d), run_time=0.8)
        self.wait(0.5)
        
        # xy平面(部分空間)を表示
        plane = Surface(
            lambda u, v: axes_3d.c2p(u, v, 0),
            u_range=[-1.5, 1.5],
            v_range=[-1.5, 1.5],
            resolution=(10, 10),
            fill_opacity=0.4,
            fill_color=BLUE
        )
        
        self.play(Create(plane), run_time=0.8)
        self.wait(0.5)
        
        # xy平面上の基底ベクトル
        basis_1 = Arrow3D(
            start=axes_3d.c2p(0, 0, 0),
            end=axes_3d.c2p(1, 0, 0),
            color=RED,
            thickness=0.02
        )
        
        basis_2 = Arrow3D(
            start=axes_3d.c2p(0, 0, 0),
            end=axes_3d.c2p(0, 1, 0),
            color=GREEN,
            thickness=0.02
        )
        
        basis_1_label = MathTex(r"\mathbf{b}_1", color=RED, font_size=24)
        basis_1_label.move_to(axes_3d.c2p(1.3, 0, 0))
        
        basis_2_label = MathTex(r"\mathbf{b}_2", color=GREEN, font_size=24)
        basis_2_label.move_to(axes_3d.c2p(0, 1.3, 0))
        
        self.play(
            Create(basis_1), Write(basis_1_label),
            Create(basis_2), Write(basis_2_label),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 右側に説明
        explanation5_part1 = VGroup(
            Text("3次元空間内の部分空間", color=WHITE, font_size=24),
            Text("（xy平面）", color=WHITE, font_size=24),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        explanation5_part1.to_edge(RIGHT).shift(LEFT * 1.5 + UP * 1.8)
        self.add_fixed_in_frame_mobjects(explanation5_part1)
        
        explanation5_part2 = VGroup(
            Text("この平面の基底:", color=YELLOW, font_size=22),
            MathTex(r"\mathbf{b}_1, \mathbf{b}_2", color=GREEN, font_size=26),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        explanation5_part2.to_edge(RIGHT).shift(LEFT * 1.5 + UP * 0.3)
        self.add_fixed_in_frame_mobjects(explanation5_part2)
        
        explanation5_part3 = VGroup(
            Text("2本で十分！", color=GREEN, font_size=26, weight=BOLD),
            Text("(平面は2次元)", color=WHITE, font_size=20),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        explanation5_part3.to_edge(RIGHT).shift(LEFT * 1.5 + DOWN * 1.2)
        self.add_fixed_in_frame_mobjects(explanation5_part3)
        
        for item in explanation5_part1:
            self.play(Write(item), run_time=0.6)
            self.wait(0.3)
        
        for item in explanation5_part2:
            if isinstance(item, MathTex) or (hasattr(item, 'text') and item.text != ""):
                self.play(Write(item), run_time=0.6)
                self.wait(0.3)
        
        # カメラを回転させて平面を様々な角度から見せる
        self.wait(0.5)
        
        # 上から見る（真上に近い角度）
        self.move_camera(phi=85 * DEGREES, theta=45 * DEGREES, run_time=2.0)
        self.wait(1.0)
        
        # # 横から見る（平面が縦に見える）
        # self.move_camera(phi=0 * DEGREES, theta=0 * DEGREES, run_time=2.0)
        # self.wait(1.0)
        
        # 斜めから見る（立体的に見える角度）
        self.move_camera(phi=70 * DEGREES, theta=-30 * DEGREES, run_time=2.0)
        self.wait(1.0)
        
        # 最後の説明を表示
        for item in explanation5_part3:
            self.play(Write(item), run_time=0.6)
            self.wait(0.3)
        
        self.wait(1.5)
        
        # カメラを元の角度に戻す
        self.move_camera(phi=60 * DEGREES, theta=45 * DEGREES, run_time=1.5)
        self.wait(0.5)
        
        # クリーンアップ
        self.play(
            FadeOut(axes_3d), FadeOut(plane),
            FadeOut(basis_1), FadeOut(basis_1_label),
            FadeOut(basis_2), FadeOut(basis_2_label),
            FadeOut(explanation5_part1), FadeOut(explanation5_part2), FadeOut(explanation5_part3), FadeOut(subtitle8)
        )
        self.wait(0.3)
        
        # カメラを2D表示に戻す
        self.set_camera_orientation(phi=0 * DEGREES, theta=0 * DEGREES)
        
        # === パート9: まとめ ===
        subtitle9 = Text("まとめ", font_size=32, color=GREEN)
        subtitle9.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle9)
        self.play(Write(subtitle9), run_time=0.6)
        self.wait(0.5)
        
        summary = VGroup(
            Text("1. 基底 = 過不足ないベクトルの組", color=WHITE, font_size=26),
            Text("2. 不足 → すべての点を表現できない", color=RED, font_size=24),
            Text("3. 過剰 → 余分なベクトルがある", color=ORANGE, font_size=24),
            Text("4. 基底の本数 = 注目している空間の次元", color=YELLOW, font_size=24),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        summary.shift(DOWN * 0.2)
        self.add_fixed_in_frame_mobjects(summary)
        
        for item in summary:
            self.play(Write(item), run_time=0.6)
            self.wait(0.4)
        
        self.wait(2.0)
        
        # 最後のクリーンアップ
        self.play(
            FadeOut(summary), FadeOut(subtitle9)
        )
        self.wait(0.5)
