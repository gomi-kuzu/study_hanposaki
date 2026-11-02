from manim import *
import numpy as np


class KoopmanModeDecompositionOverview(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        title = Text("クープマンモード分解の概要", font_size=38, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)

        # ============================================================
        # Part 1: 導入 — 前回の復習と今回の目標
        # ============================================================
        subtitle = Text("導入：なぜモード分解をするのか", font_size=27, color=BLUE)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle), run_time=0.6)
        self.wait(0.3)

        intro1 = Text(
            "前回26話では、観測関数に作用するクープマン行列を",
            color=WHITE, font_size=26,
        )
        intro1.shift(UP * 1.9)
        if intro1.width > config.frame_width - 1.0:
            intro1.scale_to_fit_width(config.frame_width - 1.0)
        intro1b = Text(
            "辞書関数とデータを使って近似する方法を学んだ",
            color=WHITE, font_size=26,
        )
        intro1b.next_to(intro1, DOWN, buff=0.2)
        self.play(Write(intro1), run_time=0.7)
        self.play(Write(intro1b), run_time=0.7)
        self.wait(0.3)

        intro2 = Text(
            "それだけでもスナップショットペアの予測はできるが…",
            color=WHITE, font_size=26,
        )
        intro2.shift(UP * 0.4)
        self.play(Write(intro2), run_time=0.8)
        self.wait(0.3)

        intro3 = VGroup(
            Text("クープマンモード分解", color=GOLD, font_size=28, weight=BOLD),
            Text("をすると", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.15)
        intro3.shift(DOWN * 0.5)
        self.play(Write(intro3), run_time=0.7)

        intro4 = VGroup(
            Text("• さらに動的解析ができる", color=TEAL, font_size=25),
            Text("• 予測時の計算量を減らせる", color=TEAL, font_size=25),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        intro4.shift(DOWN * 1.6)
        for row in intro4:
            self.play(Write(row), run_time=0.55)
            self.wait(0.1)

        intro5 = Text(
            "今回はその概要を説明する",
            color=GOLD, font_size=26, weight=BOLD,
        )
        intro5.shift(DOWN * 2.6)
        self.play(Write(intro5), run_time=0.7)
        self.wait(1.8)

        self.play(
            FadeOut(intro1), FadeOut(intro1b), FadeOut(intro2),
            FadeOut(intro3), FadeOut(intro4), FadeOut(intro5),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: クープマン固有値・固有関数
        # ============================================================
        subtitle2 = Text("クープマン固有値・固有関数", font_size=28, color=GOLD)
        subtitle2.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle2), run_time=0.5)
        self.wait(0.3)

        eig1 = Text(
            "23話では、行列の固有値・固有ベクトルと同じように、",
            color=WHITE, font_size=26,
        )
        eig1.shift(UP * 1.9)
        if eig1.width > config.frame_width - 0.8:
            eig1.scale_to_fit_width(config.frame_width - 0.8)
        eig2 = Text(
            "作用素に対しても固有値・固有関数が定義できることを学んだ",
            color=WHITE, font_size=26,
        )
        eig2.next_to(eig1, DOWN, buff=0.2)
        if eig2.width > config.frame_width - 0.8:
            eig2.scale_to_fit_width(config.frame_width - 0.8)
        self.play(Write(eig1), run_time=0.7)
        self.play(Write(eig2), run_time=0.7)
        self.wait(0.3)

        eig3 = VGroup(
            Text("クープマン作用素", color=WHITE, font_size=26),
            MathTex(r"\mathcal{K}", color=TEAL, font_size=34),
            Text("も作用素の一種なので、同様に", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.15)
        eig3.shift(UP * 0.5)
        self.play(Write(eig3), run_time=0.8)
        self.wait(0.3)

        eig_eq = MathTex(
            r"\mathcal{K}\,\varphi_m(\boldsymbol{x})"
            r"= (\mathcal{K}\varphi_m)(\boldsymbol{x})"
            r"= \mu_m\,\varphi_m(\boldsymbol{x}),"
            r"\quad m = 1, 2, \dots, M_{\text{eigen}}",
            font_size=38, color=YELLOW,
        )
        if eig_eq.width > config.frame_width - 0.8:
            eig_eq.scale_to_fit_width(config.frame_width - 0.8)
        eig_eq.shift(DOWN * 0.6)
        eig_box = SurroundingRectangle(eig_eq, color=YELLOW, buff=0.22)
        self.play(Write(eig_eq), Create(eig_box), run_time=1.1)
        self.wait(0.3)

        eig4 = VGroup(
            Text("を満たす固有値", color=WHITE, font_size=26),
            MathTex(r"\mu_m", color=GOLD, font_size=32),
            Text("と固有関数", color=WHITE, font_size=26),
            MathTex(r"\varphi_m", color=GOLD, font_size=32),
            Text("が存在する", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.12)
        eig4.shift(DOWN * 1.9)
        self.play(Write(eig4), run_time=0.8)
        self.wait(0.3)

        eig5 = Text(
            "これらを特にクープマン固有値・クープマン固有関数と呼ぶ",
            color=GOLD, font_size=26, weight=BOLD,
        )
        eig5.shift(DOWN * 2.8)
        if eig5.width > config.frame_width - 0.8:
            eig5.scale_to_fit_width(config.frame_width - 0.8)
        self.play(Write(eig5), run_time=0.8)
        self.wait(1.8)

        self.play(
            FadeOut(eig1), FadeOut(eig2), FadeOut(eig3),
            FadeOut(eig_eq), FadeOut(eig_box), FadeOut(eig4), FadeOut(eig5),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: 状態量を関数として表現する
        # ============================================================
        subtitle3 = Text("ステップ1：状態量を関数として表す", font_size=28, color=TEAL)
        subtitle3.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle3), run_time=0.5)
        self.wait(0.3)

        rep1 = Text(
            "クープマン固有関数は1次独立なので、辞書として利用できる",
            color=WHITE, font_size=26,
        )
        rep1.shift(UP * 1.9)
        if rep1.width > config.frame_width - 0.8:
            rep1.scale_to_fit_width(config.frame_width - 0.8)
        self.play(Write(rep1), run_time=0.8)
        self.wait(0.3)

        rep2 = Text(
            "これを使って状態量を表現したい。ただしこの後に作用素を導入するため、",
            color=WHITE, font_size=25,
        )
        rep2.shift(UP * 1.2)
        if rep2.width > config.frame_width - 0.8:
            rep2.scale_to_fit_width(config.frame_width - 0.8)
        rep3 = Text(
            "ベクトルではなく「関数」として表現しておきたい",
            color=GOLD, font_size=26, weight=BOLD,
        )
        rep3.next_to(rep2, DOWN, buff=0.2)
        self.play(Write(rep2), run_time=0.8)
        self.play(Write(rep3), run_time=0.7)
        self.wait(0.3)

        rep4 = VGroup(
            Text("状態量", color=WHITE, font_size=25),
            MathTex(r"\boldsymbol{x}", color=TEAL, font_size=30),
            Text("から d 番目の要素を取り出す関数", color=WHITE, font_size=25),
            MathTex(r"g_d(\cdot)", color=GOLD, font_size=30),
            Text("を定義し、", color=WHITE, font_size=25),
        ).arrange(RIGHT, buff=0.12)
        if rep4.width > config.frame_width - 0.8:
            rep4.scale_to_fit_width(config.frame_width - 0.8)
        rep4.shift(DOWN * 0.1)
        rep5 = VGroup(
            Text("それらを並べたベクトル値関数", color=WHITE, font_size=25),
            MathTex(r"\boldsymbol{g}(\cdot)", color=GOLD, font_size=30),
            Text("を考える", color=WHITE, font_size=25),
        ).arrange(RIGHT, buff=0.12)
        rep5.next_to(rep4, DOWN, buff=0.25)
        self.play(Write(rep4), run_time=0.9)
        self.play(Write(rep5), run_time=0.7)
        self.wait(0.3)

        rep_eq = MathTex(
            r"\boldsymbol{x}"
            r"= \begin{bmatrix} x_1 \\ \vdots \\ x_D \end{bmatrix}"
            r"= \boldsymbol{g}(\boldsymbol{x})"
            r"= \begin{bmatrix} g_1(\boldsymbol{x}) \\ \vdots \\ g_D(\boldsymbol{x}) \end{bmatrix}"
            r"= \sum_{m=1}^{M_{\text{eigen}}} \boldsymbol{v}_m\,\varphi_m(\boldsymbol{x})",
            font_size=36, color=YELLOW,
        )
        if rep_eq.width > config.frame_width - 0.8:
            rep_eq.scale_to_fit_width(config.frame_width - 0.8)
        rep_eq.shift(DOWN * 2.2)
        rep_box = SurroundingRectangle(rep_eq, color=YELLOW, buff=0.22)
        self.play(Write(rep_eq), Create(rep_box), run_time=1.2)
        self.wait(1.8)

        self.play(
            FadeOut(rep1), FadeOut(rep2), FadeOut(rep3),
            FadeOut(rep4), FadeOut(rep5),
        )
        self.wait(0.2)

        # ============================================================
        # Part 4: クープマン・モード
        # ============================================================
        subtitle4 = Text("クープマン・モードの定義", font_size=28, color=ORANGE)
        subtitle4.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle4), run_time=0.5)

        # 直前の式を上部へ移動して残す
        self.play(
            rep_eq.animate.scale(0.9).shift(UP * 3.5),
            rep_box.animate.scale(0.9).shift(UP * 3.5),
            run_time=0.8,
        )
        self.wait(0.3)

        mode1 = VGroup(
            Text("ここで現れる展開係数", color=WHITE, font_size=26),
            MathTex(r"\boldsymbol{v}_m", color=GOLD, font_size=34),
            Text("を", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.15)
        mode1.shift(DOWN * 0.2)
        self.play(Write(mode1), run_time=0.8)
        self.wait(0.3)

        mode2 = VGroup(
            Text("m 番目のクープマン固有値に対する", color=WHITE, font_size=26),
            Text("クープマン・モード", color=GOLD, font_size=28, weight=BOLD),
            Text("と呼ぶ", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.15)
        if mode2.width > config.frame_width - 0.8:
            mode2.scale_to_fit_width(config.frame_width - 0.8)
        mode2.shift(DOWN * 1.3)
        mode_box = SurroundingRectangle(mode2, color=GOLD, buff=0.22)
        self.play(Write(mode2), Create(mode_box), run_time=0.9)
        self.wait(1.8)

        self.play(
            FadeOut(rep_eq), FadeOut(rep_box),
            FadeOut(mode1), FadeOut(mode2), FadeOut(mode_box),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: スナップショットペア予測の再考
        # ============================================================
        subtitle5 = Text("ステップ2：スナップショットペア予測の再考", font_size=27, color=YELLOW)
        subtitle5.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle5), run_time=0.5)
        self.wait(0.3)

        snap1 = VGroup(
            Text("求めたい", color=WHITE, font_size=26),
            MathTex(r"\boldsymbol{g}(\boldsymbol{y}_n)", color=TEAL, font_size=32),
            Text("は", color=WHITE, font_size=26),
            MathTex(r"\boldsymbol{g}(\boldsymbol{x}_n)", color=TEAL, font_size=32),
            Text("をクープマン作用素", color=WHITE, font_size=26),
            MathTex(r"\mathcal{K}", color=GOLD, font_size=32),
            Text("に作用させたもの", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.1)
        if snap1.width > config.frame_width - 0.6:
            snap1.scale_to_fit_width(config.frame_width - 0.6)
        snap1.shift(UP * 1.9)
        self.play(Write(snap1), run_time=1.0)
        self.wait(0.3)

        snap_eq = MathTex(
            r"\boldsymbol{g}(\boldsymbol{y}_n)",
            r"&= \mathcal{K}\,\boldsymbol{g}(\boldsymbol{x}_n) \\",
            r"&= \mathcal{K} \left( \sum_{m=1}^{M_{\text{eigen}}} \boldsymbol{v}_m\,\varphi_m(\boldsymbol{x}_n) \right)"
            r"= \sum_{m=1}^{M_{\text{eigen}}} \boldsymbol{v}_m\,(\mathcal{K}\varphi_m)(\boldsymbol{x}_n) \\",
            r"&= \sum_{m=1}^{M_{\text{eigen}}} \boldsymbol{v}_m\,\bigl(\mu_m\,\varphi_m(\boldsymbol{x}_n)\bigr)",
            font_size=36, color=WHITE,
        )
        if snap_eq.width > config.frame_width - 0.8:
            snap_eq.scale_to_fit_width(config.frame_width - 0.8)
        snap_eq.shift(DOWN * 0.3)

        snap_lab1 = Text("分解の式を代入", color=TEAL, font_size=20)
        snap_lab1.next_to(snap_eq[2], RIGHT, buff=0.3)
        snap_lab2 = Text("固有関数の定義より", color=GOLD, font_size=20)
        snap_lab2.next_to(snap_eq[3], RIGHT, buff=0.3)

        self.play(Write(snap_eq[0]), Write(snap_eq[1]), run_time=0.9)
        self.wait(0.3)
        self.play(Write(snap_eq[2]), FadeIn(snap_lab1), run_time=1.3)
        self.wait(0.3)
        self.play(Write(snap_eq[3]), FadeIn(snap_lab2), run_time=1.0)
        self.wait(1.8)

        self.play(
            FadeOut(snap1), FadeOut(snap_eq),
            FadeOut(snap_lab1), FadeOut(snap_lab2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 6: 計算量が劇的に減る
        # ============================================================
        subtitle6 = Text("結論：予測のオンライン計算では行列計算すら不要に", font_size=28, color=PURPLE)
        subtitle6.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle6), run_time=0.5)
        self.wait(0.3)

        final_eq = MathTex(
            r"\boldsymbol{g}(\boldsymbol{y}_n)"
            r"= \sum_{m=1}^{M_{\text{eigen}}} \boldsymbol{v}_m\,\mu_m\,\varphi_m(\boldsymbol{x}_n)",
            font_size=44, color=YELLOW,
        )
        if final_eq.width > config.frame_width - 0.8:
            final_eq.scale_to_fit_width(config.frame_width - 0.8)
        final_eq.shift(UP * 1.2)
        final_box = SurroundingRectangle(final_eq, color=YELLOW, buff=0.22)
        self.play(Write(final_eq), Create(final_box), run_time=1.0)
        self.wait(0.3)

        cost1 = Text(
            "予測時のオンライン計算時は、次の3ステップのみ",
            color=WHITE, font_size=26,
        )
        # cost1.shift(UP * 0.4)
        self.play(Write(cost1), run_time=0.7)

        cost_list = VGroup(
            VGroup(
                Text("① 状態量に固有関数を適用する", color=WHITE, font_size=25),
                MathTex(r"\varphi_m(\boldsymbol{x}_n)", color=TEAL, font_size=28),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("② スカラ値をかける", color=WHITE, font_size=25),
                MathTex(r"\mu_m\,\varphi_m(\boldsymbol{x}_n)", color=TEAL, font_size=28),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("③ ベクトルにかけて M_eigen 個足し合わせる",
                     color=WHITE, font_size=25),
                MathTex(r"\textstyle\sum_m \boldsymbol{v}_m(\cdots)", color=TEAL, font_size=28),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        if cost_list.width > config.frame_width - 0.8:
            cost_list.scale_to_fit_width(config.frame_width - 0.8)
        cost_list.shift(DOWN * 1.6)
        for row in cost_list:
            self.play(Write(row), run_time=0.6)
            self.wait(0.15)
        self.wait(1.8)

        self.play(
            FadeOut(final_eq), FadeOut(final_box),
            FadeOut(cost1), FadeOut(cost_list),
        )
        self.wait(0.3)

        # ============================================================
        # Part 7: 注意点と展望
        # ============================================================
        subtitle7 = Text("注意点と今後の展望", font_size=28, color=RED)
        subtitle7.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle7), run_time=0.5)
        self.wait(0.3)

        note1 = Text(
            "※ ただし、クープマン固有値・固有関数・モードを求めるには",
            color=WHITE, font_size=25,
        )
        note1.shift(UP * 1.7)
        if note1.width > config.frame_width - 0.8:
            note1.scale_to_fit_width(config.frame_width - 0.8)
        note2 = Text(
            "26話で行ったような表現行列の推定の他にも、いくつかの計算が必要になる",
            color=WHITE, font_size=25,
        )
        note2.next_to(note1, DOWN, buff=0.2)
        if note2.width > config.frame_width - 0.8:
            note2.scale_to_fit_width(config.frame_width - 0.8)
        note3 = Text(
            "これについては次の動画で詳しく説明する",
            color=GOLD, font_size=26, weight=BOLD,
        )
        note3.next_to(note2, DOWN, buff=0.3)
        self.play(Write(note1), run_time=0.7)
        self.play(Write(note2), run_time=0.7)
        self.play(Write(note3), run_time=0.7)
        self.wait(0.5)

        note4 = Text(
            "また、線形システムの解析が固有値を中心になされたように、",
            color=WHITE, font_size=25,
        )
        note4.shift(DOWN * 1.1)
        if note4.width > config.frame_width - 0.8:
            note4.scale_to_fit_width(config.frame_width - 0.8)
        note5 = Text(
            "もともと非線形なシステムもこの固有値を用いて解析できる（らしい）",
            color=WHITE, font_size=25,
        )
        note5.next_to(note4, DOWN, buff=0.2)
        if note5.width > config.frame_width - 0.8:
            note5.scale_to_fit_width(config.frame_width - 0.8)
        note6 = Text(
            "が、この動画ではそこには踏み入らない",
            color=TEAL, font_size=25,
        )
        note6.next_to(note5, DOWN, buff=0.25)
        self.play(Write(note4), run_time=0.7)
        self.play(Write(note5), run_time=0.7)
        self.play(Write(note6), run_time=0.6)
        self.wait(1.8)

        self.play(
            FadeOut(note1), FadeOut(note2), FadeOut(note3),
            FadeOut(note4), FadeOut(note5), FadeOut(note6),
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
            Text("• クープマン作用素にも固有値 μ_m・固有関数 φ_m が定義できる",
                 color=WHITE, font_size=25),
            Text("• 固有関数は辞書として使え、状態量を g(x)=Σ v_m φ_m(x) と分解",
                 color=WHITE, font_size=25),
            Text("• 展開係数 v_m をクープマン・モードと呼ぶ",
                 color=WHITE, font_size=25),
            Text("• 予測は g(y_n)=Σ v_m μ_m φ_m(x_n) と書ける",
                 color=WHITE, font_size=25),
            Text("• オンライン予測では固有関数適用→スカラ倍→和 のみ",
                 color=GOLD, font_size=25, weight=BOLD),
            Text("• 固有値・固有関数・モードの求め方は次回へ",
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
