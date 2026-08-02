from manim import *
import numpy as np


class DiagonalizationAndControlTheory(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        title = Text("おまけ：対角化と制御工学の応答性解析", font_size=36, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.7)

        # ============================================================
        # Part 0: イントロダクション
        # ============================================================
        subtitle0 = Text("制御工学への半歩先", font_size=28, color=BLUE)
        subtitle0.next_to(title, DOWN)
        self.play(Write(subtitle0), run_time=0.6)
        self.wait(0.4)

        intro_text = Text(
            "今回学んだ行列の対角化が",
            color=WHITE, font_size=28,
        )
        intro_text.shift(UP * 1.2)
        self.play(Write(intro_text), run_time=0.7)
        self.wait(0.4)

        intro_text2 = Text(
            "実際のシステムの挙動解析にどう役立つか見てみよう",
            color=WHITE, font_size=28,
        )
        intro_text2.shift(UP * 0.5)
        self.play(Write(intro_text2), run_time=0.7)
        self.wait(0.8)

        self.play(
            FadeOut(intro_text), FadeOut(intro_text2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 1: モード分解の意義
        # ============================================================
        subtitle1 = Text("モード分解とは", font_size=28, color=TEAL)
        subtitle1.next_to(title, DOWN)
        self.play(Transform(subtitle0, subtitle1), run_time=0.5)
        self.wait(0.4)

        mode_intro = VGroup(
            Text("複雑な多変数・多自由度の動的システムを、", color=ORANGE, font_size=26, weight=BOLD),
            Text("独立した個別の要素（モード）の足し合わせに変換する手法", color=ORANGE, font_size=26, weight=BOLD),
        ).arrange(DOWN, buff=0.15)
        mode_intro.shift(UP * 1.8)
        self.play(Write(mode_intro), run_time=0.7)
        self.wait(0.5)

        key_concept = VGroup(
            Text("線形システムでは、", color=WHITE, font_size=24, weight=BOLD),
            Text("システム行列を対角化", color=YELLOW, font_size=24, weight=BOLD),
            MathTex(r"\Downarrow", color=WHITE, font_size=28),
            Text("システムの特性を評価", color=TEAL, font_size=24, weight=BOLD),
        ).arrange(DOWN, buff=0.2)
        key_concept.shift(DOWN * 0.1)
        
        for item in key_concept:
            self.play(Write(item), run_time=0.4)
            self.wait(0.2)
        
        self.wait(0.6)

        self.play(FadeOut(key_concept))
        self.wait(0.2)

        mode_significance = VGroup(
            Text("モード分解の利点：", color=ORANGE, font_size=26, weight=BOLD),
            Text("① 物理的意味から離れるが、相互干渉のないシンプルな系として評価できる", color=WHITE, font_size=24),
            Text("② システムの持つ特性（速いモード、遅いモード）を明確に分離して評価できる", color=WHITE, font_size=24),
            Text("③ 対角化できない場合でも、ジョルダン標準形で一方向の依存関係を評価", color=WHITE, font_size=24),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        mode_significance.shift(DOWN * 0.3)
        
        for item in mode_significance:
            self.play(Write(item), run_time=0.4)
            self.wait(0.2)
        
        self.wait(1.5)

        self.play(FadeOut(mode_intro), FadeOut(mode_significance))
        self.wait(0.3)

        # ============================================================
        # Part 2: マスバネダンパ系の復習
        # ============================================================
        subtitle2 = Text("具体例で見てみよう", font_size=28, color=GOLD)
        subtitle2.next_to(title, DOWN)
        self.play(Transform(subtitle0, subtitle2), run_time=0.5)
        self.wait(0.4)

        review_intro = Text(
            "対角化の3分類が実際の挙動としてどう現れるか",
            color=ORANGE, font_size=26, weight=BOLD,
        )
        review_intro.shift(UP * 1.8)
        self.play(Write(review_intro), run_time=0.7)
        self.wait(0.5)

        review_intro2 = Text(
            "マスバネダンパ系を例に見てみよう",
            color=WHITE, font_size=24,
        )
        review_intro2.shift(UP * 1.2+LEFT*0.5)
        self.play(Write(review_intro2), run_time=0.6)
        self.wait(0.5)

        # ポンチ絵：マスバネダンパ系（sec19から転用）
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
        
        # 座標軸（自然長の位置を原点として配置）
        axis_y_pos = DOWN * 0.5
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
        
        system_diagram = VGroup(
            wall, hatches, spring, mass, mass_label,
            floor, floor_hatches, axis_arrow, axis_label,
            origin_mark, origin_label,
        )
        
        self.play(Create(wall), Create(hatches), run_time=0.4)
        self.play(Create(spring), run_time=0.4)
        self.play(FadeIn(mass), Write(mass_label), run_time=0.4)
        self.play(Create(floor), Create(floor_hatches), run_time=0.4)
        self.play(Create(axis_arrow), Write(axis_label), run_time=0.3)
        self.play(Create(origin_mark), Write(origin_label), run_time=0.3)
        self.wait(0.6)

        # 系を左に移動
        self.play(
            system_diagram.animate.shift(LEFT * 1.5).scale(0.75),
            review_intro.animate.shift(LEFT * 3.5).scale(0.85),
            run_time=0.6
        )
        self.wait(0.3)

        # パラメータの説明
        params = VGroup(
            Text("m：質量", color=RED, font_size=24),
            Text("k：バネ定数", color=BLUE, font_size=24),
            Text("γ：摩擦係数", color=ORANGE, font_size=24),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        params.shift(RIGHT * 3.8 + UP * 1.7)
        
        for param in params:
            self.play(Write(param), run_time=0.4)
            self.wait(0.2)
        
        self.wait(0.4)

        # 運動方程式
        eq_title = Text("運動方程式：", color=TEAL, font_size=22)
        eq_title.shift(RIGHT * 3.8 + UP * 0.5)
        self.play(Write(eq_title), run_time=0.5)
        self.wait(0.3)

        equation = MathTex(
            r"m\ddot{x} = -kx - \gamma \dot{x}",
            color=YELLOW,
            font_size=30,
        )
        equation.shift(RIGHT * 3.8 + UP * 0.0)
        self.play(Write(equation), run_time=0.6)
        self.wait(0.5)

        # 状態空間表現
        state_title = Text("状態空間表現：", color=TEAL, font_size=22)
        state_title.shift(RIGHT * 3.8 + DOWN * 0.7)
        self.play(Write(state_title), run_time=0.5)
        self.wait(0.3)

        state_eq = MathTex(
            r"\frac{d}{dt}\begin{pmatrix} x \\ \dot{x} \end{pmatrix} = "
            r"\begin{pmatrix} 0 & 1 \\ -\frac{k}{m} & -\frac{\gamma}{m} \end{pmatrix}"
            r"\begin{pmatrix} x \\ \dot{x} \end{pmatrix}",
            color=GREEN,
            font_size=26,
        )
        state_eq.shift(RIGHT * 3.8 + DOWN * 1.5)
        state_box = SurroundingRectangle(state_eq, color=GREEN, buff=0.15)
        self.play(Write(state_eq), Create(state_box), run_time=0.7)
        self.wait(0.8)

        system_matrix_label = Text(
            "システム行列A", color=BLUE, font_size=20,
        )
        system_matrix_label.shift(RIGHT * 3.8 + DOWN * 2.3)
        self.play(Write(system_matrix_label), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(review_intro), FadeOut(review_intro2), FadeOut(system_diagram),
            FadeOut(params), FadeOut(eq_title),
            FadeOut(equation), FadeOut(state_title),
        )
        self.wait(0.3)

        # システム行列を中央に移動
        self.play(
            state_eq.animate.shift(LEFT * 3.8 + UP * 2.0).scale(1.2),
            state_box.animate.shift(LEFT * 3.8 + UP * 2.0).scale(1.2),
            system_matrix_label.animate.shift(LEFT * 3.8 + UP * 2.0),
            run_time=0.6
        )
        self.wait(0.3)

        # 固有値の説明
        eigenvalue_intro = Text(
            "このシステム行列の固有値がシステムの挙動を決定する",
            color=ORANGE, font_size=26, weight=BOLD,
        )
        eigenvalue_intro.shift(UP * 0.3)
        self.play(Write(eigenvalue_intro), run_time=0.8)
        self.wait(0.6)

        eigenvalue_eq = MathTex(
            r"\det(A - \lambda I) = 0",
            color=YELLOW,
            font_size=36,
        )
        eigenvalue_eq.shift(DOWN * 0.5)
        self.play(Write(eigenvalue_eq), run_time=0.7)
        self.wait(0.5)

        arrow = MathTex(r"\Downarrow", color=WHITE, font_size=32)
        arrow.shift(DOWN * 1.2)
        self.play(Write(arrow), run_time=0.3)
        self.wait(0.2)

        eigenvalue_result = MathTex(
            r"\lambda = -\frac{\gamma}{2m} \pm \sqrt{\left(\frac{\gamma}{2m}\right)^2 - \frac{k}{m}}",
            color=GREEN,
            font_size=32,
        )
        eigenvalue_result.shift(DOWN * 2.0)
        eigenvalue_box = SurroundingRectangle(eigenvalue_result, color=GREEN, buff=0.2)
        self.play(Write(eigenvalue_result), Create(eigenvalue_box), run_time=0.8)
        self.wait(0.8)

        key_note = Text(
            "この固有値の性質がシステムの応答パターンを決める！",
            color=YELLOW, font_size=24, weight=BOLD,
        )
        key_note.shift(DOWN * 3.0)
        self.play(Write(key_note), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(state_eq), FadeOut(state_box),
            FadeOut(system_matrix_label), FadeOut(eigenvalue_intro),
            FadeOut(eigenvalue_eq), FadeOut(arrow),
            FadeOut(eigenvalue_result), FadeOut(eigenvalue_box),
            FadeOut(key_note),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: パターン1 - 実数で対角化可能（過減衰）
        # ============================================================
        subtitle3 = Text("パターン1：過減衰", font_size=28, color=BLUE)
        subtitle3.next_to(title, DOWN)
        self.play(Transform(subtitle0, subtitle3), run_time=0.5)
        self.wait(0.4)

        # 条件の説明
        condition1 = Text(
            "条件：ダンパが強い（γ² > 4km）",
            color=ORANGE, font_size=26, weight=BOLD,
        )
        condition1.shift(UP * 2.0)
        self.play(Write(condition1), run_time=0.7)
        self.wait(0.5)

        # 数学的構造
        math_title1 = Text("数学的構造：", color=TEAL, font_size=24, weight=BOLD)
        math_title1.shift(UP * 1.2)
        self.play(Write(math_title1), run_time=0.5)
        self.wait(0.3)

        math_structure1 = VGroup(
            Text("• 2つの異なる実数固有値", color=WHITE, font_size=22),
            MathTex(r"\lambda_1, \lambda_2 \in \mathbb{R}, \quad \lambda_1 \neq \lambda_2", 
                   color=YELLOW, font_size=28),
            Text("• 2つの一次独立な固有ベクトルが存在", color=WHITE, font_size=22),
            Text("• 完全な対角化が可能", color=GREEN, font_size=22),
            MathTex(r"P^{-1}AP = \text{diag}(\lambda_1, \lambda_2)", 
                   color=GREEN, font_size=26),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        math_structure1.shift(UP * 0.1)
        
        for item in math_structure1:
            self.play(Write(item), run_time=0.5)
            self.wait(0.2)
        
        self.wait(0.8)

        # 物理的挙動へ
        self.play(
            FadeOut(condition1), FadeOut(math_title1),
            FadeOut(math_structure1),
        )
        self.wait(0.3)

        phys_title1 = Text("物理的挙動：", color=GOLD, font_size=26, weight=BOLD)
        phys_title1.shift(UP * 2.3)
        self.play(Write(phys_title1), run_time=0.6)
        self.wait(0.4)

        phys_desc1 = Text(
            "「バネの復元力」よりも「ダンパの抵抗力」が圧倒的に強い",
            color=ORANGE, font_size=24,
        )
        phys_desc1.shift(UP * 1.6)
        self.play(Write(phys_desc1), run_time=0.7)
        self.wait(0.5)

        mode_decomp1 = VGroup(
            Text("システムは2つの独立したモードに分解される：", color=WHITE, font_size=22),
            Text("① 速い減衰モード：初期の急激な動き", color=BLUE, font_size=20),
            Text("② 遅い減衰モード：ジワジワとした戻り", color=TEAL, font_size=20),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        mode_decomp1.shift(UP * 0.5)
        
        for item in mode_decomp1:
            self.play(Write(item), run_time=0.5)
            self.wait(0.3)
        
        self.wait(0.6)

        key_feature1 = Text(
            "→ 振動（オーバーシュート）は発生しない",
            color=GREEN, font_size=24, weight=BOLD,
        )
        key_feature1.shift(DOWN * 0.6)
        self.play(Write(key_feature1), run_time=0.7)
        self.wait(1.0)

        # グラフィック表示のための準備
        self.play(
            FadeOut(mode_decomp1), FadeOut(key_feature1),
        )
        self.wait(0.3)

        self.play(
            phys_title1.animate.shift(UP * 0.5).scale(0.85),
            phys_desc1.animate.shift(UP * 0.5).scale(0.85),
            run_time=0.5
        )
        self.wait(0.2)

        # マスバネダンパ系を再作成（過減衰のシミュレーション用）
        # パラメータ設定
        m, k, gamma = 1.0, 1.0, 4.0  # 過減衰条件: γ² = 16 > 4km = 4
        
        # 初期条件
        x0 = 1.5  # 初期変位（右に引っ張る）
        v0 = 0.0  # 初期速度
        
        # 固有値
        discriminant = (gamma/(2*m))**2 - k/m
        lambda1 = -gamma/(2*m) + np.sqrt(discriminant)  # 遅いモード
        lambda2 = -gamma/(2*m) - np.sqrt(discriminant)  # 速いモード
        
        # 時間応答関数
        def x_overdamped(t):
            # 初期条件から係数を計算
            c1 = (v0 - lambda2*x0)/(lambda1 - lambda2)
            c2 = (lambda1*x0 - v0)/(lambda1 - lambda2)
            return c1 * np.exp(lambda1 * t) + c2 * np.exp(lambda2 * t)
        
        # マスバネダンパ系の作成
        spring_natural_pos_sim = LEFT * 2
        wall_sim = Line(
            start=UP * 1.0 + LEFT * 5,
            end=DOWN * 1.0 + LEFT * 5,
            color=GREY,
            stroke_width=8,
        )
        
        hatches_sim = VGroup()
        for i in range(6):
            hatch = Line(
                start=LEFT * 5 + UP * (1.0 - i * 0.33) + LEFT * 0.3,
                end=LEFT * 5 + UP * (0.67 - i * 0.33),
                color=GREY,
                stroke_width=3,
            )
            hatches_sim.add(hatch)
        
        mass_sim = Square(side_length=0.6, color=RED, fill_opacity=0.7)
        mass_label_sim = MathTex("m", color=WHITE, font_size=28)
        
        floor_sim = Line(
            start=LEFT * 6 + DOWN * 0.4,
            end=RIGHT * 2 + DOWN * 0.4,
            color=GREY,
            stroke_width=4,
        )
        
        floor_hatches_sim = VGroup()
        for i in range(32):
            hatch = Line(
                start=LEFT * 6 + RIGHT * (i * 0.25) + DOWN * 0.4,
                end=LEFT * 6 + RIGHT * (i * 0.25) + LEFT * 0.15 + DOWN * 0.65,
                color=GREY,
                stroke_width=2,
            )
            floor_hatches_sim.add(hatch)
        
        axis_y_pos_sim = DOWN * 0.8
        axis_arrow_sim = Arrow(
            start=LEFT * 5 + axis_y_pos_sim,
            end=RIGHT * 1 + axis_y_pos_sim,
            color=YELLOW,
            buff=0,
            stroke_width=3,
        )
        axis_label_sim = MathTex("x", color=YELLOW, font_size=28)
        axis_label_sim.next_to(axis_arrow_sim, RIGHT, buff=0.1)
        
        origin_mark_sim = Line(
            spring_natural_pos_sim + axis_y_pos_sim + UP * 0.15,
            spring_natural_pos_sim + axis_y_pos_sim + DOWN * 0.15,
            color=YELLOW,
            stroke_width=4,
        )
        origin_label_sim = MathTex("0", color=YELLOW, font_size=24)
        origin_label_sim.next_to(spring_natural_pos_sim + axis_y_pos_sim, DOWN, buff=0.2)
        
        system_diagram_sim = VGroup(
            wall_sim, hatches_sim, floor_sim, floor_hatches_sim,
            axis_arrow_sim, axis_label_sim, origin_mark_sim, origin_label_sim,
        )
        system_diagram_sim.shift(DOWN * 1.3)
        
        self.play(Create(system_diagram_sim), run_time=0.6)
        self.wait(0.3)
        
        # 初期位置に質量を配置
        x_initial = spring_natural_pos_sim[0] + x0
        spring_initial = self.create_spring(
            LEFT * 5, 
            [x_initial, spring_natural_pos_sim[1], 0],
            color=BLUE, 
            num_coils=12
        )
        spring_initial.shift(DOWN * 1.3)
        
        mass_sim.move_to([x_initial + 0.3, spring_natural_pos_sim[1], 0])
        mass_sim.shift(DOWN * 1.3)
        mass_label_sim.move_to(mass_sim.get_center())
        
        self.play(Create(spring_initial), FadeIn(mass_sim), Write(mass_label_sim), run_time=0.5)
        self.wait(0.5)

        # 時間経過のアニメーション
        time_label = Text("t = 0.0 s", color=WHITE, font_size=22)
        time_label.shift(DOWN * 3.2 + LEFT * 4.5)
        self.play(Write(time_label), run_time=0.3)
        self.wait(0.3)

        # アニメーション実行
        dt = 0.05
        total_time = 4.0
        spring_mobject = spring_initial
        
        for t in np.arange(dt, total_time, dt):
            x_t = x_overdamped(t)
            x_pos = spring_natural_pos_sim[0] + x_t
            
            new_spring = self.create_spring(
                LEFT * 5,
                [x_pos, spring_natural_pos_sim[1], 0],
                color=BLUE,
                num_coils=12
            )
            new_spring.shift(DOWN * 1.3)
            
            new_time_label = Text(f"t = {t:.1f} s", color=WHITE, font_size=22)
            new_time_label.shift(DOWN * 3.2 + LEFT * 4.5)
            
            self.play(
                Transform(spring_mobject, new_spring),
                mass_sim.animate.move_to([x_pos + 0.3, spring_natural_pos_sim[1] - 1.3, 0]),
                mass_label_sim.animate.move_to([x_pos + 0.3, spring_natural_pos_sim[1] - 1.3, 0]),
                Transform(time_label, new_time_label),
                run_time=dt,
                rate_func=linear,
            )
        
        self.wait(1.0)

        conclusion1 = Text(
            "ゆっくりと目標値に収束（振動なし）",
            color=GREEN, font_size=24, weight=BOLD,
        )
        conclusion1.shift(DOWN * 3.2 + RIGHT * 2.5)
        self.play(Write(conclusion1), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(phys_title1), FadeOut(phys_desc1),
            FadeOut(system_diagram_sim), FadeOut(spring_mobject),
            FadeOut(mass_sim), FadeOut(mass_label_sim),
            FadeOut(time_label), FadeOut(conclusion1),
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: パターン2 - 複素数で対角化（減衰振動）
        # ============================================================
        subtitle4 = Text("パターン2：減衰振動", font_size=28, color=TEAL)
        subtitle4.next_to(title, DOWN)
        self.play(Transform(subtitle0, subtitle4), run_time=0.5)
        self.wait(0.4)

        # 条件の説明
        condition2 = Text(
            "条件：ダンパが弱い（γ² < 4km）",
            color=ORANGE, font_size=26, weight=BOLD,
        )
        condition2.shift(UP * 2.0)
        self.play(Write(condition2), run_time=0.7)
        self.wait(0.5)

        # 数学的構造
        math_title2 = Text("数学的構造：", color=TEAL, font_size=24, weight=BOLD)
        math_title2.shift(UP * 1.2)
        self.play(Write(math_title2), run_time=0.5)
        self.wait(0.3)

        math_structure2 = VGroup(
            Text("• 互いに共役な複素固有値", color=WHITE, font_size=22),
            MathTex(r"\lambda = -\alpha \pm j\omega", 
                   color=YELLOW, font_size=28),
            Text("• 実数の範囲では対角化できない", color=WHITE, font_size=22),
            Text("• 行列指数関数は回転行列を含む", color=GREEN, font_size=22),
            MathTex(r"e^{At} \propto e^{-\alpha t} \begin{pmatrix} \cos \omega t & \sin \omega t \\ -\sin \omega t & \cos \omega t \end{pmatrix}", 
                   color=GREEN, font_size=22),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        math_structure2.shift(UP * 0.0)
        
        for item in math_structure2:
            self.play(Write(item), run_time=0.5)
            self.wait(0.2)
        
        self.wait(0.8)

        # 物理的挙動へ
        self.play(
            FadeOut(condition2), FadeOut(math_title2),
            FadeOut(math_structure2),
        )
        self.wait(0.3)

        phys_title2 = Text("物理的挙動：", color=GOLD, font_size=26, weight=BOLD)
        phys_title2.shift(UP * 2.3)
        self.play(Write(phys_title2), run_time=0.6)
        self.wait(0.4)

        phys_desc2 = Text(
            "「ダンパの抵抗力」が弱く、「バネの勢い」が勝る",
            color=ORANGE, font_size=24,
        )
        phys_desc2.shift(UP * 1.6)
        self.play(Write(phys_desc2), run_time=0.7)
        self.wait(0.5)

        mode_decomp2 = VGroup(
            Text("運動エネルギーと位置エネルギーの間でキャッチボール", color=WHITE, font_size=22),
            Text("→ 目標値を通り過ぎて振動（オーバーシュート）", color=BLUE, font_size=20),
            Text("→ ダンパが徐々にエネルギーを吸収", color=TEAL, font_size=20),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        mode_decomp2.shift(UP * 0.5)
        
        for item in mode_decomp2:
            self.play(Write(item), run_time=0.5)
            self.wait(0.3)
        
        self.wait(0.6)

        key_feature2 = VGroup(
            Text("• ダンパが減衰のペース（-α）を決定", color=GREEN, font_size=22),
            Text("• バネとダンパが共同で振動のペース（ω）を決定", color=GREEN, font_size=22),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        key_feature2.shift(DOWN * 0.5)
        
        for item in key_feature2:
            self.play(Write(item), run_time=0.5)
            self.wait(0.3)
        
        self.wait(1.0)

        # グラフィック表示のための準備
        self.play(
            FadeOut(mode_decomp2), FadeOut(key_feature2),
        )
        self.wait(0.3)

        self.play(
            phys_title2.animate.shift(UP * 0.5).scale(0.85),
            phys_desc2.animate.shift(UP * 0.5).scale(0.85),
            run_time=0.5
        )
        self.wait(0.2)

        # マスバネダンパ系を再作成（減衰振動のシミュレーション用）
        # パラメータ設定
        m2, k2, gamma2 = 1.0, 4.0, 0.5  # 減衰振動条件: γ² = 0.25 < 4km = 16
        
        # 初期条件
        x0_2 = 1.5
        v0_2 = 0.0
        
        # 固有値（複素数）
        alpha = gamma2/(2*m2)
        omega = np.sqrt(k2/m2 - (gamma2/(2*m2))**2)
        
        # 時間応答関数
        def x_underdamped(t):
            # 初期条件から係数を計算
            A = x0_2
            B = (v0_2 + alpha*x0_2)/omega
            return np.exp(-alpha * t) * (A * np.cos(omega * t) + B * np.sin(omega * t))
        
        # マスバネダンパ系の作成
        wall_sim2 = Line(
            start=UP * 1.0 + LEFT * 5,
            end=DOWN * 1.0 + LEFT * 5,
            color=GREY,
            stroke_width=8,
        )
        
        hatches_sim2 = VGroup()
        for i in range(6):
            hatch = Line(
                start=LEFT * 5 + UP * (1.0 - i * 0.33) + LEFT * 0.3,
                end=LEFT * 5 + UP * (0.67 - i * 0.33),
                color=GREY,
                stroke_width=3,
            )
            hatches_sim2.add(hatch)
        
        mass_sim2 = Square(side_length=0.6, color=RED, fill_opacity=0.7)
        mass_label_sim2 = MathTex("m", color=WHITE, font_size=28)
        
        floor_sim2 = Line(
            start=LEFT * 6 + DOWN * 0.4,
            end=RIGHT * 2 + DOWN * 0.4,
            color=GREY,
            stroke_width=4,
        )
        
        floor_hatches_sim2 = VGroup()
        for i in range(32):
            hatch = Line(
                start=LEFT * 6 + RIGHT * (i * 0.25) + DOWN * 0.4,
                end=LEFT * 6 + RIGHT * (i * 0.25) + LEFT * 0.15 + DOWN * 0.65,
                color=GREY,
                stroke_width=2,
            )
            floor_hatches_sim2.add(hatch)
        
        axis_y_pos_sim2 = DOWN * 0.8
        axis_arrow_sim2 = Arrow(
            start=LEFT * 5 + axis_y_pos_sim2,
            end=RIGHT * 1 + axis_y_pos_sim2,
            color=YELLOW,
            buff=0,
            stroke_width=3,
        )
        axis_label_sim2 = MathTex("x", color=YELLOW, font_size=28)
        axis_label_sim2.next_to(axis_arrow_sim2, RIGHT, buff=0.1)
        
        origin_mark_sim2 = Line(
            spring_natural_pos_sim + axis_y_pos_sim2 + UP * 0.15,
            spring_natural_pos_sim + axis_y_pos_sim2 + DOWN * 0.15,
            color=YELLOW,
            stroke_width=4,
        )
        origin_label_sim2 = MathTex("0", color=YELLOW, font_size=24)
        origin_label_sim2.next_to(spring_natural_pos_sim + axis_y_pos_sim2, DOWN, buff=0.2)
        
        system_diagram_sim2 = VGroup(
            wall_sim2, hatches_sim2, floor_sim2, floor_hatches_sim2,
            axis_arrow_sim2, axis_label_sim2, origin_mark_sim2, origin_label_sim2,
        )
        system_diagram_sim2.shift(DOWN * 1.3)
        
        self.play(Create(system_diagram_sim2), run_time=0.6)
        self.wait(0.3)
        
        # 初期位置に質量を配置
        x_initial_2 = spring_natural_pos_sim[0] + x0_2
        spring_initial_2 = self.create_spring(
            LEFT * 5, 
            [x_initial_2, spring_natural_pos_sim[1], 0],
            color=BLUE, 
            num_coils=12
        )
        spring_initial_2.shift(DOWN * 1.3)
        
        mass_sim2.move_to([x_initial_2 + 0.3, spring_natural_pos_sim[1], 0])
        mass_sim2.shift(DOWN * 1.3)
        mass_label_sim2.move_to(mass_sim2.get_center())
        
        self.play(Create(spring_initial_2), FadeIn(mass_sim2), Write(mass_label_sim2), run_time=0.5)
        self.wait(0.5)

        # 時間経過のアニメーション
        time_label_2 = Text("t = 0.0 s", color=WHITE, font_size=22)
        time_label_2.shift(DOWN * 3.2 + LEFT * 4.5)
        self.play(Write(time_label_2), run_time=0.3)
        self.wait(0.3)

        # アニメーション実行
        dt_2 = 0.04
        total_time_2 = 6.0
        spring_mobject_2 = spring_initial_2
        
        for t in np.arange(dt_2, total_time_2, dt_2):
            x_t = x_underdamped(t)
            x_pos = spring_natural_pos_sim[0] + x_t
            
            new_spring = self.create_spring(
                LEFT * 5,
                [x_pos, spring_natural_pos_sim[1], 0],
                color=BLUE,
                num_coils=12
            )
            new_spring.shift(DOWN * 1.3)
            
            new_time_label = Text(f"t = {t:.1f} s", color=WHITE, font_size=22)
            new_time_label.shift(DOWN * 3.2 + LEFT * 4.5)
            
            self.play(
                Transform(spring_mobject_2, new_spring),
                mass_sim2.animate.move_to([x_pos + 0.3, spring_natural_pos_sim[1] - 1.3, 0]),
                mass_label_sim2.animate.move_to([x_pos + 0.3, spring_natural_pos_sim[1] - 1.3, 0]),
                Transform(time_label_2, new_time_label),
                run_time=dt_2,
                rate_func=linear,
            )
        
        self.wait(1.0)

        conclusion2 = Text(
            "振動しながら徐々に収束",
            color=GREEN, font_size=24, weight=BOLD,
        )
        conclusion2.shift(DOWN * 3.2 + RIGHT * 2.5)
        self.play(Write(conclusion2), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(phys_title2), FadeOut(phys_desc2),
            FadeOut(system_diagram_sim2), FadeOut(spring_mobject_2),
            FadeOut(mass_sim2), FadeOut(mass_label_sim2),
            FadeOut(time_label_2), FadeOut(conclusion2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: パターン3 - 対角化不可能 / ジョルダン標準形（臨界減衰）
        # ============================================================
        subtitle5 = Text("パターン3：臨界減衰", font_size=28, color=GOLD)
        subtitle5.next_to(title, DOWN)
        self.play(Transform(subtitle0, subtitle5), run_time=0.5)
        self.wait(0.4)

        # 条件の説明
        condition3 = Text(
            "条件：バネとダンパが完璧にバランス（γ² = 4km）",
            color=ORANGE, font_size=26, weight=BOLD,
        )
        condition3.shift(UP * 2.0)
        self.play(Write(condition3), run_time=0.7)
        self.wait(0.5)

        # 数学的構造
        math_title3 = Text("数学的構造：", color=TEAL, font_size=24, weight=BOLD)
        math_title3.shift(UP * 1.2)
        self.play(Write(math_title3), run_time=0.5)
        self.wait(0.3)

        math_structure3 = VGroup(
            Text("• 実数の重根", color=WHITE, font_size=22),
            MathTex(r"\lambda = -\omega_n \text{ (repeated root)}", 
                   color=YELLOW, font_size=28),
            Text("• 一次独立な固有ベクトルが1つしか存在しない", color=WHITE, font_size=22),
            Text("• 対角化は不可能", color=RED, font_size=22, weight=BOLD),
            Text("• ジョルダン標準形への変換が限界", color=GREEN, font_size=22),
            MathTex(r"J = \begin{pmatrix} -\omega_n & 1 \\ 0 & -\omega_n \end{pmatrix}", 
                   color=GREEN, font_size=26),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        math_structure3.shift(UP * 0.1)
        
        for item in math_structure3:
            self.play(Write(item), run_time=0.5)
            self.wait(0.2)
        
        self.wait(0.8)

        # 物理的挙動へ
        self.play(
            FadeOut(condition3), FadeOut(math_title3),
            FadeOut(math_structure3),
        )
        self.wait(0.3)

        phys_title3 = Text("物理的挙動：", color=GOLD, font_size=26, weight=BOLD)
        phys_title3.shift(UP * 2.3)
        self.play(Write(phys_title3), run_time=0.6)
        self.wait(0.4)

        phys_desc3 = Text(
            "バネとダンパのペースが完全に調和した奇跡のバランス点",
            color=ORANGE, font_size=24,
        )
        phys_desc3.shift(UP * 1.6)
        self.play(Write(phys_desc3), run_time=0.7)
        self.wait(0.5)

        mode_decomp3 = VGroup(
            Text("独立したモードとして分解できず、", color=WHITE, font_size=22),
            Text("モード間で一方向のカスケード接続（主従関係）が発生", color=BLUE, font_size=20),
            Text("→ 時間応答に t·e^(-ωₙt) という積分項が出現", color=TEAL, font_size=20),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        mode_decomp3.shift(UP * 0.7)
        
        for item in mode_decomp3:
            self.play(Write(item), run_time=0.5)
            self.wait(0.3)
        
        self.wait(0.6)

        key_feature3 = VGroup(
            Text("エネルギーの流れ：", color=GREEN, font_size=22, weight=BOLD),
            Text("  ばね → 質量 → ダンパ", color=GREEN, font_size=20),
            Text("→ 振動を起こさず、かつ最速で目標値に収束", color=GREEN, font_size=22, weight=BOLD),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        key_feature3.shift(DOWN * 0.3)
        
        for item in key_feature3:
            self.play(Write(item), run_time=0.5)
            self.wait(0.3)
        
        self.wait(1.0)

        # グラフィック表示のための準備
        self.play(
            FadeOut(mode_decomp3), FadeOut(key_feature3),
        )
        self.wait(0.3)

        self.play(
            phys_title3.animate.shift(UP * 0.5).scale(0.85),
            phys_desc3.animate.shift(UP * 0.5).scale(0.85),
            run_time=0.5
        )
        self.wait(0.2)

        # マスバネダンパ系を再作成（臨界減衰のシミュレーション用）
        # パラメータ設定
        m3, k3 = 1.0, 4.0
        gamma3 = 2*np.sqrt(k3*m3)  # 臨界減衰条件: γ² = 4km
        
        # 初期条件
        x0_3 = 1.5
        v0_3 = 0.0
        
        # 固有値（重根）
        omega_n = np.sqrt(k3/m3)
        
        # 時間応答関数
        def x_critical(t):
            # 臨界減衰の解：(c1 + c2*t)*exp(-ωₙ*t)
            c1 = x0_3
            c2 = v0_3 + omega_n*x0_3
            return (c1 + c2*t) * np.exp(-omega_n * t)
        
        # マスバネダンパ系の作成
        wall_sim3 = Line(
            start=UP * 1.0 + LEFT * 5,
            end=DOWN * 1.0 + LEFT * 5,
            color=GREY,
            stroke_width=8,
        )
        
        hatches_sim3 = VGroup()
        for i in range(6):
            hatch = Line(
                start=LEFT * 5 + UP * (1.0 - i * 0.33) + LEFT * 0.3,
                end=LEFT * 5 + UP * (0.67 - i * 0.33),
                color=GREY,
                stroke_width=3,
            )
            hatches_sim3.add(hatch)
        
        mass_sim3 = Square(side_length=0.6, color=RED, fill_opacity=0.7)
        mass_label_sim3 = MathTex("m", color=WHITE, font_size=28)
        
        floor_sim3 = Line(
            start=LEFT * 6 + DOWN * 0.4,
            end=RIGHT * 2 + DOWN * 0.4,
            color=GREY,
            stroke_width=4,
        )
        
        floor_hatches_sim3 = VGroup()
        for i in range(32):
            hatch = Line(
                start=LEFT * 6 + RIGHT * (i * 0.25) + DOWN * 0.4,
                end=LEFT * 6 + RIGHT * (i * 0.25) + LEFT * 0.15 + DOWN * 0.65,
                color=GREY,
                stroke_width=2,
            )
            floor_hatches_sim3.add(hatch)
        
        axis_y_pos_sim3 = DOWN * 0.8
        axis_arrow_sim3 = Arrow(
            start=LEFT * 5 + axis_y_pos_sim3,
            end=RIGHT * 1 + axis_y_pos_sim3,
            color=YELLOW,
            buff=0,
            stroke_width=3,
        )
        axis_label_sim3 = MathTex("x", color=YELLOW, font_size=28)
        axis_label_sim3.next_to(axis_arrow_sim3, RIGHT, buff=0.1)
        
        origin_mark_sim3 = Line(
            spring_natural_pos_sim + axis_y_pos_sim3 + UP * 0.15,
            spring_natural_pos_sim + axis_y_pos_sim3 + DOWN * 0.15,
            color=YELLOW,
            stroke_width=4,
        )
        origin_label_sim3 = MathTex("0", color=YELLOW, font_size=24)
        origin_label_sim3.next_to(spring_natural_pos_sim + axis_y_pos_sim3, DOWN, buff=0.2)
        
        system_diagram_sim3 = VGroup(
            wall_sim3, hatches_sim3, floor_sim3, floor_hatches_sim3,
            axis_arrow_sim3, axis_label_sim3, origin_mark_sim3, origin_label_sim3,
        )
        system_diagram_sim3.shift(DOWN * 1.3)
        
        self.play(Create(system_diagram_sim3), run_time=0.6)
        self.wait(0.3)
        
        # 初期位置に質量を配置
        x_initial_3 = spring_natural_pos_sim[0] + x0_3
        spring_initial_3 = self.create_spring(
            LEFT * 5, 
            [x_initial_3, spring_natural_pos_sim[1], 0],
            color=BLUE, 
            num_coils=12
        )
        spring_initial_3.shift(DOWN * 1.3)
        
        mass_sim3.move_to([x_initial_3 + 0.3, spring_natural_pos_sim[1], 0])
        mass_sim3.shift(DOWN * 1.3)
        mass_label_sim3.move_to(mass_sim3.get_center())
        
        self.play(Create(spring_initial_3), FadeIn(mass_sim3), Write(mass_label_sim3), run_time=0.5)
        self.wait(0.5)

        # 時間経過のアニメーション
        time_label_3 = Text("t = 0.0 s", color=WHITE, font_size=22)
        time_label_3.shift(DOWN * 3.2 + LEFT * 4.5)
        self.play(Write(time_label_3), run_time=0.3)
        self.wait(0.3)

        # アニメーション実行
        dt_3 = 0.04
        total_time_3 = 4.0
        spring_mobject_3 = spring_initial_3
        
        for t in np.arange(dt_3, total_time_3, dt_3):
            x_t = x_critical(t)
            x_pos = spring_natural_pos_sim[0] + x_t
            
            new_spring = self.create_spring(
                LEFT * 5,
                [x_pos, spring_natural_pos_sim[1], 0],
                color=BLUE,
                num_coils=12
            )
            new_spring.shift(DOWN * 1.3)
            
            new_time_label = Text(f"t = {t:.1f} s", color=WHITE, font_size=22)
            new_time_label.shift(DOWN * 3.2 + LEFT * 4.5)
            
            self.play(
                Transform(spring_mobject_3, new_spring),
                mass_sim3.animate.move_to([x_pos + 0.3, spring_natural_pos_sim[1] - 1.3, 0]),
                mass_label_sim3.animate.move_to([x_pos + 0.3, spring_natural_pos_sim[1] - 1.3, 0]),
                Transform(time_label_3, new_time_label),
                run_time=dt_3,
                rate_func=linear,
            )
        
        self.wait(1.0)

        conclusion3 = Text(
            "最速で収束（振動なし）",
            color=GREEN, font_size=24, weight=BOLD,
        )
        conclusion3.shift(DOWN * 3.2 + RIGHT * 2.5)
        self.play(Write(conclusion3), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(phys_title3), FadeOut(phys_desc3),
            FadeOut(system_diagram_sim3), FadeOut(spring_mobject_3),
            FadeOut(mass_sim3), FadeOut(mass_label_sim3),
            FadeOut(time_label_3), FadeOut(conclusion3),
        )
        self.wait(0.3)

        # ============================================================
        # Part 6: 3つのパターンの比較
        # ============================================================
        subtitle6 = Text("3つのパターンの比較", font_size=28, color=BLUE)
        subtitle6.next_to(title, DOWN)
        self.play(Transform(subtitle0, subtitle6), run_time=0.5)
        self.wait(0.4)

        # comparison_title = Text(
        #     "固有値の性質がシステムの応答を決定する",
        #     color=ORANGE, font_size=26, weight=BOLD,
        # )
        # comparison_title.shift(UP * 2.8)
        # self.play(Write(comparison_title), run_time=0.7)
        # self.wait(0.5)

        # グラフの作成
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[-0.4, 1.6, 0.5],
            x_length=8,
            y_length=3.5,
            axis_config={"color": GREY},
            tips=False,
        )
        axes.shift(DOWN * 0.5)
        
        # 軸ラベル
        x_label = MathTex("t", font_size=28, color=YELLOW)
        x_label.next_to(axes.x_axis, RIGHT, buff=0.2)
        y_label = MathTex("x(t)", font_size=28, color=YELLOW)
        y_label.next_to(axes.y_axis, UP, buff=0.2)
        
        self.play(Create(axes), Write(x_label), Write(y_label), run_time=0.8)
        self.wait(0.4)

        # 各パターンの時間応答関数を定義
        # パターン1: 過減衰 (m=1.0, k=1.0, gamma=4.0)
        m1, k1, gamma1 = 1.0, 1.0, 4.0
        x0 = 1.5
        v0 = 0.0
        discriminant1 = (gamma1/(2*m1))**2 - k1/m1
        lambda1_1 = -gamma1/(2*m1) + np.sqrt(discriminant1)
        lambda2_1 = -gamma1/(2*m1) - np.sqrt(discriminant1)
        c1_1 = (v0 - lambda2_1*x0)/(lambda1_1 - lambda2_1)
        c2_1 = (lambda1_1*x0 - v0)/(lambda1_1 - lambda2_1)
        
        def overdamped_response(t):
            return c1_1 * np.exp(lambda1_1 * t) + c2_1 * np.exp(lambda2_1 * t)
        
        # パターン2: 減衰振動 (m=1.0, k=4.0, gamma=0.5)
        m2, k2, gamma2 = 1.0, 4.0, 0.5
        alpha2 = gamma2/(2*m2)
        omega2 = np.sqrt(k2/m2 - (gamma2/(2*m2))**2)
        A2 = x0
        B2 = (v0 + alpha2*x0)/omega2
        
        def underdamped_response(t):
            return np.exp(-alpha2 * t) * (A2 * np.cos(omega2 * t) + B2 * np.sin(omega2 * t))
        
        # パターン3: 臨界減衰 (m=1.0, k=4.0, gamma=2*sqrt(km))
        m3, k3 = 1.0, 4.0
        gamma3 = 2*np.sqrt(k3*m3)
        omega_n3 = np.sqrt(k3/m3)
        c1_3 = x0
        c2_3 = v0 + omega_n3*x0
        
        def critical_response(t):
            return (c1_3 + c2_3*t) * np.exp(-omega_n3 * t)

        # グラフのプロット
        graph_overdamped = axes.plot(overdamped_response, color=BLUE, x_range=[0, 6])
        label_overdamped = Text("過減衰", color=BLUE, font_size=22)
        label_overdamped.next_to(axes.c2p(6, overdamped_response(6)), RIGHT, buff=0.2)
        
        self.play(Create(graph_overdamped), Write(label_overdamped), run_time=0.8)
        self.wait(0.5)

        graph_underdamped = axes.plot(underdamped_response, color=TEAL, x_range=[0, 6])
        label_underdamped = Text("減衰振動", color=TEAL, font_size=22)
        label_underdamped.next_to(axes.c2p(6, underdamped_response(6)), RIGHT, buff=0.2)
        
        self.play(Create(graph_underdamped), Write(label_underdamped), run_time=0.8)
        self.wait(0.5)

        graph_critical = axes.plot(critical_response, color=GOLD, x_range=[0, 6])
        label_critical = Text("臨界減衰", color=GOLD, font_size=22)
        label_critical.next_to(axes.c2p(6, critical_response(6)), RIGHT, buff=0.2)
        
        self.play(Create(graph_critical), Write(label_critical), run_time=0.8)
        self.wait(1.0)

        # 特徴の説明
        feature_note = VGroup(
            Text("• 臨界減衰：振動せず最速で収束", color=GOLD, font_size=20),
            Text("• 過減衰：振動せずゆっくり収束", color=BLUE, font_size=20),
            Text("• 減衰振動：振動しながら収束", color=TEAL, font_size=20),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        feature_note.shift(DOWN * 3.2 + LEFT * 4)
        
        for item in feature_note:
            self.play(Write(item), run_time=0.5)
            self.wait(0.3)
        
        self.wait(1.5)

        # key_insight = Text(
        #     "固有値が決まれば、システムの性質が数学的に決定される！",
        #     color=GREEN, font_size=24, weight=BOLD,
        # )
        # key_insight.shift(DOWN * 3.2 + RIGHT * 2.5)
        # self.play(Write(key_insight), run_time=0.8)
        # self.wait(1.5)

        self.play(
            FadeOut(subtitle6),
            # FadeOut(comparison_title),
            FadeOut(axes), FadeOut(x_label), FadeOut(y_label),
            FadeOut(graph_overdamped), FadeOut(graph_underdamped), FadeOut(graph_critical),
            FadeOut(label_overdamped), FadeOut(label_underdamped), FadeOut(label_critical),
            FadeOut(feature_note), # FadeOut(key_insight),
        )
        self.wait(0.3)

        # ============================================================
        # Part 8: まとめ
        # ============================================================
        # subtitle8 = Text("まとめ", font_size=36, color=GOLD)
        # subtitle8.next_to(title, DOWN)
        # self.play(Transform(subtitle0, subtitle8), run_time=0.6)
        # self.wait(0.4)

        # summary = VGroup(
        #     Text("• 行列の対角化は、システムをモード分解する強力な手法", color=WHITE, font_size=24),
        #     Text("• 固有値の性質が、システムの応答パターンを決定する", color=WHITE, font_size=24),
        #     Text("  - 実数で異なる → 過減衰（振動なし、遅い）", color=BLUE, font_size=22),
        #     Text("  - 複素共役 → 減衰振動（振動あり）", color=TEAL, font_size=22),
        #     Text("  - 実数の重根 → 臨界減衰（振動なし、最速）", color=GOLD, font_size=22),
        #     Text("• 対角化できない場合も、ジョルダン標準形で評価可能", color=WHITE, font_size=24),
        #     Text("• 制御工学では、この理論を応用してシステムを設計", color=GREEN, font_size=24),
        # ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        # summary.shift(UP * 0.3)
        
        # for row in summary:
        #     self.play(Write(row), run_time=0.5)
        #     self.wait(0.3)
        
        # self.wait(1.0)

        # final_message = Text(
        #     "数学の理論が実システムの解析・設計に直結している！",
        #     color=YELLOW, font_size=26, weight=BOLD,
        # )
        # final_message.shift(DOWN * 2.5)
        # self.play(Write(final_message), run_time=0.8)
        # self.wait(2.0)

        # self.play(
        #     FadeOut(VGroup(
        #         title, subtitle0, summary, final_message
        #     )),
        #     run_time=1.0
        # )
        # self.wait(0.5)


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
