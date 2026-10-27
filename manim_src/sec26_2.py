from manim import *
import numpy as np


class KoopmanMatrixEstimation(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        title = Text("クープマン行列の推定方法", font_size=38, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)

        # ============================================================
        # Part 1: 導入 — 前回の復習と今回の目標
        # ============================================================
        subtitle = Text("導入：最小二乗法でクープマン行列を解く", font_size=27, color=BLUE)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle), run_time=0.6)
        self.wait(0.3)

        intro1 = Text(
            "前の動画では、クープマン行列をデータから回帰で求められると分かった",
            color=WHITE, font_size=26,
        )
        intro1.shift(UP * 1.7)
        if intro1.width > config.frame_width - 1.0:
            intro1.scale_to_fit_width(config.frame_width - 1.0)
        self.play(Write(intro1), run_time=0.8)
        self.wait(0.3)

        intro2 = Text(
            "今回は、実際に最小二乗法を解いて行列を得る具体的な手順を見る",
            color=GOLD, font_size=26, weight=BOLD,
        )
        intro2.shift(UP * 0.9)
        if intro2.width > config.frame_width - 1.0:
            intro2.scale_to_fit_width(config.frame_width - 1.0)
        self.play(Write(intro2), run_time=0.8)
        self.wait(0.3)

        intro3 = Text(
            "回帰の元になる誤差関数（コスト関数）は次のように定義された",
            color=WHITE, font_size=26,
        )
        intro3.shift(DOWN * 0.1)
        self.play(Write(intro3), run_time=0.8)

        intro_eq = MathTex(
            r"J(K) = \sum_{n=1}^{N} \left\| \boldsymbol{\psi}(\boldsymbol{y}_n) "
            r"- K\, \boldsymbol{\psi}(\boldsymbol{x}_n) \right\|^2",
            font_size=42, color=YELLOW,
        )
        if intro_eq.width > config.frame_width - 0.8:
            intro_eq.scale_to_fit_width(config.frame_width - 0.8)
        intro_eq.shift(DOWN * 1.3)
        intro_box = SurroundingRectangle(intro_eq, color=YELLOW, buff=0.22)
        self.play(Write(intro_eq), Create(intro_box), run_time=1.0)
        self.wait(1.8)

        self.play(
            FadeOut(intro1), FadeOut(intro2), FadeOut(intro3),
            FadeOut(intro_eq), FadeOut(intro_box),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: 最適化方針 — 制約なしの二次系
        # ============================================================
        subtitle2 = Text("最適化の方針：制約なしの二次系", font_size=28, color=GOLD)
        subtitle2.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle2), run_time=0.5)
        self.wait(0.3)

        plan1 = VGroup(
            Text("この J は、2部で見た最小二乗法と同じ", color=WHITE, font_size=26),
            Text("制約なしの二次系", color=TEAL, font_size=26, weight=BOLD),
        ).arrange(RIGHT, buff=0.12)
        plan1.shift(UP * 1.6)
        self.play(Write(plan1), run_time=0.8)
        self.wait(0.3)

        plan2 = Text(
            "したがって、得たいパラメータ K で微分して 0 とおいた式で分かる停留点が、",
            color=WHITE, font_size=25,
        )
        plan2.shift(UP * 0.6)
        if plan2.width > config.frame_width - 0.8:
            plan2.scale_to_fit_width(config.frame_width - 0.8)
        plan3 = Text(
            "そのまま大域的最適解になる",
            color=GOLD, font_size=26, weight=BOLD,
        )
        plan3.next_to(plan2, DOWN, buff=0.25)
        self.play(Write(plan2), run_time=0.8)
        self.play(Write(plan3), run_time=0.6)
        self.wait(0.3)

        plan_eq = MathTex(
            r"\frac{\partial J}{\partial K} = \boldsymbol{0}"
            r"\quad\Longrightarrow\quad \hat{K}=\cdots",
            font_size=44, color=YELLOW,
        )
        plan_eq.shift(DOWN * 1.5)
        self.play(Write(plan_eq), run_time=0.8)
        self.wait(1.8)

        self.play(
            FadeOut(plan1), FadeOut(plan2), FadeOut(plan3), FadeOut(plan_eq),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: コスト関数の式展開
        # ============================================================
        subtitle3 = Text("ステップ1：コスト関数を式展開する", font_size=28, color=TEAL)
        subtitle3.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle3), run_time=0.5)
        self.wait(0.3)

        exp_eq = MathTex(
            r"J(K)",
            r"&= \sum_{n=1}^{N} \left\| \boldsymbol{\psi}(\boldsymbol{y}_n) "
            r"- K\, \boldsymbol{\psi}(\boldsymbol{x}_n) \right\|^2 \\",
            r"&= \sum_{n=1}^{N} \bigl(\boldsymbol{\psi}(\boldsymbol{y}_n) - K\boldsymbol{\psi}(\boldsymbol{x}_n)\bigr)^{\top}"
            r"\bigl(\boldsymbol{\psi}(\boldsymbol{y}_n) - K\boldsymbol{\psi}(\boldsymbol{x}_n)\bigr) \\",
            r"&= \sum_{n=1}^{N} \Big( \boldsymbol{\psi}(\boldsymbol{y}_n)^{\top}\boldsymbol{\psi}(\boldsymbol{y}_n)"
            r"- \boldsymbol{\psi}(\boldsymbol{y}_n)^{\top} K \boldsymbol{\psi}(\boldsymbol{x}_n) \\",
            r"&\qquad\quad - \boldsymbol{\psi}(\boldsymbol{x}_n)^{\top} K^{\top} \boldsymbol{\psi}(\boldsymbol{y}_n)"
            r"+ \boldsymbol{\psi}(\boldsymbol{x}_n)^{\top} K^{\top} K \boldsymbol{\psi}(\boldsymbol{x}_n) \Big)",
            font_size=34, color=WHITE,
        )
        if exp_eq.width > config.frame_width - 0.8:
            exp_eq.scale_to_fit_width(config.frame_width - 0.8)
        exp_eq.shift(DOWN * 0.3)
        self.play(Write(exp_eq[0]), Write(exp_eq[1]), run_time=1.0)
        self.wait(0.3)
        self.play(Write(exp_eq[2]), run_time=1.0)
        self.wait(0.3)
        self.play(Write(exp_eq[3]), Write(exp_eq[4]), run_time=1.3)
        self.wait(1.8)

        self.play(FadeOut(exp_eq), run_time=0.8)
        self.wait(0.3)

        # ============================================================
        # Part 4: 行列微分の公式
        # ============================================================
        subtitle4 = Text("ステップ2：行列微分の公式を用意する", font_size=28, color=ORANGE)
        subtitle4.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle4), run_time=0.5)
        self.wait(0.3)

        form_intro = Text(
            "これを K で微分していくため、行列を含む微分の公式を用意する",
            color=WHITE, font_size=26,
        )
        form_intro.shift(UP * 1.9)
        if form_intro.width > config.frame_width - 0.8:
            form_intro.scale_to_fit_width(config.frame_width - 0.8)
        self.play(Write(form_intro), run_time=0.8)
        self.wait(0.3)

        # --- 1つ目：元になる基本公式 → 転置を使った導出 ---
        base1 = MathTex(
            r"\frac{\partial}{\partial A}\, \boldsymbol{a}^{\top} A \boldsymbol{b}"
            r"= \boldsymbol{a}\boldsymbol{b}^{\top}",
            font_size=34, color=TEAL,
        )
        if base1.width > config.frame_width - 0.8:
            base1.scale_to_fit_width(config.frame_width - 0.8)
        base1.shift(UP)
        base1_lab = Text("基本公式", color=TEAL, font_size=20)
        base1_lab.next_to(base1, LEFT, buff=0.3)
        self.play(Write(base1), FadeIn(base1_lab), run_time=0.9)
        self.wait(0.3)

        form1 = MathTex(
            r"\frac{\partial}{\partial A}\, \boldsymbol{c}^{\top} A^{\top} \boldsymbol{d}"
            r"= \left( \frac{\partial}{\partial A^{\top}}\, \boldsymbol{c}^{\top} A^{\top} \boldsymbol{d} \right)^{\top}"
            r"= (\boldsymbol{c}\boldsymbol{d}^{\top})^{\top} = \boldsymbol{d}\boldsymbol{c}^{\top}",
            font_size=36, color=WHITE,
        )
        if form1.width > config.frame_width - 0.8:
            form1.scale_to_fit_width(config.frame_width - 0.8)
        form1.shift(UP * 0.1)
        self.play(Write(form1), run_time=1.2)
        self.wait(0.4)

        # --- 2つ目：元になる基本公式 → 転置を使った導出 ---
        base2 = MathTex(
            r"\frac{\partial}{\partial A}\, \boldsymbol{a}^{\top} A A^{\top} \boldsymbol{b}"
            r"= \bigl(\boldsymbol{a}\boldsymbol{b}^{\top} + \boldsymbol{b}\boldsymbol{a}^{\top}\bigr) A",
            font_size=34, color=TEAL,
        )
        if base2.width > config.frame_width - 0.8:
            base2.scale_to_fit_width(config.frame_width - 0.8)
        base2.shift(DOWN * 1.2)
        base2_lab = Text("基本公式", color=TEAL, font_size=20)
        base2_lab.next_to(base2, LEFT, buff=0.3)
        self.play(Write(base2), FadeIn(base2_lab), run_time=0.9)
        self.wait(0.3)

        form2 = MathTex(
            r"\frac{\partial}{\partial A}\, \boldsymbol{c}^{\top} A^{\top} A \boldsymbol{d}"
            r"= \left( \bigl(\boldsymbol{c}\boldsymbol{d}^{\top} + \boldsymbol{d}\boldsymbol{c}^{\top}\bigr) A^{\top} \right)^{\top}"
            r"= A\bigl(\boldsymbol{c}\boldsymbol{d}^{\top} + \boldsymbol{d}\boldsymbol{c}^{\top}\bigr)",
            font_size=36, color=WHITE,
        )
        if form2.width > config.frame_width - 0.8:
            form2.scale_to_fit_width(config.frame_width - 0.8)
        form2.shift(DOWN * 2.1)
        self.play(Write(form2), run_time=1.2)
        self.wait(1.8)

        self.play(
            FadeOut(form_intro),
            FadeOut(base1), FadeOut(base1_lab), FadeOut(form1),
            FadeOut(base2), FadeOut(base2_lab), FadeOut(form2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: K で微分した式
        # ============================================================
        subtitle5 = Text("ステップ3：K で微分する", font_size=28, color=YELLOW)
        subtitle5.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle5), run_time=0.5)
        self.wait(0.3)

        deriv_intro = Text(
            "公式を各項に当てはめると、コスト関数の K による微分は",
            color=WHITE, font_size=26,
        )
        deriv_intro.shift(UP * 1.8)
        self.play(Write(deriv_intro), run_time=0.8)
        self.wait(0.3)

        deriv_eq = MathTex(
            r"\frac{\partial J}{\partial K}",
            r"&= \sum_{n=1}^{N} \Big( -\boldsymbol{\psi}(\boldsymbol{y}_n)\boldsymbol{\psi}(\boldsymbol{x}_n)^{\top}"
            r"- \boldsymbol{\psi}(\boldsymbol{y}_n)\boldsymbol{\psi}(\boldsymbol{x}_n)^{\top} \\",
            r"&\qquad\quad + K\bigl(\boldsymbol{\psi}(\boldsymbol{x}_n)\boldsymbol{\psi}(\boldsymbol{x}_n)^{\top}"
            r"+ \boldsymbol{\psi}(\boldsymbol{x}_n)\boldsymbol{\psi}(\boldsymbol{x}_n)^{\top}\bigr) \Big) \\",
            r"&= \sum_{n=1}^{N} \Big( -2\,\boldsymbol{\psi}(\boldsymbol{y}_n)\boldsymbol{\psi}(\boldsymbol{x}_n)^{\top}"
            r"+ 2K\,\boldsymbol{\psi}(\boldsymbol{x}_n)\boldsymbol{\psi}(\boldsymbol{x}_n)^{\top} \Big)",
            font_size=34, color=WHITE,
        )
        if deriv_eq.width > config.frame_width - 0.8:
            deriv_eq.scale_to_fit_width(config.frame_width - 0.8)
        deriv_eq.shift(DOWN * 0.4)
        self.play(Write(deriv_eq[0]), Write(deriv_eq[1]), Write(deriv_eq[2]), run_time=1.5)
        self.wait(0.4)
        self.play(Write(deriv_eq[3]), run_time=1.2)
        self.wait(1.8)

        self.play(
            FadeOut(deriv_intro), FadeOut(deriv_eq),
        )
        self.wait(0.3)

        # ============================================================
        # Part 6: データ行列の定義
        # ============================================================
        subtitle6 = Text("ステップ4：データ行列でまとめて書く", font_size=28, color=PURPLE)
        subtitle6.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle6), run_time=0.5)
        self.wait(0.3)

        data_intro = Text(
            "N個のスナップショットを並べたデータ行列を定義する",
            color=WHITE, font_size=26,
        )
        data_intro.shift(UP * 1.9)
        self.play(Write(data_intro), run_time=0.8)
        self.wait(0.3)

        psi_x_mat = MathTex(
            r"\Psi_X = \begin{bmatrix}"
            r"\psi_1(\boldsymbol{x}_1) & \dots & \psi_1(\boldsymbol{x}_N) \\"
            r"\vdots & \ddots & \vdots \\"
            r"\psi_M(\boldsymbol{x}_1) & \dots & \psi_M(\boldsymbol{x}_N)"
            r"\end{bmatrix}",
            font_size=34, color=WHITE,
        )
        psi_y_mat = MathTex(
            r"\Psi_Y = \begin{bmatrix}"
            r"\psi_1(\boldsymbol{y}_1) & \dots & \psi_1(\boldsymbol{y}_N) \\"
            r"\vdots & \ddots & \vdots \\"
            r"\psi_M(\boldsymbol{y}_1) & \dots & \psi_M(\boldsymbol{y}_N)"
            r"\end{bmatrix}",
            font_size=34, color=WHITE,
        )
        mats = VGroup(psi_x_mat, psi_y_mat).arrange(RIGHT, buff=0.8)
        if mats.width > config.frame_width - 0.8:
            mats.scale_to_fit_width(config.frame_width - 0.8)
        mats.shift(UP * 0.6)
        self.play(Write(psi_x_mat), run_time=1.0)
        self.play(Write(psi_y_mat), run_time=1.0)
        self.wait(0.4)

        data_rel = Text(
            "すると、微分式に現れた和が次のように書き換えられる",
            color=WHITE, font_size=25,
        )
        data_rel.shift(DOWN * 1.1)
        self.play(Write(data_rel), run_time=0.7)

        data_eq = MathTex(
            r"\sum_{n=1}^{N} \boldsymbol{\psi}(\boldsymbol{x}_n)\boldsymbol{\psi}(\boldsymbol{x}_n)^{\top}"
            r"= \Psi_X \Psi_X^{\top},"
            r"\quad"
            r"\sum_{n=1}^{N} \boldsymbol{\psi}(\boldsymbol{y}_n)\boldsymbol{\psi}(\boldsymbol{x}_n)^{\top}"
            r"= \Psi_Y \Psi_X^{\top}",
            font_size=34, color=YELLOW,
        )
        if data_eq.width > config.frame_width - 0.8:
            data_eq.scale_to_fit_width(config.frame_width - 0.8)
        data_eq.shift(DOWN * 2.1)
        self.play(Write(data_eq), run_time=1.2)
        self.wait(1.8)

        self.play(
            FadeOut(data_intro), FadeOut(mats), FadeOut(data_rel), FadeOut(data_eq),
        )
        self.wait(0.3)

        # ============================================================
        # Part 7: 停留点を解く
        # ============================================================
        subtitle7 = Text("ステップ5：微分を 0 とおいて解く", font_size=28, color=GOLD)
        subtitle7.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle7), run_time=0.5)
        self.wait(0.3)

        solve_intro = Text(
            "データ行列を微分式に代入すると",
            color=WHITE, font_size=26,
        )
        solve_intro.shift(UP * 1.9)
        self.play(Write(solve_intro), run_time=0.6)

        solve_eq1 = MathTex(
            r"\frac{\partial J}{\partial K} = -2\,\Psi_Y \Psi_X^{\top} + 2K\,\Psi_X \Psi_X^{\top}",
            font_size=38, color=WHITE,
        )
        solve_eq1.shift(UP * 1.2)
        self.play(Write(solve_eq1), run_time=0.9)
        self.wait(0.4)

        solve_mid = Text(
            "これを 𝟎 とおくと",
            color=WHITE, font_size=26,
        )
        solve_mid.shift(UP * 0.3)
        self.play(Write(solve_mid), run_time=0.5)

        solve_eq2 = MathTex(
            r"K\,\Psi_X \Psi_X^{\top} = \Psi_Y \Psi_X^{\top}",
            font_size=40, color=WHITE,
        )
        solve_eq2.shift(DOWN * 0.5)
        self.play(Write(solve_eq2), run_time=0.8)
        self.wait(0.4)

        solve_concl = Text(
            "したがって、データから求めた推定値 K̂（ハット付き）は",
            color=WHITE, font_size=25,
        )
        solve_concl.shift(DOWN * 1.4)
        self.play(Write(solve_concl), run_time=0.7)

        solve_eq3 = MathTex(
            r"\hat{K} = \Psi_Y \Psi_X^{\top} \bigl(\Psi_X \Psi_X^{\top}\bigr)^{-1}",
            font_size=44, color=YELLOW,
        )
        solve_eq3.shift(DOWN * 2.4)
        solve_box = SurroundingRectangle(solve_eq3, color=YELLOW, buff=0.22)
        self.play(Write(solve_eq3), Create(solve_box), run_time=1.0)
        self.wait(1.8)

        self.play(
            FadeOut(solve_intro), FadeOut(solve_eq1), FadeOut(solve_mid),
            FadeOut(solve_eq2), FadeOut(solve_concl),
            FadeOut(solve_eq3), FadeOut(solve_box),
        )
        self.wait(0.3)

        # ============================================================
        # Part 8: 疑似逆行列（特異値分解）
        # ============================================================
        subtitle8 = Text("逆行列が無いとき：疑似逆行列を使う", font_size=27, color=RED)
        subtitle8.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle8), run_time=0.5)
        self.wait(0.3)

        pinv1 = VGroup(
            MathTex(r"\Psi_X \Psi_X^{\top}", color=WHITE, font_size=30),
            Text("は、必ずしも逆行列を持つとは限らない", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.15)
        pinv1.shift(UP * 1.8)
        self.play(Write(pinv1), run_time=0.8)
        self.wait(0.3)

        pinv2 = VGroup(
            Text("そこで", color=WHITE, font_size=26),
            MathTex(r"\Psi_X^{\top}\bigl(\Psi_X \Psi_X^{\top}\bigr)^{-1}", color=TEAL, font_size=30),
            Text("の部分を", color=WHITE, font_size=26),
            Text("右疑似逆行列", color=GOLD, font_size=26, weight=BOLD),
            MathTex(r"\Psi_X^{\dagger}", color=GOLD, font_size=34),
            Text("とみなす", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.12)
        if pinv2.width > config.frame_width - 0.8:
            pinv2.scale_to_fit_width(config.frame_width - 0.8)
        pinv2.shift(UP * 0.9)
        self.play(Write(pinv2), run_time=1.0)
        self.wait(0.3)

        pinv3 = Text(
            "18話で見たように、特異値分解で得た特異値を使って疑似逆行列を作れる",
            color=WHITE, font_size=26,
        )
        pinv3.shift(UP * 0.0)
        if pinv3.width > config.frame_width - 0.8:
            pinv3.scale_to_fit_width(config.frame_width - 0.8)
        self.play(Write(pinv3), run_time=0.8)
        self.wait(0.3)

        pinv_eq = MathTex(
            r"\Psi_X^{\dagger} = V"
            r"\begin{bmatrix}"
            r"\Sigma_{R \times R}^{-1} & \mathbf{0}_{R \times m} \\"
            r"\mathbf{0}_{n \times R} & \mathbf{0}_{n \times m}"
            r"\end{bmatrix} U^{\top}",
            font_size=40, color=WHITE,
        )
        if pinv_eq.width > config.frame_width - 0.8:
            pinv_eq.scale_to_fit_width(config.frame_width - 0.8)
        pinv_eq.shift(DOWN * 1.4)
        pinv_box = SurroundingRectangle(pinv_eq, color=GOLD, buff=0.22)
        self.play(Write(pinv_eq), Create(pinv_box), run_time=1.1)
        self.wait(0.3)

        pinv4 = VGroup(
            Text("これを使えば、", color=WHITE, font_size=26),
            MathTex(r"\hat{K} = \Psi_Y \Psi_X^{\dagger}", color=YELLOW, font_size=34),
            Text("が計算できる", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.15)
        pinv4.shift(DOWN * 2.8)
        self.play(Write(pinv4), run_time=0.9)
        self.wait(1.8)

        self.play(
            FadeOut(pinv1), FadeOut(pinv2), FadeOut(pinv3),
            FadeOut(pinv_eq), FadeOut(pinv_box), FadeOut(pinv4),
        )
        self.wait(0.3)

        # ============================================================
        # Part 9: まとめ
        # ============================================================
        subtitle9 = Text("まとめ", font_size=34, color=TEAL)
        subtitle9.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle9), run_time=0.6)
        self.wait(0.3)

        summary = VGroup(
            Text("• コスト関数 J(K) は制約なしの二次系 → 停留点が大域的最適解",
                 color=WHITE, font_size=25),
            Text("• J を展開し、行列微分の公式で K について微分する",
                 color=WHITE, font_size=25),
            Text("• ∂J/∂K = −2Ψ_Y Ψ_Xᵀ + 2K Ψ_X Ψ_Xᵀ を 0 とおく",
                 color=WHITE, font_size=25),
            Text("• 解は K̂ = Ψ_Y Ψ_Xᵀ (Ψ_X Ψ_Xᵀ)⁻¹（データからの推定値）",
                 color=WHITE, font_size=25),
            Text("• 逆行列が無い場合は右疑似逆行列 Ψ_X† を特異値分解で構成",
                 color=WHITE, font_size=25),
            Text("• まとめると K̂ = Ψ_Y Ψ_X† でクープマン行列が求まる",
                 color=GOLD, font_size=25, weight=BOLD),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        summary.shift(DOWN * 0.1)
        if summary.width > config.frame_width - 0.8:
            summary.scale_to_fit_width(config.frame_width - 0.8)

        for row in summary:
            self.play(Write(row), run_time=0.55)
            self.wait(0.15)
        self.wait(2.0)

        self.play(
            FadeOut(VGroup(title, subtitle, summary)),
            run_time=1.0,
        )
        self.wait(0.5)
