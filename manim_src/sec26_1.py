from manim import *
import numpy as np


class KoopmanOperatorIntro(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        title = Text("クープマン作用素とは", font_size=38, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)

        # ============================================================
        # Part 1: 導入 — 前回の復習と今回の目標
        # ============================================================
        subtitle = Text("導入：随伴作用素の具体例としてのクープマン作用素", font_size=27, color=BLUE)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle), run_time=0.6)
        self.wait(0.3)

        intro1 = Text(
            "前回は『随伴作用素』を導入した",
            color=WHITE, font_size=26,
        )
        intro1.shift(UP * 1.9)
        self.play(Write(intro1), run_time=0.8)
        self.wait(0.3)

        intro2 = Text(
            "これにより、状態量と観測量の内積を含む計算を、"
            "観測関数への作用素を起点に行えると分かった",
            color=GOLD, font_size=25, weight=BOLD,
        )
        intro2.shift(UP * 0.9)
        if intro2.width > config.frame_width - 1.0:
            intro2.scale_to_fit_width(config.frame_width - 1.0)
        self.play(Write(intro2), run_time=0.8)
        self.wait(0.3)

        intro3 = VGroup(
            Text("今回は、24話で登場した", color=WHITE, font_size=26),
            Text("ペロン・フロベニウス作用素", color=TEAL, font_size=26, weight=BOLD),
            Text("の", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.1)
        intro3.shift(DOWN * 0.1)
        self.play(Write(intro3), run_time=0.8)

        intro4 = VGroup(
            Text("随伴作用素にあたる", color=WHITE, font_size=26),
            Text("クープマン作用素", color=RED, font_size=26, weight=BOLD),
            MathTex(r"\mathcal{K}", color=RED, font_size=34),
            Text("を扱う", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.15)
        intro4.shift(DOWN * 1.0)
        self.play(Write(intro4), run_time=0.8)
        self.wait(0.3)

        intro5 = Text(
            "※問題設定は前回同様、少し未来の観測値（スナップショットペア）の予測",
            color=GRAY, font_size=24,
        )
        intro5.shift(DOWN * 2.0)
        self.play(Write(intro5), run_time=0.8)
        self.wait(1.8)

        self.play(
            FadeOut(intro1), FadeOut(intro2), FadeOut(intro3),
            FadeOut(intro4), FadeOut(intro5),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: 問題設定のおさらい（reproduce_fig26_1 のアニメ版）
        # ============================================================
        subtitle2 = Text("問題設定のおさらい", font_size=28, color=GOLD)
        subtitle2.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle2), run_time=0.5)
        self.wait(0.3)

        green_bg = "#708E50"
        orange_bg = "#D76C51"
        blue_arrow = "#3B75B4"
        red_accent = "#D9381E"
        gray_dashed = "#9AA0A6"

        # --- 上段：状態 x_n と y_n ---
        box_left = RoundedRectangle(
            width=3.0, height=0.6, corner_radius=0.12,
            fill_color=green_bg, fill_opacity=1.0, stroke_width=0,
        )
        box_left_lab = Text("現在時刻での状態", color=WHITE, font_size=22, weight=BOLD)
        box_left_lab.move_to(box_left)
        x_n = MathTex(r"\boldsymbol{x}_n", color=WHITE, font_size=34)
        left_group = VGroup(box_left, box_left_lab)
        left_group.shift(LEFT * 4.2 + UP * 1.3)
        x_n.next_to(left_group, RIGHT, buff=0.3)

        box_right = RoundedRectangle(
            width=3.0, height=0.6, corner_radius=0.12,
            fill_color=orange_bg, fill_opacity=1.0, stroke_width=0,
        )
        box_right_lab = Text("次の時刻での状態", color=WHITE, font_size=22, weight=BOLD)
        box_right_lab.move_to(box_right)
        y_n = MathTex(r"\boldsymbol{y}_n", color=WHITE, font_size=34)
        right_group = VGroup(box_right, box_right_lab)
        right_group.shift(RIGHT * 2.6 + UP * 1.3)
        y_n.next_to(right_group, RIGHT, buff=0.3)

        self.play(
            FadeIn(left_group), Write(x_n),
            FadeIn(right_group), Write(y_n),
            run_time=0.9,
        )

        # 上段矢印：Δt_obs の時間発展
        top_arrow = Arrow(
            x_n.get_right() + UP * 0.5, y_n.get_left() + UP * 0.5,
            color=blue_arrow, buff=0.1, stroke_width=4,
            max_tip_length_to_length_ratio=0.05,
        )
        top_arrow_lab = VGroup(
            MathTex(r"\Delta t_{\mathrm{obs}}", color=WHITE, font_size=28),
            Text("の時間発展", color=WHITE, font_size=20),
        ).arrange(RIGHT, buff=0.12)
        top_arrow_lab.next_to(top_arrow, UP, buff=0.05)
        self.play(GrowArrow(top_arrow), Write(top_arrow_lab), run_time=0.7)
        self.wait(0.3)

        # --- 縦の観測矢印 ---
        obs_arrow_l = DashedVMobject(Arrow(
            x_n.get_bottom() + DOWN * 0.1, x_n.get_bottom() + DOWN * 1.3,
            color=gray_dashed, buff=0.1, stroke_width=3,
            max_tip_length_to_length_ratio=0.12,
        ), num_dashes=8)
        obs_l_lab = Text("観測", color=gray_dashed, font_size=22)
        obs_l_lab.next_to(obs_arrow_l, LEFT, buff=0.1)

        obs_arrow_r = DashedVMobject(Arrow(
            y_n.get_bottom() + DOWN * 0.1, y_n.get_bottom() + DOWN * 1.3,
            color=gray_dashed, buff=0.1, stroke_width=3,
            max_tip_length_to_length_ratio=0.12,
        ), num_dashes=8)
        obs_r_lab = Text("観測", color=gray_dashed, font_size=22)
        obs_r_lab.next_to(obs_arrow_r, LEFT, buff=0.1)

        self.play(
            Create(obs_arrow_l), Write(obs_l_lab),
            Create(obs_arrow_r), Write(obs_r_lab),
            run_time=0.7,
        )

        # --- 下段：観測量 φ(x_n) と φ(y_n) ---
        phi_x = MathTex(r"\phi(\boldsymbol{x}_n)", color=WHITE, font_size=34)
        phi_x.next_to(obs_arrow_l, DOWN, buff=0.2)
        phi_x_lab = Text("とある観測量の値", color="#BBBBBB", font_size=22)
        phi_x_lab.next_to(phi_x, DOWN, buff=0.15)

        phi_y = MathTex(r"\phi(\boldsymbol{y}_n)", color=WHITE, font_size=34)
        phi_y.next_to(obs_arrow_r, DOWN, buff=0.2)
        phi_y_lab = Text("時間発展後の観測量の値", color="#BBBBBB", font_size=22)
        phi_y_lab.next_to(phi_y, DOWN, buff=0.15)

        self.play(
            Write(phi_x), Write(phi_x_lab),
            Write(phi_y), Write(phi_y_lab),
            run_time=0.8,
        )
        self.wait(0.3)

        # --- クープマン作用素：赤の目的ラベル & 曲線矢印 ---
        koop_lab = VGroup(
            Text("[目的]", color=red_accent, font_size=24, weight=BOLD),
            MathTex(r"(\mathcal{K}\phi)(\boldsymbol{x}_n)", color=red_accent, font_size=36),
        ).arrange(RIGHT, buff=0.15)
        koop_lab.move_to(ORIGIN + UP * 0.3)

        koop_arrow = CurvedArrow(
            x_n.get_bottom() + DOWN * 0.05 +RIGHT * 0.05,
            koop_lab.get_left() + LEFT * 0.1,
            color=orange_bg, stroke_width=3, angle=-TAU / 7,
            tip_length=0.2,
        )
        self.play(Write(koop_lab), run_time=0.6)
        self.play(Create(koop_arrow), run_time=0.9)


        koop_note = Text(
            "現在状態を入力すると「これ」を出力する関数",
            color=red_accent, font_size=24, weight=BOLD,
        )
        koop_note.shift(DOWN * 2)

        koop_arrow2 = CurvedArrow(
            koop_lab.get_bottom() + DOWN * 0.05,
            koop_note.get_left() + RIGHT *3 + UP * 0.07,
            color=orange_bg, stroke_width=3, angle=-TAU / 7,
            tip_length=0.2,
        )
        self.play(Create(koop_arrow2), run_time=0.9)
        koop_note_arr = Arrow(
            koop_note.get_right()+LEFT * 3 + UP * 0.05, phi_y.get_bottom() + DOWN * 0.1,
            color=orange_bg, buff=0.1, stroke_width=2.5,
            max_tip_length_to_length_ratio=0.15,
        )
        self.play(Write(koop_note), GrowArrow(koop_note_arr), run_time=0.8)
        self.wait(2.0)

        fig_group = VGroup(
            left_group, x_n, right_group, y_n, top_arrow, top_arrow_lab,
            obs_arrow_l, obs_l_lab, obs_arrow_r, obs_r_lab,
            phi_x, phi_x_lab, phi_y, phi_y_lab,
            koop_lab, koop_arrow, koop_note, koop_note_arr,
            koop_arrow2
        )
        self.play(FadeOut(fig_group), run_time=0.8)
        self.wait(0.3)

        # ============================================================
        # Part 3: 辞書と辞書ベクトル
        # ============================================================
        subtitle3 = Text("観測関数を基底で書き直す：辞書と辞書ベクトル", font_size=27, color=TEAL)
        subtitle3.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle3), run_time=0.5)
        self.wait(0.3)

        dict1 = Text(
            "2部と同じ要領で、観測関数 ϕ(𝐱) に適当な基底関数を設定し、",
            color=WHITE, font_size=26,
        )
        dict1.shift(UP * 1.9)
        dict2 = Text(
            "その線形結合で ϕ(𝐱) を書き直す",
            color=WHITE, font_size=26,
        )
        dict2.next_to(dict1, DOWN, buff=0.2)
        self.play(Write(dict1), run_time=0.7)
        self.play(Write(dict2), run_time=0.6)
        self.wait(0.3)

        dict3 = VGroup(
            Text("この基底の集まりを", color=WHITE, font_size=26),
            Text("辞書", color=GOLD, font_size=26, weight=BOLD),
            Text("、辞書と状態量から作るベクトルを", color=WHITE, font_size=26),
            Text("辞書ベクトル", color=GOLD, font_size=26, weight=BOLD),
            Text("と呼ぶ", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.08)
        if dict3.width > config.frame_width - 0.8:
            dict3.scale_to_fit_width(config.frame_width - 0.8)
        dict3.shift(UP * 0.75)
        self.play(Write(dict3), run_time=0.9)
        self.wait(0.3)

        dict_ex_lab = Text("例：単項式辞書による辞書ベクトル", color=BLUE, font_size=24)
        # dict_ex_lab.shift(DOWN * 0.3)
        psi_vec = MathTex(
            r"\boldsymbol{\psi}(\boldsymbol{x}) = "
            r"\begin{bmatrix} 1 \\ x_1 \\ x_2 \\ x_1^2 \\ x_1 x_2 \\ x_2^2 \\ \vdots \end{bmatrix}",
            font_size=34, color=WHITE,
        )
        psi_vec.next_to(dict_ex_lab, DOWN, buff=0.3)
        self.play(Write(dict_ex_lab), run_time=0.5)
        self.play(Write(psi_vec), run_time=1.0)
        self.wait(1.8)

        self.play(
            FadeOut(dict1), FadeOut(dict2), FadeOut(dict3),
            FadeOut(dict_ex_lab), FadeOut(psi_vec),
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: 観測関数を係数ベクトルと辞書ベクトルの内積で表す
        # ============================================================
        subtitle4 = Text("観測関数を『係数ベクトル × 辞書ベクトル』で表す", font_size=27, color=ORANGE)
        subtitle4.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle4), run_time=0.5)
        self.wait(0.3)

        iso1 = Text(
            "2部で学んだ通り、基底を設定すれば係数ベクトル空間と関数空間が全単射で結ばれ、",
            color=WHITE, font_size=24,
        )
        iso1.shift(UP * 1.9)
        if iso1.width > config.frame_width - 0.8:
            iso1.scale_to_fit_width(config.frame_width - 0.8)
        iso2 = Text(
            "議論をベクトル空間に持ち込める",
            color=WHITE, font_size=24,
        )
        iso2.next_to(iso1, DOWN, buff=0.2)
        self.play(Write(iso1), run_time=0.8)
        self.play(Write(iso2), run_time=0.5)
        self.wait(0.3)

        now_eq = MathTex(
            r"\phi(\boldsymbol{x}) = x_1 = 0 \times 1 + 1 \times x_1 + 0 \times x_2 "
            r"+ 0 \times x_1^2 + \dots = \boldsymbol{c}_{\mathrm{ini}}^{\top}\, \boldsymbol{\psi}(\boldsymbol{x})",
            font_size=36, color=WHITE,
        )
        now_lab = Text("現在時刻の観測関数", color=BLUE, font_size=24)
        now_group = VGroup(now_lab, now_eq).arrange(DOWN, buff=0.22)
        if now_eq.width > config.frame_width - 0.8:
            now_group.scale_to_fit_width(config.frame_width - 0.8)
        # now_group.shift(UP * 0.5)
        self.play(Write(now_lab), run_time=0.4)
        self.play(Write(now_eq), run_time=1.1)
        self.wait(0.4)

        fut_eq = MathTex(
            r"(\mathcal{K}\phi)(\boldsymbol{x}) = c_0 \times 1 + c_1 \times x_1 "
            r"+ c_2 \times x_2 + c_3 \times x_1^2 + \dots = \boldsymbol{c}^{\top}\, \boldsymbol{\psi}(\boldsymbol{x})",
            font_size=36, color=WHITE,
        )
        fut_lab = Text("時間発展後の観測関数", color=RED, font_size=24)
        fut_group = VGroup(fut_lab, fut_eq).arrange(DOWN, buff=0.22)
        if fut_eq.width > config.frame_width - 0.8:
            fut_group.scale_to_fit_width(config.frame_width - 0.8)
        fut_group.shift(DOWN * 1.6)
        self.play(Write(fut_lab), run_time=0.4)
        self.play(Write(fut_eq), run_time=1.1)
        self.wait(1.8)

        self.play(
            FadeOut(iso1), FadeOut(iso2),
            FadeOut(now_lab), FadeOut(now_eq),
            FadeOut(fut_lab), FadeOut(fut_eq),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: 求めたい線形写像 K
        # ============================================================
        subtitle5 = Text("求めたいのは係数ベクトルを写す線形写像 K", font_size=27, color=YELLOW)
        subtitle5.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle5), run_time=0.5)
        self.wait(0.3)

        k_intro = Text(
            "2つの式を眺めると、求めたいのは次の関係を満たす線形写像 K だと分かる",
            color=WHITE, font_size=25,
        )
        k_intro.shift(UP * 1.8)
        if k_intro.width > config.frame_width - 0.8:
            k_intro.scale_to_fit_width(config.frame_width - 0.8)
        self.play(Write(k_intro), run_time=0.8)
        self.wait(0.3)

        k_eq = MathTex(
            r"\boldsymbol{c} = K\, \boldsymbol{c}_{\mathrm{ini}}",
            font_size=52, color=YELLOW,
        )
        k_eq.shift(UP * 0.4)
        k_box = SurroundingRectangle(k_eq, color=YELLOW, buff=0.25)
        self.play(Write(k_eq), Create(k_box), run_time=0.9)
        self.wait(0.4)

        k_caution = Text(
            "※ 本来は無限個の線形結合で表される関数を、",
            color=GRAY, font_size=24,
        )
        k_caution2 = Text(
            "有限のベクトルと行列で扱うには、どこかで和を打ち切る必要があり、",
            color=GRAY, font_size=24,
        )
        k_caution3 = VGroup(
            Text("K は", color=GRAY, font_size=24),
            Text("近似", color=ORANGE, font_size=24, weight=BOLD),
            Text("になる点に注意", color=GRAY, font_size=24),
        ).arrange(RIGHT, buff=0.1)
        k_cautions = VGroup(k_caution, k_caution2, k_caution3).arrange(
            DOWN, aligned_edge=LEFT, buff=0.22)
        k_cautions.shift(DOWN * 1.6)
        for c in k_cautions:
            self.play(Write(c), run_time=0.6)
        self.wait(1.8)

        self.play(
            FadeOut(k_intro), FadeOut(k_eq), FadeOut(k_box),
            FadeOut(k_cautions),
        )
        self.wait(0.3)

        # ============================================================
        # Part 6: どうやって K を得るか — 作用素は関数にのみ作用
        # ============================================================
        subtitle6 = Text("どうやって K を得るか：作用素は関数にのみ作用する", font_size=27, color=PURPLE)
        subtitle6.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle6), run_time=0.5)
        self.wait(0.3)

        how1 = Text(
            "作用素の性質を思い出すと、作用素は『関数』にしか作用しない",
            color=WHITE, font_size=26,
        )
        how1.shift(UP * 1.9)
        self.play(Write(how1), run_time=0.8)
        self.wait(0.3)

        how_eq = MathTex(
            r"(\mathcal{K}\phi)(\boldsymbol{x})",
            r"= \mathcal{K}\!\left( \sum_{m=1}^{M} c_{\mathrm{ini}, m}\, \psi_m(\boldsymbol{x}) \right)",
            r"= \sum_{m=1}^{M} c_{\mathrm{ini}, m}\, \bigl((\mathcal{K}\psi_m)(\boldsymbol{x})\bigr)",
            font_size=36, color=WHITE,
        )
        if how_eq.width > config.frame_width - 0.8:
            how_eq.scale_to_fit_width(config.frame_width - 0.8)
        how_eq.shift(UP * 0.7)
        self.play(Write(how_eq), run_time=1.3)
        self.wait(0.4)

        how_ann = Text(
            "時間発展前の係数は素通りし、作用素は辞書関数のみに作用する",
            color=GOLD, font_size=25, weight=BOLD,
        )
        how_ann.shift(DOWN * 0.4)
        how_ann_box = SurroundingRectangle(how_ann, color=YELLOW, buff=0.2)
        self.play(Write(how_ann), Create(how_ann_box), run_time=0.9)
        self.wait(0.3)

        how_concl = Text(
            "→ 𝒦 は辞書関数しか時間発展させないので、",
            color=WHITE, font_size=25,
        )
        how_concl2 = Text(
            "辞書関数の空間でデータから回帰すればよい",
            color=TEAL, font_size=26, weight=BOLD,
        )
        how_concls = VGroup(how_concl, how_concl2).arrange(
            DOWN, aligned_edge=LEFT, buff=0.25)
        how_concls.shift(DOWN * 1.7)
        self.play(Write(how_concl), run_time=0.7)
        self.play(Write(how_concl2), run_time=0.7)
        self.wait(1.8)

        self.play(
            FadeOut(how1), FadeOut(how_eq),
            FadeOut(how_ann), FadeOut(how_ann_box),
            FadeOut(how_concls),
        )
        self.wait(0.3)

        # ============================================================
        # Part 7: 辞書関数を M 個で打ち切った行列変換
        # ============================================================
        subtitle7 = Text("辞書関数を M 個で打ち切り、行列変換に落とす", font_size=27, color=GOLD)
        subtitle7.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle7), run_time=0.5)
        self.wait(0.3)

        tr1 = Text(
            "計算のため辞書関数を M 個で打ち切って近似する",
            color=WHITE, font_size=26,
        )
        tr1.shift(UP * 1.9)
        tr2 = Text(
            "飛ばされた先の空間も辞書関数を基底とするので、辞書関数の線形結合で表せる",
            color=WHITE, font_size=24,
        )
        tr2.next_to(tr1, DOWN, buff=0.2)
        if tr2.width > config.frame_width - 0.8:
            tr2.scale_to_fit_width(config.frame_width - 0.8)
        self.play(Write(tr1), run_time=0.7)
        self.play(Write(tr2), run_time=0.8)
        self.wait(0.3)

        tr_eq = MathTex(
            r"\begin{bmatrix} \psi_1(\boldsymbol{y}_n) \\ \psi_2(\boldsymbol{y}_n) \\ \vdots \\ \psi_M(\boldsymbol{y}_n) \end{bmatrix}"
            r"\simeq"
            r"\begin{bmatrix} K_{11} & K_{12} & \dots & K_{1M} \\ K_{21} & K_{22} & \dots & K_{2M} \\ \vdots & \vdots & \ddots & \vdots \\ K_{M1} & K_{M2} & \dots & K_{MM} \end{bmatrix}"
            r"\begin{bmatrix} \psi_1(\boldsymbol{x}_n) \\ \psi_2(\boldsymbol{x}_n) \\ \vdots \\ \psi_M(\boldsymbol{x}_n) \end{bmatrix}",
            font_size=36, color=WHITE,
        )
        if tr_eq.width > config.frame_width - 0.8:
            tr_eq.scale_to_fit_width(config.frame_width - 0.8)
        tr_eq.shift(DOWN * 0.3)
        self.play(Write(tr_eq), run_time=1.5)
        self.wait(0.4)

        tr_concl = VGroup(
            Text("この", color=WHITE, font_size=26),
            MathTex(r"K_{mm'}", color=YELLOW, font_size=32),
            Text("を並べた行列こそが、求めたい", color=WHITE, font_size=26),
            Text("クープマン行列", color=YELLOW, font_size=26, weight=BOLD),
        ).arrange(RIGHT, buff=0.12)
        tr_concl.shift(DOWN * 2.6)
        self.play(Write(tr_concl), run_time=0.9)
        self.wait(1.8)

        self.play(
            FadeOut(tr1), FadeOut(tr2), FadeOut(tr_eq), FadeOut(tr_concl),
        )
        self.wait(0.3)

        # ============================================================
        # Part 8: 学習データによるフィッティング問題
        # ============================================================
        subtitle8 = Text("学習データによるフィッティング問題へ", font_size=28, color=BLUE)
        subtitle8.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle8), run_time=0.5)
        self.wait(0.3)

        fit1 = Text(
            "手元に N 個のスナップショットペア学習データがあるなら、",
            color=WHITE, font_size=26,
        )
        fit1.shift(UP * 1.9)
        fit2 = Text(
            "次を最もよく満たす K をフィッティングで求める問題になる",
            color=WHITE, font_size=26,
        )
        fit2.next_to(fit1, DOWN, buff=0.2)
        self.play(Write(fit1), run_time=0.7)
        self.play(Write(fit2), run_time=0.7)
        self.wait(0.3)

        fit_eq = MathTex(
            r"\boldsymbol{\psi}(\boldsymbol{y}_n) \simeq K\, \boldsymbol{\psi}(\boldsymbol{x}_n)"
            r"\qquad (n = 1, 2, \dots, N)",
            font_size=40, color=YELLOW,
        )
        if fit_eq.width > config.frame_width - 0.8:
            fit_eq.scale_to_fit_width(config.frame_width - 0.8)
        fit_eq.shift(UP * 0.5)
        self.play(Write(fit_eq), run_time=1.0)
        self.wait(0.4)

        fit3 = Text(
            "最小二乗法で解くなら、コスト関数 J は",
            color=WHITE, font_size=26,
        )
        fit3.shift(DOWN * 0.4)
        self.play(Write(fit3), run_time=0.6)

        cost_eq = MathTex(
            r"J(K) = \sum_{n=1}^{N} \left\| \boldsymbol{\psi}(\boldsymbol{y}_n) "
            r"- K\, \boldsymbol{\psi}(\boldsymbol{x}_n) \right\|^2",
            font_size=40, color=WHITE,
        )
        if cost_eq.width > config.frame_width - 0.8:
            cost_eq.scale_to_fit_width(config.frame_width - 0.8)
        cost_eq.shift(DOWN * 1.6)
        cost_box = SurroundingRectangle(cost_eq, color=YELLOW, buff=0.22)
        self.play(Write(cost_eq), Create(cost_box), run_time=1.0)
        self.wait(0.3)

        fit4 = Text(
            "これを最小化する K が、データから推定したクープマン行列",
            color=GOLD, font_size=24, weight=BOLD,
        )
        fit4.shift(DOWN * 2.8)
        self.play(Write(fit4), run_time=0.8)
        self.wait(1.8)

        self.play(
            FadeOut(fit1), FadeOut(fit2), FadeOut(fit_eq),
            FadeOut(fit3), FadeOut(cost_eq), FadeOut(cost_box), FadeOut(fit4),
        )
        self.wait(0.3)

        # ============================================================
        # Part 9: クープマン行列を使う利点
        # ============================================================
        subtitle9 = Text("クープマン行列を使う利点", font_size=28, color=TEAL)
        subtitle9.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle9), run_time=0.5)
        self.wait(0.3)

        adv1 = Text(
            "→最終的に欲しい物までの操作を線形計算でショートカットできる幅が大きい",
            color=GOLD, font_size=25, weight=BOLD,
        )
        adv1.shift(UP * 1.9)
        if adv1.width > config.frame_width - 0.8:
            adv1.scale_to_fit_width(config.frame_width - 0.8)
        self.play(Write(adv1), run_time=0.8)
        self.wait(0.3)

        # クープマン側
        koop_box = RoundedRectangle(
            width=6.0, height=2.0, corner_radius=0.15,
            fill_color="#1a3a2a", fill_opacity=1.0, stroke_color=RED, stroke_width=2,
        )
        koop_title = Text("クープマン作用素", color=RED, font_size=24, weight=BOLD)
        koop_body = VGroup(
            MathTex(r"\boldsymbol{c}_{\mathrm{ini}} \;\xrightarrow{\;\times K\;}\; \boldsymbol{c}",
                    color=WHITE, font_size=34),
            Text("K を掛けるだけで、時間遷移後の", color=WHITE, font_size=20),
            Text("観測量の係数ベクトルが直接得られる", color=WHITE, font_size=20),
        ).arrange(DOWN, buff=0.18)
        koop_content = VGroup(koop_title, koop_body).arrange(DOWN, buff=0.25)
        koop_content.move_to(koop_box)
        koop_panel = VGroup(koop_box, koop_content)
        koop_panel.shift(LEFT * 3.3 + DOWN * 0.6)

        # ペロン・フロベニウス側
        pf_box = RoundedRectangle(
            width=6.0, height=2.0, corner_radius=0.15,
            fill_color="#2a2416", fill_opacity=1.0, stroke_color=BLUE, stroke_width=2,
        )
        pf_title = Text("ペロン・フロベニウス作用素", color=BLUE, font_size=24, weight=BOLD)
        pf_body = VGroup(
            Text("表現行列で線形計算しても、得られるのは", color=WHITE, font_size=20),
            Text("確率密度関数の時間発展", color=GOLD, font_size=20, weight=BOLD),
            Text("欲しい物まで、さらに数段階の計算が要る", color=WHITE, font_size=20),
        ).arrange(DOWN, buff=0.18)
        pf_content = VGroup(pf_title, pf_body).arrange(DOWN, buff=0.25)
        pf_content.move_to(pf_box)
        pf_panel = VGroup(pf_box, pf_content)
        pf_panel.shift(RIGHT * 3.3 + DOWN * 0.6)

        self.play(FadeIn(koop_panel), run_time=0.8)
        self.wait(0.3)
        self.play(FadeIn(pf_panel), run_time=0.8)
        self.wait(0.4)

        vs = Text("vs", color=WHITE, font_size=30, weight=BOLD)
        vs.move_to(ORIGIN + DOWN * 0.6)
        self.play(FadeIn(vs, scale=1.5), run_time=0.4)
        self.wait(1.8)

        self.play(
            FadeOut(adv1), FadeOut(koop_panel), FadeOut(pf_panel), FadeOut(vs),
        )
        self.wait(0.3)

        # ============================================================
        # Part 10: まとめ
        # ============================================================
        subtitle10 = Text("まとめ", font_size=34, color=TEAL)
        subtitle10.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle10), run_time=0.6)
        self.wait(0.3)

        summary = VGroup(
            Text("• クープマン作用素 𝒦：ペロン・フロベニウス作用素の随伴作用素",
                 color=WHITE, font_size=25),
            Text("• 観測関数 ϕ を辞書（基底）の線形結合で表し、ϕ = 𝐜ᵀ𝛙(𝐱) とする",
                 color=WHITE, font_size=25),
            Text("• 求めたいのは係数を写す線形写像：𝐜 = K 𝐜_ini（有限打ち切りで近似）",
                 color=WHITE, font_size=25),
            Text("• 作用素は辞書関数にのみ作用 → 辞書関数の空間で回帰すればよい",
                 color=WHITE, font_size=25),
            Text("• N個のペアで 𝛙(𝐲_n) ≃ K 𝛙(𝐱_n) を最小二乗フィッティング",
                 color=WHITE, font_size=25),
            Text("• 利点：K を掛けるだけで観測量の時間遷移を線形にショートカットできる",
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
