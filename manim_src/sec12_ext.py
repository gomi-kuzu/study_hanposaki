from manim import *
import numpy as np

class LaplaceTransform(Scene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"

        # タイトル
        title = Text("【おまけ】ラプラス変換", font_size=34, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)

        # === Part 1: 導入 ===
        subtitle1 = Text("フーリエ変換に似た変換", font_size=30, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.5)

        recall_text = VGroup(
            Text("フーリエ変換は信号を「周波数成分」に分解する", color=WHITE, font_size=24),
        ).arrange(DOWN, buff=0.2)
        recall_text.shift(UP * 1.4)
        self.play(Write(recall_text), run_time=0.7)
        self.wait(0.4)

        ft_formula = MathTex(
            r"F(\omega) = \int_{-\infty}^{\infty} f(t) \, e^{-j\omega t} \, dt",
            color=TEAL, font_size=30
        )
        ft_formula.shift(UP * 0.4)
        ft_box = SurroundingRectangle(ft_formula, color=TEAL, buff=0.15)
        self.play(Write(ft_formula), Create(ft_box), run_time=0.8)
        self.wait(0.5)

        intro_note = VGroup(
            Text("実は、フーリエ変換によく似た変換が他にもある…", color=ORANGE, font_size=24),
            Text("それは「ラプラス変換」", color=YELLOW, font_size=28, weight=BOLD),
        ).arrange(DOWN, buff=0.2)
        intro_note.shift(DOWN * 1.2)
        self.play(Write(intro_note), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(recall_text), FadeOut(ft_formula), FadeOut(ft_box),
            FadeOut(intro_note), FadeOut(subtitle1)
        )
        self.wait(0.3)

        # === Part 2: ラプラス変換の定義式 ===
        subtitle2 = Text("ラプラス変換の定義", font_size=30, color=GREEN)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)

        def_intro = Text("ラプラス変換の定義式:", color=YELLOW, font_size=24, weight=BOLD)
        def_intro.shift(UP * 1.8 + LEFT * 3.5)
        self.play(Write(def_intro), run_time=0.5)

        laplace_formula = MathTex(
            r"\mathcal{L}[f(t)] = F(s) = \int_0^{\infty} f(t) \, e^{-st} \, dt",
            color=YELLOW, font_size=32
        )
        laplace_formula.shift(UP * 0.9)
        laplace_box = SurroundingRectangle(laplace_formula, color=YELLOW, buff=0.2)
        self.play(Write(laplace_formula), Create(laplace_box), run_time=0.9)
        self.wait(0.5)

        s_note = VGroup(
            Text("ただしsは複素数", color=WHITE, font_size=24),
            MathTex(r"(s = \sigma + j\omega)", color=WHITE, font_size=30),
        ).arrange(RIGHT, buff=0.2)
        s_note.shift(UP * 0.1)
        self.play(Write(s_note), run_time=0.6)
        self.wait(0.5)

        # フーリエ変換と比較
        compare_title = Text("フーリエ変換と比べてみると…", color=WHITE, font_size=22)
        compare_title.shift(DOWN * 0.6)
        self.play(Write(compare_title), run_time=0.5)
        self.wait(0.3)

        ft_compare = VGroup(
            # Text("フーリエ変換:", color=TEAL, font_size=24, weight=BOLD),
            MathTex(r"F(\omega) = \int_{-\infty}^{\infty} f(t) e^{-j\omega t} dt", color=TEAL, font_size=28),
        ).arrange(DOWN, buff=0.2)
        ft_compare.shift(DOWN * 1.3)
        self.play(Write(ft_compare), run_time=0.8)
        self.wait(0.6)

        # 違いを強調
        diff_group = VGroup(
            Text("違い①: 積分区間が 0 から ∞（過去の時間は考えない）", color=WHITE, font_size=21),
            VGroup(
                Text("違い②: e の肩が ", color=WHITE, font_size=21),
                MathTex(r"-j\omega t", color=WHITE, font_size=26),
                Text(" →  ", color=WHITE, font_size=21),
                MathTex(r"-st = -(\sigma + j\omega)t", color=WHITE, font_size=26),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        diff_group.shift(DOWN * 2.1)
        self.play(Write(diff_group), run_time=0.7)
        self.wait(0.3)

        diff3 = Text("共通点: 信号を別の空間の基底で分解している！", color=GREEN, font_size=21, weight=BOLD)
        diff3.shift(DOWN * 2.8)
        self.play(Write(diff3), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(def_intro), FadeOut(laplace_formula), FadeOut(laplace_box),
            FadeOut(s_note), FadeOut(compare_title), FadeOut(ft_compare),
            FadeOut(diff_group), FadeOut(diff3),
            FadeOut(subtitle2)
        )
        self.wait(0.3)

        # === Part 3: ラプラス変換の基底を分解する ===
        subtitle3 = Text("ラプラス変換はどんな成分に分解するか", font_size=28, color=ORANGE)
        subtitle3.next_to(title, DOWN)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.5)

        basis_intro = Text("ラプラス変換の基底を見てみよう:", color=WHITE, font_size=26)
        basis_intro.shift(UP * 1.6)
        self.play(Write(basis_intro), run_time=0.6)
        self.wait(0.3)

        kernel_formula = MathTex(
            r"e^{-st} = e^{-(\sigma + j\omega)t} = e^{-\sigma t} \cdot e^{-j\omega t}",
            color=YELLOW, font_size=32
        )
        kernel_formula.shift(UP * 0.9)
        kernel_box = SurroundingRectangle(kernel_formula, color=YELLOW, buff=0.15)
        self.play(Write(kernel_formula), Create(kernel_box), run_time=0.9)
        self.wait(0.5)

        # 2つの成分に分解して説明
        comp1 = VGroup(
            MathTex(r"e^{-j\omega t}", color=TEAL, font_size=32),
            Text(": 振動成分", color=TEAL, font_size=26, weight=BOLD),
            Text("（フーリエ変換と同様）", color=GRAY, font_size=20),
        ).arrange(RIGHT, buff=0.2)
        comp1.shift(UP * 0.1)
        self.play(Write(comp1), run_time=0.6)
        self.wait(0.3)

        comp1_detail = Text("→ どのくらい強い振動成分があるかがわかる", color=TEAL, font_size=26)
        comp1_detail.shift(DOWN * 0.4)
        self.play(Write(comp1_detail), run_time=0.5)
        self.wait(0.3)

        comp2 = VGroup(
            MathTex(r"e^{-\sigma t}", color=ORANGE, font_size=32),
            Text(": 減衰・発散成分", color=ORANGE, font_size=26, weight=BOLD),
            Text("（新たに加わった項）", color=GRAY, font_size=20),
        ).arrange(RIGHT, buff=0.2)
        comp2.shift(DOWN * 1.0)
        self.play(Write(comp2), run_time=0.6)
        self.wait(0.3)

        comp2_detail = Text("→ 信号が収束するのか発散するのかがわかる", color=ORANGE, font_size=26)
        comp2_detail.shift(DOWN * 1.5)
        self.play(Write(comp2_detail), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(basis_intro), FadeOut(kernel_formula), FadeOut(kernel_box),
            FadeOut(comp1), FadeOut(comp1_detail),
            FadeOut(comp2), FadeOut(comp2_detail),
            FadeOut(subtitle3)
        )
        self.wait(0.3)

        # === Part 4: e^{-σt} の可視化 ===
        subtitle4 = Text("減衰・発散成分のグラフ", font_size=30, color=ORANGE)
        subtitle4.next_to(title, DOWN)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.5)

        sigma_intro = VGroup(
            MathTex(r"e^{-\sigma t}", color=ORANGE, font_size=32),
            Text("の形は σ の符号で大きく変わる", color=WHITE, font_size=24),
        ).arrange(RIGHT, buff=0.2)
        sigma_intro.shift(UP * 1.8 + LEFT*1.7 )
        self.play(Write(sigma_intro), run_time=0.6)
        self.wait(0.3)

        # グラフの軸
        sigma_axes = Axes(
            x_range=[0, 4, 1],
            y_range=[-0.5, 5.5, 0.5],
            x_length=9,
            y_length=4,
            axis_config={"color": GRAY},
            x_axis_config={"include_tip": True},
            y_axis_config={"include_tip": True},
        ).scale(0.7)
        sigma_axes.shift(DOWN * 0.3 + LEFT * 1.5)

        x_label_s = MathTex(r"t", color=WHITE, font_size=22)
        x_label_s.next_to(sigma_axes.x_axis, RIGHT, buff=0.1)
        y_label_s = MathTex(r"e^{-\sigma t}", color=WHITE, font_size=22)
        y_label_s.next_to(sigma_axes.y_axis, UP, buff=0.1)

        self.play(Create(sigma_axes), Write(x_label_s), Write(y_label_s), run_time=0.6)
        self.wait(0.2)

        # σ > 0: 減衰（収束）
        decay_curve = sigma_axes.plot(
            lambda t: np.exp(-1.0 * t),
            x_range=[0, 4],
            color=BLUE, stroke_width=3
        )
        decay_label = VGroup(
            MathTex(r"\sigma > 0", color=BLUE, font_size=28),
            Text(": 減衰（収束）", color=BLUE, font_size=26),
        ).arrange(RIGHT, buff=0.1)
        decay_label.next_to(sigma_axes, RIGHT, buff=0.2).shift(UP * 1.2)

        self.play(Create(decay_curve), Write(decay_label), run_time=0.8)
        self.wait(0.3)

        decay_note = Text("→ 信号はいずれ0に収束する", color=BLUE, font_size=22)
        decay_note.next_to(sigma_axes, RIGHT, buff=0.2).shift(UP * 0.6)
        self.play(Write(decay_note), run_time=0.5)
        self.wait(0.5)

        # σ = 0: 定常
        flat_curve = sigma_axes.plot(
            lambda t: 1.0,
            x_range=[0, 4],
            color=GREEN, stroke_width=3
        )
        flat_label = VGroup(
            MathTex(r"\sigma = 0", color=GREEN, font_size=28),
            Text(": 定常（フーリエと同じ）", color=GREEN, font_size=26),
        ).arrange(RIGHT, buff=0.1)
        flat_label.next_to(sigma_axes, RIGHT, buff=0.2).shift(UP * 0.0)

        self.play(Create(flat_curve), Write(flat_label), run_time=0.8)
        self.wait(0.3)

        flat_note = Text("→ 振幅変化なし", color=GREEN, font_size=22)
        flat_note.next_to(sigma_axes, RIGHT, buff=0.2).shift(DOWN * 0.6)
        self.play(Write(flat_note), run_time=0.5)
        self.wait(0.5)

        # σ < 0: 発散
        grow_curve = sigma_axes.plot(
            lambda t: np.exp(0.5 * t),
            x_range=[0, 4],
            color=RED, stroke_width=3
        )
        grow_label = VGroup(
            MathTex(r"\sigma < 0", color=RED, font_size=28),
            Text(": 発散", color=RED, font_size=26),
        ).arrange(RIGHT, buff=0.1)
        grow_label.next_to(sigma_axes, RIGHT, buff=0.2).shift(DOWN * 1.2)

        self.play(Create(grow_curve), Write(grow_label), run_time=0.8)
        self.wait(0.3)

        grow_note = Text("→ 信号は時間とともに大きくなる", color=RED, font_size=22)
        grow_note.next_to(sigma_axes, RIGHT, buff=0.2).shift(DOWN * 1.8)
        self.play(Write(grow_note), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(sigma_intro),
            FadeOut(sigma_axes), FadeOut(x_label_s), FadeOut(y_label_s),
            FadeOut(decay_curve), FadeOut(decay_label), FadeOut(decay_note),
            FadeOut(flat_curve), FadeOut(flat_label), FadeOut(flat_note),
            FadeOut(grow_curve), FadeOut(grow_label), FadeOut(grow_note),
            FadeOut(subtitle4)
        )
        self.wait(0.3)

        # === Part 5: 振動と減衰の組み合わせ ===
        subtitle5 = Text("振動 × 減衰の組み合わせ", font_size=30, color=TEAL)
        subtitle5.next_to(title, DOWN)
        self.play(Write(subtitle5), run_time=0.6)
        self.wait(0.5)

        combo_intro = Text("実際のラプラス基底は振動成分と減衰成分の積:", color=WHITE, font_size=26)
        combo_intro.shift(UP * 1.6)
        self.play(Write(combo_intro), run_time=0.6)
        self.wait(0.3)

        combo_formula = MathTex(
            r"e^{-st} = e^{-\sigma t} \cdot e^{-j\omega t}",
            color=YELLOW, font_size=34
        )
        combo_formula.shift(UP * 1.0)
        self.play(Write(combo_formula), run_time=0.7)
        self.wait(0.3)

        # グラフ：振動しながら減衰する信号
        combo_axes = Axes(
            x_range=[0, 4 * PI, PI],
            y_range=[-1.5, 1.5, 0.5],
            x_length=10,
            y_length=3.5,
            axis_config={"color": GRAY},
            x_axis_config={"include_tip": True},
            y_axis_config={"include_tip": True},
        ).scale(0.6)
        combo_axes.shift(DOWN * 0.3)

        x_label_c = MathTex(r"t", color=WHITE, font_size=22)
        x_label_c.next_to(combo_axes.x_axis, RIGHT, buff=0.1)

        self.play(Create(combo_axes), Write(x_label_c), run_time=0.5)
        self.wait(0.1)

        # 振動のみ（フーリエ）
        osc_wave = combo_axes.plot(
            lambda t: np.cos(2 * t),
            color=TEAL, stroke_width=2
        )
        osc_label = VGroup(
            MathTex(r"e^{-j\omega t}", color=TEAL, font_size=26),
            Text(": 振動のみ（σ=0）", color=TEAL, font_size=22),
        ).arrange(RIGHT, buff=0.1)
        osc_label.next_to(combo_axes, UP, buff=0.1).shift(LEFT * 4)

        self.play(Create(osc_wave), Write(osc_label), run_time=0.8)
        self.wait(0.5)

        # 振動しながら減衰
        decay_osc_wave = combo_axes.plot(
            lambda t: np.exp(-0.3 * t) * np.cos(2 * t),
            color=ORANGE, stroke_width=3
        )
        # 上下包絡線
        envelope_upper = combo_axes.plot(
            lambda t: np.exp(-0.3 * t),
            color=RED, stroke_width=1.5
        )
        envelope_lower = combo_axes.plot(
            lambda t: -np.exp(-0.3 * t),
            color=RED, stroke_width=1.5
        )
        decay_osc_label = VGroup(
            MathTex(r"e^{-\sigma t} \cdot e^{-j\omega t}", color=ORANGE, font_size=26),
            Text(": 振動しながら減衰（σ>0）", color=ORANGE, font_size=22),
        ).arrange(RIGHT, buff=0.1)
        decay_osc_label.next_to(combo_axes, DOWN, buff=0.1).shift(LEFT * 3)

        self.play(
            Create(decay_osc_wave),
            Create(envelope_upper), Create(envelope_lower),
            Write(decay_osc_label),
            run_time=0.9
        )
        self.wait(0.5)

        combo_summary = VGroup(
            Text("ラプラス変換は", color=WHITE, font_size=24),
            Text("「振動の速さ（周波数）」", color=TEAL, font_size=24, weight=BOLD),
            Text("と", color=WHITE, font_size=24),
            Text("「収束・発散の速さ」", color=ORANGE, font_size=24, weight=BOLD),
            Text("を同時に解析！", color=YELLOW, font_size=24, weight=BOLD),
        ).arrange(RIGHT, buff=0.1)
        combo_summary.shift(DOWN * 2.8)
        combo_box = SurroundingRectangle(combo_summary, color=YELLOW, buff=0.1)
        self.play(Write(combo_summary), Create(combo_box), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(combo_intro), FadeOut(combo_formula),
            FadeOut(combo_axes), FadeOut(x_label_c),
            FadeOut(osc_wave), FadeOut(osc_label),
            FadeOut(decay_osc_wave), FadeOut(envelope_upper), FadeOut(envelope_lower),
            FadeOut(decay_osc_label),
            FadeOut(combo_summary), FadeOut(combo_box),
            FadeOut(subtitle5)
        )
        self.wait(0.3)

        # === Part 6: s 平面（複素平面）のイメージ ===
        # subtitle6 = Text("s 平面：ラプラス変換の「地図」", font_size=28, color=GOLD)
        # subtitle6.next_to(title, DOWN)
        # self.play(Write(subtitle6), run_time=0.6)
        # self.wait(0.5)

        # s_intro = VGroup(
        #     Text("複素数 s の値を平面上にプロットすると", color=WHITE, font_size=22),
        #     Text("→ s 平面（複素平面）", color=YELLOW, font_size=26, weight=BOLD),
        # ).arrange(DOWN, buff=0.2)
        # s_intro.shift(UP * 1.6)
        # self.play(Write(s_intro), run_time=0.7)
        # self.wait(0.4)

        # # s 平面の図
        # s_plane_axes = Axes(
        #     x_range=[-2.5, 2.5, 1],
        #     y_range=[-2.5, 2.5, 1],
        #     x_length=5,
        #     y_length=5,
        #     axis_config={"color": GRAY},
        #     x_axis_config={"include_tip": True},
        #     y_axis_config={"include_tip": True},
        # ).scale(0.75)
        # s_plane_axes.shift(LEFT * 2.5 + DOWN * 0.5)

        # sigma_label = MathTex(r"\sigma", color=WHITE, font_size=22)
        # sigma_label.next_to(s_plane_axes.x_axis, RIGHT, buff=0.1)
        # jomega_label = MathTex(r"j\omega", color=WHITE, font_size=22)
        # jomega_label.next_to(s_plane_axes.y_axis, UP, buff=0.1)

        # self.play(Create(s_plane_axes), Write(sigma_label), Write(jomega_label), run_time=0.6)
        # self.wait(0.2)

        # # 左半平面（安定領域）の塗りつぶし
        # stable_region = Polygon(
        #     s_plane_axes.c2p(-2.5, -2.5),
        #     s_plane_axes.c2p(0, -2.5),
        #     s_plane_axes.c2p(0, 2.5),
        #     s_plane_axes.c2p(-2.5, 2.5),
        #     color=BLUE, fill_opacity=0.2, stroke_width=0
        # )
        # unstable_region = Polygon(
        #     s_plane_axes.c2p(0, -2.5),
        #     s_plane_axes.c2p(2.5, -2.5),
        #     s_plane_axes.c2p(2.5, 2.5),
        #     s_plane_axes.c2p(0, 2.5),
        #     color=RED, fill_opacity=0.2, stroke_width=0
        # )
        # stable_text = Text("安定領域\n(σ<0)", color=BLUE, font_size=18)
        # stable_text.move_to(s_plane_axes.c2p(-1.2, 0))
        # unstable_text = Text("不安定領域\n(σ>0)", color=RED, font_size=18)
        # unstable_text.move_to(s_plane_axes.c2p(1.2, 0))

        # self.play(FadeIn(stable_region), FadeIn(unstable_region), run_time=0.6)
        # self.play(Write(stable_text), Write(unstable_text), run_time=0.6)
        # self.wait(0.3)

        # # 虚軸上の点（純粋な振動）- 複素共役ペア
        # jw_dot_upper = Dot(s_plane_axes.c2p(0, 1.5), color=GREEN, radius=0.1)
        # jw_dot_lower = Dot(s_plane_axes.c2p(0, -1.5), color=GREEN, radius=0.1)
        # jw_label = MathTex(r"s = \pm j\omega", color=GREEN, font_size=20)
        # jw_label.next_to(jw_dot_upper, RIGHT, buff=0.1)
        # jw_note = Text("純粋な振動\n(フーリエ変換)", color=GREEN, font_size=16)
        # jw_note.next_to(jw_label, RIGHT, buff=0.1)

        # self.play(FadeIn(jw_dot_upper), FadeIn(jw_dot_lower), Write(jw_label), Write(jw_note), run_time=0.7)
        # self.wait(0.3)

        # # 左半平面上の点（安定な振動）- 複素共役ペア
        # stable_dot_upper = Dot(s_plane_axes.c2p(-1, 1), color=BLUE, radius=0.1)
        # stable_dot_lower = Dot(s_plane_axes.c2p(-1, -1), color=BLUE, radius=0.1)
        # stable_s_label = MathTex(r"s = -1 \pm j", color=BLUE, font_size=18)
        # stable_s_label.next_to(stable_dot_upper, LEFT, buff=0.05)
        # stable_s_note = Text("減衰振動\n（安定）", color=BLUE, font_size=14)
        # stable_s_note.next_to(stable_s_label, DOWN, buff=0.05)

        # self.play(FadeIn(stable_dot_upper), FadeIn(stable_dot_lower), Write(stable_s_label), Write(stable_s_note), run_time=0.6)
        # self.wait(0.3)

        # # 右半平面上の点（不安定な振動）- 複素共役ペア
        # unstable_dot_upper = Dot(s_plane_axes.c2p(1, 1), color=RED, radius=0.1)
        # unstable_dot_lower = Dot(s_plane_axes.c2p(1, -1), color=RED, radius=0.1)
        # unstable_s_label = MathTex(r"s = 1 \pm j", color=RED, font_size=18)
        # unstable_s_label.next_to(unstable_dot_upper, RIGHT, buff=0.05)
        # unstable_s_note = Text("発散振動\n（不安定）", color=RED, font_size=14)
        # unstable_s_note.next_to(unstable_s_label, DOWN, buff=0.05)

        # self.play(FadeIn(unstable_dot_upper), FadeIn(unstable_dot_lower), Write(unstable_s_label), Write(unstable_s_note), run_time=0.6)
        # self.wait(0.5)

        # # 右側の説明
        # s_summary = VGroup(
        #     Text("s 平面の横軸（σ）:", color=WHITE, font_size=20, weight=BOLD),
        #     Text("信号の収束・発散の速さ", color=ORANGE, font_size=20),
        #     Text("s 平面の縦軸（ω）:", color=WHITE, font_size=20, weight=BOLD),
        #     Text("振動の速さ（周波数）", color=TEAL, font_size=20),
        # ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        # s_summary.shift(RIGHT * 3.5 + DOWN * 0.3)
        # self.play(Write(s_summary), run_time=0.8)
        # self.wait(1.5)

        # self.play(
        #     FadeOut(s_intro),
        #     FadeOut(s_plane_axes), FadeOut(sigma_label), FadeOut(jomega_label),
        #     FadeOut(stable_region), FadeOut(unstable_region),
        #     FadeOut(stable_text), FadeOut(unstable_text),
        #     FadeOut(jw_dot_upper), FadeOut(jw_dot_lower), FadeOut(jw_label), FadeOut(jw_note),
        #     FadeOut(stable_dot_upper), FadeOut(stable_dot_lower), FadeOut(stable_s_label), FadeOut(stable_s_note),
        #     FadeOut(unstable_dot_upper), FadeOut(unstable_dot_lower), FadeOut(unstable_s_label), FadeOut(unstable_s_note),
        #     FadeOut(s_summary),
        #     FadeOut(subtitle6)
        # )
        # self.wait(0.3)

        # === Part 7: 線形代数的な意味 ===
        subtitle7 = Text("線形代数的な意味", font_size=30, color=PURPLE)
        subtitle7.next_to(title, DOWN)
        self.play(Write(subtitle7), run_time=0.6)
        self.wait(0.5)

        la_intro = Text("フーリエ変換と同様に、線形代数の言葉で表すと:", color=WHITE, font_size=22)
        la_intro.shift(UP * 1.6)
        self.play(Write(la_intro), run_time=0.6)
        self.wait(0.3)

        la_points = VGroup(
            VGroup(
                Text("●", color=TEAL, font_size=22),
                Text("基底：", color=WHITE, font_size=22),
                MathTex(r"e^{-st}", color=YELLOW, font_size=28),
                Text("（振動 × 減衰の複合モード）", color=GRAY, font_size=20),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                Text("●", color=TEAL, font_size=22),
                Text("座標（スペクトル）：", color=WHITE, font_size=22),
                MathTex(r"F(s)", color=YELLOW, font_size=28),
                Text("（各モードの大きさ）", color=GRAY, font_size=20),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                Text("●", color=TEAL, font_size=22),
                Text("写像：信号 f(t) を", color=WHITE, font_size=22),
                MathTex(r"s", color=ORANGE, font_size=28),
                Text("空間（複素平面）へ射影", color=WHITE, font_size=22),
            ).arrange(RIGHT, buff=0.15),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        la_points.shift(UP * 0.4)
        self.play(Write(la_points), run_time=1.0)
        self.wait(0.6)

        # 注意書き
        caution_note = VGroup(
            Text("※ ただし、実はラプラス変換の基底はフーリエ変換のときと違って", color=GRAY, font_size=20),
            Text("直交していないので、フーリエ変換ほどきれいに分解はできない点は注意！", color=GRAY, font_size=20),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        caution_note.shift(DOWN * 1)
        self.play(Write(caution_note), run_time=0.8)
        self.wait(1.2)

        la_box_text = VGroup(
            Text("ラプラス変換 = 複素空間への写像", color=YELLOW, font_size=24, weight=BOLD),
            Text("振動モード と 減衰モード を同時に分析", color=YELLOW, font_size=24, weight=BOLD),
        ).arrange(DOWN, buff=0.15)
        la_box_text.shift(DOWN * 2.2)
        la_box = SurroundingRectangle(la_box_text, color=YELLOW, buff=0.2)
        self.play(Write(la_box_text), Create(la_box), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(la_intro), FadeOut(la_points),
            FadeOut(la_box_text), FadeOut(la_box),
            FadeOut(caution_note),
            FadeOut(subtitle7)
        )
        self.wait(0.3)

        # === Part 8: 制御工学への応用 ===
        subtitle8 = Text("制御工学での応用", font_size=30, color=RED)
        subtitle8.next_to(title, DOWN)
        self.play(Write(subtitle8), run_time=0.6)
        self.wait(0.5)

        ctrl_intro = VGroup(
            Text("制御工学では系の入出力の関係を", color=WHITE, font_size=24),
            Text("「伝達関数」", color=YELLOW, font_size=26, weight=BOLD),
            Text("として表す", color=WHITE, font_size=24),
        ).arrange(RIGHT, buff=0.15)
        ctrl_intro.shift(UP * 1.7)
        self.play(Write(ctrl_intro), run_time=0.7)
        self.wait(0.4)

        tf_formula = VGroup(
            MathTex(r"G(s) = \frac{Y(s)}{U(s)}", color=TEAL, font_size=30),
            VGroup(
                Text("=", color=TEAL, font_size=26),
                VGroup(
                    Text("出力のラプラス変換", color=TEAL, font_size=20),
                    Line(LEFT * 1.3, RIGHT * 1.3, color=TEAL, stroke_width=1.5),
                    Text("入力のラプラス変換", color=TEAL, font_size=20),
                ).arrange(DOWN, buff=0.1),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(RIGHT, buff=0.3)
        tf_formula.shift(UP * 0.9)
        tf_box = SurroundingRectangle(tf_formula, color=TEAL, buff=0.15)
        self.play(Write(tf_formula), Create(tf_box), run_time=0.8)
        self.wait(0.5)

        # 極（pole）の説明
        pole_intro = Text("伝達関数の「極（pole）」= G(s) が無限大になる s の値", color=ORANGE, font_size=21)
        pole_intro.shift(UP * 0.1)
        self.play(Write(pole_intro), run_time=0.6)
        self.wait(0.3)

        pole_detail = VGroup(
            VGroup(
                Text("全極が左半平面（σ<0）", color=BLUE, font_size=21, weight=BOLD),
                Text("→ 出力が収束 →", color=WHITE, font_size=21),
                Text("漸近安定", color=BLUE, font_size=23, weight=BOLD),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("極が虚軸上（σ=0）", color=GREEN, font_size=21, weight=BOLD),
                Text("→ 振動が持続 →", color=WHITE, font_size=21),
                Text("限界安定", color=GREEN, font_size=23, weight=BOLD),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("極が右半平面（σ>0）", color=RED, font_size=21, weight=BOLD),
                Text("→ 出力が発散 →", color=WHITE, font_size=21),
                Text("不安定", color=RED, font_size=23, weight=BOLD),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("極の虚部（ω）が大きい", color=TEAL, font_size=21, weight=BOLD),
                Text("→", color=WHITE, font_size=21),
                Text("振動しやすい", color=TEAL, font_size=23, weight=BOLD),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        pole_detail.shift(DOWN * 1.3)

        for line in pole_detail:
            self.play(Write(line), run_time=0.6)
            self.wait(0.2)
        self.wait(0.5)

        ctrl_summary = Text("→ 極の位置を見るだけでシステムの安定性・振動性がわかる！", color=YELLOW, font_size=21, weight=BOLD)
        ctrl_summary.shift(DOWN * 2.8)
        ctrl_box = SurroundingRectangle(ctrl_summary, color=YELLOW, buff=0.1)
        self.play(Write(ctrl_summary), Create(ctrl_box), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(ctrl_intro), FadeOut(tf_formula), FadeOut(tf_box),
            FadeOut(pole_intro), FadeOut(pole_detail),
            FadeOut(ctrl_summary), FadeOut(ctrl_box),
            FadeOut(subtitle8)
        )
        self.wait(0.3)

        # === まとめ ===
        # subtitle_end = Text("まとめ", font_size=36, color=GOLD, weight=BOLD)
        # subtitle_end.next_to(title, DOWN)
        # self.play(Write(subtitle_end), run_time=0.7)
        # self.wait(0.5)

        # summary = VGroup(
        #     VGroup(
        #         Text("1.", color=WHITE, font_size=24, weight=BOLD),
        #         VGroup(
        #             Text("ラプラス変換はフーリエ変換の拡張", color=WHITE, font_size=24),
        #             MathTex(
        #                 r"\mathcal{L}[f] = \int_0^\infty f(t) e^{-st} dt \quad (s = \sigma + j\omega)",
        #                 color=TEAL, font_size=22
        #             ),
        #         ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
        #     ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        #     VGroup(
        #         Text("2.", color=WHITE, font_size=24, weight=BOLD),
        #         VGroup(
        #             Text("基底は振動 × 減衰の複合モード", color=WHITE, font_size=24),
        #             MathTex(r"e^{-st} = e^{-\sigma t} \cdot e^{-j\omega t}", color=YELLOW, font_size=22),
        #         ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
        #     ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        #     VGroup(
        #         Text("3.", color=WHITE, font_size=24, weight=BOLD),
        #         VGroup(
        #             Text("線形代数的には複素空間への基底分解", color=WHITE, font_size=24),
        #             Text("振動モードと減衰モードを同時に解析", color=ORANGE, font_size=22),
        #         ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
        #     ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        #     VGroup(
        #         Text("4.", color=WHITE, font_size=24, weight=BOLD),
        #         VGroup(
        #             Text("制御工学：極の位置でシステムの安定性を判定", color=WHITE, font_size=24),
        #             VGroup(
        #                 Text("左半平面 → 安定", color=BLUE, font_size=22),
        #                 Text("／", color=WHITE, font_size=22),
        #                 Text("右半平面 → 不安定", color=RED, font_size=22),
        #             ).arrange(RIGHT, buff=0.2),
        #         ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
        #     ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        # ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        # summary.scale(0.85)
        # summary.shift(UP * 0.1)

        # for point in summary:
        #     self.play(Write(point), run_time=0.7)
        #     self.wait(0.3)

        # self.wait(1.5)

        # all_final = VGroup(summary, subtitle_end, title)
        # self.play(FadeOut(all_final), run_time=1.0)
        # self.wait(0.5)

        self.play(FadeOut(title), run_time=1.0)
