from manim import *
import numpy as np


class DataCompressionVectorApproximation(Scene):
    def fit(self, mob, margin=0.8):
        if mob.width > config.frame_width - margin:
            mob.scale_to_fit_width(config.frame_width - margin)
        return mob

    def construct(self):
        self.camera.background_color = "#012817"

        title = Text("データ圧縮を考える（ベクトルの近似編）", font_size=36, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)

        # ============================================================
        # Part 1: 前回の復習と、今回の問題意識
        # ============================================================
        subtitle = Text("復習：ひとつ前の動画のポイント", font_size=27, color=BLUE)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle), run_time=0.6)
        self.wait(0.3)

        rv1 = Text(
            "1次独立かつクロネッカー積が使える辞書を定義すれば、",
            color=WHITE, font_size=25,
        )
        rv1.shift(UP * 1.9)
        self.fit(rv1)
        self.play(Write(rv1), run_time=0.8)

        rv2 = VGroup(
            MathTex(r"L^D", color=YELLOW, font_size=38),
            Text("個の要素をもつ巨大なベクトルを", color=WHITE, font_size=25),
            MathTex(r"L", color=TEAL, font_size=34),
            Text("次元のベクトル", color=WHITE, font_size=25),
            MathTex(r"D", color=TEAL, font_size=34),
            Text("個で保存できる", color=WHITE, font_size=25),
        ).arrange(RIGHT, buff=0.12)
        self.fit(rv2)
        rv2.shift(UP * 1.0)
        self.play(Write(rv2), run_time=0.9)
        self.wait(0.3)

        rv_eq = MathTex(
            r"\boldsymbol{\psi}(\boldsymbol{x}) = \boldsymbol{\psi}^{(1)}(\boldsymbol{x})"
            r"\otimes \cdots \otimes \boldsymbol{\psi}^{(D)}(\boldsymbol{x})",
            font_size=38, color=YELLOW,
        )
        self.fit(rv_eq)
        rv_eq.shift(DOWN * 0.1)
        rv_box = SurroundingRectangle(rv_eq, color=YELLOW, buff=0.2)
        self.play(Write(rv_eq), Create(rv_box), run_time=1.0)
        self.wait(0.5)

        rv3 = Text(
            "しかし、これは単項式の辞書が変数を独立に扱えるから",
            color=GOLD, font_size=26, weight=BOLD,
        )
        rv3.shift(DOWN * 1.5)
        self.fit(rv3)
        rv4 = Text(
            "他の辞書では、そう都合よくはいかないことがある",
            color=GOLD, font_size=26, weight=BOLD,
        )
        rv4.next_to(rv3, DOWN, buff=0.25)
        self.fit(rv4)
        self.play(Write(rv3), run_time=0.8)
        self.play(Write(rv4), run_time=0.8)
        self.wait(1.8)

        self.play(
            FadeOut(rv1), FadeOut(rv2), FadeOut(rv_eq), FadeOut(rv_box),
            FadeOut(rv3), FadeOut(rv4),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: 各変数が独立という仮定による近似
        # ============================================================
        subtitle2 = Text("発想の転換：独立だと仮定して近似する", font_size=28, color=GOLD)
        subtitle2.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle2), run_time=0.5)
        self.wait(0.3)

        ap1 = Text(
            "逆に、各変数が独立であるという仮定で近似してしまえば、",
            color=WHITE, font_size=25,
        )
        ap1.shift(UP * 1.9)
        self.fit(ap1)
        ap2 = Text(
            "要素数を劇的に減らせるとも言える",
            color=WHITE, font_size=25,
        )
        ap2.next_to(ap1, DOWN, buff=0.2)
        self.play(Write(ap1), run_time=0.8)
        self.play(Write(ap2), run_time=0.7)
        self.wait(0.3)

        ap_eq = MathTex(
            r"p_{n_1, n_2, \dots, n_D} \simeq "
            r"p^{(1)}_{n_1}\, p^{(2)}_{n_2} \cdots p^{(D)}_{n_D}",
            font_size=44, color=YELLOW,
        )
        self.fit(ap_eq)
        ap_eq.shift(UP * 0.0)
        ap_box = SurroundingRectangle(ap_eq, color=YELLOW, buff=0.22)
        self.play(Write(ap_eq), Create(ap_box), run_time=1.1)
        self.wait(0.4)

        ap_note = VGroup(
            Text("※", color=GRAY, font_size=22),
            MathTex(r"\boldsymbol{\psi}(\boldsymbol{x})", color=GRAY, font_size=28),
            Text("を", color=GRAY, font_size=22),
            MathTex(r"\boldsymbol{p}", color=GRAY, font_size=28),
            Text("とおき直した", color=GRAY, font_size=22),
        ).arrange(RIGHT, buff=0.1)
        ap_note.shift(DOWN * 1.2)
        self.play(FadeIn(ap_note), run_time=0.6)

        ap3 = VGroup(
            Text("必要な要素数は", color=WHITE, font_size=25),
            MathTex(r"L \times D", color=GREEN, font_size=38),
            Text("で済む", color=WHITE, font_size=25),
        ).arrange(RIGHT, buff=0.15)
        ap3.shift(DOWN * 2.0)
        self.play(Write(ap3), run_time=0.8)
        self.wait(1.2)

        ap4 = Text(
            "計算しやすいのがメリットだが、近似精度が悪い",
            color=RED, font_size=26, weight=BOLD,
        )
        ap4.shift(DOWN * 2.9)
        self.fit(ap4)
        self.play(Write(ap4), run_time=0.8)
        self.wait(1.8)

        self.play(
            FadeOut(ap1), FadeOut(ap2), FadeOut(ap_eq), FadeOut(ap_box),
            FadeOut(ap_note), FadeOut(ap3), FadeOut(ap4),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: R 個の和への拡張
        # ============================================================
        subtitle3 = Text("拡張：R 個の足し合わせ", font_size=30, color=TEAL)
        subtitle3.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle3), run_time=0.5)
        self.wait(0.3)

        ex1 = Text("そこで、次のように少し拡張を行う（R は自分で選ぶ項の数）", color=WHITE, font_size=26)
        ex1.shift(UP * 1.9)
        self.fit(ex1)
        self.play(Write(ex1), run_time=0.7)

        ex_eq = MathTex(
            r"p_{n_1, n_2, \dots, n_D} &\simeq "
            r"p^{(1)}_{1,n_1} p^{(2)}_{1,n_2} \cdots p^{(D)}_{1,n_D}"
            r"+ p^{(1)}_{2,n_1} p^{(2)}_{2,n_2} \cdots p^{(D)}_{2,n_D}"
            r"+ \cdots + p^{(1)}_{R,n_1} p^{(2)}_{R,n_2} \cdots p^{(D)}_{R,n_D} \\"
            r"&= \sum_{r=1}^{R} p^{(1)}_{r,n_1} p^{(2)}_{r,n_2} \cdots p^{(D)}_{r,n_D}",
            font_size=34, color=WHITE,
        )
        self.fit(ex_eq)
        ex_eq.shift(UP * 0.5)
        self.play(Write(ex_eq), run_time=2.0)
        self.wait(0.8)

        ex_box = SurroundingRectangle(ex_eq, color=YELLOW, buff=0.2)
        self.play(Create(ex_box), run_time=0.6)
        self.wait(0.5)

        ex2 = Text(
            "L 個の辞書を線形結合し、互いに直交する R 個のバリエーションの辞書を作り直し、",
            color=WHITE, font_size=23,
        )
        ex2.shift(DOWN * 1.8)
        self.fit(ex2)
        ex3 = VGroup(
            MathTex(r"\{\boldsymbol{p}^{(d)}_r\}", color=GOLD, font_size=32),
            Text("について、各変数を独立に近似したものを R 個足し合わせている",
                 color=WHITE, font_size=23),
        ).arrange(RIGHT, buff=0.12)
        self.fit(ex3)
        ex3.next_to(ex2, DOWN, buff=0.2)
        self.play(Write(ex2), run_time=0.9)
        self.play(Write(ex3), run_time=0.9)
        self.wait(1.8)

        self.play(
            FadeOut(ex1), FadeOut(ex_eq), FadeOut(ex_box),
            FadeOut(ex2), FadeOut(ex3),
        )
        self.wait(0.3)

        # 要素数の比較
        cmp1 = VGroup(
            Text("これによって、必要な要素数は", color=WHITE, font_size=26),
            MathTex(r"R \times L \times D", color=GREEN, font_size=44),
            Text("となった", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.18)
        self.fit(cmp1)
        cmp1.shift(UP * 1.9)
        self.play(Write(cmp1), run_time=0.9)
        self.wait(0.3)

        cmp_rows = VGroup(
            VGroup(
                Text("素直な表現", color=WHITE, font_size=24),
                MathTex(r"L^D", color=RED, font_size=40),
                MathTex(r"(10^{10})", color=RED, font_size=30),
            ),
            VGroup(
                Text("独立と仮定した近似", color=WHITE, font_size=24),
                MathTex(r"L \times D", color=ORANGE, font_size=40),
                MathTex(r"(100)", color=ORANGE, font_size=30),
            ),
            VGroup(
                Text("R 個の和への拡張", color=WHITE, font_size=24),
                MathTex(r"R \times L \times D", color=GREEN, font_size=40),
                MathTex(r"(500)", color=GREEN, font_size=30),
            ),
        )
        for row in cmp_rows:
            row.arrange(RIGHT, buff=0.4)
        cmp_rows.arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        cmp_rows.shift(DOWN * 0.2)
        cmp_note = Text("（L = 10, D = 10, R = 5 の場合）", color=GRAY, font_size=22)
        cmp_note.next_to(cmp_rows, DOWN, buff=0.3)

        for row in cmp_rows:
            self.play(Write(row), run_time=0.7)
            self.wait(0.15)
        self.play(FadeIn(cmp_note), run_time=0.5)
        self.wait(0.5)

        cmp2 = Text(
            "L × D よりは増えたが、L^D よりはずっとマシで、近似精度も良くなる",
            color=GOLD, font_size=25, weight=BOLD,
        )
        cmp2.shift(DOWN * 2.7)
        self.fit(cmp2)
        self.play(Write(cmp2), run_time=0.9)
        self.wait(2.0)

        self.play(
            FadeOut(cmp1), FadeOut(cmp_rows), FadeOut(cmp_note), FadeOut(cmp2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: 2変数の場合は厳密 — 行列への並べ直し
        # ============================================================
        subtitle4 = Text("2変数の場合は、近似ではなく厳密に表せる", font_size=28, color=ORANGE)
        subtitle4.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle4), run_time=0.5)
        self.wait(0.3)

        ex2v1 = Text(
            "実際に、2変数の場合この分解は厳密であることが分かっている",
            color=WHITE, font_size=25,
        )
        ex2v1.shift(UP * 2.0)
        self.fit(ex2v1)
        self.play(Write(ex2v1), run_time=0.8)
        self.wait(0.3)

        self.reshape_animation()

        self.play(FadeOut(ex2v1))
        self.wait(0.3)

        # ============================================================
        # Part 5: 特異値分解
        # ============================================================
        subtitle5 = Text("行列 P を特異値分解する", font_size=30, color=YELLOW)
        subtitle5.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle5), run_time=0.5)
        self.wait(0.3)

        sv1 = Text("行列なので、特異値分解できて", color=WHITE, font_size=26)
        sv1.shift(UP * 1.9)
        self.play(Write(sv1), run_time=0.7)

        sv_eq = MathTex(
            r"P = U \Sigma V^{\top} = "
            r"\begin{bmatrix} \boldsymbol{u}_1 & \cdots & \boldsymbol{u}_R \end{bmatrix}"
            r"\begin{bmatrix} \sigma_1 & 0 & \cdots & 0 \\ 0 & \sigma_2 & \cdots & 0 \\"
            r"\vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & \sigma_R \end{bmatrix}"
            r"\begin{bmatrix} \boldsymbol{v}_1^{\top} \\ \vdots \\ \boldsymbol{v}_R^{\top} \end{bmatrix}",
            font_size=36, color=WHITE,
        )
        self.fit(sv_eq)
        sv_eq.shift(UP * 0.4)
        self.play(Write(sv_eq), run_time=1.6)
        self.wait(0.6)

        sv_rank = VGroup(
            Text("ここでの", color=WHITE, font_size=24),
            MathTex(r"R = \operatorname{rank} P", color=GOLD, font_size=34),
            Text("、特異値は大きい順", color=WHITE, font_size=24),
            MathTex(r"\sigma_1 \ge \sigma_2 \ge \cdots \ge \sigma_R > 0",
                    color=GOLD, font_size=34),
        ).arrange(RIGHT, buff=0.12)
        self.fit(sv_rank)
        sv_rank.shift(DOWN * 1.5)
        self.play(Write(sv_rank), run_time=0.9)
        self.wait(1.0)

        sv2 = VGroup(
            Text("ここで", color=WHITE, font_size=25),
            MathTex(r"\Sigma", color=GOLD, font_size=34),
            Text("と", color=WHITE, font_size=25),
            MathTex(r"V^{\top}", color=GOLD, font_size=34),
            Text("の積を", color=WHITE, font_size=25),
            MathTex(r"\widetilde{V}^{\top}", color=YELLOW, font_size=36),
            Text("とおき直す", color=WHITE, font_size=25),
        ).arrange(RIGHT, buff=0.12)
        self.fit(sv2)
        sv2.shift(DOWN * 2.4)
        self.play(Write(sv2), run_time=0.9)
        self.wait(1.5)

        self.play(FadeOut(sv1), FadeOut(sv_eq), FadeOut(sv_rank), FadeOut(sv2))

        sv3 = Text("さらに、行ベクトル表現になおすと", color=WHITE, font_size=26)
        sv3.shift(UP * 1.9)
        self.play(Write(sv3), run_time=0.7)

        sv_eq2 = MathTex(
            r"P = U \widetilde{V}^{\top} = "
            r"\begin{bmatrix} \boldsymbol{u}_1 & \cdots & \boldsymbol{u}_R \end{bmatrix}"
            r"\begin{bmatrix} \widetilde{\boldsymbol{v}}_1^{\top} \\ \vdots \\"
            r"\widetilde{\boldsymbol{v}}_R^{\top} \end{bmatrix}"
            r"= \sum_{r=1}^{R} \boldsymbol{u}_r \widetilde{\boldsymbol{v}}_r^{\top}",
            font_size=40, color=YELLOW,
        )
        self.fit(sv_eq2)
        sv_eq2.shift(UP * 0.4)
        sv_box = SurroundingRectangle(sv_eq2, color=YELLOW, buff=0.22)
        self.play(Write(sv_eq2), run_time=1.6)
        self.play(Create(sv_box), run_time=0.6)
        self.wait(0.6)

        sv4 = Text(
            "つまり、P はランク 1 の行列 R（= rank P）個の和で厳密に書ける",
            color=TEAL, font_size=26, weight=BOLD,
        )
        sv4.shift(DOWN * 1.6)
        self.fit(sv4)
        self.play(Write(sv4), run_time=0.8)
        self.wait(1.8)

        self.play(FadeOut(sv3), FadeOut(sv_eq2), FadeOut(sv_box), FadeOut(sv4))
        self.wait(0.3)

        # ============================================================
        # Part 6: 紙芝居 — ランク1行列の足し合わせ
        # ============================================================
        subtitle6 = Text("ランク 1 の行列を足し合わせる", font_size=30, color=PURPLE)
        subtitle6.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle6), run_time=0.5)
        self.wait(0.3)

        self.outer_product_animation()
        self.wait(0.3)

        # ============================================================
        # Part 7: (n1, n2) 要素が R 個の積和の式に一致する
        # ============================================================
        subtitle7 = Text("(n_1, n_2) 要素を見ると…", font_size=30, color=GOLD)
        subtitle7.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle7), run_time=0.5)
        self.wait(0.3)

        el1 = VGroup(
            Text("この行列の", color=WHITE, font_size=26),
            MathTex(r"(n_1, n_2)", color=GOLD, font_size=36),
            Text("要素は", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.15)
        el1.shift(UP * 1.7)
        self.play(Write(el1), run_time=0.7)

        el_eq = MathTex(
            r"[P]_{n_1, n_2} = \sum_{r=1}^{R} u_{r,n_1}\, \widetilde{v}_{r,n_2}",
            font_size=48, color=YELLOW,
        )
        el_eq.shift(UP * 0.4)
        el_box = SurroundingRectangle(el_eq, color=YELLOW, buff=0.22)
        self.play(Write(el_eq), Create(el_box), run_time=1.0)
        self.wait(0.5)

        el2 = Text(
            "これは先ほどの「変数ごとの積の近似を R 個足し合わせた式」で、",
            color=WHITE, font_size=25,
        )
        el2.shift(DOWN * 0.9)
        self.fit(el2)
        el2b = Text(
            "項の数を R = rank P に取った場合に一致する（≃ ではなく = ）",
            color=WHITE, font_size=25,
        )
        el2b.next_to(el2, DOWN, buff=0.15)
        self.fit(el2b)
        self.fit(el2)
        self.play(Write(el2), run_time=0.9)
        self.play(Write(el2b), run_time=0.9)

        el_cmp = MathTex(
            r"p^{(1)}_{r,n_1} = u_{r,n_1},\quad p^{(2)}_{r,n_2} = \widetilde{v}_{r,n_2}",
            font_size=38, color=GOLD,
        )
        self.fit(el_cmp)
        el_cmp.shift(DOWN * 2.6)
        self.play(Write(el_cmp), run_time=0.9)
        self.wait(2.0)

        self.play(
            FadeOut(el1), FadeOut(el_eq), FadeOut(el_box),
            FadeOut(el2), FadeOut(el2b), FadeOut(el_cmp),
        )
        self.wait(0.3)

        # ============================================================
        # Part 8: 低ランク近似の再確認
        # ============================================================
        subtitle8 = Text("低ランク近似の再確認", font_size=30, color=TEAL)
        subtitle8.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle8), run_time=0.5)
        self.wait(0.3)

        lr1 = Text(
            "特異値分解の回で出てきた低ランク近似は、",
            color=WHITE, font_size=26,
        )
        lr1.shift(UP * 1.9)
        self.fit(lr1)
        self.play(Write(lr1), run_time=0.7)

        lr_eq = MathTex(
            r"P = \sum_{r=1}^{R} \sigma_r \boldsymbol{u}_r \boldsymbol{v}_r^{\top}"
            r"\;\simeq\; \sum_{r=1}^{R'} \sigma_r \boldsymbol{u}_r \boldsymbol{v}_r^{\top}"
            r"\quad (R' < R = \operatorname{rank} P)",
            font_size=40, color=YELLOW,
        )
        self.fit(lr_eq)
        lr_eq.shift(UP * 0.6)
        self.play(Write(lr_eq), run_time=1.3)

        lr2 = Text(
            "R 個の全ての特異値を使えば厳密な表現になる",
            color=GREEN, font_size=26, weight=BOLD,
        )
        lr2.shift(DOWN * 0.7)
        self.fit(lr2)
        lr3 = Text(
            "大きい順に R' 個だけ使い、意図的に全ては使わないことで近似していた",
            color=GOLD, font_size=26, weight=BOLD,
        )
        lr3.next_to(lr2, DOWN, buff=0.3)
        self.fit(lr3)
        self.play(Write(lr2), run_time=0.8)
        self.play(Write(lr3), run_time=0.9)
        self.wait(1.8)

        self.play(FadeOut(lr1), FadeOut(lr_eq), FadeOut(lr2), FadeOut(lr3))
        self.wait(0.3)

        # ============================================================
        # Part 9: 3変数以上への拡張
        # ============================================================
        subtitle9 = Text("3変数以上への拡張", font_size=30, color=RED)
        subtitle9.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle9), run_time=0.5)
        self.wait(0.3)

        m1 = Text(
            "3変数以上でも、平面を取り出して SVD して足し合わせる、",
            color=WHITE, font_size=25,
        )
        m1.shift(UP * 1.9)
        self.fit(m1)
        m2 = Text(
            "という操作を繰り返すことで、厳密さを保つことができる",
            color=WHITE, font_size=25,
        )
        m2.next_to(m1, DOWN, buff=0.2)
        self.fit(m2)
        self.play(Write(m1), run_time=0.8)
        self.play(Write(m2), run_time=0.8)
        self.wait(0.4)

        m3 = Text("3変数の場合の式は", color=WHITE, font_size=26)
        m3.shift(UP * 0.1)
        self.play(Write(m3), run_time=0.6)

        m_eq = MathTex(
            r"p_{n_1, n_2, n_3} = \sum_{r_1=1}^{R_1} \sum_{r_2=1}^{R_2}"
            r"p^{(1)}_{n_1, r_1}\, p^{(2)}_{r_1, n_2, r_2}\, p^{(3)}_{r_2, n_3}",
            font_size=42, color=YELLOW,
        )
        self.fit(m_eq)
        m_eq.shift(DOWN * 1.1)
        m_box = SurroundingRectangle(m_eq, color=YELLOW, buff=0.22)
        self.play(Write(m_eq), Create(m_box), run_time=1.5)
        self.wait(0.5)

        # 添字のつながりを強調
        m4 = Text(
            "真ん中のテンソルが r_1, r_2 の添字で両隣とつながっている",
            color=TEAL, font_size=23,
        )
        m4.shift(DOWN * 2.4)
        self.fit(m4)
        self.play(Write(m4), run_time=0.8)
        self.wait(1.8)

        self.play(
            FadeOut(m1), FadeOut(m2), FadeOut(m3),
            FadeOut(m_eq), FadeOut(m_box), FadeOut(m4),
        )
        self.wait(0.3)

        # ============================================================
        # Part 10: まとめ・次回予告
        # ============================================================
        subtitle10 = Text("まとめ", font_size=34, color=TEAL)
        subtitle10.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle10), run_time=0.6)
        self.wait(0.3)

        summary = VGroup(
            Text("• 単項式以外の辞書では、前回のようにうまく分解できないこともある",
                 color=WHITE, font_size=26),
            Text("• 各変数が独立と仮定すれば要素数は L×D だが、精度が悪い",
                 color=WHITE, font_size=26),
            Text("• R 個の独立な近似の和にすると、要素数は R×L×D で精度も向上",
                 color=GOLD, font_size=26, weight=BOLD),
            Text("• 2変数では R = rank P に取れば、SVD によりこの分解は厳密になる",
                 color=WHITE, font_size=26),
            Text("• 低ランク近似は、大きい特異値 R' 個だけを使う近似だった",
                 color=WHITE, font_size=26),
            Text("• 3変数以上も、SVD を繰り返せば厳密に表現できる",
                 color=TEAL, font_size=26, weight=BOLD),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        summary.shift(DOWN * 0.1)
        self.fit(summary)

        for row in summary:
            self.play(Write(row), run_time=0.55)
            self.wait(0.15)
        self.wait(1.2)

        nxt = Text(
            "次回：多変数の場合を一般化し、データから実際に近似する方法を学ぶ",
            color=YELLOW, font_size=25, weight=BOLD,
        )
        nxt.to_edge(DOWN, buff=0.4)
        self.fit(nxt)
        self.play(Write(nxt), run_time=0.9)
        self.wait(2.0)

        self.play(
            FadeOut(VGroup(title, subtitle, summary, nxt)),
            run_time=1.0,
        )
        self.wait(0.5)

    # ================================================================
    # L^2 ベクトル → L×L 行列 P への並べ直し（L = 3）
    # ================================================================
    def reshape_animation(self):
        L = 3
        vcell = 0.4
        mcell = 0.85

        vec_group = VGroup()
        vec_cells = []
        for k in range(L * L):
            n1, n2 = k // L + 1, k % L + 1
            sq = Square(side_length=vcell)
            sq.set_stroke(TEAL, 2)
            sq.set_fill(TEAL, 0.15)
            sq.move_to(DOWN * k * vcell)
            lab = MathTex(rf"p_{{{n1},{n2}}}", font_size=18, color=WHITE)
            lab.move_to(sq.get_center())
            cg = VGroup(sq, lab)
            vec_group.add(cg)
            vec_cells.append(cg)
        vec_group.move_to(LEFT * 4.0 + DOWN * 0.7)

        vec_label = MathTex(r"\boldsymbol{p}", font_size=34, color=TEAL)
        vec_label.next_to(vec_group, UP, buff=0.2)
        vec_size = Text("L² 個の要素", color=WHITE, font_size=22)
        vec_size.next_to(vec_group, DOWN, buff=0.2)

        self.play(FadeIn(vec_group), Write(vec_label), Write(vec_size), run_time=0.9)
        self.wait(0.4)

        mat_group = VGroup()
        mat_origin = RIGHT * 2.0 + DOWN * 0.7
        mat_squares = []
        for n1 in range(L):
            for n2 in range(L):
                sq = Square(side_length=mcell)
                sq.set_stroke(ORANGE, 2)
                sq.set_fill(ORANGE, 0.15)
                sq.move_to(
                    mat_origin
                    + RIGHT * (n2 - (L - 1) / 2) * mcell
                    + DOWN * (n1 - (L - 1) / 2) * mcell
                )
                mat_squares.append(sq)
                mat_group.add(sq)

        arrow = Arrow(LEFT * 2.2 + DOWN * 0.7, LEFT * 0.4 + DOWN * 0.7, color=WHITE, buff=0)
        arrow_txt = Text("並べ直す", font_size=22, color=WHITE)
        arrow_txt.next_to(arrow, UP, buff=0.1)
        self.play(GrowArrow(arrow), Write(arrow_txt), run_time=0.7)

        # 3 要素ずつ（n1 固定）行として並べ直す
        placed = VGroup()
        for n1 in range(L):
            anims = []
            for n2 in range(L):
                k = n1 * L + n2
                target_sq = mat_squares[k]
                src = vec_cells[k]
                new_lab = MathTex(rf"p_{{{n1+1},{n2+1}}}", font_size=26, color=WHITE)
                new_lab.move_to(target_sq.get_center())
                cell_grp = VGroup(target_sq, new_lab)
                placed.add(cell_grp)
                anims.append(ReplacementTransform(src.copy(), cell_grp))
            hl = SurroundingRectangle(
                VGroup(*[vec_cells[n1 * L + n2] for n2 in range(L)]),
                color=YELLOW, buff=0.03,
            )
            self.play(Create(hl), run_time=0.3)
            self.play(*anims, run_time=0.7)
            self.play(FadeOut(hl), run_time=0.2)

        mat_label = MathTex(r"P \in \mathbb{R}^{L \times L}", font_size=34, color=ORANGE)
        mat_label.next_to(mat_group, UP, buff=0.3)
        mat_size = Text("L × L の行列", color=WHITE, font_size=22)
        mat_size.next_to(mat_group, DOWN, buff=0.3)
        self.play(Write(mat_label), Write(mat_size), run_time=0.8)

        note = Text(
            "L² のベクトルを、一度 L × L の行列 P に並べ直したとする",
            color=GOLD, font_size=25, weight=BOLD,
        )
        note.to_edge(DOWN, buff=0.4)
        self.fit(note)
        self.play(Write(note), run_time=0.9)
        self.wait(1.8)

        self.play(
            FadeOut(vec_group), FadeOut(vec_label), FadeOut(vec_size),
            FadeOut(arrow), FadeOut(arrow_txt), FadeOut(placed),
            FadeOut(mat_label), FadeOut(mat_size), FadeOut(note),
            run_time=0.8,
        )

    # ================================================================
    # ランク1行列 u_r v_r^T を足し合わせて P を作る紙芝居
    # ================================================================
    def outer_product_animation(self):
        # SVD の成分として整合する数値（u_r は正規直交、ṽ_r = σ_r v_r は直交）
        #   u_1 = (1,2,2)/3, u_2 = (2,1,-2)/3
        #   ṽ_1 = (6,3,6)  (σ_1 = 9),  ṽ_2 = (3,0,-3)  (σ_2 = 3√2)
        u_tex = [
            [r"\tfrac{1}{3}", r"\tfrac{2}{3}", r"\tfrac{2}{3}"],
            [r"\tfrac{2}{3}", r"\tfrac{1}{3}", r"-\tfrac{2}{3}"],
        ]
        v_tex = [["6", "3", "6"], ["3", "0", "-3"]]
        M1 = np.outer([1, 2, 2], [6, 3, 6]) // 3
        M2 = np.outer([2, 1, -2], [3, 0, -3]) // 3
        colors = [TEAL, ORANGE]
        cell = 0.55
        L = 3

        def make_block(u, v, color, with_margin, center):
            grid = VGroup()
            for i in range(L):
                for j in range(L):
                    sq = Square(side_length=cell)
                    sq.set_stroke(color, 2)
                    sq.set_fill(color, 0.1)
                    sq.move_to(RIGHT * (j - 1) * cell + DOWN * (i - 1) * cell)
                    grid.add(sq)
            grid.move_to(center)
            margins = VGroup()
            if with_margin:
                for i in range(L):
                    t = MathTex(u[i], font_size=24, color=YELLOW)
                    t.next_to(grid[i * L], LEFT, buff=0.15)
                    margins.add(t)
                for j in range(L):
                    t = MathTex(v[j], font_size=24, color=GOLD)
                    t.next_to(grid[j], UP, buff=0.15)
                    margins.add(t)
            return grid, margins

        centers = [LEFT * 4.6 + DOWN * 0.2, LEFT * 0.4 + DOWN * 0.2, RIGHT * 4.2 + DOWN * 0.2]

        g1, mg1 = make_block(u_tex[0], v_tex[0], colors[0], True, centers[0])
        g2, mg2 = make_block(u_tex[1], v_tex[1], colors[1], True, centers[1])
        P_val = M1 + M2
        gP, _ = make_block(None, None, YELLOW, False, centers[2])

        plus = MathTex(r"+", font_size=44, color=WHITE).move_to((centers[0] + centers[1]) / 2)
        equal = MathTex(r"=", font_size=44, color=WHITE).move_to((centers[1] + centers[2]) / 2)

        lab1 = MathTex(r"\boldsymbol{u}_1 \widetilde{\boldsymbol{v}}_1^{\top}",
                       font_size=30, color=TEAL)
        lab1.next_to(g1, DOWN, buff=0.4)
        lab2 = MathTex(r"\boldsymbol{u}_2 \widetilde{\boldsymbol{v}}_2^{\top}",
                       font_size=30, color=ORANGE)
        lab2.next_to(g2, DOWN, buff=0.4)
        labP = MathTex(r"P", font_size=34, color=YELLOW)
        labP.next_to(gP, DOWN, buff=0.4)

        intro = Text(
            "例：L = 3, R = 2。縦ベクトルと横ベクトルの積で行列を作る",
            color=WHITE, font_size=24,
        )
        intro.shift(UP * 1.8)
        self.fit(intro)
        self.play(Write(intro), run_time=0.8)

        # 1 項目
        self.play(Create(g1), FadeIn(mg1), Write(lab1), run_time=0.8)
        nums1 = VGroup()
        for i in range(L):
            for j in range(L):
                t = MathTex(str(int(M1[i, j])), font_size=22, color=WHITE)
                t.move_to(g1[i * L + j].get_center())
                nums1.add(t)
        self.play(Write(nums1), run_time=0.9)
        self.wait(0.3)

        self.play(Write(plus), run_time=0.3)

        # 2 項目
        self.play(Create(g2), FadeIn(mg2), Write(lab2), run_time=0.8)
        nums2 = VGroup()
        for i in range(L):
            for j in range(L):
                t = MathTex(str(int(M2[i, j])), font_size=22, color=WHITE)
                t.move_to(g2[i * L + j].get_center())
                nums2.add(t)
        self.play(Write(nums2), run_time=0.9)
        self.wait(0.3)

        # 和
        self.play(Write(equal), Create(gP), Write(labP), run_time=0.8)
        numsP = VGroup()
        for i in range(L):
            for j in range(L):
                t = MathTex(str(int(P_val[i, j])), font_size=22, color=YELLOW)
                t.move_to(gP[i * L + j].get_center())
                numsP.add(t)
        self.play(
            *[
                ReplacementTransform(
                    VGroup(nums1[k].copy(), nums2[k].copy()), numsP[k]
                )
                for k in range(L * L)
            ],
            run_time=1.2,
        )
        self.wait(0.5)

        svd_note = MathTex(
            r"\boldsymbol{u}_1 \perp \boldsymbol{u}_2,\ \|\boldsymbol{u}_r\| = 1,\qquad"
            r"\widetilde{\boldsymbol{v}}_1 \perp \widetilde{\boldsymbol{v}}_2,\ "
            r"\|\widetilde{\boldsymbol{v}}_1\| = \sigma_1 = 9,\ "
            r"\|\widetilde{\boldsymbol{v}}_2\| = \sigma_2 = 3\sqrt{2}",
            font_size=28, color=GRAY,
        )
        self.fit(svd_note)
        svd_note.shift(DOWN * 2.3)
        self.play(FadeIn(svd_note), run_time=0.6)
        self.wait(1.0)

        concl = Text(
            "ランク 1 の行列を R 個足し合わせると、元の行列 P を作れる",
            color=GREEN, font_size=26, weight=BOLD,
        )
        concl.to_edge(DOWN, buff=0.4)
        self.fit(concl)
        self.play(Write(concl), run_time=0.8)
        self.wait(2.0)

        self.play(
            FadeOut(intro), FadeOut(g1), FadeOut(mg1), FadeOut(lab1), FadeOut(nums1),
            FadeOut(plus), FadeOut(g2), FadeOut(mg2), FadeOut(lab2), FadeOut(nums2),
            FadeOut(equal), FadeOut(gP), FadeOut(labP), FadeOut(numsP),
            FadeOut(svd_note), FadeOut(concl),
            run_time=0.8,
        )
