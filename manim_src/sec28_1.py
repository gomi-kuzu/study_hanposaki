from manim import *
import numpy as np


class DataCompressionIntroduction(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        title = Text("データ圧縮を考える（導入編）", font_size=38, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)

        # ============================================================
        # Part 1: 導入 — データ圧縮技術の必要性
        # ============================================================
        subtitle = Text("導入：なぜデータ圧縮が必要か", font_size=27, color=BLUE)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle), run_time=0.6)
        self.wait(0.3)

        intro1 = Text(
            "これまでの動画では、様々な線形代数のトピックを扱ってきた",
            color=WHITE, font_size=26,
        )
        intro1.shift(UP * 1.9)
        if intro1.width > config.frame_width - 1.0:
            intro1.scale_to_fit_width(config.frame_width - 1.0)
        self.play(Write(intro1), run_time=0.8)
        self.wait(0.3)

        intro2 = Text(
            "その中で、たくさんの行列計算が登場した",
            color=WHITE, font_size=26,
        )
        intro2.shift(UP * 1.0)
        if intro2.width > config.frame_width - 1.0:
            intro2.scale_to_fit_width(config.frame_width - 1.0)
        self.play(Write(intro2), run_time=0.8)
        self.wait(0.3)

        intro3 = Text(
            "それを現実的な時間でコンピュータに解かせるには、",
            color=WHITE, font_size=26,
        )
        intro3.shift(UP * 0.1)
        if intro3.width > config.frame_width - 1.0:
            intro3.scale_to_fit_width(config.frame_width - 1.0)
        intro4 = Text(
            "データの圧縮技術が必要になることがある",
            color=GOLD, font_size=26, weight=BOLD,
        )
        intro4.next_to(intro3, DOWN, buff=0.25)
        if intro4.width > config.frame_width - 1.0:
            intro4.scale_to_fit_width(config.frame_width - 1.0)
        self.play(Write(intro3), run_time=0.7)
        self.play(Write(intro4), run_time=0.7)
        self.wait(0.3)

        intro5 = Text(
            "28・29話では、そのデータ圧縮技術の半歩先を見る",
            color=TEAL, font_size=27, weight=BOLD,
        )
        intro5.shift(DOWN * 1.5)
        if intro5.width > config.frame_width - 1.0:
            intro5.scale_to_fit_width(config.frame_width - 1.0)
        intro5_box = SurroundingRectangle(intro5, color=TEAL, buff=0.22)
        self.play(Write(intro5), Create(intro5_box), run_time=0.9)
        self.wait(1.8)

        self.play(
            FadeOut(intro1), FadeOut(intro2), FadeOut(intro3),
            FadeOut(intro4), FadeOut(intro5), FadeOut(intro5_box),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: 対象のデータ行列 Ψ_X
        # ============================================================
        subtitle2 = Text("対象：データ行列 Ψ_X の圧縮", font_size=28, color=GOLD)
        subtitle2.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle2), run_time=0.5)
        self.wait(0.3)

        obj1 = Text(
            "26・27話で扱ったスナップショットペアの予測問題に",
            color=WHITE, font_size=25,
        )
        obj1.shift(UP * 1.9)
        if obj1.width > config.frame_width - 0.8:
            obj1.scale_to_fit_width(config.frame_width - 0.8)
        obj2 = Text(
            "登場した、次のデータ行列の圧縮を考える",
            color=WHITE, font_size=25,
        )
        obj2.next_to(obj1, DOWN, buff=0.2)
        self.play(Write(obj1), run_time=0.7)
        self.play(Write(obj2), run_time=0.7)
        self.wait(0.3)

        psi_mat = MathTex(
            r"\Psi_X = \begin{bmatrix}"
            r"\psi_1(\boldsymbol{x}_1) & \psi_1(\boldsymbol{x}_2) & \dots & \psi_1(\boldsymbol{x}_N) \\"
            r"\psi_2(\boldsymbol{x}_1) & \psi_2(\boldsymbol{x}_2) & \dots & \psi_2(\boldsymbol{x}_N) \\"
            r"\vdots & \vdots & \ddots & \vdots \\"
            r"\psi_M(\boldsymbol{x}_1) & \psi_M(\boldsymbol{x}_2) & \dots & \psi_M(\boldsymbol{x}_N)"
            r"\end{bmatrix}",
            font_size=36, color=WHITE,
        )
        if psi_mat.width > config.frame_width - 1.0:
            psi_mat.scale_to_fit_width(config.frame_width - 1.0)
        psi_mat.shift(DOWN * 0.3)
        self.play(Write(psi_mat), run_time=1.2)
        self.wait(0.5)

        obj3 = VGroup(
            Text("・", color=WHITE, font_size=24),
            MathTex(r"\{\psi_m(\boldsymbol{x})\}", color=GOLD, font_size=32),
            Text("は辞書関数、", color=WHITE, font_size=24),
            MathTex(r"M", color=GOLD, font_size=32),
            Text("は辞書の数", color=WHITE, font_size=24),
        ).arrange(RIGHT, buff=0.12)
        if obj3.width > config.frame_width - 0.8:
            obj3.scale_to_fit_width(config.frame_width - 0.8)
        obj3.shift(DOWN * 2.3)
        self.play(Write(obj3), run_time=0.8)
        self.wait(1.5)

        self.play(FadeOut(obj1), FadeOut(obj2), FadeOut(obj3))
        # psi_mat を上に移動して条件を説明
        self.play(psi_mat.animate.scale(0.8).shift(UP * 1.7), run_time=0.7)

        cond1 = VGroup(
            Text("ここでは", color=WHITE, font_size=26),
            MathTex(r"M \gg N", color=YELLOW, font_size=40),
            Text("を想定する", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.2)
        cond1.shift(DOWN * 0.1)
        self.play(Write(cond1), run_time=0.8)

        cond2 = Text(
            "データ数 N に比べ、辞書関数の数 M が膨大な場合",
            color=TEAL, font_size=25,
        )
        cond2.next_to(cond1, DOWN, buff=0.3)
        if cond2.width > config.frame_width - 0.8:
            cond2.scale_to_fit_width(config.frame_width - 0.8)
        self.play(Write(cond2), run_time=0.7)

        cond3 = Text(
            "さらに、簡単のためデータ x_n は全て独立で、行列のランクは N とする",
            color=GRAY, font_size=24,
        )
        cond3.shift(DOWN * 1.8)
        if cond3.width > config.frame_width - 0.8:
            cond3.scale_to_fit_width(config.frame_width - 0.8)
        self.play(Write(cond3), run_time=0.8)
        self.wait(1.8)

        self.play(
            FadeOut(psi_mat), FadeOut(cond1), FadeOut(cond2), FadeOut(cond3),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: 17話の復習 — SVD と低ランク近似
        # ============================================================
        subtitle3 = Text("復習：特異値分解による低ランク近似", font_size=28, color=TEAL)
        subtitle3.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle3), run_time=0.5)
        self.wait(0.3)

        svd1 = Text(
            "17話では、データ行列を次のように特異値分解した上で、",
            color=WHITE, font_size=26,
        )
        svd1.shift(UP * 1.9)
        if svd1.width > config.frame_width - 0.8:
            svd1.scale_to_fit_width(config.frame_width - 0.8)
        self.play(Write(svd1), run_time=0.8)

        svd_eq = MathTex(
            r"\Psi_X = U \Sigma V^{\top}",
            font_size=48, color=YELLOW,
        )
        svd_eq.shift(UP * 0.9)
        svd_box = SurroundingRectangle(svd_eq, color=YELLOW, buff=0.22)
        self.play(Write(svd_eq), Create(svd_box), run_time=0.9)
        self.wait(0.3)

        svd2 = Text(
            "0 の特異値や、0 に近いものを削って",
            color=WHITE, font_size=26,
        )
        svd2.shift(DOWN * 0.2)
        svd3 = Text(
            "行列サイズを小さくする低ランク近似をすでに学んだ",
            color=WHITE, font_size=26,
        )
        svd3.next_to(svd2, DOWN, buff=0.2)
        if svd3.width > config.frame_width - 0.8:
            svd3.scale_to_fit_width(config.frame_width - 0.8)
        self.play(Write(svd2), run_time=0.7)
        self.play(Write(svd3), run_time=0.7)
        self.wait(0.3)

        svd4 = Text(
            "しかし、これだけではカバーできないほど辞書が多くなり得る",
            color=GOLD, font_size=26, weight=BOLD,
        )
        svd4.shift(DOWN * 1.8)
        if svd4.width > config.frame_width - 0.8:
            svd4.scale_to_fit_width(config.frame_width - 0.8)
        self.play(Write(svd4), run_time=0.8)
        self.wait(1.8)

        self.play(
            FadeOut(svd1), FadeOut(svd_eq), FadeOut(svd_box),
            FadeOut(svd2), FadeOut(svd3), FadeOut(svd4),
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: 2変数の単項式の例 — 辞書の爆発
        # ============================================================
        subtitle4 = Text("例：単項式で辞書を組むと数が爆発する", font_size=28, color=ORANGE)
        subtitle4.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle4), run_time=0.5)
        self.wait(0.3)

        ex1 = VGroup(
            Text("2変数を単項式", color=WHITE, font_size=25),
            MathTex(r"x_1^{n_1} x_2^{n_2}", color=GOLD, font_size=34),
            Text("で構成する例を見てみよう", color=WHITE, font_size=25),
        ).arrange(RIGHT, buff=0.15)
        if ex1.width > config.frame_width - 0.8:
            ex1.scale_to_fit_width(config.frame_width - 0.8)
        ex1.shift(UP * 1.9)
        self.play(Write(ex1), run_time=0.8)
        self.wait(0.3)

        ex_eq = MathTex(
            r"\psi_1(\boldsymbol{x}) &= 1,\ \psi_2 = x_1,\ \psi_3 = x_2,\ \psi_4 = x_1^2, \\"
            r"\psi_5 &= x_1 x_2,\ \psi_6 = x_2^2,\ \psi_7 = x_1^3,\ \psi_8 = x_1^2 x_2,\ \dots",
            font_size=34, color=WHITE,
        )
        if ex_eq.width > config.frame_width - 0.8:
            ex_eq.scale_to_fit_width(config.frame_width - 0.8)
        ex_eq.shift(UP * 0.7)
        self.play(Write(ex_eq), run_time=1.2)
        self.wait(0.5)

        ex2 = VGroup(
            Text("各変数の最大次数を", color=WHITE, font_size=24),
            MathTex(r"n_1, n_2 \le L-1", color=GOLD, font_size=32),
            Text("とすると、辞書の数は", color=WHITE, font_size=24),
            MathTex(r"L^2", color=YELLOW, font_size=34),
        ).arrange(RIGHT, buff=0.13)
        if ex2.width > config.frame_width - 0.8:
            ex2.scale_to_fit_width(config.frame_width - 0.8)
        ex2.shift(DOWN * 0.7)
        self.play(Write(ex2), run_time=0.9)
        self.wait(0.3)

        ex3 = VGroup(
            Text("D 変数に拡張すると辞書の数は", color=WHITE, font_size=24),
            MathTex(r"L^D", color=YELLOW, font_size=36),
        ).arrange(RIGHT, buff=0.15)
        ex3.shift(DOWN * 1.7)
        self.play(Write(ex3), run_time=0.8)
        self.wait(1.5)

        self.play(FadeOut(ex1), FadeOut(ex_eq), FadeOut(ex2), FadeOut(ex3))

        # 100億の衝撃
        shock_eq = MathTex(
            r"L = 10,\ D = 10 \quad\Longrightarrow\quad M = 10^{10}",
            font_size=46, color=YELLOW,
        )
        if shock_eq.width > config.frame_width - 0.8:
            shock_eq.scale_to_fit_width(config.frame_width - 0.8)
        shock_eq.shift(UP * 0.5)
        shock_box = SurroundingRectangle(shock_eq, color=RED, buff=0.25)
        self.play(Write(shock_eq), Create(shock_box), run_time=1.0)

        shock1 = Text(
            "この程度でも辞書の数 M は 100 億",
            color=GOLD, font_size=28, weight=BOLD,
        )
        shock1.shift(DOWN * 0.8)
        self.play(Write(shock1), run_time=0.8)

        shock2 = Text(
            "次数や変数が増えればさらに膨れ上がり、低ランク近似だけでは足りない",
            color=TEAL, font_size=24,
        )
        shock2.shift(DOWN * 1.8)
        if shock2.width > config.frame_width - 0.8:
            shock2.scale_to_fit_width(config.frame_width - 0.8)
        self.play(Write(shock2), run_time=0.8)
        self.wait(1.8)

        self.play(
            FadeOut(shock_eq), FadeOut(shock_box),
            FadeOut(shock1), FadeOut(shock2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: クロネッカー積の導入（定義）
        # ============================================================
        subtitle5 = Text("クロネッカー積の導入", font_size=30, color=YELLOW)
        subtitle5.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle5), run_time=0.5)
        self.wait(0.3)

        kr1 = Text(
            "本格的な行列の圧縮を考えるために、クロネッカー積を導入する",
            color=WHITE, font_size=25,
        )
        kr1.shift(UP * 1.9)
        if kr1.width > config.frame_width - 0.8:
            kr1.scale_to_fit_width(config.frame_width - 0.8)
        self.play(Write(kr1), run_time=0.8)

        kr2 = VGroup(
            Text("定義：", color=WHITE, font_size=24),
            MathTex(r"M_1 \times N_1", color=TEAL, font_size=30),
            Text("行列", color=WHITE, font_size=24),
            MathTex(r"A^{(1)}", color=TEAL, font_size=32),
            Text("と", color=WHITE, font_size=24),
            MathTex(r"M_2 \times N_2", color=ORANGE, font_size=30),
            Text("行列", color=WHITE, font_size=24),
            MathTex(r"A^{(2)}", color=ORANGE, font_size=32),
            Text("に対して", color=WHITE, font_size=24),
        ).arrange(RIGHT, buff=0.1)
        if kr2.width > config.frame_width - 0.6:
            kr2.scale_to_fit_width(config.frame_width - 0.6)
        kr2.shift(UP * 1.2)
        self.play(Write(kr2), run_time=0.9)
        self.wait(0.3)

        kr_eq = MathTex(
            r"A^{(1)} \otimes A^{(2)} = \begin{bmatrix}"
            r"A_{11}^{(1)} A^{(2)} & \dots & A_{1 N_1}^{(1)} A^{(2)} \\"
            r"\vdots & \ddots & \vdots \\"
            r"A_{M_1 1}^{(1)} A^{(2)} & \dots & A_{M_1 N_1}^{(1)} A^{(2)}"
            r"\end{bmatrix}",
            font_size=36, color=WHITE,
        )
        if kr_eq.width > config.frame_width - 0.8:
            kr_eq.scale_to_fit_width(config.frame_width - 0.8)
        kr_eq.shift(DOWN * 0.4)
        kr_box = SurroundingRectangle(kr_eq, color=YELLOW, buff=0.2)
        self.play(Write(kr_eq), Create(kr_box), run_time=1.3)
        self.wait(0.3)

        kr3 = MathTex(
            r"\in \mathbb{R}^{(M_1 M_2) \times (N_1 N_2)}",
            font_size=38, color=GOLD,
        )
        kr3.shift(DOWN * 2.3)
        self.play(Write(kr3), run_time=0.8)
        self.wait(1.8)

        self.play(
            FadeOut(kr1), FadeOut(kr2),
            FadeOut(kr_eq), FadeOut(kr_box), FadeOut(kr3),
        )
        self.wait(0.3)

        # ============================================================
        # Part 6: 紙芝居 — クロネッカー積で要素数を削減（行列）
        # ============================================================
        subtitle6 = Text("【利点】少ない要素で大きな行列を表現", font_size=28, color=PURPLE)
        subtitle6.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle6), run_time=0.5)
        self.wait(0.3)

        self.kronecker_paper_animation()

        self.wait(0.3)

        # ============================================================
        # Part 7: 辞書関数ベクトルの整理
        # ============================================================
        subtitle7 = Text("辞書関数ベクトルの整理", font_size=30, color=BLUE)
        subtitle7.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle7), run_time=0.5)
        self.wait(0.3)

        dv1 = VGroup(
            Text("D 個の状態変数", color=WHITE, font_size=25),
            MathTex(r"\{x_d\}", color=GOLD, font_size=32),
            Text("のうち、1 つ目に辞書を用意する", color=WHITE, font_size=25),
        ).arrange(RIGHT, buff=0.13)
        if dv1.width > config.frame_width - 0.8:
            dv1.scale_to_fit_width(config.frame_width - 0.8)
        dv1.shift(UP * 1.9)
        self.play(Write(dv1), run_time=0.8)

        dv_eq = MathTex(
            r"\psi_1^{(1)}(\boldsymbol{x}) = 1,\ \psi_2^{(1)} = x_1,\ "
            r"\psi_3^{(1)} = x_1^2,\ \cdots,\ \psi_L^{(1)} = x_1^{L-1}",
            font_size=34, color=WHITE,
        )
        if dv_eq.width > config.frame_width - 0.8:
            dv_eq.scale_to_fit_width(config.frame_width - 0.8)
        dv_eq.shift(UP * 1.2)
        self.play(Write(dv_eq), run_time=1.1)
        self.wait(0.3)

        dv2 = VGroup(
            Text("同様に", color=WHITE, font_size=24),
            MathTex(r"x_d", color=GOLD, font_size=32),
            Text("に対し L 個の辞書を用意し、ベクトル表記を導入する", color=WHITE, font_size=24),
        ).arrange(RIGHT, buff=0.12)
        if dv2.width > config.frame_width - 0.8:
            dv2.scale_to_fit_width(config.frame_width - 0.8)
        dv2.shift(UP * 0.3)
        self.play(Write(dv2), run_time=0.8)

        dv_vec = MathTex(
            r"\boldsymbol{\psi}^{(d)}(\boldsymbol{x}) = \begin{bmatrix}"
            r"\psi_1^{(d)}(\boldsymbol{x}) \\ \psi_2^{(d)}(\boldsymbol{x}) \\"
            r"\vdots \\ \psi_L^{(d)}(\boldsymbol{x})"
            r"\end{bmatrix}",
            font_size=36, color=YELLOW,
        )
        dv_vec.shift(DOWN * 1.5)
        dv_box = SurroundingRectangle(dv_vec, color=YELLOW, buff=0.2)
        self.play(Write(dv_vec), Create(dv_box), run_time=1.0)
        self.wait(1.8)

        self.play(
            FadeOut(dv1), FadeOut(dv_eq), FadeOut(dv2),
            FadeOut(dv_vec), FadeOut(dv_box),
        )
        self.wait(0.3)

        # ============================================================
        # Part 8: クロネッカー積で2変数の辞書の組み合わせ
        # ============================================================
        subtitle8 = Text("クロネッカー積で辞書を組み合わせる", font_size=28, color=GOLD)
        subtitle8.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle8), run_time=0.5)
        self.wait(0.3)

        cb1 = Text(
            "クロネッカー積を使うと、2変数の辞書の組み合わせは",
            color=WHITE, font_size=25,
        )
        cb1.shift(UP * 1.9)
        if cb1.width > config.frame_width - 0.8:
            cb1.scale_to_fit_width(config.frame_width - 0.8)
        self.play(Write(cb1), run_time=0.8)

        cb_eq = MathTex(
            r"\boldsymbol{\psi}^{(1)} \otimes \boldsymbol{\psi}^{(2)}"
            r"= \begin{bmatrix}"
            r"\psi_1^{(1)} \boldsymbol{\psi}^{(2)} \\"
            r"\psi_2^{(1)} \boldsymbol{\psi}^{(2)} \\"
            r"\vdots \\"
            r"\psi_L^{(1)} \boldsymbol{\psi}^{(2)}"
            r"\end{bmatrix}"
            r"= \begin{bmatrix}"
            r"\psi_1^{(1)} \psi_1^{(2)} \\"
            r"\psi_1^{(1)} \psi_2^{(2)} \\"
            r"\vdots \\"
            r"\psi_1^{(1)} \psi_L^{(2)} \\"
            r"\psi_2^{(1)} \psi_1^{(2)} \\"
            r"\vdots \\"
            r"\psi_L^{(1)} \psi_L^{(2)}"
            r"\end{bmatrix}",
            font_size=30, color=WHITE,
        )
        if cb_eq.height > config.frame_height - 2.5:
            cb_eq.scale_to_fit_height(config.frame_height - 2.5)
        if cb_eq.width > config.frame_width - 0.8:
            cb_eq.scale_to_fit_width(config.frame_width - 0.8)
        cb_eq.shift(DOWN * 0.3)
        self.play(Write(cb_eq), run_time=1.6)
        self.wait(1.8)

        self.play(FadeOut(cb1), FadeOut(cb_eq))

        cb2 = Text(
            "同様にして、D 変数の辞書ベクトルは",
            color=WHITE, font_size=26,
        )
        cb2.shift(UP * 1.2)
        self.play(Write(cb2), run_time=0.7)

        cb_eq2 = MathTex(
            r"\boldsymbol{\psi}(\boldsymbol{x}) = \boldsymbol{\psi}^{(1)}(\boldsymbol{x})"
            r"\otimes \boldsymbol{\psi}^{(2)}(\boldsymbol{x}) \otimes \cdots"
            r"\otimes \boldsymbol{\psi}^{(D)}(\boldsymbol{x})",
            font_size=40, color=YELLOW,
        )
        if cb_eq2.width > config.frame_width - 0.8:
            cb_eq2.scale_to_fit_width(config.frame_width - 0.8)
        cb_eq2.shift(DOWN * 0.1)
        cb_box2 = SurroundingRectangle(cb_eq2, color=YELLOW, buff=0.22)
        self.play(Write(cb_eq2), Create(cb_box2), run_time=1.0)

        cb3 = Text(
            "これは巨大な列ベクトルになる",
            color=GOLD, font_size=26, weight=BOLD,
        )
        cb3.shift(DOWN * 1.5)
        self.play(Write(cb3), run_time=0.7)
        self.wait(1.8)

        self.play(
            FadeOut(cb2), FadeOut(cb_eq2), FadeOut(cb_box2), FadeOut(cb3),
        )
        self.wait(0.3)

        # ============================================================
        # Part 9: インデックス表現 (n_1, ..., n_D)
        # ============================================================
        subtitle9 = Text("要素の指定：指数の並びで番地を表す", font_size=28, color=RED)
        subtitle9.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle9), run_time=0.5)
        self.wait(0.3)

        idx1 = Text(
            "巨大な列ベクトルなので、要素の指定方法を工夫する",
            color=WHITE, font_size=26,
        )
        idx1.shift(UP * 1.9)
        if idx1.width > config.frame_width - 0.8:
            idx1.scale_to_fit_width(config.frame_width - 0.8)
        self.play(Write(idx1), run_time=0.8)

        idx2 = Text(
            "各変数の指数を並べて次のように書くと、",
            color=WHITE, font_size=26,
        )
        idx2.shift(UP * 1.2)
        self.play(Write(idx2), run_time=0.7)

        idx_eq = MathTex(
            r"\psi_{n_1, n_2, \dots, n_D}(\boldsymbol{x})",
            font_size=44, color=YELLOW,
        )
        idx_eq.shift(UP * 0.3)
        idx_box = SurroundingRectangle(idx_eq, color=YELLOW, buff=0.22)
        self.play(Write(idx_eq), Create(idx_box), run_time=0.9)

        idx3 = VGroup(
            MathTex(r"(n_1, n_2, \dots, n_D)", color=GOLD, font_size=36),
            Text("が、ベクトルのユニークな番地を表現する", color=WHITE, font_size=25),
        ).arrange(RIGHT, buff=0.2)
        if idx3.width > config.frame_width - 0.8:
            idx3.scale_to_fit_width(config.frame_width - 0.8)
        idx3.shift(DOWN * 0.9)
        self.play(Write(idx3), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(idx1), FadeOut(idx2),
            FadeOut(idx_eq), FadeOut(idx_box), FadeOut(idx3),
        )
        self.wait(0.2)

        # 2変数の具体例（紙芝居的に1行ずつ）
        ex_head = Text(
            "例：2変数の場合に、自然数を振り直してみると",
            color=WHITE, font_size=26,
        )
        ex_head.shift(UP * 1.9)
        if ex_head.width > config.frame_width - 0.8:
            ex_head.scale_to_fit_width(config.frame_width - 0.8)
        self.play(Write(ex_head), run_time=0.7)

        idx_rows = VGroup(
            MathTex(r"[\boldsymbol{\psi}]_1 = \psi_{1,1} = \psi_1^{(1)} \psi_1^{(2)} = 1",
                    font_size=34, color=WHITE),
            MathTex(r"[\boldsymbol{\psi}]_2 = \psi_{1,2} = \psi_1^{(1)} \psi_2^{(2)} = x_2",
                    font_size=34, color=WHITE),
            MathTex(r"\vdots", font_size=34, color=WHITE),
            MathTex(r"[\boldsymbol{\psi}]_L = \psi_{1,L} = \psi_1^{(1)} \psi_L^{(2)} = x_2^{L-1}",
                    font_size=34, color=WHITE),
            MathTex(r"[\boldsymbol{\psi}]_{L+1} = \psi_{2,1} = \psi_2^{(1)} \psi_1^{(2)} = x_1",
                    font_size=34, color=GOLD),
            MathTex(r"[\boldsymbol{\psi}]_{L+2} = \psi_{2,2} = \psi_2^{(1)} \psi_2^{(2)} = x_1 x_2",
                    font_size=34, color=GOLD),
            MathTex(r"\vdots", font_size=34, color=WHITE),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        if idx_rows.width > config.frame_width - 0.8:
            idx_rows.scale_to_fit_width(config.frame_width - 0.8)
        idx_rows.next_to(ex_head, DOWN, buff=0.2)

        for row in idx_rows:
            self.play(Write(row), run_time=0.55)
            self.wait(0.12)
        self.wait(1.5)

        self.play(FadeOut(ex_head), FadeOut(idx_rows))
        self.wait(0.2)

        # 紙芝居：ψ^(1) ⊗ ψ^(2) を展開し、各要素に (n_1, n_2) の番地を振る
        self.dict_vector_index_animation()

        concl = Text(
            "次の動画からは、辞書ベクトルを (n_1, ..., n_D) の形で表現する",
            color=TEAL, font_size=25, weight=BOLD,
        )
        concl.to_edge(DOWN, buff=0.4)
        if concl.width > config.frame_width - 0.8:
            concl.scale_to_fit_width(config.frame_width - 0.8)
        self.play(Write(concl), run_time=0.8)
        self.wait(1.8)

        self.play(FadeOut(concl))
        self.wait(0.3)

        # ============================================================
        # Part 10: まとめ
        # ============================================================
        subtitle10 = Text("まとめ", font_size=34, color=TEAL)
        subtitle10.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle10), run_time=0.6)
        self.wait(0.3)

        summary = VGroup(
            Text("• 行列計算を現実的に解くにはデータ圧縮が必要になり得る",
                 color=WHITE, font_size=25),
            Text("• 対象：M≫N のデータ行列 Ψ_X（ランク N）",
                 color=WHITE, font_size=25),
            Text("• 低ランク近似だけでは、爆発する辞書数 L^D を捌けない",
                 color=WHITE, font_size=25),
            Text("• クロネッカー積で、少ない要素から大きな行列を表現",
                 color=GOLD, font_size=25, weight=BOLD),
            Text("• 辞書ベクトルは ψ^(1)⊗…⊗ψ^(D) で構成する",
                 color=WHITE, font_size=25),
            Text("• 要素は指数の並び (n_1, ..., n_D) で番地指定する",
                 color=TEAL, font_size=25, weight=BOLD),
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

    # ================================================================
    # クロネッカー積の紙芝居アニメーション（行列の要素数削減）
    # ================================================================
    def kronecker_paper_animation(self):
        A = [[2, 3], [0, 1]]
        B = [[1, 4], [2, 5]]
        cell = 0.62

        def make_matrix(values, color, label_tex):
            rows = len(values)
            cols = len(values[0])
            grid = VGroup()
            cells = {}
            for r in range(rows):
                for c in range(cols):
                    sq = Square(side_length=cell)
                    sq.set_stroke(color, 2)
                    sq.set_fill(color, 0.12)
                    sq.move_to(RIGHT * c * cell + DOWN * r * cell)
                    num = MathTex(str(values[r][c]), font_size=28, color=WHITE)
                    num.move_to(sq.get_center())
                    cellgrp = VGroup(sq, num)
                    grid.add(cellgrp)
                    cells[(r, c)] = cellgrp
            grid.move_to(ORIGIN)
            bracket = SurroundingRectangle(grid, color=color, buff=0.08)
            bracket.set_stroke(width=1)
            label = MathTex(label_tex, font_size=34, color=color)
            label.next_to(grid, UP, buff=0.18)
            whole = VGroup(grid, label)
            return whole, grid, cells, label

        # 左の A, B を小さく配置
        A_whole, A_grid, A_cells, _ = make_matrix(A, TEAL, r"A^{(1)}")
        B_whole, B_grid, B_cells, _ = make_matrix(B, ORANGE, r"A^{(2)}")

        A_whole.shift(LEFT * 4 + UP * 1.15)
        B_whole.shift(LEFT * 4 + DOWN * 1.6)

        otimes = MathTex(r"\otimes", font_size=40, color=WHITE)
        otimes.move_to((A_grid.get_center() + B_grid.get_center()) / 2)

        self.play(FadeIn(A_whole), FadeIn(B_whole), Write(otimes), run_time=0.8)
        self.wait(0.3)

        store_small = VGroup(
            Text("保持する要素数", color=WHITE, font_size=22),
            MathTex(r"4 + 4 = 8", color=GREEN, font_size=34),
        ).arrange(DOWN, buff=0.15)
        store_small.next_to(B_whole, DOWN, buff=0.4)
        self.play(Write(store_small), run_time=0.7)
        self.wait(0.3)

        # 右に 4x4 の結果ブロックを構築
        big_origin = RIGHT * 2.0 + UP * 0.2
        big_cell = 0.62
        big_blocks = {}  # (p,q) -> VGroup of 2x2
        big_group = VGroup()
        for p in range(2):
            for q in range(2):
                block = VGroup()
                for r in range(2):
                    for c in range(2):
                        sq = Square(side_length=big_cell)
                        sq.set_stroke(GREY, 1.5)
                        sq.set_fill(BLACK, 0.0)
                        xx = (q * 2 + c) * big_cell
                        yy = (p * 2 + r) * big_cell
                        sq.move_to(big_origin + RIGHT * xx + DOWN * yy)
                        block.add(VGroup(sq))
                big_blocks[(p, q)] = block
                big_group.add(block)
        big_group.move_to(big_origin)

        big_bracket = SurroundingRectangle(big_group, color=YELLOW, buff=0.1)
        big_label = MathTex(r"A^{(1)} \otimes A^{(2)}", font_size=32, color=YELLOW)
        big_label.next_to(big_group, UP, buff=0.2)
        self.play(Create(big_bracket), Write(big_label), run_time=0.7)

        # 結果ブロックに書き込む数値をまとめて保持
        all_nums = VGroup()
        # ブロックごとに A_{pq} * B を埋めていく（紙芝居）
        for p in range(2):
            for q in range(2):
                a_val = A[p][q]
                # A のセルを強調
                hl = A_cells[(p, q)][0].copy().set_stroke(YELLOW, 4)
                # B 全体を強調
                b_hl = SurroundingRectangle(B_grid, color=YELLOW, buff=0.06)
                self.play(Create(hl), Create(b_hl), run_time=0.4)

                block = big_blocks[(p, q)]
                nums = VGroup()
                for r in range(2):
                    for c in range(2):
                        val = a_val * B[r][c]
                        sq = block[r * 2 + c][0]
                        t = MathTex(str(val), font_size=24, color=WHITE)
                        t.move_to(sq.get_center())
                        sq.set_fill(ORANGE, 0.18)
                        nums.add(t)
                all_nums.add(nums)
                formula = MathTex(
                    rf"{a_val}\,A^{{(2)}}", font_size=26, color=GOLD,
                )
                formula.next_to(block, DOWN, buff=0.12)
                self.play(
                    *[sq[0].animate.set_fill(ORANGE, 0.18) for sq in block],
                    Write(nums), FadeIn(formula), run_time=0.6,
                )
                self.play(FadeOut(hl), FadeOut(b_hl), FadeOut(formula), run_time=0.3)
                self.wait(0.1)

        self.wait(0.5)

        store_big = VGroup(
            Text("展開後の要素数", color=WHITE, font_size=22),
            MathTex(r"4 \times 4 = 16", color=RED, font_size=34),
        ).arrange(DOWN, buff=0.15)
        store_big.next_to(big_group, DOWN, buff=0.5)
        self.play(Write(store_big), run_time=0.7)
        self.wait(0.3)

        concl = Text(
            "8 個を保持するだけで 16 要素の行列を表現できる",
            color=GREEN, font_size=26, weight=BOLD,
        )
        concl.to_edge(DOWN, buff=0.35)
        if concl.width > config.frame_width - 0.8:
            concl.scale_to_fit_width(config.frame_width - 0.8)
        self.play(Write(concl), run_time=0.8)
        self.wait(2.0)

        self.play(
            FadeOut(A_whole), FadeOut(B_whole), FadeOut(otimes),
            FadeOut(store_small), FadeOut(big_group), FadeOut(big_bracket),
            FadeOut(big_label), FadeOut(store_big), FadeOut(concl),
            FadeOut(all_nums),
            run_time=0.8,
        )

    # ================================================================
    # 辞書ベクトルのインデックス表現の紙芝居アニメーション
    #   ψ^(1) ⊗ ψ^(2) を展開し、各要素に (n_1, n_2) の番地を振る
    # ================================================================
    def dict_vector_index_animation(self):
        # 変数1,2 の辞書（L=3）: 1, x, x^2
        psi1 = [r"1", r"x_1", r"x_1^2"]
        psi2 = [r"1", r"x_2", r"x_2^2"]
        # 展開後の単項式 (n1, n2) -> x_1^{n1-1} x_2^{n2-1}
        prod = [
            [r"1", r"x_2", r"x_2^2"],
            [r"x_1", r"x_1 x_2", r"x_1 x_2^2"],
            [r"x_1^2", r"x_1^2 x_2", r"x_1^2 x_2^2"],
        ]
        cell = 0.7

        def make_vec(entries, color, label_tex, idx_prefix):
            grp = VGroup()
            cells = []
            for k, e in enumerate(entries):
                sq = Square(side_length=cell)
                sq.set_stroke(color, 2)
                sq.set_fill(color, 0.12)
                sq.move_to(DOWN * k * cell)
                num = MathTex(e, font_size=26, color=WHITE)
                num.move_to(sq.get_center())
                idx = MathTex(rf"{idx_prefix}={k+1}", font_size=20, color=color)
                idx.next_to(sq, LEFT, buff=0.12)
                cg = VGroup(sq, num, idx)
                grp.add(cg)
                cells.append(cg)
            grp.move_to(ORIGIN)
            label = MathTex(label_tex, font_size=30, color=color)
            label.next_to(grp, UP, buff=0.2)
            return VGroup(grp, label), cells

        v1_whole, v1_cells = make_vec(
            psi1, TEAL, r"\boldsymbol{\psi}^{(1)}", "n_1")
        v2_whole, v2_cells = make_vec(
            psi2, ORANGE, r"\boldsymbol{\psi}^{(2)}", "n_2")

        v1_whole.shift(LEFT * 5.2 + UP * 0.3)
        v2_whole.shift(LEFT * 3 + UP * 0.3)

        otimes = MathTex(r"\otimes", font_size=40, color=WHITE)
        otimes.move_to((v1_whole[0].get_center() + v2_whole[0].get_center()) / 2)

        eq = MathTex(r"=", font_size=40, color=WHITE)
        eq.move_to(RIGHT * 1.8 + UP * 0.3)

        self.play(FadeIn(v1_whole), FadeIn(v2_whole), Write(otimes), run_time=0.8)
        self.wait(0.3)

        # 右側：9要素の展開ベクトル（n1 固定で 3 ブロック）
        big_group = VGroup()
        big_cells = {}
        for n1 in range(3):
            for n2 in range(3):
                row = n1 * 3 + n2
                sq = Square(side_length=cell * 0.9)
                sq.set_stroke(GREY, 1.5)
                sq.set_fill(BLACK, 0.0)
                sq.move_to(DOWN * row * cell * 0.9)
                big_cells[(n1, n2)] = sq
                big_group.add(sq)
        big_group.move_to(RIGHT * 4.7)

        big_bracket = SurroundingRectangle(big_group, color=YELLOW, buff=0.12)
        big_label = MathTex(
            r"\boldsymbol{\psi}^{(1)} \otimes \boldsymbol{\psi}^{(2)}",
            font_size=28, color=YELLOW,
        )
        big_label.next_to(big_group, UP, buff=0.2)
        self.play(Write(eq), Create(big_bracket), Write(big_label), run_time=0.7)

        value_mobs = VGroup()
        # ブロックごと（n1 固定）に展開
        for n1 in range(3):
            src1 = v1_cells[n1]
            hl1 = SurroundingRectangle(src1[0], color=YELLOW, buff=0.04)
            hl2 = SurroundingRectangle(v2_whole[0], color=YELLOW, buff=0.06)
            self.play(Create(hl1), Create(hl2), run_time=0.4)

            anims = []
            addr_group = VGroup()
            for n2 in range(3):
                sq = big_cells[(n1, n2)]
                val = MathTex(prod[n1][n2], font_size=20, color=WHITE)
                val.move_to(sq.get_center())
                addr = MathTex(rf"({n1+1},{n2+1})", font_size=18, color=GOLD)
                addr.next_to(sq, RIGHT, buff=0.12)
                addr_group.add(val, addr)
                anims.append(sq.animate.set_fill(ORANGE, 0.15))
            value_mobs.add(addr_group)

            block_formula = MathTex(
                rf"\psi_{{{n1+1}}}^{{(1)}}\,\boldsymbol{{\psi}}^{{(2)}}",
                font_size=24, color=GOLD,
            )
            block_formula.next_to(v2_whole, DOWN, buff=0.6)
            self.play(*anims, Write(addr_group), FadeIn(block_formula), run_time=0.6)
            self.play(FadeOut(hl1), FadeOut(hl2), FadeOut(block_formula), run_time=0.3)
            self.wait(0.1)

        self.wait(0.5)

        note = VGroup(
            MathTex(r"(n_1, n_2)", color=GOLD, font_size=30),
            Text("で各単項式の番地を一意に指定できる", color=WHITE, font_size=24),
        ).arrange(RIGHT, buff=0.2)
        if note.width > config.frame_width - 0.8:
            note.scale_to_fit_width(config.frame_width - 0.8)
        note.to_edge(DOWN, buff=1.4)
        self.play(Write(note), run_time=0.8)
        self.wait(2.0)

        self.play(
            FadeOut(v1_whole), FadeOut(v2_whole), FadeOut(otimes), FadeOut(eq),
            FadeOut(big_group), FadeOut(big_bracket), FadeOut(big_label),
            FadeOut(value_mobs), FadeOut(note),
            run_time=0.8,
        )
