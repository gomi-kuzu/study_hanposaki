from manim import *
import numpy as np


class KoopmanModeDecompositionProcedure(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        title = Text("クープマンモード分解の具体的手順", font_size=38, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)

        # ============================================================
        # Part 1: 導入 — 前回の復習と今回の目標
        # ============================================================
        subtitle = Text("導入：概要から具体的手順へ", font_size=27, color=BLUE)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle), run_time=0.6)
        self.wait(0.3)

        intro1 = Text(
            "前回の動画では、クープマンモード分解の概要と利点を学んだ",
            color=WHITE, font_size=26,
        )
        intro1.shift(UP * 1.9)
        if intro1.width > config.frame_width - 1.0:
            intro1.scale_to_fit_width(config.frame_width - 1.0)
        self.play(Write(intro1), run_time=0.8)
        self.wait(0.3)

        intro2 = Text(
            "今回は、その分解を実際に求めるための具体的な手順を確認する",
            color=WHITE, font_size=26,
        )
        intro2.shift(UP * 1.0)
        if intro2.width > config.frame_width - 1.0:
            intro2.scale_to_fit_width(config.frame_width - 1.0)
        self.play(Write(intro2), run_time=0.8)
        self.wait(0.3)

        intro3 = VGroup(
            Text("前提：26話で学んだ方法などを使って、", color=WHITE, font_size=26),
            Text("クープマン行列の推定値", color=WHITE, font_size=26),
            MathTex(r"\hat{K}", color=GOLD, font_size=36),
            Text("が得られているとする", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.12)
        if intro3.width > config.frame_width - 0.8:
            intro3.scale_to_fit_width(config.frame_width - 0.8)
        intro3.shift(DOWN * 0.1)
        self.play(Write(intro3), run_time=0.9)
        self.wait(0.3)

        intro4 = VGroup(
            Text("以下の説明では、単に", color=WHITE, font_size=26),
            MathTex(r"K", color=TEAL, font_size=36),
            Text("と書く", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.15)
        intro4.shift(DOWN * 1.0)
        self.play(Write(intro4), run_time=0.7)
        self.wait(1.8)

        self.play(
            FadeOut(intro1), FadeOut(intro2),
            FadeOut(intro3), FadeOut(intro4),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: 補足 — 回帰の向きについての注意
        # ============================================================
        subtitle2 = Text("補足：K の定義の向きについて", font_size=28, color=GOLD)
        subtitle2.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle2), run_time=0.5)
        self.wait(0.3)

        rem1 = Text(
            "26.1節では、回帰の目的のイメージとして次のように書いた",
            color=WHITE, font_size=26,
        )
        rem1.shift(UP * 1.9)
        if rem1.width > config.frame_width - 0.8:
            rem1.scale_to_fit_width(config.frame_width - 0.8)
        self.play(Write(rem1), run_time=0.8)

        rem_eq1 = MathTex(
            r"\boldsymbol{c} = K\,\boldsymbol{c}_{\text{ini}}",
            font_size=40, color=WHITE,
        )
        rem_eq1.shift(UP * 0.7)
        self.play(Write(rem_eq1), run_time=0.7)
        self.wait(0.3)

        rem2 = Text(
            "しかし結果的に、K は辞書ベクトルを写す行列として定義された",
            color=WHITE, font_size=26,
        )
        rem2.shift(DOWN * 0.3)
        if rem2.width > config.frame_width - 0.8:
            rem2.scale_to_fit_width(config.frame_width - 0.8)
        self.play(Write(rem2), run_time=0.8)
        self.wait(0.3)

        rem3 = Text(
            "よって正確には次の形になる",
            color=GOLD, font_size=26, weight=BOLD,
        )
        rem3.shift(DOWN * 1.2)
        self.play(Write(rem3), run_time=0.6)

        rem_eq2 = MathTex(
            r"\boldsymbol{c} = K^{\top}\,\boldsymbol{c}_{\text{ini}}",
            font_size=42, color=YELLOW,
        )
        rem_eq2.shift(DOWN * 2.2)
        rem_box = SurroundingRectangle(rem_eq2, color=YELLOW, buff=0.22)
        self.play(Write(rem_eq2), Create(rem_box), run_time=0.9)
        self.wait(1.8)

        self.play(
            FadeOut(rem1), FadeOut(rem_eq1), FadeOut(rem2),
            FadeOut(rem3), FadeOut(rem_eq2), FadeOut(rem_box),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: ステップ1 — 左固有ベクトルと固有関数
        # ============================================================
        subtitle3 = Text("ステップ1：左固有ベクトルから固有関数へ", font_size=28, color=TEAL)
        subtitle3.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle3), run_time=0.5)
        self.wait(0.3)

        step1a = VGroup(
            Text("行列 K に対して、次を満たす", color=WHITE, font_size=26),
            Text("左固有ベクトル", color=GOLD, font_size=27, weight=BOLD),
            MathTex(r"\boldsymbol{z}_i", color=GOLD, font_size=36),
            Text("をM個算出する", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.13)
        if step1a.width > config.frame_width - 0.8:
            step1a.scale_to_fit_width(config.frame_width - 0.8)
        step1a.shift(UP * 1.9)
        self.play(Write(step1a), run_time=0.9)
        self.wait(0.3)

        step1_eq = MathTex(
            r"\boldsymbol{z}_i^{\top} K = \mu_i\,\boldsymbol{z}_i^{\top}",
            font_size=42, color=YELLOW,
        )
        step1_eq.shift(UP * 0.8)
        step1_box = SurroundingRectangle(step1_eq, color=YELLOW, buff=0.22)
        self.play(Write(step1_eq), Create(step1_box), run_time=0.9)
        self.wait(0.3)

        step1b = Text(
            "この z_i を辞書ベクトルの線形和の重みとすれば、",
            color=WHITE, font_size=26,
        )
        step1b.shift(DOWN * 0.3)
        if step1b.width > config.frame_width - 0.8:
            step1b.scale_to_fit_width(config.frame_width - 0.8)
        step1c = VGroup(
            Text("これが i 番目の", color=WHITE, font_size=26),
            Text("クープマン固有関数", color=GOLD, font_size=27, weight=BOLD),
            MathTex(r"\varphi_i(\boldsymbol{x})", color=GOLD, font_size=36),
            Text("となる", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.13)
        if step1c.width > config.frame_width - 0.8:
            step1c.scale_to_fit_width(config.frame_width - 0.8)
        step1c.next_to(step1b, DOWN, buff=0.25)
        self.play(Write(step1b), run_time=0.7)
        self.play(Write(step1c), run_time=0.8)
        self.wait(0.3)

        step1_eq2 = MathTex(
            r"\varphi_i(\boldsymbol{x}) = \boldsymbol{z}_i^{\top}\,\boldsymbol{\psi}(\boldsymbol{x})",
            font_size=42, color=YELLOW,
        )
        step1_eq2.shift(DOWN * 2.2)
        step1_box2 = SurroundingRectangle(step1_eq2, color=YELLOW, buff=0.22)
        self.play(Write(step1_eq2), Create(step1_box2), run_time=0.9)
        self.wait(1.8)

        self.play(
            FadeOut(step1a), FadeOut(step1_eq), FadeOut(step1_box),
            FadeOut(step1b), FadeOut(step1c),
            FadeOut(step1_eq2), FadeOut(step1_box2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: ステップ2 — 右固有ベクトルと行列 W
        # ============================================================
        subtitle4 = Text("ステップ2：右固有ベクトルと行列 W", font_size=28, color=ORANGE)
        subtitle4.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle4), run_time=0.5)
        self.wait(0.3)

        step2a = VGroup(
            Text("一方で、次を満たし z と直交する", color=WHITE, font_size=26),
            Text("右固有ベクトル", color=GOLD, font_size=27, weight=BOLD),
            MathTex(r"\boldsymbol{w}_i", color=GOLD, font_size=36),
            Text("も算出する", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.13)
        if step2a.width > config.frame_width - 0.8:
            step2a.scale_to_fit_width(config.frame_width - 0.8)
        step2a.shift(UP * 1.9)
        self.play(Write(step2a), run_time=0.9)
        self.wait(0.3)

        step2_eq = MathTex(
            r"K\,\boldsymbol{w}_i = \mu_i\,\boldsymbol{w}_i",
            font_size=42, color=YELLOW,
        )
        step2_eq.shift(UP * 0.8)
        step2_box = SurroundingRectangle(step2_eq, color=YELLOW, buff=0.22)
        self.play(Write(step2_eq), Create(step2_box), run_time=0.9)
        self.wait(0.3)

        step2b = Text(
            "そして、これらを並べた行列 W を作る",
            color=WHITE, font_size=26,
        )
        step2b.shift(DOWN * 0.3)
        self.play(Write(step2b), run_time=0.7)

        step2_eq2 = MathTex(
            r"W = \begin{bmatrix} \boldsymbol{w}_1 & \cdots & \boldsymbol{w}_M \end{bmatrix}",
            font_size=42, color=YELLOW,
        )
        if step2_eq2.width > config.frame_width - 0.8:
            step2_eq2.scale_to_fit_width(config.frame_width - 0.8)
        step2_eq2.shift(DOWN * 1.7)
        step2_box2 = SurroundingRectangle(step2_eq2, color=YELLOW, buff=0.22)
        self.play(Write(step2_eq2), Create(step2_box2), run_time=0.9)
        self.wait(1.8)

        self.play(
            FadeOut(step2a), FadeOut(step2_eq), FadeOut(step2_box),
            FadeOut(step2b), FadeOut(step2_eq2), FadeOut(step2_box2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: ステップ3 — 行列 B
        # ============================================================
        subtitle5 = Text("ステップ3：状態量を再構成する行列 B", font_size=28, color=YELLOW)
        subtitle5.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle5), run_time=0.5)
        self.wait(0.3)

        step3a = Text(
            "更に、次を満たす行列 B を作成する",
            color=WHITE, font_size=26,
        )
        step3a.shift(UP * 1.9)
        self.play(Write(step3a), run_time=0.7)

        step3_eq = MathTex(
            r"\boldsymbol{x} = B\,\boldsymbol{\psi}(\boldsymbol{x})",
            font_size=44, color=YELLOW,
        )
        step3_eq.shift(UP * 0.9)
        step3_box = SurroundingRectangle(step3_eq, color=YELLOW, buff=0.22)
        self.play(Write(step3_eq), Create(step3_box), run_time=0.9)
        self.wait(0.3)

        step3b = Text(
            "・辞書に状態量の成分が現れるなら、",
            color=WHITE, font_size=25,
        )
        step3b.shift(DOWN * 0.3)
        if step3b.width > config.frame_width - 0.8:
            step3b.scale_to_fit_width(config.frame_width - 0.8)
        step3c = Text(
            "　それを使って x を再構成するように B を定義すればよい",
            color=TEAL, font_size=25,
        )
        step3c.next_to(step3b, DOWN, buff=0.2)
        if step3c.width > config.frame_width - 0.8:
            step3c.scale_to_fit_width(config.frame_width - 0.8)
        self.play(Write(step3b), run_time=0.7)
        self.play(Write(step3c), run_time=0.7)
        self.wait(0.3)

        step3d = Text(
            "・あるいは、最小二乗法などでデータから回帰することもできる",
            color=TEAL, font_size=25,
        )
        step3d.shift(DOWN * 1.7)
        if step3d.width > config.frame_width - 0.8:
            step3d.scale_to_fit_width(config.frame_width - 0.8)
        self.play(Write(step3d), run_time=0.7)
        self.wait(1.8)

        self.play(
            FadeOut(step3a), FadeOut(step3_eq), FadeOut(step3_box),
            FadeOut(step3b), FadeOut(step3c), FadeOut(step3d),
        )
        self.wait(0.3)

        # ============================================================
        # Part 6: ステップ4 — クープマンモード BW
        # ============================================================
        subtitle6 = Text("ステップ4：BW からクープマンモードを得る", font_size=28, color=PURPLE)
        subtitle6.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle6), run_time=0.5)
        self.wait(0.3)

        step4a = Text(
            "ここから BW を計算する",
            color=WHITE, font_size=26,
        )
        step4a.shift(UP * 1.9)
        self.play(Write(step4a), run_time=0.7)

        step4_eq = MathTex(
            r"B\,W = \begin{bmatrix} \boldsymbol{v}_1 & \cdots & \boldsymbol{v}_M \end{bmatrix}",
            font_size=42, color=YELLOW,
        )
        if step4_eq.width > config.frame_width - 0.8:
            step4_eq.scale_to_fit_width(config.frame_width - 0.8)
        step4_eq.shift(UP * 0.8)
        step4_box = SurroundingRectangle(step4_eq, color=YELLOW, buff=0.22)
        self.play(Write(step4_eq), Create(step4_box), run_time=0.9)
        self.wait(0.3)

        step4b = Text(
            "求まる行列に並んでいる M 本の列ベクトルが、",
            color=WHITE, font_size=26,
        )
        step4b.shift(DOWN * 0.3)
        if step4b.width > config.frame_width - 0.8:
            step4b.scale_to_fit_width(config.frame_width - 0.8)
        step4c = VGroup(
            Text("各固有値に対応する", color=WHITE, font_size=26),
            Text("クープマンモード", color=GOLD, font_size=28, weight=BOLD),
            MathTex(r"\boldsymbol{v}_m", color=GOLD, font_size=36),
            Text("となる", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.13)
        if step4c.width > config.frame_width - 0.8:
            step4c.scale_to_fit_width(config.frame_width - 0.8)
        step4c.next_to(step4b, DOWN, buff=0.25)
        step4_box2 = SurroundingRectangle(step4c, color=GOLD, buff=0.2)
        self.play(Write(step4b), run_time=0.7)
        self.play(Write(step4c), Create(step4_box2), run_time=0.9)
        self.wait(1.8)

        self.play(
            FadeOut(step4a), FadeOut(step4_eq), FadeOut(step4_box),
            FadeOut(step4b), FadeOut(step4c), FadeOut(step4_box2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 7: ステップ5 — スナップショットペアの予測
        # ============================================================
        subtitle7 = Text("ステップ5：スナップショットペアの予測", font_size=28, color=RED)
        subtitle7.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle7), run_time=0.5)
        self.wait(0.3)

        step5a = VGroup(
            Text("クープマンモード", color=WHITE, font_size=25),
            MathTex(r"\boldsymbol{v}_m", color=GOLD, font_size=34),
            Text("、固有値", color=WHITE, font_size=25),
            MathTex(r"\mu_m", color=GOLD, font_size=34),
            Text("、固有関数", color=WHITE, font_size=25),
            MathTex(r"\varphi_m", color=GOLD, font_size=34),
            Text("が揃った", color=WHITE, font_size=25),
        ).arrange(RIGHT, buff=0.1)
        if step5a.width > config.frame_width - 0.6:
            step5a.scale_to_fit_width(config.frame_width - 0.6)
        step5a.shift(UP * 1.9)
        self.play(Write(step5a), run_time=0.9)
        self.wait(0.3)

        step5b = Text(
            "よって、現在の状態量からスナップショットペアを求められる",
            color=WHITE, font_size=26,
        )
        step5b.shift(UP * 0.9)
        if step5b.width > config.frame_width - 0.8:
            step5b.scale_to_fit_width(config.frame_width - 0.8)
        self.play(Write(step5b), run_time=0.8)
        self.wait(0.3)

        step5_eq = MathTex(
            r"\boldsymbol{g}(\boldsymbol{y}_n)"
            r"= \sum_{m=1}^{M_{\text{eigen}}} \boldsymbol{v}_m\,"
            r"\bigl(\mu_m\,\varphi_m(\boldsymbol{x}_n)\bigr)",
            font_size=44, color=YELLOW,
        )
        if step5_eq.width > config.frame_width - 0.8:
            step5_eq.scale_to_fit_width(config.frame_width - 0.8)
        step5_eq.shift(DOWN * 0.6)
        step5_box = SurroundingRectangle(step5_eq, color=YELLOW, buff=0.25)
        self.play(Write(step5_eq), Create(step5_box), run_time=1.1)
        self.wait(0.3)

        step5c = Text(
            "これで非線形システムの予測が、固有値・固有関数・モードで書けた",
            color=GOLD, font_size=26, weight=BOLD,
        )
        step5c.shift(DOWN * 2.3)
        if step5c.width > config.frame_width - 0.8:
            step5c.scale_to_fit_width(config.frame_width - 0.8)
        self.play(Write(step5c), run_time=0.8)
        self.wait(1.8)

        self.play(
            FadeOut(step5a), FadeOut(step5b),
            FadeOut(step5_eq), FadeOut(step5_box), FadeOut(step5c),
        )
        self.wait(0.3)

        # ============================================================
        # Part 8: まとめ
        # ============================================================
        subtitle8 = Text("まとめ", font_size=34, color=TEAL)
        subtitle8.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle8), run_time=0.6)
        self.wait(0.3)

        summary = VGroup(
            Text("• 前提：推定したクープマン行列 K が得られている",
                 color=WHITE, font_size=25),
            Text("• 左固有ベクトル z_i → 固有関数 φ_i(x)=z_i^T ψ(x)",
                 color=WHITE, font_size=25),
            Text("• 右固有ベクトル w_i を並べて行列 W を作る",
                 color=WHITE, font_size=25),
            Text("• x=B ψ(x) を満たす行列 B を作る",
                 color=WHITE, font_size=25),
            Text("• BW の各列がクープマンモード v_m となる",
                 color=GOLD, font_size=25, weight=BOLD),
            Text("• 予測時の計算量が大幅に削減された",
                 color=TEAL, font_size=25),
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
