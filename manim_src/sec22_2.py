from manim import *
import numpy as np


class ProbabilityDensitySolution(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        title = Text("線形に時間変化する確率密度関数の一般解とその応用", font_size=32, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.7)

        # ============================================================
        # Part 1: 前回の復習
        # ============================================================
        subtitle1 = Text("前の動画の復習", font_size=28, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.4)

        recap_text = Text(
            "前の動画の最後に、多変量のフォッカー・プランク方程式を見た",
            color=WHITE, font_size=26,
        )
        recap_text.shift(UP * 1.8)
        self.play(Write(recap_text), run_time=0.8)
        self.wait(0.6)

        fpe_eq = MathTex(
            r"\frac{\partial}{\partial t}p(\mathbf{x},t) = ",
            r"-\sum_{d=1}^{D} \frac{\partial}{\partial x_d}(a_d(\mathbf{x})p(\mathbf{x},t))",
            r"+ \frac{1}{2}\sum_{d,d'} \frac{\partial^2}{\partial x_d \partial x_{d'}} \left( [B(\mathbf{x})B(\mathbf{x})^\top]_{dd'} p(\mathbf{x},t) \right)",
            color=YELLOW,
            font_size=36,
        )
        fpe_eq.shift(UP * 0.8)
        self.play(Write(fpe_eq), run_time=1.2)
        self.wait(1.0)

        terms_label = Text(
            "ドリフト項と拡散項を含む連立偏微分方程式",
            color=TEAL, font_size=24,
        )
        terms_label.shift(DOWN * 0.2)
        self.play(Write(terms_label), run_time=0.8)
        self.wait(0.8)

        today_text = Text(
            "今回は、この方程式の一般解を導出する",
            color=GOLD, font_size=26, weight=BOLD,
        )
        today_text.shift(DOWN * 1.0)
        self.play(Write(today_text), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(recap_text), FadeOut(fpe_eq), FadeOut(terms_label), FadeOut(today_text),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: 線形作用素の定義
        # ============================================================
        subtitle2 = Text("線形作用素の定義", font_size=28, color=GOLD)
        subtitle2.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle2), run_time=0.5)
        self.wait(0.4)

        operator_intro = Text(
            "式を簡潔に書くため、線形作用素を導入する",
            color=WHITE, font_size=26,
        )
        operator_intro.shift(UP * 1.8)
        self.play(Write(operator_intro), run_time=0.8)
        self.wait(0.6)

        L_def = MathTex(
            r"\mathcal{L} = ",
            r"- \sum_{d=1}^{D} \frac{\partial}{\partial x_d} a_d(\mathbf{x})",
            r"+ \frac{1}{2}\sum_{d,d'} \frac{\partial^2}{\partial x_d \partial x_{d'}} [B(\mathbf{x})B(\mathbf{x})^\top]_{dd'}",
            color=YELLOW,
            font_size=34,
        )
        L_def.shift(UP * 0.6)
        # L_box = SurroundingRectangle(L_def, color=YELLOW, buff=0.25)
        self.play(Write(L_def), run_time=1.0)
        self.wait(0.8)

        drift_label = Text("ドリフト部分", color=GREEN, font_size=20)
        drift_label.shift(DOWN * 0.5 + LEFT * 2)
        drift_arrow = Arrow(drift_label.get_top(), L_def[1].get_bottom(), color=GREEN, buff=0.1, stroke_width=3)
        
        diffusion_label = Text("拡散部分", color=BLUE, font_size=20)
        diffusion_label.shift(DOWN * 0.5 + RIGHT * 2.5)
        diffusion_arrow = Arrow(diffusion_label.get_top(), L_def[2].get_bottom(), color=BLUE, buff=0.1, stroke_width=3)

        self.play(
            Write(drift_label), Create(drift_arrow),
            Write(diffusion_label), Create(diffusion_arrow),
            run_time=0.8
        )
        self.wait(1.0)

        linearity_note = Text(
            "この作用素は線形：L(αf + βg) = αL(f) + βL(g)",
            color=ORANGE, font_size=24,
        )
        linearity_note.shift(DOWN * 1.5)
        self.play(Write(linearity_note), run_time=0.8)
        self.wait(0.8)

        self.play(
            FadeOut(operator_intro), FadeOut(drift_label), FadeOut(drift_arrow),
            FadeOut(diffusion_label), FadeOut(diffusion_arrow), FadeOut(linearity_note),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: シンプルな偏微分方程式
        # ============================================================
        subtitle3 = Text("シンプルな形への変換", font_size=28, color=TEAL)
        subtitle3.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle3), run_time=0.5)
        self.wait(0.4)

        simplification_text = Text(
            "線形作用素を使うと、方程式は次のように書ける",
            color=WHITE, font_size=24,
        )
        simplification_text.shift(DOWN * 0.5)
        self.play(Write(simplification_text), run_time=0.8)
        self.wait(0.6)

        simple_eq = MathTex(
            r"\frac{\partial}{\partial t}p(\mathbf{x},t) = \mathcal{L}p(\mathbf{x},t)",
            color=YELLOW,
            font_size=34,
        )
        simple_eq.shift(DOWN * 1.5)
        simple_box = SurroundingRectangle(simple_eq, color=YELLOW, buff=0.3)
        self.play(Write(simple_eq), Create(simple_box), run_time=0.8)
        self.wait(0.8)

        # comparison_text = Text(
        #     "非常にシンプルな形！",
        #     color=GOLD, font_size=24, weight=BOLD,
        # )
        # comparison_text.shift(DOWN * 0.7)
        # self.play(Write(comparison_text), run_time=0.7)
        # self.wait(0.6)

        analogy_text = Text(
            "これは通常の微分方程式 dy/dt = ay と同じ構造",
            color=TEAL, font_size=24,
        )
        analogy_text.shift(DOWN * 2.7)
        self.play(Write(analogy_text), run_time=0.8)
        self.wait(1.0)

        self.play(
            FadeOut(simplification_text), # FadeOut(comparison_text),
            FadeOut(analogy_text),
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: 通常の微分方程式との類似
        # ============================================================
        subtitle4 = Text("通常の微分方程式との類似", font_size=28, color=BLUE)
        subtitle4.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle4), run_time=0.5)
        self.wait(0.4)

        recall_text = Text(
            "dy/dt = ay という方程式を思い出そう",
            color=WHITE, font_size=26,
        )
        recall_text.shift(UP * 1.5)
        self.play(Write(recall_text), run_time=0.8)
        self.wait(0.6)

        # 簡単な方程式を残しながら横に移動
        self.play(
            simple_eq.animate.shift(UP * 1.9 + LEFT * 3.5),
            simple_box.animate.shift(UP * 1.9 + LEFT * 3.5).scale(0.93),
            FadeOut(L_def), #FadeOut(L_box),
            run_time=0.8
        )
        self.wait(0.3)

        ode_eq = MathTex(
            r"\frac{dy}{dt} = ay",
            color=YELLOW,
            font_size=42,
        )
        ode_eq.shift(UP * 0.3 + RIGHT * 3)
        ode_box = SurroundingRectangle(ode_eq, color=YELLOW, buff=0.3)
        self.play(Write(ode_eq), Create(ode_box), run_time=0.8)
        self.wait(0.8)

        # 解の形
        pde_solution = MathTex(
            r"p(\mathbf{x},t) = ?",
            color=GREEN,
            font_size=32,
        )
        pde_solution.shift(DOWN * 0.8 + LEFT * 3.5)
        
        ode_solution = MathTex(
            r"y(t) = e^{at}y(0)",
            color=GREEN,
            font_size=32,
        )
        ode_solution.shift(DOWN * 0.8 + RIGHT * 3)

        self.play(
            FadeOut(recall_text),
            Write(pde_solution), Write(ode_solution),
            run_time=0.8
        )
        self.wait(0.8)

        hint_text = Text(
            "同じ構造なので、同じように解ける！",
            color=GOLD, font_size=24, weight=BOLD,
        )
        hint_text.shift(DOWN * 1.8)
        self.play(Write(hint_text), run_time=0.8)
        self.wait(1.0)

        self.play(
            FadeOut(simple_eq), FadeOut(simple_box),
            FadeOut(ode_eq), FadeOut(ode_box),
            FadeOut(pde_solution), FadeOut(ode_solution),
            FadeOut(hint_text),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: 一般解の導出
        # ============================================================
        subtitle5 = Text("一般解の導出", font_size=28, color=GOLD)
        subtitle5.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle5), run_time=0.5)
        self.wait(0.4)

        derivation_intro = Text(
            "行列指数関数を用いて一般解を書く",
            color=WHITE, font_size=26,
        )
        derivation_intro.shift(UP * 1.8)
        self.play(Write(derivation_intro), run_time=0.8)
        self.wait(0.6)

        general_solution = MathTex(
            r"p(\mathbf{x},t) = e^{\mathcal{L}t}p(\mathbf{x},0)",
            color=YELLOW,
            font_size=44,
        )
        general_solution.shift(UP * 0.5)
        solution_box = SurroundingRectangle(general_solution, color=YELLOW, buff=0.3)
        self.play(Write(general_solution), Create(solution_box), run_time=1.0)
        self.wait(1.0)

        initial_label = Text(
            "p(𝐱,0): 初期条件（t=0での確率密度関数）",
            color=TEAL, font_size=22,
        )
        initial_label.shift(DOWN * 0.5)
        self.play(Write(initial_label), run_time=0.7)
        self.wait(0.6)

        exponential_note = Text(
            "exp(ℒt): 作用素の行列指数関数",
            color=ORANGE, font_size=22,
        )
        exponential_note.shift(DOWN * 1.1)
        self.play(Write(exponential_note), run_time=0.7)
        self.wait(0.6)

        verification = Text(
            "検証: ∂/∂t [exp(ℒt)p(𝐱,0)] = ℒ exp(ℒt)p(𝐱,0) ✓",
            color=GREEN, font_size=22,
        )
        verification.shift(DOWN * 1.8)
        self.play(Write(verification), run_time=0.8)
        self.wait(1.0)

        self.play(
            FadeOut(derivation_intro), FadeOut(initial_label),
            FadeOut(exponential_note), FadeOut(verification),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5.5: 一般解を求めると何が嬉しいか
        # ============================================================
        subtitle5b = Text("一般解を求められると何が嬉しいか？", font_size=28, color=ORANGE)
        subtitle5b.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle5b), run_time=0.5)
        self.wait(0.4)

        # 一般解を小さくして上に残す
        self.play(
            general_solution.animate.shift(UP * 1.3).scale(0.85),
            solution_box.animate.shift(UP * 1.3).scale(0.8),
            run_time=0.6
        )
        self.wait(0.3)

        usefulness_text = Text(
            "確率密度関数の時間発展が分かれば...",
            color=WHITE, font_size=26,
        )
        usefulness_text.shift(UP * 0.8)
        self.play(Write(usefulness_text), run_time=0.8)
        self.wait(0.6)

        benefit_title = Text(
            "確率論で非常に重要な統計量が計算できる！",
            color=GOLD, font_size=28, weight=BOLD,
        )
        benefit_title.shift(UP * 0.2)
        self.play(Write(benefit_title), run_time=0.8)
        self.wait(0.6)

        benefits = VGroup(
            Text("期待値（平均）", color=GREEN, font_size=24),
            Text("モーメント（分布の形を特徴づける量）", color=TEAL, font_size=24),
            Text("分散・共分散", color=BLUE, font_size=24),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        benefits.shift(DOWN + LEFT * 1.2)

        for item in benefits:
            self.play(Write(item), run_time=0.5)
            self.wait(0.2)
        self.wait(0.8)

        key_point = Text(
            "p(𝐱,t) が分かれば、任意の時刻での統計量が求まる",
            color=ORANGE, font_size=26,
        )
        key_point.shift(DOWN * 2.3)
        self.play(Write(key_point), run_time=0.8)
        self.wait(1.2)

        self.play(
            FadeOut(usefulness_text), FadeOut(benefit_title),
            FadeOut(benefits), FadeOut(key_point),
        )
        self.wait(0.3)

        # ============================================================
        # Part 6: 期待値の定義
        # ============================================================
        subtitle6 = Text("期待値の定義", font_size=28, color=TEAL)
        subtitle6.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle6), run_time=0.5)
        self.wait(0.4)

        self.play(
            general_solution.animate.shift(RIGHT * 3.8),
            solution_box.animate.shift(RIGHT * 3.8),
            run_time=0.6
        )
        self.wait(0.3)

        expectation_intro = Text(
            "まずは期待値の定義を確認！",
            color=WHITE, font_size=26,
        )
        expectation_intro.shift(UP * 1.3 + LEFT * 2.1)
        self.play(Write(expectation_intro), run_time=0.8)
        self.wait(0.6)

        self.play(FadeOut(expectation_intro))
        self.wait(0.3)

        expectation_def = MathTex(
            r"\mathbb{E}[f(\mathbf{x})] = \int f(\mathbf{x})p(\mathbf{x},t)d\mathbf{x}",
            color=GREEN,
            font_size=38,
        )
        expectation_def.shift(UP * 0.2)
        exp_box = SurroundingRectangle(expectation_def, color=GREEN, buff=0.25)
        self.play(Write(expectation_def), Create(exp_box), run_time=0.8)
        self.wait(0.8)

        f_note = Text(
            "f(𝐱): 確率変数の関数",
            color=GRAY, font_size=22,
        )
        f_note.shift(DOWN * 0.7)
        self.play(Write(f_note), run_time=0.7)
        self.wait(0.6)

        integral_note = Text(
            "全空間で積分して期待値を計算",
            color=TEAL, font_size=24,
        )
        integral_note.shift(DOWN * 1.3)
        self.play(Write(integral_note), run_time=0.7)
        self.wait(0.8)

        self.play(
            FadeOut(f_note), FadeOut(integral_note),
        )
        self.wait(0.3)

        # ============================================================
        # Part 7: n次モーメント
        # ============================================================
        subtitle7 = Text("n次モーメントの計算", font_size=28, color=BLUE)
        subtitle7.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle7), run_time=0.5)
        self.wait(0.4)

        moment_intro = Text(
            "期待値を使って統計量を計算できる",
            color=WHITE, font_size=26,
        )
        moment_intro.shift(DOWN * 0.9 + LEFT * 3.5)
        self.play(Write(moment_intro), run_time=0.8)
        self.wait(0.6)

        moment_def = MathTex(
            r"\mathbb{E}[X_d^n] = \int x_d^n p(\mathbf{x},t)d\mathbf{x}",
            color=YELLOW,
            font_size=36,
        )
        moment_def.shift(DOWN * 1.3)
        self.play(Write(moment_def), run_time=0.8)
        self.wait(0.8)

        self.play(FadeOut(moment_intro))
        self.wait(0.2)

        examples_title = Text(
            "具体例：",
            color=GOLD, font_size=26, weight=BOLD,
        )
        examples_title.shift(DOWN * 2.1 + LEFT * 3.4)
        self.play(Write(examples_title), run_time=0.6)
        self.wait(0.3)

        # n=1の場合
        moment_n1 = MathTex(
            r"n=1: \quad \mathbb{E}[X_d] = \int x_d p(\mathbf{x},t)d\mathbf{x}",
            color=WHITE,
            font_size=24,
        )
        moment_n1.shift(DOWN * 2.0 + RIGHT * 1.0)
        moment_n1_label = Text("（平均）", color=TEAL, font_size=22)
        moment_n1_label.next_to(moment_n1, RIGHT, buff=0.2)
        
        self.play(Write(moment_n1), Write(moment_n1_label), run_time=0.7)
        self.wait(0.5)

        # n=2の場合
        moment_n2 = MathTex(
            r"n=2: \quad \mathbb{E}[X_d^2] = \int x_d^2 p(\mathbf{x},t)d\mathbf{x}",
            color=WHITE,
            font_size=24,
        )
        moment_n2.shift(DOWN * 2.6 + RIGHT * 1.0)
        moment_n2_label = Text("（2次モーメント）", color=TEAL, font_size=22)
        moment_n2_label.next_to(moment_n2, RIGHT, buff=0.2)
        
        self.play(Write(moment_n2), Write(moment_n2_label), run_time=0.7)
        self.wait(0.8)

        variance_note = Text(
            "分散 = E[X²] - E[X]²",
            color=ORANGE, font_size=24,
        )
        variance_note.shift(DOWN * 3.1+ RIGHT * 1.0)
        self.play(Write(variance_note), run_time=0.7)
        self.wait(1.0)

        self.play(
            FadeOut(moment_def), FadeOut(examples_title),
            FadeOut(moment_n1), FadeOut(moment_n1_label),
            FadeOut(moment_n2), FadeOut(moment_n2_label),
            FadeOut(variance_note),
        )
        self.wait(0.3)

        # ============================================================
        # Part 8: 時間発展する期待値
        # ============================================================
        subtitle8 = Text("時間発展する期待値", font_size=28, color=GOLD)
        subtitle8.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle8), run_time=0.5)
        self.wait(0.4)

        time_evolution_intro = Text(
            "一般解を代入すると、時間依存性が明示的に",
            color=WHITE, font_size=26,
        )
        time_evolution_intro.shift(DOWN * 0.8)
        self.play(Write(time_evolution_intro), run_time=0.8)
        self.wait(0.6)

        # 期待値の式を再表示
        self.play(
            general_solution.animate.shift(DOWN * 1.8 + LEFT * 2.5).scale(0.0),
            solution_box.animate.shift(DOWN * 1.8 + LEFT * 2.5).scale(0.0),
            # expectation_def.animate.shift(DOWN * 0.3).scale(0.95),
            # exp_box.animate.shift(DOWN * 0.3).scale(0.95),
            FadeOut(time_evolution_intro),
            run_time=0.6
        )
        self.wait(0.3)

        substitution = MathTex(
            r"\mathbb{E}[g(\mathbf{x})] = \int g(\mathbf{x}) e^{\mathcal{L}t}p(\mathbf{x},0) d\mathbf{x}",
            color=YELLOW,
            font_size=36,
        )
        substitution.shift(DOWN * 1.3)
        self.play(Write(substitution), run_time=1.0)
        self.wait(0.8)

        advantage = Text(
            "初期分布p(𝐱,0)から任意の時刻tでの期待値が計算可能",
            color=TEAL, font_size=26,
        )
        advantage.shift(DOWN * 2.5)
        self.play(Write(advantage), run_time=0.8)
        self.wait(1.5)

        self.play( 
            FadeOut(general_solution), FadeOut(solution_box),
            FadeOut(expectation_def), FadeOut(exp_box),
            FadeOut(advantage),
        )
        self.wait(0.3)

        # ============================================================
        # Part 9: デルタ関数の初期条件
        # ============================================================
        subtitle9 = Text("デルタ関数の初期条件", font_size=28, color=TEAL)
        subtitle9.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle9), run_time=0.5)
        self.wait(0.4)
        
        self.play(
            substitution.animate.shift(UP * 2.4).scale(1.25),
            run_time=0.6
        )
        delta_intro = Text(
            "初期分布を点に集中させる場合を考える",
            color=WHITE, font_size=26,
        )
        delta_intro.shift(DOWN * 0.8)
        self.play(Write(delta_intro), run_time=0.8)
        self.wait(0.6)

        delta_condition = MathTex(
            r"p(\mathbf{x},0) = \delta(\mathbf{x} - \mathbf{x}_0)",
            color=YELLOW,
            font_size=36,
        )
        delta_condition.shift(DOWN * 1.5)
        self.play(
            FadeOut(delta_intro),
            Write(delta_condition),
            run_time=0.8
        )
        self.wait(0.8)

        delta_meaning = Text(
            "粒子が初期位置 𝐱₀ に確実に存在する",
            color=TEAL, font_size=26,
        )
        delta_meaning.shift(DOWN * 2.3)
        self.play(Write(delta_meaning), run_time=0.7)
        self.wait(0.8)

        self.play(
            FadeOut(delta_meaning),
        )
        self.wait(0.3)

        # ============================================================
        # Part 10: デルタ関数での期待値計算
        # ============================================================
        subtitle10 = Text("デルタ関数での期待値計算", font_size=28, color=BLUE)
        subtitle10.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle10), run_time=0.5)
        self.wait(0.4)

        calculation_steps = Text(
            "期待値の計算式に代入する",
            color=WHITE, font_size=26,
        )
        calculation_steps.shift(DOWN * 2.5)
        self.play(Write(calculation_steps), run_time=0.8)
        self.wait(0.6)

        # 一般解と期待値の式を小さくして上に
        self.play(
            # general_solution.animate.shift(UP * 0.4).scale(0.75),
            # solution_box.animate.shift(UP * 0.4).scale(0.75),
            # expectation_def.animate.shift(UP * 0.4).scale(0.75),
            # exp_box.animate.shift(UP * 0.4).scale(0.75),
            delta_condition.animate.shift(UP * 3.45 + RIGHT * 1.4).scale(0.0),
            FadeOut(calculation_steps),
            run_time=0.6
        )
        self.wait(0.3)

        step1 = MathTex(
            r"\mathbb{E}[g(\mathbf{x})] = \int g(\mathbf{x})p(\mathbf{x},t)d\mathbf{x}",
            color=WHITE,
            font_size=32,
        )
        # step1.shift(UP * 1.0)
        # self.play(Write(step1), run_time=0.8)
        # self.wait(0.5)

        # step2 = MathTex(
        #     r"= \int g(\mathbf{x}) e^{\mathcal{L}t}p(\mathbf{x},0) d\mathbf{x}",
        #     color=WHITE,
        #     font_size=32,
        # )
        # step2.shift(UP * 0.1)
        # self.play(Write(step2), run_time=0.8)
        # self.wait(0.5)

        step3 = MathTex(
            r"= \int g(\mathbf{x}) e^{\mathcal{L}t}\delta(\mathbf{x} - \mathbf{x}_0) d\mathbf{x}",
            color=YELLOW,
            font_size=36,
        )
        step3.shift(DOWN * 0.6)
        step3_box = SurroundingRectangle(step3, color=YELLOW, buff=0.2)
        self.play(Write(step3), Create(step3_box), run_time=0.8)
        self.wait(1.0)

        final_note = Text(
            "これが初期位置 𝐱₀ からの時間発展を表す",
            color=GOLD, font_size=26,
        )
        final_note.shift(DOWN * 1.8)
        self.play(Write(final_note), run_time=0.8)
        self.wait(1.8)

        self.play(
            # FadeOut(step1), FadeOut(step2), 
            FadeOut(step3), FadeOut(step3_box),
            FadeOut(final_note), FadeOut(delta_condition),
            FadeOut(substitution),
        )
        self.wait(0.3)

        # # ============================================================
        # # Part 11: 具体例（1次元ドリフト拡散）
        # # ============================================================
        # subtitle11 = Text("具体例：1次元ドリフト拡散", font_size=28, color=GOLD)
        # subtitle11.next_to(title, DOWN)
        # self.play(Transform(subtitle1, subtitle11), run_time=0.5)
        # self.wait(0.4)


        # self.wait(0.3)

        # example_intro = Text(
        #     "1次元での簡単な例を見てみよう",
        #     color=WHITE, font_size=26,
        # )
        # example_intro.shift(UP * 1.8)
        # self.play(Write(example_intro), run_time=0.8)
        # self.wait(0.6)

        # example_operator = MathTex(
        #     r"\mathcal{L} = -\gamma \frac{\partial}{\partial x} + \frac{D}{2} \frac{\partial^2}{\partial x^2}",
        #     color=YELLOW,
        #     font_size=36,
        # )
        # example_operator.shift(UP * 0.9)
        # self.play(Write(example_operator), run_time=0.8)
        # self.wait(0.6)

        # example_params = Text(
        #     "γ: ドリフト係数、D: 拡散係数",
        #     color=GRAY, font_size=22,
        # )
        # example_params.shift(UP * 0.2)
        # self.play(Write(example_params), run_time=0.7)
        # self.wait(0.5)

        # # グラフの作成
        # axes = Axes(
        #     x_range=[-4, 4, 1],
        #     y_range=[0, 1.2, 0.2],
        #     x_length=8,
        #     y_length=4,
        #     axis_config={"color": WHITE},
        #     tips=False,
        # )
        # axes.scale(0.7).shift(DOWN * 1.3)

        # x_label = axes.get_x_axis_label("x", direction=RIGHT, buff=0.2).scale(0.8)
        # y_label = axes.get_y_axis_label("p(x,t)", direction=UP, buff=0.2).scale(0.8)

        # self.play(
        #     FadeOut(example_intro), FadeOut(example_params),
        #     Create(axes), Write(x_label), Write(y_label),
        #     run_time=0.8
        # )
        # self.wait(0.5)

        # # 時間発展の可視化
        # def gaussian(x, mu=0, sigma=1):
        #     return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

        # time_params = [
        #     (-1.5, 0.3),
        #     (-0.5, 0.5),
        #     (0.5, 0.7),
        #     (1.5, 0.9),
        # ]

        # graphs = []
        # time_labels = []

        # for i, (mu, sigma) in enumerate(time_params):
        #     graph = axes.plot(
        #         lambda x: gaussian(x, mu=mu, sigma=sigma),
        #         x_range=[-4, 4],
        #         color=interpolate_color(YELLOW, PURPLE, i / (len(time_params) - 1))
        #     )
        #     graphs.append(graph)
            
        #     time_label = MathTex(f"t = {i * 0.5}", color=WHITE, font_size=20)
        #     time_label.shift(UP * 1.8 + RIGHT * 4.5)
        #     time_labels.append(time_label)

        # # 最初のグラフ
        # self.play(Create(graphs[0]), Write(time_labels[0]), run_time=0.8)
        # self.wait(0.5)

        # # 時間発展
        # for i in range(1, len(graphs)):
        #     self.play(
        #         Transform(graphs[0], graphs[i]),
        #         FadeOut(time_labels[i-1]),
        #         Write(time_labels[i]),
        #         run_time=0.9
        #     )
        #     self.wait(0.4)

        # conclusion_example = Text(
        #     "ドリフト（移動）と拡散（広がり）が同時に起こる",
        #     color=TEAL, font_size=22,
        # )
        # conclusion_example.shift(DOWN * 3.2)
        # self.play(Write(conclusion_example), run_time=0.8)
        # self.wait(1.2)

        # self.play(
        #     FadeOut(example_operator), FadeOut(axes), FadeOut(x_label), FadeOut(y_label),
        #     FadeOut(graphs[0]), FadeOut(time_labels[-1]), FadeOut(conclusion_example),
        # )
        # self.wait(0.3)

        # ============================================================
        # Part 12: まとめ
        # ============================================================
        subtitle12 = Text("まとめ", font_size=36, color=TEAL)
        subtitle12.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle12), run_time=0.6)
        self.wait(0.4)

        summary = VGroup(
            Text("• 線形作用素ℒで方程式を簡潔に表現", color=WHITE, font_size=26),
            Text("• 一般解：p(𝐱,t) = exp(ℒt)p(𝐱,0)", color=WHITE, font_size=26),
            Text("• 期待値：E[f(𝐱)] = ∫f(𝐱)p(𝐱,t)d𝐱", color=WHITE, font_size=26),
            Text("• n次モーメントで統計量を計算", color=WHITE, font_size=26),
            Text("• デルタ関数の初期条件で点からの発展を記述", color=WHITE, font_size=26),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        summary.shift(UP * 0.2)
        
        for row in summary:
            self.play(Write(row), run_time=0.6)
            self.wait(0.3)
        
        self.wait(1.0)

        final_message = VGroup(
            Text(
                "ただし、結局具体的な計算のためには、",
                color=GOLD, font_size=24,
            ),
            Text(
                "適当に基底をとって線形作用素の表現行列を定める必要がある？",
                color=GOLD, font_size=24,
            )
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
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
