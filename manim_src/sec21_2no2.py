from manim import *
import numpy as np


class NumericalMethodsComparison(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        title = Text("数値解法の精度の比較", font_size=36, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.7)

        # ============================================================
        # Part 1: 線形システムへの適用
        # ============================================================
        subtitle1 = Text("線形システムへの適用", font_size=28, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.4)

        intro_text = Text(
            "前回紹介した数値解法を線形システムに適用してみる",
            color=WHITE, font_size=26,
        )
        intro_text.shift(UP * 1.8)
        self.play(Write(intro_text), run_time=0.8)
        self.wait(0.6)

        system_title = Text(
            "解きたい連立微分方程式：",
            color=WHITE, font_size=26,
        )
        system_title.shift(UP * 1.0)
        self.play(Write(system_title), run_time=0.7)
        self.wait(0.4)

        system_eq = MathTex(
            r"\frac{d}{dt}\mathbf{x} = L\mathbf{x}(t)",
            color=YELLOW,
            font_size=40,
        )
        system_eq.shift(UP * 0.3)
        # system_box = SurroundingRectangle(system_eq, color=YELLOW, buff=0.25)
        self.play(Write(system_eq), run_time=0.8)
        self.wait(0.8)

        note_text = Text(
            "この場合、f⃗(x⃗(t)) = Lx⃗(t) となる",
            color=TEAL, font_size=24,
        )
        note_text.shift(DOWN * 0.7)
        self.play(Write(note_text), run_time=0.7)
        self.wait(1.0)

        self.play(
            FadeOut(intro_text), FadeOut(system_title),
            FadeOut(note_text),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: オイラー法の適用
        # ============================================================
        subtitle2 = Text("オイラー法の適用", font_size=28, color=GOLD)
        subtitle2.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle2), run_time=0.5)
        self.wait(0.4)

        # system_eqを上に移動
        self.play(
            system_eq.animate.shift(UP * 1.5).scale(0.85),
            # system_box.animate.shift(UP * 1.5).scale(0.85),
            run_time=0.6
        )
        self.wait(0.3)

        euler_general_title = Text(
            "オイラー法の一般形：",
            color=WHITE, font_size=26,
        )
        euler_general_title.shift(UP * 0.8)
        self.play(Write(euler_general_title), run_time=0.7)
        self.wait(0.4)

        euler_general = MathTex(
            r"\mathbf{x}(t+\Delta t) = \mathbf{x}(t) + \mathbf{f}(\mathbf{x}(t))\Delta t",
            color=WHITE,
            font_size=34,
        )
        euler_general.shift(UP * 0.1)
        self.play(Write(euler_general), run_time=0.7)
        self.wait(0.6)

        arrow1 = Text("↓", color=BLUE, font_size=32)
        arrow1.shift(DOWN * 0.5)
        self.play(Write(arrow1), run_time=0.4)
        self.wait(0.3)

        substitution_text = Text(
            "f⃗(x⃗(t)) = Lx⃗(t) を代入すると：",
            color=TEAL, font_size=24,
        )
        substitution_text.shift(DOWN * 1.0)
        self.play(Write(substitution_text), run_time=0.7)
        self.wait(0.5)

        euler_linear = MathTex(
            r"\mathbf{x}(t+\Delta t) = \mathbf{x}(t) + L\mathbf{x}(t)\Delta t",
            color=YELLOW,
            font_size=38,
        )
        euler_linear.shift(DOWN * 1.8)
        euler_box = SurroundingRectangle(euler_linear, color=YELLOW, buff=0.25)
        self.play(Write(euler_linear), Create(euler_box), run_time=0.8)
        self.wait(1.2)

        self.play(
            FadeOut(euler_general_title), FadeOut(euler_general),
            FadeOut(arrow1), FadeOut(substitution_text),
            FadeOut(system_eq), #FadeOut(system_box),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: ホイン法の適用
        # ============================================================
        subtitle3 = Text("ホイン法の適用", font_size=28, color=TEAL)
        subtitle3.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle3), run_time=0.5)
        self.wait(0.4)

        # 式を上に移動
        self.play(
            # system_eq.animate.shift(UP * 0.3 + LEFT * 2.0).scale(0.9),
            # system_box.animate.shift(UP * 0.3 + LEFT * 2.0).scale(0.9),
            euler_linear.animate.shift(UP * 3.5 + RIGHT * 4).scale(0.85),
            euler_box.animate.shift(UP * 3.5 + RIGHT * 4).scale(0.8),
            run_time=0.6
        )
        self.wait(0.3)

        heun_general_title = Text(
            "ホイン法の一般形：",
            color=WHITE, font_size=26,
        )
        heun_general_title.shift(UP * 0.8)
        self.play(Write(heun_general_title), run_time=0.7)
        self.wait(0.4)

        heun_general = MathTex(
            r"\mathbf{x}(t+\Delta t) = \mathbf{x}(t) + \frac{\Delta t}{2}\left(\mathbf{f}(\mathbf{x}(t)) + \mathbf{f}(\tilde{\mathbf{x}}(t+\Delta t))\right)",
            color=WHITE,
            font_size=28,
        )
        heun_general.shift(UP * 0.1)
        self.play(Write(heun_general), run_time=0.8)
        self.wait(0.6)

        heun_note = Text(
            "ここで、x̃(t+Δt) = x⃗(t) + Lx⃗(t)Δt",
            color=GRAY, font_size=22,
        )
        heun_note.shift(DOWN * 0.6)
        self.play(Write(heun_note), run_time=0.7)
        self.wait(0.5)

        arrow2 = Text("↓", color=BLUE, font_size=32)
        arrow2.shift(DOWN * 1.1)
        self.play(Write(arrow2), run_time=0.4)
        self.wait(0.3)

        heun_substitution_text = Text(
            "代入して整理すると：",
            color=TEAL, font_size=24,
        )
        heun_substitution_text.shift(DOWN * 1.6)
        self.play(Write(heun_substitution_text), run_time=0.7)
        self.wait(0.5)

        heun_linear = MathTex(
            r"\mathbf{x}(t+\Delta t) = \mathbf{x}(t) + L\mathbf{x}(t)\Delta t + L^2\mathbf{x}(t)\frac{(\Delta t)^2}{2}",
            color=GREEN,
            font_size=32,
        )
        heun_linear.shift(DOWN * 2.7)
        heun_box = SurroundingRectangle(heun_linear, color=GREEN, buff=0.25)
        self.play(Write(heun_linear), Create(heun_box), run_time=1.0)
        self.wait(1.5)

        self.play(
            FadeOut(heun_general_title), FadeOut(heun_general),
            FadeOut(heun_note), FadeOut(arrow2),
            FadeOut(heun_substitution_text),
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: 式の比較
        # ============================================================
        subtitle4 = Text("2つの手法の比較", font_size=28, color=BLUE)
        subtitle4.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle4), run_time=0.5)
        self.wait(0.4)

        # 式を整列
        self.play(
            euler_linear.animate.shift(LEFT * 1.5 + DOWN * 0.4).scale(1.1),
            euler_box.animate.shift(LEFT * 1.5 + DOWN * 0.4).scale(1.1),
            heun_linear.animate.shift(LEFT * 3.5 + UP * 4.1).scale(0.95),
            heun_box.animate.shift(LEFT * 3.5 + UP * 4.1).scale(0.9),
            run_time=0.8
        )
        self.wait(0.5)

        comparison_text = Text(
            "ホイン法には2次の項が含まれている",
            color=WHITE, font_size=26,
        )
        comparison_text.shift(UP * 0.3)
        self.play(Write(comparison_text), run_time=0.8)
        self.wait(0.6)

        highlight_term = MathTex(
            r"L^2\mathbf{x}(t)\frac{(\Delta t)^2}{2}",
            color=RED,
            font_size=36,
        )
        highlight_term.shift(DOWN * 0.8)
        highlight_box = SurroundingRectangle(highlight_term, color=RED, buff=0.25)
        self.play(Write(highlight_term), Create(highlight_box), run_time=0.8)
        self.wait(0.8)

        precision_note = Text(
            "この項が精度向上に寄与する",
            color=TEAL, font_size=26,
        )
        precision_note.shift(DOWN * 2)
        self.play(Write(precision_note), run_time=0.7)
        self.wait(1.0)

        self.play(
            FadeOut(comparison_text), FadeOut(highlight_term),
            FadeOut(highlight_box), FadeOut(precision_note),
            FadeOut(euler_linear), FadeOut(euler_box),
            FadeOut(heun_linear), FadeOut(heun_box),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: 数値実験の設定
        # ============================================================
        subtitle5 = Text("数値実験の設定", font_size=28, color=GOLD)
        subtitle5.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle5), run_time=0.5)
        self.wait(0.4)

        experiment_text = Text(
            "具体例で精度を比較してみる",
            color=WHITE, font_size=26,
        )
        experiment_text.shift(UP * 1.8)
        self.play(Write(experiment_text), run_time=0.7)
        self.wait(0.5)

        system_intro = Text(
            "バネマスダンパ系（m=1, k=3, γ=1/2）",
            color=TEAL, font_size=26,
        )
        system_intro.shift(UP * 1.2)
        self.play(Write(system_intro), run_time=0.7)
        self.wait(0.5)

        matrix_title = Text(
            "係数行列 L：",
            color=WHITE, font_size=26,
        )
        matrix_title.shift(UP * 0.5)
        self.play(Write(matrix_title), run_time=0.7)
        self.wait(0.4)

        matrix_L = MathTex(
            r"L = \begin{pmatrix} 0 & 1 \\ -3 & -\frac{1}{2} \end{pmatrix}",
            color=YELLOW,
            font_size=38,
        )
        matrix_L.shift(DOWN * 0.3)
        self.play(Write(matrix_L), run_time=0.8)
        self.wait(0.6)

        initial_title = Text(
            "初期値：",
            color=WHITE, font_size=26,
        )
        initial_title.shift(DOWN * 1.2)
        self.play(Write(initial_title), run_time=0.7)
        self.wait(0.4)

        initial_value = MathTex(
            r"\mathbf{x}(0) = \begin{pmatrix} 1 \\ 0 \end{pmatrix}",
            color=TEAL,
            font_size=38,
        )
        initial_value.shift(DOWN * 2.0)
        self.play(Write(initial_value), run_time=0.8)
        self.wait(0.6)

        timestep_title = Text(
            "時間刻み：",
            color=WHITE, font_size=26,
        )
        timestep_title.shift(DOWN * 2.7)
        self.play(Write(timestep_title), run_time=0.7)
        self.wait(0.4)

        timestep_value = MathTex(
            r"\Delta t = 0.1",
            color=ORANGE,
            font_size=38,
        )
        timestep_value.next_to(timestep_title, RIGHT, buff=0.3)
        self.play(Write(timestep_value), run_time=0.8)
        self.wait(1.0)

        self.play(
            FadeOut(experiment_text), FadeOut(system_intro),
            FadeOut(matrix_title), FadeOut(matrix_L),
            FadeOut(initial_title), FadeOut(initial_value),
            FadeOut(timestep_title), FadeOut(timestep_value),
        )
        self.wait(0.3)

        # ============================================================
        # Part 6: プロットの作成と比較
        # ============================================================
        subtitle6 = Text("解の可視化", font_size=28, color=TEAL)
        subtitle6.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle6), run_time=0.5)
        self.wait(0.4)

        plot_intro = Text(
            "3つの手法で計算した x₁(t) をプロット",
            color=WHITE, font_size=26,
        )
        plot_intro.shift(UP * 1.8)
        self.play(Write(plot_intro), run_time=0.8)
        self.wait(0.7)

        # 数値計算の準備（バネマスダンパ系: m=1, k=3, gamma=0.5）
        L = np.array([[0, 1], [-3, -0.5]])
        x0 = np.array([1, 0])  # 初期条件: 位置1, 速度0
        dt = 0.1
        t_max = 10.0
        t_values = np.arange(0, t_max + dt, dt)

        # 固有値と固有ベクトル
        lambda1 = (-1 + 1j * np.sqrt(47)) / 4
        lambda2 = (-1 - 1j * np.sqrt(47)) / 4
        v1 = np.array([1, lambda1])
        v2 = np.array([1, lambda2])
        
        # 係数を求める（P c = x0）
        P = np.column_stack([v1, v2])
        c = np.linalg.solve(P, x0)
        
        # 固有値展開（真の解）
        def exact_solution(t):
            return np.real(c[0] * np.exp(lambda1 * t) * v1[0] + c[1] * np.exp(lambda2 * t) * v2[0])

        # オイラー法
        def euler_method(L, x0, dt, t_max):
            t_values = np.arange(0, t_max + dt, dt)
            x_values = np.zeros((len(t_values), 2))
            x_values[0] = x0
            for i in range(1, len(t_values)):
                x_values[i] = x_values[i-1] + L @ x_values[i-1] * dt
            return t_values, x_values

        # ホイン法
        def heun_method(L, x0, dt, t_max):
            t_values = np.arange(0, t_max + dt, dt)
            x_values = np.zeros((len(t_values), 2))
            x_values[0] = x0
            for i in range(1, len(t_values)):
                x_current = x_values[i-1]
                x_values[i] = x_current + L @ x_current * dt + L @ L @ x_current * (dt**2) / 2
            return t_values, x_values

        # 計算実行
        t_euler, x_euler = euler_method(L, x0, dt, t_max)
        t_heun, x_heun = heun_method(L, x0, dt, t_max)
        x_exact = np.array([exact_solution(t) for t in t_values])
        
        # 位置成分（第1成分）を取得
        x_euler_pos = x_euler[:, 0]
        x_heun_pos = x_heun[:, 0]

        # グラフの作成
        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[-0.5, 1.2, 0.5],
            x_length=10,
            y_length=5,
            axis_config={"color": WHITE, "include_numbers": True},
            tips=False,
        )
        axes.scale(0.65).shift(DOWN * 0.8)

        x_label = axes.get_x_axis_label("t", direction=RIGHT, buff=0.2).scale(0.8)
        y_label = axes.get_y_axis_label("x(t)", direction=UP, buff=0.2).scale(0.8)

        self.play(
            FadeOut(plot_intro),
            Create(axes), Write(x_label), Write(y_label),
            run_time=1.0
        )
        self.wait(0.5)

        # プロットの作成
        # 固有値展開（真の解）
        exact_points = [axes.c2p(t_values[i], x_exact[i]) for i in range(len(t_values))]
        exact_line = VMobject(color=BLUE)
        exact_line.set_points_smoothly(exact_points)
        
        exact_label = Text("固有値展開", color=BLUE, font_size=20)
        exact_label.next_to(axes, UP).shift(LEFT * 3 + UP * 0.8 )
        
        self.play(Create(exact_line), Write(exact_label), run_time=1.0)
        self.wait(0.5)

        # ホイン法
        heun_points = [axes.c2p(t_heun[i], x_heun_pos[i]) for i in range(len(t_heun))]
        heun_line = VMobject(color=GREEN)
        heun_line.set_points_smoothly(heun_points)
        
        heun_label = Text("ホイン法", color=GREEN, font_size=20)
        heun_label.next_to(exact_label, RIGHT, buff=1)
        
        self.play(Create(heun_line), Write(heun_label), run_time=1.0)
        self.wait(0.5)

        # オイラー法
        euler_points = [axes.c2p(t_euler[i], x_euler_pos[i]) for i in range(len(t_euler))]
        euler_line = VMobject(color=YELLOW)
        euler_line.set_points_smoothly(euler_points)
        
        euler_label = Text("オイラー法", color=YELLOW, font_size=20)
        euler_label.next_to(heun_label, RIGHT, buff=1)
        
        self.play(Create(euler_line), Write(euler_label), run_time=1.0)
        self.wait(1.0)

        # 観察
        observation1 = Text(
            "ホイン法と固有値展開はほぼ重なっている",
            color=GREEN, font_size=22,
        )
        observation1.shift(DOWN * 3 + RIGHT * 1.5)
        self.play(Write(observation1), run_time=0.8)
        self.wait(0.8)

        observation2 = Text(
            "オイラー法は目に見えて誤差がある",
            color=YELLOW, font_size=22,
        )
        observation2.shift(DOWN * 3.4 + RIGHT * 1.5)
        self.play(Write(observation2), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(axes), FadeOut(x_label), FadeOut(y_label),
            FadeOut(exact_line), FadeOut(heun_line), FadeOut(euler_line),
            FadeOut(exact_label), FadeOut(heun_label), FadeOut(euler_label),
            FadeOut(observation1), FadeOut(observation2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 7: 精度の次数の説明
        # ============================================================
        subtitle7 = Text("精度の次数", font_size=28, color=BLUE)
        subtitle7.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle7), run_time=0.5)
        self.wait(0.4)

        accuracy_intro = Text(
            "Δtを小さくすると誤差はどう変化するか？",
            color=WHITE, font_size=26,
        )
        accuracy_intro.shift(UP * 1.8)
        self.play(Write(accuracy_intro), run_time=0.8)
        self.wait(0.7)

        euler_accuracy_title = Text(
            "オイラー法：1次精度",
            color=YELLOW, font_size=26, weight=BOLD,
        )
        euler_accuracy_title.shift(UP * 0.9)
        self.play(Write(euler_accuracy_title), run_time=0.7)
        self.wait(0.5)

        euler_accuracy_detail = Text(
            "Δtが1/10になると誤差も約1/10になる",
            color=WHITE, font_size=24,
        )
        euler_accuracy_detail.shift(UP * 0.3)
        self.play(Write(euler_accuracy_detail), run_time=0.8)
        self.wait(0.6)

        euler_error_formula = MathTex(
            r"\text{Error} \propto \Delta t",
            color=YELLOW,
            font_size=34,
        )
        euler_error_formula.shift(DOWN * 0.4)
        self.play(Write(euler_error_formula), run_time=0.8)
        self.wait(0.8)

        heun_accuracy_title = Text(
            "ホイン法：2次精度",
            color=GREEN, font_size=26, weight=BOLD,
        )
        heun_accuracy_title.shift(DOWN * 1.2)
        self.play(Write(heun_accuracy_title), run_time=0.7)
        self.wait(0.5)

        heun_accuracy_detail = Text(
            "Δtが1/10になると誤差は約1/100になる",
            color=WHITE, font_size=24,
        )
        heun_accuracy_detail.shift(DOWN * 1.8)
        self.play(Write(heun_accuracy_detail), run_time=0.8)
        self.wait(0.6)

        heun_error_formula = MathTex(
            r"\text{Error} \propto (\Delta t)^2",
            color=GREEN,
            font_size=34,
        )
        heun_error_formula.shift(DOWN * 2.5)
        self.play(Write(heun_error_formula), run_time=0.8)
        self.wait(1.2)

        self.play(
            FadeOut(accuracy_intro), FadeOut(euler_accuracy_title),
            FadeOut(euler_accuracy_detail), FadeOut(euler_error_formula),
            FadeOut(heun_accuracy_title), FadeOut(heun_accuracy_detail),
            FadeOut(heun_error_formula),
        )
        self.wait(0.3)

        # ============================================================
        # Part 8: 行列指数関数との関係
        # ============================================================
        subtitle8 = Text("行列指数関数との関係", font_size=28, color=GOLD)
        subtitle8.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle8), run_time=0.5)
        self.wait(0.4)

        relation_intro = Text(
            "なぜオイラー法は1次精度なのか？",
            color=WHITE, font_size=26,
        )
        relation_intro.shift(UP * 1.8)
        self.play(Write(relation_intro), run_time=0.8)
        self.wait(0.6)

        exact_solution_title = Text(
            "真の解（行列指数関数）：",
            color=WHITE, font_size=26,
        )
        exact_solution_title.shift(UP * 1.0)
        self.play(Write(exact_solution_title), run_time=0.7)
        self.wait(0.4)

        exact_solution_eq = MathTex(
            r"\mathbf{x}(t+\Delta t) = e^{L\Delta t}\mathbf{x}(t)",
            color=BLUE,
            font_size=36,
        )
        exact_solution_eq.shift(UP * 0.3)
        self.play(Write(exact_solution_eq), run_time=0.8)
        self.wait(0.7)

        taylor_title = Text(
            "行列指数関数のテイラー展開：",
            color=WHITE, font_size=26,
        )
        taylor_title.shift(DOWN * 0.5)
        self.play(Write(taylor_title), run_time=0.7)
        self.wait(0.4)

        taylor_expansion = MathTex(
            r"e^{L\Delta t} = I + L\Delta t + \frac{(L\Delta t)^2}{2!} + \frac{(L\Delta t)^3}{3!} + \cdots",
            color=TEAL,
            font_size=30,
        )
        taylor_expansion.shift(DOWN * 1.3)
        self.play(Write(taylor_expansion), run_time=1.0)
        self.wait(1.0)

        arrow_down = Text("↓", color=RED, font_size=32)
        arrow_down.shift(DOWN * 1.9)
        self.play(Write(arrow_down), run_time=0.4)
        self.wait(0.3)

        first_order_approx = Text(
            "1次で打ち切ると：",
            color=WHITE, font_size=24,
        )
        first_order_approx.shift(DOWN * 2.5 + LEFT * 2.8)
        self.play(Write(first_order_approx), run_time=0.7)
        self.wait(0.4)

        euler_from_taylor = MathTex(
            r"\mathbf{x}(t+\Delta t) \approx (I + L\Delta t)\mathbf{x}(t) = \mathbf{x}(t) + L\mathbf{x}(t)\Delta t",
            color=YELLOW,
            font_size=30,
        )
        euler_from_taylor.shift(DOWN * 2.6 + RIGHT * 2.5)
        euler_from_taylor_box = SurroundingRectangle(euler_from_taylor, color=YELLOW, buff=0.2)
        self.play(Write(euler_from_taylor), Create(euler_from_taylor_box), run_time=1.0)
        self.wait(1.0)

        conclusion_text = Text(
            "これはオイラー法の式と一致！",
            color=RED, font_size=26, weight=BOLD,
        )
        conclusion_text.shift(DOWN * 3.3)
        self.play(Write(conclusion_text), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(relation_intro), FadeOut(exact_solution_title),
            FadeOut(exact_solution_eq), FadeOut(taylor_title),
            FadeOut(taylor_expansion), FadeOut(arrow_down),
            FadeOut(first_order_approx), FadeOut(euler_from_taylor),
            FadeOut(euler_from_taylor_box), FadeOut(conclusion_text),
        )
        self.wait(0.3)

        # ============================================================
        # Part 9: ホイン法と2次近似
        # ============================================================
        subtitle9 = Text("ホイン法と2次近似", font_size=28, color=TEAL)
        subtitle9.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle9), run_time=0.5)
        self.wait(0.4)

        heun_relation_intro = Text(
            "同様に、ホイン法は2次まで含む近似",
            color=WHITE, font_size=26,
        )
        heun_relation_intro.shift(UP * 1.8)
        self.play(Write(heun_relation_intro), run_time=0.8)
        self.wait(0.6)

        taylor_second_order = MathTex(
            r"e^{L\Delta t} \approx I + L\Delta t + \frac{L^2(\Delta t)^2}{2}",
            color=TEAL,
            font_size=34,
        )
        taylor_second_order.shift(UP * 0.9)
        self.play(Write(taylor_second_order), run_time=0.9)
        self.wait(0.7)

        arrow_down2 = Text("↓", color=GREEN, font_size=32)
        arrow_down2.shift(UP * 0.2)
        self.play(Write(arrow_down2), run_time=0.4)
        self.wait(0.3)

        heun_from_taylor = MathTex(
            r"\mathbf{x}(t+\Delta t) \approx \mathbf{x}(t) + L\mathbf{x}(t)\Delta t + L^2\mathbf{x}(t)\frac{(\Delta t)^2}{2}",
            color=GREEN,
            font_size=30,
        )
        heun_from_taylor.shift(DOWN * 0.7)
        heun_from_taylor_box = SurroundingRectangle(heun_from_taylor, color=GREEN, buff=0.2)
        self.play(Write(heun_from_taylor), Create(heun_from_taylor_box), run_time=1.0)
        self.wait(1.0)

        heun_conclusion = Text(
            "これはホイン法の式と一致！",
            color=GREEN, font_size=24, weight=BOLD,
        )
        heun_conclusion.shift(DOWN * 1.8)
        self.play(Write(heun_conclusion), run_time=0.8)
        self.wait(1.0)

        general_principle = Text(
            "高次の項まで含めるほど精度が向上する",
            color=ORANGE, font_size=26,
        )
        general_principle.shift(DOWN * 2.5)
        self.play(Write(general_principle), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(heun_relation_intro), FadeOut(taylor_second_order),
            FadeOut(arrow_down2), FadeOut(heun_from_taylor),
            FadeOut(heun_from_taylor_box), FadeOut(heun_conclusion),
            FadeOut(general_principle),
        )
        self.wait(0.3)

        # ============================================================
        # Part 10: まとめ
        # ============================================================
        subtitle10 = Text("まとめ", font_size=36, color=GOLD)
        subtitle10.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle10), run_time=0.6)
        self.wait(0.4)

        summary = VGroup(
            Text("• 線形システムで各手法の精度を比較", color=WHITE, font_size=26),
            Text("• オイラー法：1次精度、誤差 ∝ Δt", color=WHITE, font_size=26),
            Text("• ホイン法：2次精度、誤差 ∝ (Δt)²", color=WHITE, font_size=26),
            Text("• 数値解法は行列指数関数のテイラー展開に対応", color=WHITE, font_size=26),
            Text("• 高次の項を含めるほど精度が向上する", color=WHITE, font_size=26),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        summary.shift(UP * 0.2)
        
        for row in summary:
            self.play(Write(row), run_time=0.6)
            self.wait(0.3)
        
        self.wait(1.0)

        final_message = Text(
            "精度と計算コストのバランスが重要",
            color=TEAL, font_size=24,
        )
        final_message.shift(DOWN * 2.5)
        self.play(Write(final_message), run_time=0.8)
        self.wait(2.0)

        self.play(
            FadeOut(VGroup(
                title, subtitle1, summary, final_message
            )),
            run_time=1.0
        )
        self.wait(0.5)
