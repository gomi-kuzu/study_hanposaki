from manim import *

class OrthogonalBasisAdvantage(ThreeDScene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"
        
        # タイトル
        title = Text("直交基底の便利さ", font_size=40, color=WHITE)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)
        
        # === イントロ: 問題提起 ===
        intro_subtitle = Text("座標を求める2つの方法", font_size=32, color=YELLOW)
        intro_subtitle.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(intro_subtitle)
        self.play(Write(intro_subtitle), run_time=0.6)
        self.wait(0.5)
        
        intro_text = VGroup(
            Text("あるベクトルを基底で表現したい", color=WHITE, font_size=26),
            Text("一般の基底 vs 直交基底", color=YELLOW, font_size=26, weight=BOLD),
            Text("どちらが計算しやすい?", color=WHITE, font_size=26),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        intro_text.shift(DOWN * 0.5)
        self.add_fixed_in_frame_mobjects(intro_text)
        
        self.play(Write(intro_text), run_time=1.0)
        self.wait(1.2)
        
        self.play(FadeOut(intro_text), FadeOut(intro_subtitle))
        self.wait(0.3)
        
        # === パート1: 一般の基底での座標計算 ===
        subtitle1 = Text("ケース1: 一般の基底", font_size=28, color=RED)
        subtitle1.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle1)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.5)
        
        # 問題設定
        problem_title = Text("問題設定", color=WHITE, font_size=26, weight=BOLD)
        problem_title.shift(UP * 2.2)
        self.add_fixed_in_frame_mobjects(problem_title)
        self.play(Write(problem_title), run_time=0.5)
        self.wait(0.3)
        
        # 基底とベクトル
        basis_label = Text("基底:", color=WHITE, font_size=26)
        basis_math = MathTex(r"\mathbf{e}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \quad"
                           r"\mathbf{e}_2 = \begin{bmatrix} 1 \\ 2 \end{bmatrix}",
                           color=WHITE, font_size=26)
        basis_line = VGroup(basis_label, basis_math).arrange(RIGHT, buff=0.2)

        vector_label = Text("座標ベクトル:", color=WHITE, font_size=26)
        vector_math = MathTex(r"\mathbf{v} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}",
                            color=WHITE, font_size=26)
        vector_line = VGroup(vector_label, vector_math).arrange(RIGHT, buff=0.2)
        
        basis_and_vector = VGroup(basis_line, vector_line).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        basis_and_vector.shift(UP)
        self.add_fixed_in_frame_mobjects(basis_and_vector)
        self.play(Write(basis_and_vector), run_time=1.0)
        self.wait(0.8)
        
        # 求めたいもの
        goal_text = Text("求めたいのは…", color=WHITE, font_size=23, weight=BOLD)
        self.add_fixed_in_frame_mobjects(goal_text)
        self.play(Write(goal_text), run_time=0.5)
        self.wait(0.3)
        
        goal_eq = MathTex(
            r"\mathbf{v} = c_1 \mathbf{e}_1 + c_2 \mathbf{e}_2",
            color=WHITE, font_size=28
        )
        goal_eq.shift(DOWN * 0.5)
        self.add_fixed_in_frame_mobjects(goal_eq)
        self.play(Write(goal_eq), run_time=0.7)
        self.wait(0.6)
        
        coefficients_text = Text("としたときの係数 c₁, c₂", color=WHITE, font_size=24, slant=ITALIC)
        coefficients_text.shift(DOWN * 1.1)
        self.add_fixed_in_frame_mobjects(coefficients_text)
        self.play(Write(coefficients_text), run_time=0.6)
        self.wait(0.8)
        
        # 連立方程式
        system_title = Text("なので、連立方程式を解く！", color=ORANGE, font_size=26, weight=BOLD)
        system_title.shift(DOWN * 1.8)
        self.add_fixed_in_frame_mobjects(system_title)
        self.play(Write(system_title), run_time=0.5)
        self.wait(0.3)
        
        system_eq = MathTex(
            r"\begin{cases} c_1 \cdot 1 + c_2 \cdot 1 = 3 \\ c_1 \cdot 0 + c_2 \cdot 2 = 4 \end{cases}",
            color=WHITE, font_size=28
        )
        system_eq.shift(DOWN * 2.7)
        self.add_fixed_in_frame_mobjects(system_eq)
        self.play(Write(system_eq), run_time=0.8)
        self.wait(1.0)
        
        # 解く過程
        # solving_note = Text(
        #     "連立方程式を解く必要がある...",
        #     color=RED, font_size=24, slant=ITALIC, weight=BOLD
        # )
        # solving_note.shift(DOWN * 3.5)
        # self.add_fixed_in_frame_mobjects(solving_note)
        # self.play(Write(solving_note), run_time=0.7)
        # self.wait(1.2)
        
        self.play(
            FadeOut(problem_title), FadeOut(basis_and_vector),
            FadeOut(goal_text), FadeOut(goal_eq),
            FadeOut(coefficients_text), FadeOut(system_title),
            FadeOut(system_eq), FadeOut(subtitle1)
        )
        self.wait(0.3)
        
        # === パート2: 直交基底での座標計算 ===
        subtitle2 = Text("ケース2: 直交基底", font_size=28, color=GREEN)
        subtitle2.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle2)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)
        
        # 問題設定（直交基底）
        problem_title2 = Text("問題設定", color=WHITE, font_size=26, weight=BOLD)
        problem_title2.shift(UP * 2.2)
        self.add_fixed_in_frame_mobjects(problem_title2)
        self.play(Write(problem_title2), run_time=0.5)
        self.wait(0.3)
        
        # 直交基底とベクトル
        ortho_basis_label = Text("直交基底:", color=WHITE, font_size=26)
        ortho_basis_math = MathTex(r"\mathbf{u}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \quad"
                                 r"\mathbf{u}_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}",
                                 color=WHITE, font_size=26)
        ortho_basis_line = VGroup(ortho_basis_label, ortho_basis_math).arrange(RIGHT, buff=0.2)
        
        ortho_vector_label = Text("座標ベクトル:", color=WHITE, font_size=26)
        ortho_vector_math = MathTex(r"\mathbf{v} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}",
                                  color=WHITE, font_size=26)
        ortho_vector_line = VGroup(ortho_vector_label, ortho_vector_math).arrange(RIGHT, buff=0.2)
        
        ortho_basis_and_vector = VGroup(ortho_basis_line, ortho_vector_line).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        ortho_basis_and_vector.shift(UP * 1.2)
        self.add_fixed_in_frame_mobjects(ortho_basis_and_vector)
        self.play(Write(ortho_basis_and_vector), run_time=1.0)
        self.wait(0.8)
        
        # 直交性の確認
        orthogonality_check = MathTex(
            r"\langle \mathbf{u}_1 | \mathbf{u}_2 \rangle = 0 \quad \checkmark",
            color=GREEN, font_size=24
        )
        orthogonality_check.shift(UP * 0.2)
        self.add_fixed_in_frame_mobjects(orthogonality_check)
        self.play(Write(orthogonality_check), run_time=0.6)
        self.wait(0.6)
        
        # 魔法の公式
        magic_title = Text("直交基底の魔法の公式:", color=GOLD, font_size=26, weight=BOLD)
        magic_title.shift(DOWN * 0.4)
        self.add_fixed_in_frame_mobjects(magic_title)
        self.play(Write(magic_title), run_time=0.6)
        self.wait(0.4)
        
        magic_formula = MathTex(
            r"c_i = \frac{\langle \mathbf{v} | \mathbf{u}_i \rangle}{\langle \mathbf{u}_i | \mathbf{u}_i \rangle}",
            color=GOLD, font_size=36
        )
        magic_formula.shift(DOWN * 1.4)
        
        # 枠で囲む
        magic_box = SurroundingRectangle(magic_formula, color=GOLD, buff=0.2)
        
        self.add_fixed_in_frame_mobjects(magic_formula)
        self.play(Write(magic_formula), run_time=0.8)
        self.wait(0.5)
        self.add_fixed_in_frame_mobjects(magic_box)
        self.play(Create(magic_box), run_time=0.5)
        self.wait(0.8)
        
        # 計算
        calc_title = Text("計算:", color=WHITE, font_size=24, weight=BOLD)
        calc_title.shift(DOWN * 2.5 + LEFT *2.5)
        self.add_fixed_in_frame_mobjects(calc_title)
        self.play(Write(calc_title), run_time=0.5)
        self.wait(0.3)
        
        calculations = VGroup(
            MathTex(r"c_1 = \frac{\langle \mathbf{v} | \mathbf{u}_1 \rangle}{\langle \mathbf{u}_1 | \mathbf{u}_1 \rangle} = \frac{3}{1} = 3",
                   color=WHITE, font_size=24),
            MathTex(r"c_2 = \frac{\langle \mathbf{v} | \mathbf{u}_2 \rangle}{\langle \mathbf{u}_2 | \mathbf{u}_2 \rangle} = \frac{4}{1} = 4",
                   color=WHITE, font_size=24),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        calculations.shift(DOWN * 3.2)
        self.add_fixed_in_frame_mobjects(calculations)
        self.play(Write(calculations), run_time=1.0)
        self.wait(1.0)
        
        # 結論
        easy_note = Text(
            "連立方程式を解かなくていい!",
            color=GREEN, font_size=26, slant=ITALIC, weight=BOLD
        )
        easy_note.to_corner(DR).shift(UP * 0.5)
        self.add_fixed_in_frame_mobjects(easy_note)
        self.play(Write(easy_note), run_time=0.7)
        self.wait(1.5)
        
        self.play(
            FadeOut(problem_title2), FadeOut(ortho_basis_and_vector),
            FadeOut(orthogonality_check), FadeOut(magic_title),
            FadeOut(magic_formula), FadeOut(magic_box),
            FadeOut(calc_title), FadeOut(calculations),
            FadeOut(easy_note), FadeOut(subtitle2)
        )
        self.wait(0.3)
        
        # === パート3: なぜこの公式が成り立つか ===
        subtitle3 = Text("なぜこの公式が成り立つ?", font_size=32, color=PURPLE)
        subtitle3.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle3)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.5)
        
        # 一般の表現
        general_expr = MathTex(
            r"\mathbf{v} = c_1 \mathbf{u}_1 + c_2 \mathbf{u}_2",
            color=WHITE, font_size=32
        )
        general_expr.shift(UP * 1.8)
        self.add_fixed_in_frame_mobjects(general_expr)
        self.play(Write(general_expr), run_time=0.7)
        self.wait(0.6)
        
        # 両辺とu1の内積をとる
        step1_text = Text("両辺と u₁ の内積をとる:", color=ORANGE, font_size=26, weight=BOLD)
        step1_text.shift(UP * 1.0)
        self.add_fixed_in_frame_mobjects(step1_text)
        self.play(Write(step1_text), run_time=0.6)
        self.wait(0.4)
        
        step1_eq = MathTex(
            r"\langle \mathbf{v} | \mathbf{u}_1 \rangle = c_1 \langle \mathbf{u}_1 | \mathbf{u}_1 \rangle + c_2 \langle \mathbf{u}_2 | \mathbf{u}_1 \rangle",
            color=WHITE, font_size=28
        )
        step1_eq.shift(UP * 0.3)
        self.add_fixed_in_frame_mobjects(step1_eq)
        self.play(Write(step1_eq), run_time=1.0)
        self.wait(0.8)
        
        # 直交性を使う
        ortho_note = Text("直交性より:", color=GREEN, font_size=24, weight=BOLD)
        ortho_note.shift(DOWN * 0.5)
        self.add_fixed_in_frame_mobjects(ortho_note)
        self.play(Write(ortho_note), run_time=0.5)
        self.wait(0.3)
        
        ortho_eq = MathTex(
            r"\langle \mathbf{u}_2 | \mathbf{u}_1 \rangle = 0",
            color=GREEN, font_size=28
        )
        ortho_eq.shift(DOWN * 1.0)
        self.add_fixed_in_frame_mobjects(ortho_eq)
        self.play(Write(ortho_eq), run_time=0.7)
        self.wait(0.6)
        
        # 簡略化
        simplified_eq = MathTex(
            r"\langle \mathbf{v} | \mathbf{u}_1 \rangle = c_1 \langle \mathbf{u}_1 | \mathbf{u}_1 \rangle",
            color=YELLOW, font_size=28
        )
        simplified_eq.shift(DOWN * 1.8)
        self.add_fixed_in_frame_mobjects(simplified_eq)
        self.play(Write(simplified_eq), run_time=0.8)
        self.wait(0.8)
        
        # 結論
        final_formula = MathTex(
            r"\therefore c_1 = \frac{\langle \mathbf{v} | \mathbf{u}_1 \rangle}{\langle \mathbf{u}_1 | \mathbf{u}_1 \rangle}",
            color=GOLD, font_size=32
        )
        final_formula.shift(DOWN * 2.7 + LEFT * 1.0)
        self.add_fixed_in_frame_mobjects(final_formula)
        self.play(Write(final_formula), run_time=0.8)
        self.wait(1.2)
        
        key_point = Text(
            "直交性により、他の基底の影響が消える!",
            color=GREEN, font_size=24, slant=ITALIC, weight=BOLD
        )
        key_point.to_corner(DR).shift(UP * 0.5)
        self.add_fixed_in_frame_mobjects(key_point)
        self.play(Write(key_point), run_time=0.8)
        self.wait(1.5)
        
        self.play(
            FadeOut(general_expr), FadeOut(step1_text),
            FadeOut(step1_eq), FadeOut(ortho_note),
            FadeOut(ortho_eq), FadeOut(simplified_eq),
            FadeOut(final_formula), FadeOut(key_point),
            FadeOut(subtitle3)
        )
        self.wait(0.3)
        
        # === パート4: 3次元での比較 ===
        subtitle4 = Text("3次元での比較", font_size=32, color=TEAL)
        subtitle4.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle4)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.5)
        
        # 一般の基底
        general_3d_title = Text("一般の基底:", color=RED, font_size=26, weight=BOLD)
        general_3d_title.shift(UP * 2.0)
        self.add_fixed_in_frame_mobjects(general_3d_title)
        self.play(Write(general_3d_title), run_time=0.5)
        self.wait(0.3)
        
        general_3d_desc = Text("3元連立方程式を解く", color=RED, font_size=24)
        general_3d_math = MathTex(r"\begin{cases} a_{11}c_1 + a_{12}c_2 + a_{13}c_3 = v_1 \\ "
                                 r"a_{21}c_1 + a_{22}c_2 + a_{23}c_3 = v_2 \\ "
                                 r"a_{31}c_1 + a_{32}c_2 + a_{33}c_3 = v_3 \end{cases}",
                                 color=WHITE, font_size=22)
        general_3d_system = VGroup(general_3d_desc, general_3d_math).arrange(DOWN, buff=0.3)
        general_3d_system.shift(UP * 0.8)
        self.add_fixed_in_frame_mobjects(general_3d_system)
        self.play(Write(general_3d_system), run_time=1.0)
        self.wait(0.8)
        
        # 矢印
        vs_arrow = Text("vs", color=YELLOW, font_size=32, weight=BOLD)
        vs_arrow.shift(DOWN * 0.3)
        self.add_fixed_in_frame_mobjects(vs_arrow)
        self.play(Write(vs_arrow), run_time=0.5)
        self.wait(0.4)
        
        # 直交基底
        ortho_3d_title = Text("直交基底:", color=GREEN, font_size=26, weight=BOLD)
        ortho_3d_title.shift(DOWN * 1.2)
        self.add_fixed_in_frame_mobjects(ortho_3d_title)
        self.play(Write(ortho_3d_title), run_time=0.5)
        self.wait(0.3)
        
        ortho_3d_desc = Text("内積を3回計算するだけ", color=GREEN, font_size=24)
        ortho_3d_math = MathTex(r"c_1 = \frac{\langle \mathbf{v} | \mathbf{u}_1 \rangle}{\langle \mathbf{u}_1 | \mathbf{u}_1 \rangle}, \quad "
                               r"c_2 = \frac{\langle \mathbf{v} | \mathbf{u}_2 \rangle}{\langle \mathbf{u}_2 | \mathbf{u}_2 \rangle}, \quad "
                               r"c_3 = \frac{\langle \mathbf{v} | \mathbf{u}_3 \rangle}{\langle \mathbf{u}_3 | \mathbf{u}_3 \rangle}",
                               color=WHITE, font_size=20)
        ortho_3d_calc = VGroup(ortho_3d_desc, ortho_3d_math).arrange(DOWN, buff=0.3)
        ortho_3d_calc.shift(DOWN * 2.2)
        self.add_fixed_in_frame_mobjects(ortho_3d_calc)
        self.play(Write(ortho_3d_calc), run_time=1.0)
        self.wait(1.0)
        
        # 結論
        advantage_note = Text(
            "次元が大きくなるほど直交基底の利点が顕著に!",
            color=GOLD, font_size=24, slant=ITALIC, weight=BOLD
        )
        advantage_note.to_corner(DR)
        self.add_fixed_in_frame_mobjects(advantage_note)
        self.play(Write(advantage_note), run_time=0.8)
        self.wait(1.5)
        
        self.play(
            FadeOut(general_3d_title), FadeOut(general_3d_system),
            FadeOut(vs_arrow), FadeOut(ortho_3d_title),
            FadeOut(ortho_3d_calc), FadeOut(advantage_note),
            FadeOut(subtitle4)
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
                Text("一般の基底: 連立方程式を解く必要がある", color=RED, font_size=24),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("2.", color=WHITE, font_size=26, weight=BOLD),
                Text("直交基底: 内積だけで係数が求まる", color=GREEN, font_size=24),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("3.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    MathTex(r"c_i = \frac{\langle \mathbf{v} | \mathbf{u}_i \rangle}{\langle \mathbf{u}_i | \mathbf{u}_i \rangle}", 
                           color=GOLD, font_size=24),
                ),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("4.", color=WHITE, font_size=26, weight=BOLD),
                Text("直交性により他の基底の影響が消える", color=YELLOW, font_size=24),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("5.", color=WHITE, font_size=26, weight=BOLD),
                Text("高次元ほど計算が楽になる", color=BLUE, font_size=24),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        summary_points.shift(UP * 0.2)
        self.add_fixed_in_frame_mobjects(summary_points)
        
        for point in summary_points:
            self.play(Write(point), run_time=0.6)
            self.wait(0.4)
        
        self.wait(0.5)
        
        # 最終メッセージ
        final_message = Text(
            "直交基底は計算を簡単にする",
            color=YELLOW, font_size=28, weight=BOLD, slant=ITALIC
        )
        final_message.shift(DOWN * 3.0)
        self.add_fixed_in_frame_mobjects(final_message)
        self.play(Write(final_message), run_time=0.8)
        self.wait(1.5)
        
        self.wait(2.0)
        
        # フェードアウト
        all_objects = VGroup(
            title, summary_subtitle, summary_points, final_message
        )
        self.play(FadeOut(all_objects), run_time=1.0)
        self.wait(0.5)
