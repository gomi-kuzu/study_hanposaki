from manim import *
import numpy as np


class MultiVariableTimeEvolution(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        title = Text("変数がたくさんの時は行列の出番", font_size=36, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.7)

        # ============================================================
        # Part 1: イントロダクション
        # ============================================================
        subtitle1 = Text("前の動画の復習", font_size=28, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)

        review_text = Text(
            "1変数の時間発展は指数関数で記述できた",
            color=WHITE, font_size=26,
        )
        review_text.shift(UP * 1.5)
        self.play(Write(review_text), run_time=0.7)
        self.wait(0.4)

        review_eq = MathTex(
            r"\frac{d}{dt}x(t) = -\alpha x(t) \quad \Rightarrow \quad x(t) = x(0)e^{-\alpha t}",
            color=YELLOW,
            font_size=36,
        )
        review_eq.shift(UP * 0.5)
        self.play(Write(review_eq), run_time=0.8)
        self.wait(0.6)

        question = Text(
            "では、変数が複数ある場合はどうなるのか？",
            color=ORANGE, font_size=28, weight=BOLD,
        )
        question.shift(DOWN * 0.5)
        self.play(Write(question), run_time=0.7)
        self.wait(0.5)

        answer = Text(
            "→ ベクトルと行列を使って表現する！",
            color=GREEN, font_size=28, weight=BOLD,
        )
        answer.shift(DOWN * 1.2)
        self.play(Write(answer), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(review_text), FadeOut(review_eq),
            FadeOut(question), FadeOut(answer), FadeOut(subtitle1),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: マスバネダンパ系の紹介
        # ============================================================
        subtitle2 = Text("具体例：マスバネダンパ系", font_size=28, color=GOLD)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2), run_time=0.6)

        # system_intro = Text(
        #     "横倒しにしたバネ付き重りの運動を考える",
        #     color=WHITE, font_size=26,
        # )
        # system_intro.shift(UP * 2.3)
        # self.play(Write(system_intro), run_time=0.7)
        # self.wait(0.5)

        # ポンチ絵：マスバネダンパ系
        # 左側の壁
        wall = Line(
            start=UP * 1.5 + LEFT * 5,
            end=DOWN * 1.5 + LEFT * 5,
            color=GREY,
            stroke_width=8,
        )
        wall.shift(UP * 0.3)
        
        # 壁の模様（ハッチング）
        hatches = VGroup()
        for i in range(8):
            hatch = Line(
                start=LEFT * 5 + UP * (1.5 - i * 0.375) + LEFT * 0.3,
                end=LEFT * 5 + UP * (1.125 - i * 0.375),
                color=GREY,
                stroke_width=3,
            )
            hatch.shift(UP * 0.3)
            hatches.add(hatch)
        
        # バネ（自然長の位置）
        spring_natural_pos = LEFT * 2
        spring = self.create_spring(LEFT * 5, spring_natural_pos, color=BLUE, num_coils=12)
        spring.shift(UP * 0.3)
        
        # 質量（ボックス）
        mass = Square(side_length=0.8, color=RED, fill_opacity=0.7)
        mass.move_to(spring_natural_pos + RIGHT * 0.4)
        mass.shift(UP * 0.3)
        
        mass_label = MathTex("m", color=WHITE, font_size=34)
        mass_label.move_to(mass.get_center())
        
        # 床（質量の底部に接する位置）
        floor = Line(
            start=LEFT * 6 + DOWN * 0.1,
            end=RIGHT * 2 + DOWN * 0.1,
            color=GREY,
            stroke_width=4,
        )
        
        # 床の模様（ハッチング：摩擦を表現）
        floor_hatches = VGroup()
        for i in range(32):
            hatch = Line(
                start=LEFT * 6 + RIGHT * (i * 0.25) + DOWN * 0.1,
                end=LEFT * 6 + RIGHT * (i * 0.25) + LEFT * 0.15 + DOWN * 0.35,
                color=GREY,
                stroke_width=2,
            )
            floor_hatches.add(hatch)
        
        # ダンパ（摩擦）の記号
        # damper_symbol = VGroup(
        #     Line(mass.get_bottom(), floor.get_center() + UP * 0.02, color=ORANGE, stroke_width=4),
        #     Triangle(color=ORANGE, fill_opacity=0.8).scale(0.15).rotate(PI).move_to(
        #         floor.get_center() + UP * 0.15
        #     ),
        # )
        
        # 座標軸（自然長の位置を原点として配置）
        axis_y_pos = DOWN * 0.5  # 床の少し上
        axis_arrow = Arrow(
            start=LEFT * 5 + axis_y_pos,
            end=RIGHT * 1 + axis_y_pos,
            color=YELLOW,
            buff=0,
            stroke_width=3,
        )
        axis_label = MathTex("x", color=YELLOW, font_size=34)
        axis_label.next_to(axis_arrow, RIGHT, buff=0.1)
        
        # 原点（x=0）のマーク：自然長の位置
        origin_mark = Line(
            spring_natural_pos + axis_y_pos + UP * 0.15,
            spring_natural_pos + axis_y_pos + DOWN * 0.15,
            color=YELLOW,
            stroke_width=4,
        )
        origin_label = MathTex("0", color=YELLOW, font_size=30)
        origin_label.next_to(spring_natural_pos + axis_y_pos, DOWN, buff=0.2)
        
        # 自然長の位置を示すマーク（原点から上に伸びる破線）
        natural_mark = DashedLine(
            spring_natural_pos + axis_y_pos,
            spring_natural_pos + UP * 1.3 + UP * 0.3,
            color=GREEN,
            stroke_width=2,
        )
        natural_label = Text("自然長", color=GREEN, font_size=20)
        natural_label.next_to(natural_mark, UP, buff=0.1)
        
        system_diagram = VGroup(
            wall, hatches, spring, mass, mass_label,
            floor, floor_hatches, axis_arrow, axis_label,
            origin_mark, origin_label, natural_mark, natural_label,
        )
        
        self.play(Create(wall), Create(hatches), run_time=0.5)
        self.play(Create(spring), run_time=0.5)
        self.play(FadeIn(mass), Write(mass_label), run_time=0.5)
        self.play(Create(floor), Create(floor_hatches), run_time=0.5)
        self.play(Create(axis_arrow), Write(axis_label), run_time=0.4)
        self.play(
            Create(origin_mark), Write(origin_label),
            Create(natural_mark), Write(natural_label),
            run_time=0.5
        )
        self.wait(0.8)

        # self.play(FadeOut(system_intro), run_time=0.5)
        # self.wait(0.3)

        # ============================================================
        # Part 3: 運動方程式
        # ============================================================
        subtitle3 = Text("運動方程式を立てる", font_size=28, color=TEAL)
        subtitle3.next_to(title, DOWN)
        self.play(Transform(subtitle2, subtitle3), run_time=0.5)
        self.wait(0.4)

        # 系を上に移動
        self.play(system_diagram.animate.shift(UP * 1.5).scale(0.7), run_time=0.6)
        self.wait(0.3)

        # パラメータの説明
        params = VGroup(
            Text("m：質量", color=RED, font_size=22),
            Text("k：バネ定数", color=BLUE, font_size=22),
            Text("γ：摩擦係数", color=ORANGE, font_size=22),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        params.shift(RIGHT * 3.5 + UP * 2.0)
        
        for param in params:
            self.play(Write(param), run_time=0.4)
            self.wait(0.2)
        
        self.wait(0.5)

        newton_text = Text(
            "ニュートンの運動方程式より",
            color=WHITE, font_size=24,
        )
        newton_text.shift(DOWN * 0.5)
        self.play(Write(newton_text), run_time=0.6)
        self.wait(0.4)

        # 運動方程式
        eq1 = MathTex(
            r"m\frac{d^2}{dt^2}x(t) = -kx(t) - \gamma v(t)",
            color=YELLOW,
            font_size=36,
        )
        eq1.shift(DOWN * 1.3)
        self.play(Write(eq1), run_time=0.8)
        self.wait(0.5)

        # 速度の定義
        eq2 = MathTex(
            r"v(t) = \frac{d}{dt}x(t)",
            color=YELLOW,
            font_size=36,
        )
        eq2.shift(DOWN * 2.1)
        self.play(Write(eq2), run_time=0.7)
        self.wait(0.8)

        explanation = Text(
            "2階微分方程式（加速度の式）",
            color=TEAL, font_size=22,
        )
        explanation.shift(DOWN * 2.9)
        self.play(Write(explanation), run_time=0.6)
        self.wait(1.0)

        self.play(
            FadeOut(newton_text), FadeOut(explanation), FadeOut(params),
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: 連立方程式への変換
        # ============================================================
        subtitle4 = Text("連立微分方程式に書き直す", font_size=28, color=BLUE)
        subtitle4.next_to(title, DOWN)
        self.play(Transform(subtitle2, subtitle4), run_time=0.5)
        self.wait(0.4)

        rewrite_text = Text(
            "変位をx₁、速度をx₂と置き直す",
            color=WHITE, font_size=24,
        )
        rewrite_text.shift(UP * 2.0)
        self.play(Write(rewrite_text), run_time=0.6)
        self.wait(0.4)

        # 系とこれまでの式を消す
        self.play(FadeOut(system_diagram), FadeOut(eq1), FadeOut(eq2), run_time=0.5)
        self.wait(0.2)

        # 定義
        definition = VGroup(
            MathTex(r"x_1(t) = x(t)", color=BLUE, font_size=32),
            MathTex(r"x_2(t) = v(t)", color=BLUE, font_size=32),
        ).arrange(DOWN, buff=0.3)
        definition.shift(UP * 0.8)
        
        definition_labels = VGroup(
            Text("（変位）", color=BLUE, font_size=24),
            Text("（速度）", color=BLUE, font_size=24),
        )
        definition_labels[0].next_to(definition[0], RIGHT, buff=0.2)
        definition_labels[1].next_to(definition[1], RIGHT, buff=0.2)
        
        for i, line in enumerate(definition):
            self.play(Write(line), Write(definition_labels[i]), run_time=0.6)
            self.wait(0.3)
        
        self.wait(0.5)

        arrow = MathTex(r"\Downarrow", color=WHITE, font_size=40)
        arrow.shift(DOWN * 0.3)
        self.play(Write(arrow), run_time=0.4)
        self.wait(0.3)

        # 連立方程式
        coupled_eqs = MathTex(
            r"\begin{cases} "
            r"\frac{d}{dt}x_1(t) = x_2(t) \\ "
            r"\frac{d}{dt}x_2(t) = -\frac{k}{m}x_1(t) - \frac{\gamma}{m} x_2(t) "
            r"\end{cases}",
            color=YELLOW,
            font_size=36,
        )
        coupled_eqs.shift(DOWN * 1.5)
        coupled_box = SurroundingRectangle(coupled_eqs, color=YELLOW, buff=0.2)
        
        self.play(Write(coupled_eqs), run_time=1.0)
        self.play(Create(coupled_box), run_time=0.4)
        self.wait(0.8)

        note = Text(
            "1階の連立微分方程式になった！",
            color=GREEN, font_size=24, weight=BOLD,
        )
        note.shift(DOWN * 2.8)
        self.play(Write(note), run_time=0.6)
        self.wait(1.0)

        self.play(
            FadeOut(rewrite_text), FadeOut(definition), FadeOut(definition_labels),
            FadeOut(arrow), FadeOut(note),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: ベクトルと行列による表現
        # ============================================================
        subtitle5 = Text("行列を使ったベクトル表現", font_size=28, color=GOLD)
        subtitle5.next_to(title, DOWN)
        self.play(Transform(subtitle2, subtitle5), run_time=0.5)
        self.wait(0.4)

        # 連立方程式を上に
        self.play(
            coupled_eqs.animate.shift(UP * 3).scale(0.8),
            coupled_box.animate.shift(UP * 3).scale(0.8),
            run_time=0.6
        )
        self.wait(0.3)

        vector_intro = Text(
            "2つの変数をベクトルにまとめる",
            color=WHITE, font_size=24,
        )
        vector_intro.shift(UP * 0.6 + LEFT * 2.5)
        self.play(Write(vector_intro), run_time=0.6)
        self.wait(0.4)

        # ベクトル定義
        vector_def = MathTex(
            r"\boldsymbol{x}(t) = \begin{pmatrix} x_1(t) \\ x_2(t) \end{pmatrix}",
            color=BLUE,
            font_size=36,
        )
        vector_def.shift(UP * 0.0)
        self.play(Write(vector_def), run_time=0.7)
        self.wait(0.5)

        arrow2 = MathTex(r"\Downarrow", color=WHITE, font_size=40)
        arrow2.shift(DOWN * 0.8)
        self.play(Write(arrow2), run_time=0.4)
        self.wait(0.3)

        # 行列形式
        matrix_form = MathTex(
            r"\frac{d}{dt}\boldsymbol{x}(t) = L\boldsymbol{x}(t)",
            color=ORANGE,
            font_size=42,
        )
        matrix_form.shift(DOWN * 1.6)
        matrix_box = SurroundingRectangle(matrix_form, color=ORANGE, buff=0.25)
        
        self.play(Write(matrix_form), run_time=0.8)
        self.play(Create(matrix_box), run_time=0.4)
        self.wait(0.6)

        # 行列Lの定義
        matrix_L = MathTex(
            r"L = \begin{pmatrix} 0 & 1 \\ -\frac{k}{m} & -\frac{\gamma}{m} \end{pmatrix}",
            color=TEAL,
            font_size=32,
        )
        matrix_L.shift(DOWN * 2.7)
        self.play(Write(matrix_L), run_time=0.7)
        self.wait(0.8)

        highlight = Text(
            "連立方程式が1つの行列の式で表せた！",
            color=GREEN, font_size=24, weight=BOLD,
        )
        highlight.shift(DOWN * 3.4)
        self.play(Write(highlight), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(coupled_eqs), FadeOut(coupled_box),
            FadeOut(vector_intro), FadeOut(vector_def),
            FadeOut(arrow2), FadeOut(matrix_L), FadeOut(highlight),
        )
        self.wait(0.3)

        # ============================================================
        # Part 6: 数値例とプロット
        # ============================================================
        subtitle6 = Text("実際に計算してみよう", font_size=28, color=TEAL)
        subtitle6.next_to(title, DOWN)
        self.play(Transform(subtitle2, subtitle6), run_time=0.5)
        self.wait(0.4)

        # 行列の式を上に小さく表示
        self.play(
            matrix_form.animate.shift(UP * 2.3).scale(0.7),
            matrix_box.animate.shift(UP * 2.3).scale(0.7),
            run_time=0.6
        )
        self.wait(0.2)

        # パラメータ設定
        params_text = Text(
            "パラメータ：m=1, k=10, γ=0.5",
            color=YELLOW, font_size=24,
        )
        params_text.shift(UP * 2 + LEFT * 3.5)
        self.play(Write(params_text), run_time=0.6)
        self.wait(0.3)

        initial_text = Text(
            "初期値：x(0)=1, v(0)=0",
            color=YELLOW, font_size=24,
        )
        initial_text.shift(UP * 1.5 + LEFT * 3.8)
        self.play(Write(initial_text), run_time=0.6)
        self.wait(0.5)

        # パラメータ設定
        m, k, gamma = 1.0, 10.0, 0.5
        x0, v0 = 1.0, 0.0
        
        # 時間発展の計算
        def solve_mass_spring_damper(t_max=10, dt=0.01):
            t_vals = np.arange(0, t_max, dt)
            x1_vals = np.zeros_like(t_vals)
            x2_vals = np.zeros_like(t_vals)
            
            x1_vals[0] = x0
            x2_vals[0] = v0
            
            for i in range(1, len(t_vals)):
                dx1 = x2_vals[i-1]
                dx2 = -(k/m) * x1_vals[i-1] - (gamma/m) * x2_vals[i-1]
                
                x1_vals[i] = x1_vals[i-1] + dx1 * dt
                x2_vals[i] = x2_vals[i-1] + dx2 * dt
            
            return t_vals, x1_vals, x2_vals
        
        t_vals, x1_vals, x2_vals = solve_mass_spring_damper(t_max=10)
        
        # グラフの作成
        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=5,
            y_length=3,
            axis_config={"color": GREY, "include_tip": True},
            tips=True,
        )
        axes.shift(DOWN * 0.8 + LEFT * 0.5)
        
        x_label = MathTex("t", font_size=24).next_to(axes.x_axis, RIGHT, buff=0.1)
        y_label = Text("変位・速度", font_size=20).next_to(axes.y_axis, UP, buff=0.1)
        
        self.play(Create(axes), Write(x_label), Write(y_label), run_time=0.6)
        self.wait(0.3)

        # プロット（変位）
        x1_points = [axes.c2p(t, x) for t, x in zip(t_vals[::10], x1_vals[::10])]
        x1_curve = VMobject(color=BLUE, stroke_width=3)
        x1_curve.set_points_as_corners(x1_points)
        
        x1_label = MathTex("x_1(t)", color=BLUE, font_size=28)
        x1_label.next_to(axes.c2p(10, x1_vals[-1]), RIGHT, buff=0.1)
        x1_label.shift(UP * 0.1)
        
        # プロット（速度）
        x2_points = [axes.c2p(t, x) for t, x in zip(t_vals[::10], x2_vals[::10])]
        x2_curve = VMobject(color=RED, stroke_width=3)
        x2_curve.set_points_as_corners(x2_points)
        
        x2_label = MathTex("x_2(t)", color=RED, font_size=28)
        x2_label.next_to(axes.c2p(10, x2_vals[-1]), RIGHT, buff=0.1)
        x2_label.shift(DOWN * 0.1)

        # 系のポンチ絵（右側に小さく配置）
        mini_wall = Line(UP * 0.8, DOWN * 0.8, color=GREY, stroke_width=6)
        mini_wall.shift(RIGHT * 3.5 + UP * 0.5)
        
        mini_hatches = VGroup()
        for i in range(5):
            hatch = Line(
                LEFT * 0.2 + UP * (0.8 - i * 0.4),
                UP * (0.6 - i * 0.4),
                color=GREY, stroke_width=2
            )
            hatch.shift(RIGHT * 3.5 + UP * 0.5)
            mini_hatches.add(hatch)
        
        mini_mass = Square(side_length=0.5, color=RED, fill_opacity=0.7)
        mini_mass.shift(RIGHT * 5.0 + UP * 0.5)
        
        mini_spring = self.create_spring(
            RIGHT * 3.5 + UP * 0.5,
            RIGHT * 4.75 + UP * 0.5,
            color=BLUE, num_coils=8
        )
        
        # 床（mini_massの底部に接する位置：0.5 - 0.25 = 0.25）
        mini_floor = Line(
            RIGHT * 3.0 + UP * 0.25,
            RIGHT * 6.0 + UP * 0.25,
            color=GREY, stroke_width=3
        )
        
        # 床の模様（ハッチング：摩擦を表現）
        mini_floor_hatches = VGroup()
        for i in range(15):
            hatch = Line(
                start=RIGHT * 3.0 + RIGHT * (i * 0.2) + UP * 0.25,
                end=RIGHT * 3.0 + RIGHT * (i * 0.2) + LEFT * 0.1 + DOWN * 0.05,
                color=GREY, stroke_width=1.5
            )
            mini_floor_hatches.add(hatch)
        
        mini_system = VGroup(mini_wall, mini_hatches, mini_spring, mini_mass, mini_floor, mini_floor_hatches)
        
        self.play(FadeIn(mini_system), run_time=0.5)
        self.wait(0.3)

        # アニメーション：グラフと系を連動
        self.play(Create(x1_curve), Write(x1_label), run_time=2.0, rate_func=linear)
        self.wait(0.3)
        
        self.play(Create(x2_curve), Write(x2_label), run_time=2.0, rate_func=linear)
        self.wait(0.5)

        # 系のアニメーション（減衰振動）
        def update_mini_system(mob, alpha):
            t_index = int(alpha * (len(t_vals) - 1))
            displacement = x1_vals[t_index]
            
            new_mass_pos = RIGHT * (5.0 + displacement * 0.8) + UP * 0.5
            mob[3].move_to(new_mass_pos)
            
            new_spring = self.create_spring(
                RIGHT * 3.5 + UP * 0.5,
                new_mass_pos + LEFT * 0.25,
                color=BLUE, num_coils=8
            )
            mob[2].become(new_spring)
        
        # animation_text = Text(
        #     "系が減衰振動している！",
        #     color=GREEN, font_size=22, weight=BOLD,
        # )
        # animation_text.shift(RIGHT * 4.5 + DOWN * 1.0)
        # self.play(Write(animation_text), run_time=0.6)
        
        self.play(
            UpdateFromAlphaFunc(mini_system, update_mini_system),
            run_time=6.0,
            rate_func=linear
        )
        self.wait(1.0)

        damped_note = Text(
            "これが減衰振動：時間発展の典型例",
            color=YELLOW, font_size=24,
        )
        damped_note.shift(DOWN * 2.5 + RIGHT * 1.3)
        self.play(Write(damped_note), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(axes), FadeOut(x_label), FadeOut(y_label),
            FadeOut(x1_curve), FadeOut(x1_label),
            FadeOut(x2_curve), FadeOut(x2_label),
            FadeOut(mini_system), FadeOut(damped_note),
            FadeOut(params_text), FadeOut(initial_text),
            FadeOut(matrix_form), FadeOut(matrix_box),
        )
        self.wait(0.3)

        # ============================================================
        # Part 7: まとめと次回予告
        # ============================================================
        subtitle7 = Text("まとめ", font_size=36, color=GOLD)
        subtitle7.next_to(title, DOWN)
        self.play(Transform(subtitle2, subtitle7), run_time=0.6)
        self.wait(0.4)

        # summary_intro = Text(
        #     "今回学んだこと",
        #     color=WHITE, font_size=26, weight=BOLD,
        # )
        # summary_intro.shift(UP * 1.8)
        # self.play(Write(summary_intro), run_time=0.6)
        # self.wait(0.4)

        summary = VGroup(
            Text("• 変数が複数の場合、連立微分方程式になる", color=WHITE, font_size=28),
            Text("• ベクトルと行列を使って1つの式にまとめられる", color=WHITE, font_size=28),
            Text("• マスバネダンパ系は減衰振動を示す", color=WHITE, font_size=28),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        summary.shift(UP * 0.5)
        
        for row in summary:
            self.play(Write(row), run_time=0.6)
            self.wait(0.2)
        
        self.wait(0.7)

        # question_text = Text(
        #     "前回：1変数の時間発展は指数関数 e⁻ᵅᵗ で表せた",
        #     color=BLUE, font_size=24,
        # )
        # question_text.shift(DOWN * 0.8)
        # self.play(Write(question_text), run_time=0.7)
        # self.wait(0.5)

        next_question = Text(
            "さて、多変数の場合はどう微分方程式を解くのか…？",
            color=ORANGE, font_size=26, weight=BOLD,
        )
        next_question.shift(DOWN * 1.5)
        self.play(Write(next_question), run_time=0.7)
        self.wait(0.6)

        next_topic = Text(
            "→ これを段階的に学ぶために、次回は行列の指数関数を導入する",
            color=GREEN, font_size=26, weight=BOLD,
        )
        next_topic.shift(DOWN * 2.2)
        self.play(Write(next_topic), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(
                title, subtitle2, summary,
                next_question, next_topic
            )),
            run_time=1.0
        )
        self.wait(0.5)

    def create_spring(self, start, end, color=BLUE, num_coils=12):
        """バネを作成するヘルパー関数"""
        spring_points = []
        start_point = np.array([start[0] if isinstance(start, (list, np.ndarray)) else start.get_center()[0],
                               start[1] if isinstance(start, (list, np.ndarray)) else start.get_center()[1],
                               0])
        end_point = np.array([end[0] if isinstance(end, (list, np.ndarray)) else end.get_center()[0],
                             end[1] if isinstance(end, (list, np.ndarray)) else end.get_center()[1],
                             0])
        
        direction = end_point - start_point
        length = np.linalg.norm(direction)
        unit_dir = direction / length
        perp_dir = np.array([-unit_dir[1], unit_dir[0], 0])
        
        amplitude = 0.2
        spring_points.append(start_point)
        
        # より細かいセグメントでバネを描画（各コイルに8セグメント）
        segments_per_coil = 8
        total_segments = num_coils * segments_per_coil
        
        for i in range(1, total_segments):
            t = i / total_segments
            base_point = start_point + t * direction
            # 正弦波でバネの波形を作成
            offset = amplitude * np.sin(i * 2 * np.pi / segments_per_coil) * perp_dir
            spring_points.append(base_point + offset)
        
        spring_points.append(end_point)
        
        spring = VMobject(color=color, stroke_width=3)
        spring.set_points_as_corners(spring_points)
        return spring
