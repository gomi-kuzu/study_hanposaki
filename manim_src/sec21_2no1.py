from manim import *
import numpy as np


class NumericalMethodsODE(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        title = Text("連立微分方程式の数値的解法", font_size=36, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.7)

        # ============================================================
        # Part 1: 前回のおさらい
        # ============================================================
        subtitle1 = Text("前の動画のおさらい", font_size=28, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.4)

        review_text = Text(
            "前回は線形の連立微分方程式を解析的に解いた",
            color=WHITE, font_size=26,
        )
        review_text.shift(UP * 1.8)
        self.play(Write(review_text), run_time=0.7)
        self.wait(0.5)

        review_eq1 = MathTex(
            r"\frac{d}{dt}\mathbf{x} = L\mathbf{x}",
            color=YELLOW,
            font_size=40,
        )
        review_eq1.shift(UP * 0.9)
        self.play(Write(review_eq1), run_time=0.7)
        self.wait(0.5)

        review_eq2 = MathTex(
            r"\mathbf{x}(t) = e^{Lt}\mathbf{x}(0) = \sum_{d=1}^{D} c_d e^{\lambda_d t}\mathbf{v}_d",
            color=GREEN,
            font_size=32,
        )
        review_eq2.shift(DOWN * 0.5)
        review_box = SurroundingRectangle(review_eq2, color=GREEN, buff=0.25)
        self.play(Write(review_eq2), Create(review_box), run_time=0.8)
        self.wait(0.8)

        method_text = Text(
            "固有値・固有ベクトルを使った解析的手法",
            color=TEAL, font_size=24,
        )
        method_text.shift(DOWN * 1.8)
        self.play(Write(method_text), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(review_text), FadeOut(review_eq1),
            FadeOut(review_eq2), FadeOut(review_box),
            FadeOut(method_text),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: 数値解法の必要性
        # ============================================================
        subtitle2 = Text("数値解法の必要性", font_size=28, color=GOLD)
        subtitle2.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle2), run_time=0.5)
        self.wait(0.4)

        necessity1 = Text(
            "しかし、この解析的手法には限界がある",
            color=ORANGE, font_size=26, weight=BOLD,
        )
        necessity1.shift(UP * 1.8)
        self.play(Write(necessity1), run_time=0.7)
        self.wait(0.6)

        problem1_title = Text(
            "問題1：非線形の微分方程式",
            color=WHITE, font_size=26,
        )
        problem1_title.shift(UP * 1.0)
        self.play(Write(problem1_title), run_time=0.7)
        self.wait(0.5)

        problem1_eq = MathTex(
            r"\frac{d}{dt}\mathbf{x} = \mathbf{f}(\mathbf{x})",
            color=YELLOW,
            font_size=38,
        )
        problem1_eq.shift(UP * 0.3)
        self.play(Write(problem1_eq), run_time=0.7)
        self.wait(0.5)

        problem1_note = Text(
            "非線形の場合は解析的に解けない",
            color=RED, font_size=24, weight=BOLD,
        )
        problem1_note.shift(DOWN * 0.4)
        self.play(Write(problem1_note), run_time=0.7)
        self.wait(0.8)

        problem2_title = Text(
            "問題2：高次元での計算量",
            color=WHITE, font_size=26,
        )
        problem2_title.shift(DOWN * 1.2)
        self.play(Write(problem2_title), run_time=0.7)
        self.wait(0.5)

        problem2_note = Text(
            "線形でも、固有値計算はO(D³)の計算量",
            color=ORANGE, font_size=24,
        )
        problem2_note.shift(DOWN * 1.8)
        self.play(Write(problem2_note), run_time=0.7)
        self.wait(0.5)

        problem2_note2 = Text(
            "→ 次元Dが大きいと計算時間が爆発的に増加",
            color=ORANGE, font_size=24,
        )
        problem2_note2.shift(DOWN * 2.4)
        self.play(Write(problem2_note2), run_time=0.7)
        self.wait(1.0)

        self.play(
            FadeOut(necessity1), FadeOut(problem1_title),
            FadeOut(problem1_eq), FadeOut(problem1_note),
            FadeOut(problem2_title), FadeOut(problem2_note),
            FadeOut(problem2_note2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: 数値解法の利点
        # ============================================================
        subtitle3 = Text("数値解法の利点", font_size=28, color=TEAL)
        subtitle3.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle3), run_time=0.5)
        self.wait(0.4)

        advantage_intro = Text(
            "そこで、数値的に近似解を求める手法が有効となる",
            color=GREEN, font_size=26, weight=BOLD,
        )
        advantage_intro.shift(UP * 1.8)
        self.play(Write(advantage_intro), run_time=0.8)
        self.wait(0.7)

        advantages = VGroup(
            Text("• 非線形の微分方程式にも適用可能", color=WHITE, font_size=26),
            Text("• 高次元でも比較的効率的に計算できる", color=WHITE, font_size=26),
            Text("• 実装が比較的シンプル", color=WHITE, font_size=26),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        advantages.shift(UP * 0.3)
        
        for adv in advantages:
            self.play(Write(adv), run_time=0.6)
            self.wait(0.4)
        
        self.wait(0.8)

        coverage_note = Text(
            "この動画では、代表的な数値解法を紹介する",
            color=BLUE, font_size=24,
        )
        coverage_note.shift(DOWN * 2.0)
        self.play(Write(coverage_note), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(advantage_intro), FadeOut(advantages),
            FadeOut(coverage_note),
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: 数値解法の基本的考え方
        # ============================================================
        subtitle4 = Text("数値解法の基本的考え方", font_size=28, color=BLUE)
        subtitle4.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle4), run_time=0.5)
        self.wait(0.4)

        basic_idea = Text(
            "数値解法の基本は「時間を細かく刻んで逐次更新する」",
            color=WHITE, font_size=26,
        )
        basic_idea.shift(UP * 1.8)
        self.play(Write(basic_idea), run_time=0.8)
        self.wait(0.7)

        timestep_intro = Text(
            "時間刻みをΔtとおく",
            color=TEAL, font_size=26,
        )
        timestep_intro.shift(UP * 1.0)
        self.play(Write(timestep_intro), run_time=0.7)
        self.wait(0.5)

        timestep_eq = MathTex(
            r"\Delta t > 0",
            color=YELLOW,
            font_size=36,
        )
        timestep_eq.shift(UP * 0.3)
        self.play(Write(timestep_eq), run_time=0.7)
        self.wait(0.3)

        timestep_note = Text(
            "（小さな正の値）",
            color=GRAY, font_size=22,
        )
        timestep_note.next_to(timestep_eq, DOWN, buff=0.2)
        self.play(Write(timestep_note), run_time=0.5)
        self.wait(0.6)

        concept = Text(
            "現在の状態 x⃗(t) から次の状態 x⃗(t+Δt) を計算",
            color=WHITE, font_size=26,
        )
        concept.shift(DOWN)
        self.play(Write(concept), run_time=0.8)
        self.wait(0.6)

        concept2 = Text(
            "これを繰り返して時間発展を追跡する",
            color=WHITE, font_size=26,
        )
        concept2.shift(DOWN*1.5)
        self.play(Write(concept2), run_time=0.7)
        self.wait(1.0)

        accuracy_note = Text(
            "Δtが小さいほど精度は上がるが、計算回数も増える",
            color=ORANGE, font_size=24,
        )
        accuracy_note.shift(DOWN * 2.3)
        self.play(Write(accuracy_note), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(basic_idea), FadeOut(timestep_intro),
            FadeOut(timestep_eq), FadeOut(timestep_note),
            FadeOut(concept), FadeOut(concept2),
            FadeOut(accuracy_note),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: オイラー法の紹介
        # ============================================================
        subtitle5 = Text("オイラー法（Euler法）", font_size=28, color=GOLD)
        subtitle5.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle5), run_time=0.5)
        self.wait(0.4)

        euler_intro = Text(
            "最もシンプルな数値解法：オイラー法",
            color=WHITE, font_size=26,
        )
        euler_intro.shift(UP * 1.8)
        self.play(Write(euler_intro), run_time=0.7)
        self.wait(0.5)

        euler_idea = Text(
            "現在の微分係数を使って、次の状態を線形近似する",
            color=TEAL, font_size=26,
        )
        euler_idea.shift(UP * 1.1)
        self.play(Write(euler_idea), run_time=0.8)
        self.wait(0.6)

        ode_general = MathTex(
            r"\frac{d\mathbf{x}}{dt} = \mathbf{f}(\mathbf{x})",
            color=BLUE,
            font_size=38,
        )
        ode_general.shift(UP * 0.3)
        self.play(Write(ode_general), run_time=0.7)
        self.wait(0.5)

        euler_formula_title = Text(
            "オイラー法の更新式：",
            color=WHITE, font_size=26,
        )
        euler_formula_title.shift(DOWN * 0.5)
        self.play(Write(euler_formula_title), run_time=0.7)
        self.wait(0.4)

        euler_formula = MathTex(
            r"\mathbf{x}(t+\Delta t) = \mathbf{x}(t) + \mathbf{f}(\mathbf{x}(t))\Delta t",
            color=YELLOW,
            font_size=36,
        )
        euler_formula.shift(DOWN * 1.3)
        euler_box = SurroundingRectangle(euler_formula, color=YELLOW, buff=0.25)
        self.play(Write(euler_formula), Create(euler_box), run_time=0.8)
        self.wait(1.0)

        euler_note = Text(
            "現在の位置と傾きから、次の位置を推定",
            color=GREEN, font_size=24,
        )
        euler_note.shift(DOWN * 2.5)
        self.play(Write(euler_note), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(euler_intro), FadeOut(euler_idea),
            FadeOut(ode_general), FadeOut(euler_formula_title),
            FadeOut(euler_note),
        )
        self.wait(0.3)

        # ============================================================
        # Part 6: オイラー法の幾何学的解釈
        # ============================================================
        subtitle6 = Text("オイラー法の幾何学的解釈", font_size=28, color=TEAL)
        subtitle6.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle6), run_time=0.5)
        self.wait(0.4)

        # euler_formulaを上に移動
        self.play(
            euler_formula.animate.shift(UP * 3.1).scale(0.9),
            euler_box.animate.shift(UP * 3.1).scale(0.85),
            run_time=0.6
        )
        self.wait(0.3)

        geometric_text = Text(
            "オイラー法は「接線による近似」と解釈できる",
            color=WHITE, font_size=26,
        )
        geometric_text.shift(UP * 1.0)
        self.play(Write(geometric_text), run_time=0.8)
        self.wait(0.6)

        step1_text = Text(
            "① 現在地点での接線の傾きを計算",
            color=BLUE, font_size=24,
        )
        step1_text.shift(UP * 0.3)
        self.play(Write(step1_text), run_time=0.7)
        self.wait(0.5)

        step1_eq = MathTex(
            r"\mathbf{f}(\mathbf{x}(t))",
            color=BLUE,
            font_size=36,
        )
        step1_eq.shift(DOWN * 0.3)
        self.play(Write(step1_eq), run_time=0.7)
        self.wait(0.6)

        step2_text = Text(
            "② その接線に沿ってΔtだけ進む",
            color=GREEN, font_size=24,
        )
        step2_text.shift(DOWN * 1.0)
        self.play(Write(step2_text), run_time=0.7)
        self.wait(0.5)

        step2_eq = MathTex(
            r"\mathbf{f}(\mathbf{x}(t))\Delta t",
            color=GREEN,
            font_size=36,
        )
        step2_eq.shift(DOWN * 1.6)
        self.play(Write(step2_eq), run_time=0.7)
        self.wait(0.8)

        approximation_note = Text(
            "→ 真の曲線を直線で近似している",
            color=ORANGE, font_size=24, weight=BOLD,
        )
        approximation_note.shift(DOWN * 2.5)
        self.play(Write(approximation_note), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(euler_formula), FadeOut(euler_box),
            FadeOut(geometric_text), FadeOut(step1_text),
            FadeOut(step1_eq), FadeOut(step2_text),
            FadeOut(step2_eq), FadeOut(approximation_note),
        )
        self.wait(0.3)

        # ============================================================
        # Part 7: ホイン法の紹介
        # ============================================================
        subtitle7 = Text("ホイン法（Heun法）", font_size=28, color=BLUE)
        subtitle7.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle7), run_time=0.5)
        self.wait(0.4)

        # # euler_formulaを左上に移動
        # self.play(
        #     euler_formula.animate.shift(LEFT * 2.5 + UP * 0.3).scale(0.75),
        #     euler_box.animate.shift(LEFT * 2.5 + UP * 0.3).scale(0.75),
        #     run_time=0.6
        # )
        # self.wait(0.3)

        heun_intro = Text(
            "オイラー法を改良したホイン法",
            color=WHITE, font_size=26,
        )
        heun_intro.shift(UP * 1.8)
        self.play(Write(heun_intro), run_time=0.7)
        self.wait(0.5)

        heun_idea = Text(
            "始点と終点の傾きの平均を使う",
            color=TEAL, font_size=26,
        )
        heun_idea.shift(UP * 1.1)
        self.play(Write(heun_idea), run_time=0.8)
        self.wait(0.6)

        heun_step1_title = Text(
            "ステップ1：オイラー法で仮の次の状態を予測",
            color=WHITE, font_size=24,
        )
        heun_step1_title.shift(UP * 0.4)
        self.play(Write(heun_step1_title), run_time=0.7)
        self.wait(0.5)

        heun_step1_eq = MathTex(
            r"\tilde{\mathbf{x}}(t+\Delta t) = \mathbf{x}(t) + \mathbf{f}(\mathbf{x}(t))\Delta t",
            color=BLUE,
            font_size=30,
        )
        heun_step1_eq.shift(DOWN * 0.3)
        self.play(Write(heun_step1_eq), run_time=0.8)
        self.wait(0.7)

        heun_step2_title = Text(
            "ステップ2：始点と予測終点の傾きの平均で更新",
            color=WHITE, font_size=24,
        )
        heun_step2_title.shift(DOWN * 1.1)
        self.play(Write(heun_step2_title), run_time=0.7)
        self.wait(0.5)

        heun_step2_eq = MathTex(
            r"\mathbf{x}(t+\Delta t) = \mathbf{x}(t) + \frac{\Delta t}{2}\left(\mathbf{f}(\mathbf{x}(t)) + \mathbf{f}(\tilde{\mathbf{x}}(t+\Delta t))\right)",
            color=GREEN,
            font_size=28,
        )
        heun_step2_eq.shift(DOWN * 2.2)
        heun_box = SurroundingRectangle(heun_step2_eq, color=GREEN, buff=0.25)
        self.play(Write(heun_step2_eq), Create(heun_box), run_time=1.0)
        self.wait(1.2)

        self.play(
            FadeOut(heun_intro), FadeOut(heun_idea),
            FadeOut(heun_step1_title), FadeOut(heun_step2_title),
        )
        self.wait(0.3)

        # ============================================================
        # Part 8: ホイン法の利点
        # ============================================================
        subtitle8 = Text("ホイン法の利点", font_size=28, color=GOLD)
        subtitle8.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle8), run_time=0.5)
        self.wait(0.4)

        # 式を上に移動
        self.play(
            # euler_formula.animate.shift(UP * 1.0 + RIGHT * 2.5).scale(0.95),
            # euler_box.animate.shift(UP * 1.0 + RIGHT * 2.5).scale(0.95),
            heun_step1_eq.animate.shift(UP * 2.3).scale(0.95),
            heun_step2_eq.animate.shift(UP * 3.7).scale(0.95),
            heun_box.animate.shift(UP * 3.85).scale(1.3),
            run_time=0.6
        )
        self.wait(0.3)

        advantage_text = Text(
            "ホイン法の優位性",
            color=WHITE, font_size=26,
        )
        advantage_text.shift(UP * 0.5)
        self.play(Write(advantage_text), run_time=0.7)
        self.wait(0.5)

        comparison1 = Text(
            "• オイラー法：終点での傾きは考慮しない",
            color=YELLOW, font_size=24,
        )
        comparison1.shift(DOWN * 0.2)
        self.play(Write(comparison1), run_time=0.7)
        self.wait(0.5)

        comparison2 = Text(
            "• ホイン法：始点と終点の両方の傾きを使用",
            color=GREEN, font_size=24,
        )
        comparison2.shift(DOWN * 0.8)
        self.play(Write(comparison2), run_time=0.7)
        self.wait(0.6)

        result_text = Text(
            "→ 曲線をより正確に追跡できる",
            color=GREEN, font_size=24, weight=BOLD,
        )
        result_text.shift(DOWN * 1.5)
        self.play(Write(result_text), run_time=0.7)
        self.wait(0.8)

        cost_note = Text(
            "ただし、f を2回計算するため計算コストは約2倍",
            color=ORANGE, font_size=22,
        )
        cost_note.shift(DOWN * 2.3)
        self.play(Write(cost_note), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(heun_step1_eq), FadeOut(heun_step2_eq),
            FadeOut(heun_box),
            FadeOut(advantage_text), FadeOut(comparison1),
            FadeOut(comparison2), FadeOut(result_text),
            FadeOut(cost_note),
        )
        self.wait(0.3)

        # ============================================================
        # Part 9: 精度の比較
        # ============================================================
        subtitle9 = Text("精度の簡易比較", font_size=28, color=TEAL)
        subtitle9.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle9), run_time=0.5)
        self.wait(0.4)

        # 式を右に移動
        # self.play(
        #     euler_formula.animate.shift(DOWN * 1.0 + RIGHT * 1.5).scale(0.85),
        #     euler_box.animate.shift(DOWN * 1.0 + RIGHT * 1.5).scale(0.85),
        #     heun_step1_eq.animate.shift(DOWN * 3.5 + RIGHT * 0.5),
        #     heun_step2_eq.animate.shift(DOWN * 3.2 + RIGHT * 0.5),
        #     heun_box.animate.shift(DOWN * 3.2 + RIGHT * 0.5),
        #     run_time=0.6
        # )
        # self.wait(0.3)

        accuracy_intro = Text(
            "数値解法には「精度の次数」という概念がある",
            color=WHITE, font_size=26,
        )
        accuracy_intro.shift(UP * 1.8)
        self.play(Write(accuracy_intro), run_time=0.8)
        self.wait(0.6)

        accuracy_def = Text(
            "誤差がΔtの何乗に比例するかを示す指標",
            color=TEAL, font_size=24,
        )
        accuracy_def.shift(UP * 1.2)
        self.play(Write(accuracy_def), run_time=0.7)
        self.wait(0.6)

        euler_accuracy = Text(
            "オイラー法：1次精度",
            color=YELLOW, font_size=26, weight=BOLD,
        )
        euler_accuracy.shift(UP * 0.4)
        self.play(Write(euler_accuracy), run_time=0.7)
        self.wait(0.5)

        euler_error = MathTex(
            r"\text{Error} \propto \Delta t",
            color=YELLOW,
            font_size=32,
        )
        euler_error.shift(DOWN * 0.2)
        self.play(Write(euler_error), run_time=0.7)
        self.wait(0.6)

        heun_accuracy = Text(
            "ホイン法：2次精度",
            color=GREEN, font_size=26, weight=BOLD,
        )
        heun_accuracy.shift(DOWN * 1.0)
        self.play(Write(heun_accuracy), run_time=0.7)
        self.wait(0.5)

        heun_error = MathTex(
            r"\text{Error} \propto (\Delta t)^2",
            color=GREEN,
            font_size=32,
        )
        heun_error.shift(DOWN * 1.6)
        self.play(Write(heun_error), run_time=0.7)
        self.wait(0.8)

        conclusion_accuracy = Text(
            "→ 精度が高いほど正確だが、計算負荷も増える",
            color=ORANGE, font_size=24, weight=BOLD,
        )
        conclusion_accuracy.shift(DOWN * 2.6)
        self.play(Write(conclusion_accuracy), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(accuracy_intro), FadeOut(accuracy_def),
            FadeOut(euler_accuracy), FadeOut(euler_error),
            FadeOut(heun_accuracy), FadeOut(heun_error),
            FadeOut(conclusion_accuracy),
        )
        self.wait(0.3)

        # ============================================================
        # Part 10: 陽的解法と陰的解法
        # ============================================================
        subtitle10 = Text("陽的解法と陰的解法", font_size=28, color=BLUE)
        subtitle10.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle10), run_time=0.5)
        self.wait(0.4)

        classification_intro = Text(
            "数値解法は「陽的解法」と「陰的解法」に分類される",
            color=WHITE, font_size=26,
        )
        classification_intro.shift(UP * 1.8)
        self.play(Write(classification_intro), run_time=0.8)
        self.wait(0.7)

        explicit_title = Text(
            "陽的解法（Explicit Method）",
            color=YELLOW, font_size=26, weight=BOLD,
        )
        explicit_title.shift(UP * 1.0)
        self.play(Write(explicit_title), run_time=0.7)
        self.wait(0.5)

        explicit_def = Text(
            "現在の状態を使って次の状態を直接計算",
            color=WHITE, font_size=24,
        )
        explicit_def.shift(UP * 0.5)
        self.play(Write(explicit_def), run_time=0.7)
        self.wait(0.5)

        explicit_example = MathTex(
            r"\mathbf{x}(t+\Delta t) = \mathbf{x}(t) + \mathbf{f}(\mathbf{x}(t))\Delta t",
            color=YELLOW,
            font_size=32,
        )
        explicit_example.shift(DOWN * 0.2)
        self.play(Write(explicit_example), run_time=0.8)
        self.wait(0.6)

        explicit_note = Text(
            "オイラー法、ホイン法は陽的解法",
            color=TEAL, font_size=22,
        )
        explicit_note.shift(DOWN * 0.9)
        self.play(Write(explicit_note), run_time=0.6)
        self.wait(0.8)

        implicit_title = Text(
            "陰的解法（Implicit Method）",
            color=BLUE, font_size=26, weight=BOLD,
        )
        implicit_title.shift(DOWN * 1.6)
        self.play(Write(implicit_title), run_time=0.7)
        self.wait(0.5)

        implicit_def = Text(
            "次の状態自身を使って次の状態を計算",
            color=WHITE, font_size=24,
        )
        implicit_def.shift(DOWN * 2.1)
        self.play(Write(implicit_def), run_time=0.7)
        self.wait(0.5)

        implicit_note = Text(
            "→ 方程式を解く必要がある（計算が複雑）",
            color=ORANGE, font_size=22,
        )
        implicit_note.shift(DOWN * 2.6)
        self.play(Write(implicit_note), run_time=0.7)
        self.wait(1.0)

        self.play(
            FadeOut(classification_intro),
            FadeOut(explicit_def), FadeOut(explicit_note),
            FadeOut(implicit_def), FadeOut(implicit_note),
        )
        self.wait(0.3)

        # ============================================================
        # Part 11: 陰的オイラー法
        # ============================================================
        subtitle11 = Text("陰的オイラー法", font_size=28, color=GOLD)
        subtitle11.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle11), run_time=0.5)
        self.wait(0.4)

        # explicit_exampleを上に移動
        self.play(
            explicit_title.animate.shift(UP * 1.5 + LEFT * 4.5).scale(0.9),
            explicit_example.animate.shift(UP * 2.3 + LEFT * 4.5).scale(0.9),
            implicit_title.animate.shift(UP * 3.3),
            run_time=0.6
        )
        self.wait(0.3)

        implicit_euler_intro = Text(
            "陰的オイラー法の更新式",
            color=WHITE, font_size=26,
        )
        implicit_euler_intro.shift(UP * 0.8)
        self.play(Write(implicit_euler_intro), run_time=0.7)
        self.wait(0.5)

        implicit_euler_formula = MathTex(
            r"\mathbf{x}(t+\Delta t) = \mathbf{x}(t) + \mathbf{f}(\mathbf{x}(t+\Delta t))\Delta t",
            color=BLUE,
            font_size=34,
        )
        implicit_euler_formula.shift(UP * 0.0)
        implicit_euler_box = SurroundingRectangle(implicit_euler_formula, color=BLUE, buff=0.25)
        self.play(Write(implicit_euler_formula), Create(implicit_euler_box), run_time=0.8)
        self.wait(0.8)

        key_difference = Text(
            "右辺に x⃗(t+Δt) が現れている！",
            color=RED, font_size=24, weight=BOLD,
        )
        key_difference.shift(DOWN * 1.0)
        self.play(Write(key_difference), run_time=0.7)
        self.wait(0.7)

        solution_method = Text(
            "→ この方程式を x⃗(t+Δt) について解く必要がある",
            color=ORANGE, font_size=24,
        )
        solution_method.shift(DOWN * 1.7)
        self.play(Write(solution_method), run_time=0.8)
        self.wait(0.8)

        complexity_note = Text(
            "非線形の場合はニュートン法などの反復計算が必要",
            color=WHITE, font_size=22,
        )
        complexity_note.shift(DOWN * 2.4)
        self.play(Write(complexity_note), run_time=0.7)
        self.wait(1.0)

        self.play(
            FadeOut(implicit_euler_intro), FadeOut(key_difference),
            FadeOut(solution_method), FadeOut(complexity_note),
            FadeOut(implicit_euler_box),
        )
        self.wait(0.3)

        # ============================================================
        # Part 12: 陰的解法のメリット
        # ============================================================
        subtitle12 = Text("陰的解法のメリット", font_size=28, color=TEAL)
        subtitle12.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle12), run_time=0.5)
        self.wait(0.4)

        # 式を上に移動
        self.play(
            explicit_title.animate.shift(DOWN * 0.8  + RIGHT).scale(1.06),
            explicit_example.animate.shift(DOWN + RIGHT).scale(1.05),
            implicit_title.animate.shift(RIGHT * 2.5),
            implicit_euler_formula.animate.shift(UP *1.1 + RIGHT * 2.5).scale(0.85),
            # implicit_euler_box.animate.shift(UP * 1.1 + RIGHT * 2.5).scale(0.8),
            run_time=0.6
        )
        self.wait(0.3)

        merit_intro = Text(
            "計算は複雑になるが、重要なメリットがある",
            color=WHITE, font_size=26,
        )
        merit_intro.shift(UP * 0.4)
        self.play(Write(merit_intro), run_time=0.7)
        self.wait(0.6)

        stability_title = Text(
            "数値的安定性の向上",
            color=GREEN, font_size=26, weight=BOLD,
        )
        stability_title.shift(DOWN * 0.2)
        self.play(Write(stability_title), run_time=0.7)
        self.wait(0.5)

        stability_exp = Text(
            "陽的解法は大きなΔtで不安定になりやすい",
            color=WHITE, font_size=24,
        )
        stability_exp.shift(DOWN * 0.8)
        self.play(Write(stability_exp), run_time=0.7)
        self.wait(0.5)

        stability_exp2 = Text(
            "陰的解法は大きなΔtでも安定して計算できることが多い",
            color=GREEN, font_size=24,
        )
        stability_exp2.shift(DOWN * 1.4)
        self.play(Write(stability_exp2), run_time=0.8)
        self.wait(0.8)

        tradeoff = Text(
            "→ 精度 vs 安定性 vs 計算コストのトレードオフ",
            color=ORANGE, font_size=24, weight=BOLD,
        )
        tradeoff.shift(DOWN * 2.3)
        self.play(Write(tradeoff), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(explicit_title),
            FadeOut(explicit_example), FadeOut(implicit_title),
            FadeOut(implicit_euler_formula), 
            FadeOut(merit_intro), FadeOut(stability_title),
            FadeOut(stability_exp), FadeOut(stability_exp2),
            FadeOut(tradeoff),
        )
        self.wait(0.3)

        # ============================================================
        # Part 13: まとめ
        # ============================================================
        subtitle13 = Text("まとめ", font_size=36, color=GOLD)
        subtitle13.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle13), run_time=0.6)
        self.wait(0.4)

        summary = VGroup(
            Text("• 非線形や高次元では数値解法が必要", color=WHITE, font_size=26),
            Text("• オイラー法：1次精度、シンプルで高速", color=WHITE, font_size=26),
            Text("• ホイン法：2次精度、より正確だが計算量は約2倍", color=WHITE, font_size=26),
            Text("• 陽的解法：計算が簡単", color=WHITE, font_size=26),
            Text("• 陰的解法：計算は複雑だが安定性が向上", color=WHITE, font_size=26),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        summary.shift(UP * 0.2)
        
        for row in summary:
            self.play(Write(row), run_time=0.6)
            self.wait(0.3)
        
        self.wait(1.0)

        final_message = Text(
            "実用では、計算量と精度のバランスの良い4次ルンゲクッタ法がよく使われる",
            color=TEAL, font_size=26,
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
