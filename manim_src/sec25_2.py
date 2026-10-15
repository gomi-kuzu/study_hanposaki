from manim import *
import numpy as np


class AdjointOperatorIntro(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        title = Text("随伴作用素とは", font_size=38, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)

        # ============================================================
        # Part 1: 導入 — 前回の復習と今回の目標
        # ============================================================
        subtitle = Text("導入：少し先の未来の観測値をどう求めるか", font_size=27, color=BLUE)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle), run_time=0.6)
        self.wait(0.3)

        intro1 = Text(
            "前の動画ではスナップショットペア間の予測問題を定義した",
            color=WHITE, font_size=26,
        )
        intro1.shift(UP * 1.8)
        self.play(Write(intro1), run_time=0.8)
        self.wait(0.3)

        intro2 = Text(
            "この問題で求めたいのは「ある状態から時刻 t だけ遷移した状態の観測値」",
            color=GOLD, font_size=27, weight=BOLD,
        )
        intro2.shift(UP * 0.8)
        self.play(Write(intro2), run_time=0.8)
        self.wait(0.3)

        intro3 = Text(
            "今回は、その求め方を考え、重要な道具『随伴作用素』を導入する",
            color=WHITE, font_size=26,
        )
        intro3.shift(DOWN * 0.2)
        self.play(Write(intro3), run_time=0.8)
        self.wait(0.3)

        intro4 = Text(
            "※説明には前の動画と同じ状態量 𝐱 と観測関数 ϕ(𝐱)=x₁ を使う",
            color=GRAY, font_size=26,
        )
        intro4.shift(DOWN * 1.2)
        self.play(Write(intro4), run_time=0.8)
        self.wait(1.8)

        self.play(
            FadeOut(intro1), FadeOut(intro2), FadeOut(intro3), FadeOut(intro4),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: 確率表現についての注意
        # ============================================================
        subtitle2 = Text("注意：確率表現を使うが、一般性は失われない", font_size=27, color=PURPLE)
        subtitle2.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle2), run_time=0.5)
        self.wait(0.3)

        note1 = Text(
            "ここでは、状態や観測の遷移を『確率的』に表現するが、",
            color=WHITE, font_size=26,
        )
        note1.shift(UP * 1.6)
        self.play(Write(note1), run_time=0.8)
        self.wait(0.3)

        note2 = Text(
            "確定的な遷移でも、分布を一点に絞った確率的遷移の特殊系とみなせる",
            color=GOLD, font_size=26,
        )
        note2.shift(UP * 0.6)
        self.play(Write(note2), run_time=0.8)
        self.wait(0.3)

        # ポンチ絵：確率分布 → 一点集中（ディラックのデルタ）
        axes_d = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 1.2, 0.5],
            x_length=7.0,
            y_length=2.2,
            axis_config={"color": WHITE, "include_tip": False, "stroke_width": 2},
        )
        axes_d.shift(DOWN * 1.4)

        broad = axes_d.plot(
            lambda x: 0.8 * np.exp(-0.5 * (x / 1.1) ** 2),
            x_range=[-3, 3], color=BLUE, stroke_width=3,
        )
        broad_lab = Text("確率的な遷移（広い分布）", color=BLUE, font_size=22)
        broad_lab.next_to(axes_d, UP, buff=0.15).shift(LEFT * 2.2)

        spike = Arrow(
            axes_d.c2p(0.0, 0.0), axes_d.c2p(0.0, 1.1),
            color=RED, buff=0, stroke_width=6,
            max_tip_length_to_length_ratio=0.18,
        )
        spike_lab = Text("確定的な遷移（デルタ関数）", color=RED, font_size=22)
        spike_lab.next_to(axes_d, UP, buff=0.15).shift(RIGHT * 2.2)

        self.play(Create(axes_d), Create(broad), Write(broad_lab), run_time=0.8)
        self.play(ReplacementTransform(broad.copy(), spike), Write(spike_lab),
                  run_time=0.9)
        self.wait(1.8)

        self.play(
            FadeOut(note1), FadeOut(note2),
            FadeOut(axes_d), FadeOut(broad), FadeOut(broad_lab),
            FadeOut(spike), FadeOut(spike_lab),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: 期待値の定義式
        # ============================================================
        subtitle3 = Text("求めたい期待値を式変形してみる", font_size=27, color=GOLD)
        subtitle3.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle3), run_time=0.5)
        self.wait(0.3)

        exp_intro = Text(
            "初期状態 𝐱_ini から時刻 t だけ進めた観測値の期待値は、定義より：",
            color=WHITE, font_size=25,
        )
        exp_intro.shift(UP * 1.9)
        self.play(Write(exp_intro), run_time=0.8)
        self.wait(0.3)

        exp_eq = MathTex(
            r"\mathbb{E}\bigl[\phi(\mathbf{X})\bigr]_{\mathbf{X}(0)=\mathbf{x}_{\mathrm{ini}}}",
            r"=",
            r"\int \phi(\mathbf{x})\, p(\mathbf{x}, t)\, d\mathbf{x}",
            r"=",
            r"\int \phi(\mathbf{x})\, e^{\mathcal{L}t}\, \delta(\mathbf{x} - \mathbf{x}_{\mathrm{ini}})\, d\mathbf{x}",
            font_size=36,
        )
        exp_eq.set_color(WHITE)
        if exp_eq.width > config.frame_width - 1.0:
            exp_eq.scale_to_fit_width(config.frame_width - 1.0)
        exp_eq.shift(UP * 0.5)
        exp_box = SurroundingRectangle(exp_eq, color=YELLOW, buff=0.22)
        self.play(Write(exp_eq), run_time=1.2)
        self.play(Create(exp_box), run_time=0.4)
        self.wait(0.4)

        ann_p = Text("確率密度の時間発展の一般解", color=BLUE, font_size=22)
        ann_p.next_to(exp_eq[2], DOWN, buff=0.7)
        ann_p_arr = Arrow(ann_p.get_top(), exp_eq[2].get_bottom(),
                          color=BLUE, buff=0.05, stroke_width=3,
                          max_tip_length_to_length_ratio=0.25)

        ann_d = Text("初期分布(デルタ関数)", color=RED, font_size=22)
        ann_d.next_to(exp_eq[4], DOWN, buff=0.7)
        ann_d_arr = Arrow(ann_d.get_top(), exp_eq[4].get_bottom(),
                          color=RED, buff=0.05, stroke_width=3,
                          max_tip_length_to_length_ratio=0.25)

        self.play(Write(ann_p), GrowArrow(ann_p_arr),
                  Write(ann_d), GrowArrow(ann_d_arr), run_time=1.0)
        self.wait(0.3)

        op_note = Text(
            "※e^{𝓛t}は偏微分方程式の一般解中に現れる項",
            color=GRAY, font_size=24,
        )
        op_note.shift(DOWN * 1.3)
        self.play(Write(op_note), run_time=0.8)
        self.wait(0.3)
        
        add_comment = VGroup(
            Text("これより、任意の初期状態から", color=WHITE, font_size=26),
            MathTex(r"\Delta t_{\text{obs}}",color=WHITE, font_size=32),
            Text("だけ時間発展させれば、", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.15).shift(DOWN * 2.3)
        add_comment2 = Text(
            "欲しかったスナップショットペア予測が得られる",
            color=GOLD, font_size=26, weight=BOLD,
        ).shift(DOWN * 2.8)
        self.play(Write(add_comment), Write(add_comment2), run_time=0.8)
        self.wait(1.8)
        
        self.play(
            FadeOut(exp_intro), FadeOut(exp_box),
            FadeOut(ann_p), FadeOut(ann_p_arr),
            FadeOut(ann_d), FadeOut(ann_d_arr), FadeOut(op_note),
            FadeOut(add_comment), FadeOut(add_comment2)
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: 素直な解法（密度の時間発展として解く）
        # ============================================================
        subtitle4 = Text("素直な解法：確率密度関数の時間発展として解く", font_size=27, color=BLUE)
        subtitle4.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle4), run_time=0.5)
        self.wait(0.3)

        # exp_eq を上部へ移動
        self.play(exp_eq.animate.scale(0.85).to_edge(UP, buff=1.9), run_time=0.6)

        straight1 = Text(
            "これまで通り、確率密度関数の時間遷移として捉えるなら：",
            color=WHITE, font_size=26,
        )
        straight1.shift(UP * 0.9)
        self.play(Write(straight1), run_time=0.7)

        step_a = Text(
            "① 4部と同じく、線形作用素 𝓛 を表現行列 L に変換する",
            color=WHITE, font_size=25,
        )
        step_b = Text(
            "② 行列指数 e^{Lt} を積分の式に代入して解く",
            color=WHITE, font_size=25,
        )
        straight_steps = VGroup(step_a, step_b).arrange(
            DOWN, aligned_edge=LEFT, buff=0.35)
        straight_steps.shift(DOWN * 0.3)
        for s in straight_steps:
            self.play(Write(s), run_time=0.7)
        self.wait(0.4)

        branch = Text(
            "しかし、同じ答えに至る『計算過程の異なる』別の道がある",
            color=GOLD, font_size=27, weight=BOLD,
        )
        branch.shift(DOWN * 1.8)
        self.play(Write(branch), run_time=0.8)
        self.wait(0.3)

        branch2 = Text("それが『随伴作用素』を使う道", color=YELLOW, font_size=28, weight=BOLD)
        branch2.shift(DOWN * 2.6)
        self.play(Write(branch2), run_time=0.7)
        self.wait(1.8)

        self.play(
            FadeOut(exp_eq), FadeOut(straight1), FadeOut(straight_steps),
            FadeOut(branch), FadeOut(branch2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: 随伴作用素の定義
        # ============================================================
        subtitle5 = Text("随伴作用素の定義", font_size=28, color=TEAL)
        subtitle5.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle5), run_time=0.5)
        self.wait(0.3)

        adj_intro = Text(
            "要素 𝐱 に作用素 A を作用させたものと、別の要素 𝐲 の内積を考える",
            color=WHITE, font_size=26,
        )
        adj_intro.shift(UP * 1.6)
        self.play(Write(adj_intro), run_time=0.8)
        self.wait(0.3)

        adj_eq = MathTex(
            r"\langle \mathbf{y},\, A\mathbf{x} \rangle",
            r"=",
            r"\langle A^{\dagger}\mathbf{y},\, \mathbf{x} \rangle",
            font_size=50,
        )
        adj_eq.set_color(WHITE)
        adj_eq[0].set_color(BLUE)
        adj_eq[2].set_color(RED)
        adj_eq.shift(UP * 0.3)
        adj_box = SurroundingRectangle(adj_eq, color=YELLOW, buff=0.25)
        self.play(Write(adj_eq), Create(adj_box), run_time=1.0)
        self.wait(0.4)

        adj_def = Text(
            "この等式を満たす A† を、A の『随伴作用素』と呼ぶ",
            color=GOLD, font_size=27, weight=BOLD,
        )
        adj_def.shift(DOWN * 1.1)
        self.play(Write(adj_def), run_time=0.8)
        self.wait(0.3)

        adj_idea = Text(
            "ポイント：作用素を、内積の『相手側』へ移す操作",
            color=TEAL, font_size=25,
        )
        adj_idea.shift(DOWN * 2.1)
        self.play(Write(adj_idea), run_time=0.8)
        self.wait(1.8)

        self.play(
            FadeOut(adj_intro), FadeOut(adj_eq), FadeOut(adj_box),
            FadeOut(adj_def), FadeOut(adj_idea),
        )
        self.wait(0.3)

        # ============================================================
        # Part 6: 関数空間の内積は積分
        # ============================================================
        subtitle6 = Text("関数空間の内積は積分で定義される", font_size=28, color=ORANGE)
        subtitle6.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle6), run_time=0.5)
        self.wait(0.3)

        fn1 = Text(
            "2部で見たように、関数空間の内積は積分で定義できる",
            color=WHITE, font_size=26,
        )
        fn1.shift(UP * 1.7)
        self.play(Write(fn1), run_time=0.8)
        self.wait(0.3)

        inner_eq = MathTex(
            r"\langle \phi,\, p \rangle \;=\; \int \phi(\mathbf{x})\, p(\mathbf{x})\, d\mathbf{x}",
            font_size=44, color=YELLOW,
        )
        inner_eq.shift(UP * 0.5)
        self.play(Write(inner_eq), run_time=0.9)
        self.wait(0.3)

        fn2 = Text(
            "求めたい期待値も積分で書けている",
            color=GOLD, font_size=26,
        )
        fn2.shift(DOWN * 0.5)
        self.play(Write(fn2), run_time=0.7)
        self.wait(0.2)

        fn3 = Text(
            "→ その積分に含まれる作用素に対して、随伴作用素を定められる",
            color=TEAL, font_size=26, weight=BOLD,
        )
        fn3.shift(DOWN * 1.5)
        self.play(Write(fn3), run_time=0.8)
        self.wait(1.8)

        self.play(
            FadeOut(fn1), FadeOut(inner_eq), FadeOut(fn2), FadeOut(fn3),
        )
        self.wait(0.3)

        # ============================================================
        # Part 7: 部分積分の例
        # ============================================================
        subtitle7 = Text("具体例：部分積分で作用素を移す", font_size=28, color=GOLD)
        subtitle7.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle7), run_time=0.5)
        self.wait(0.3)

        ibp_intro = Text(
            "「p に a(x) を掛けて x で微分する」作用素の随伴を求めてみる",
            color=WHITE, font_size=25,
        )
        ibp_intro.shift(UP * 2)
        self.play(Write(ibp_intro), run_time=0.8)
        self.wait(0.3)

        line1 = MathTex(
            r"\int_{-\infty}^{\infty} \phi(x)\, \frac{d}{dx}\bigl(a(x)\, p(x,t)\bigr)\, dx",
            font_size=36, color=WHITE,
        )
        line2 = MathTex(
            r"=\; \Bigl[\phi(x)\, a(x)\, p(x,t)\Bigr]_{-\infty}^{\infty}"
            r"\;-\; \int_{-\infty}^{\infty} \Bigl(\frac{d}{dx}\phi(x)\Bigr) a(x)\, p(x,t)\, dx",
            font_size=36, color=WHITE,
        )
        line3 = MathTex(
            r"=\; \int_{-\infty}^{\infty} p(x,t)\, \Bigl(-a(x)\, \frac{d}{dx}\phi(x)\Bigr)\, dx",
            font_size=36, color=WHITE,
        )
        ibp = VGroup(line1, line2, line3).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        for ln in ibp:
            if ln.width > config.frame_width - 1.0:
                ln.scale_to_fit_width(config.frame_width - 1.0)
        ibp.shift(DOWN * 0.3)

        self.play(Write(line1), run_time=0.9)
        self.wait(0.3)

        vanish = Text("境界項は 0（遠方で密度は 0）", color=RED, font_size=22)
        vanish.next_to(line2, DOWN, buff=0.08).shift(LEFT * 2.5)
        self.play(Write(line2), run_time=1.1)
        self.play(Write(vanish), run_time=0.5)
        self.wait(0.3)
        self.play(Write(line3), run_time=0.9)
        self.wait(0.4)

        ibp_concl = Text(
            "「a(x) を掛けて微分」の随伴は「微分して −a(x) を掛ける」",
            color=GOLD, font_size=25, weight=BOLD,
        )
        ibp_concl.shift(DOWN * 2.9)
        self.play(FadeOut(vanish), Write(ibp_concl), run_time=0.8)
        self.wait(1.8)

        self.play(
            FadeOut(ibp_intro), FadeOut(ibp), FadeOut(ibp_concl),
        )
        self.wait(0.3)

        # ============================================================
        # Part 8: 期待値の書き換え
        # ============================================================
        subtitle8 = Text("期待値の書き換え：作用素を ϕ 側へ移す", font_size=27, color=YELLOW)
        subtitle8.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle8), run_time=0.5)
        self.wait(0.3)

        rw_intro = Text(
            "同じ操作をSSペア推定問題に適用すると、作用素が ϕ 側へ移る：",
            color=WHITE, font_size=26,
        )
        rw_intro.shift(UP * 1.8)
        self.play(Write(rw_intro), run_time=0.8)
        self.wait(0.3)

        rw_eq = MathTex(
            r"\int \phi(\mathbf{x})\, e^{\mathcal{L}t}\, \delta(\mathbf{x} - \mathbf{x}_{\mathrm{ini}})\, d\mathbf{x}",
            r"=",
            r"\int \bigl(e^{\mathcal{L}^{\dagger}t}\, \phi(\mathbf{x})\bigr)\, \delta(\mathbf{x} - \mathbf{x}_{\mathrm{ini}})\, d\mathbf{x}",
            font_size=38,
        )
        rw_eq.set_color(WHITE)
        rw_eq[0].set_color(BLUE)
        rw_eq[2].set_color(RED)
        if rw_eq.width > config.frame_width - 1.0:
            rw_eq.scale_to_fit_width(config.frame_width - 1.0)
        rw_eq.shift(UP * 0.4)
        rw_box = SurroundingRectangle(rw_eq, color=YELLOW, buff=0.22)
        self.play(Write(rw_eq), Create(rw_box), run_time=1.2)
        self.wait(0.4)

        rw_a = Text("作用素𝓛 は密度関数δ に作用", color=BLUE, font_size=24)
        rw_a.next_to(rw_eq[0], DOWN, buff=0.9)
        rw_a_arr = Arrow(rw_a.get_top(), rw_eq[0].get_bottom(),
                         color=BLUE, buff=0.05, stroke_width=3,
                         max_tip_length_to_length_ratio=0.22)

        rw_b = Text("随伴作用素𝓛† は観測関数ϕ に作用", color=RED, font_size=24)
        rw_b.next_to(rw_eq[2], DOWN, buff=1.4)
        rw_b_arr = Arrow(rw_b.get_top(), rw_eq[2].get_bottom(),
                         color=RED, buff=0.05, stroke_width=3,
                         max_tip_length_to_length_ratio=0.22)

        self.play(Write(rw_a), GrowArrow(rw_a_arr),
                  Write(rw_b), GrowArrow(rw_b_arr), run_time=1.0)
        self.wait(1.8)

        self.play(
            FadeOut(rw_intro), FadeOut(rw_eq), FadeOut(rw_box),
            FadeOut(rw_a), FadeOut(rw_a_arr),
            FadeOut(rw_b), FadeOut(rw_b_arr),
        )
        self.wait(0.3)

        # ============================================================
        # Part 9: 観測関数の時間発展式
        # ============================================================
        subtitle9 = Text("問題の置き換え：観測関数の時間発展式へ", font_size=27, color=ORANGE)
        subtitle9.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle9), run_time=0.5)
        self.wait(0.3)

        # 対比：密度の時間発展 vs 観測関数の時間発展
        left_title = Text("これまで：確率密度関数の時間発展", color=BLUE, font_size=25)
        left_eq = MathTex(
            r"\frac{\partial}{\partial t} p(\mathbf{x}, t) = \mathcal{L}\, p(\mathbf{x}, t)",
            font_size=38, color=BLUE,
        )
        left_group = VGroup(left_title, left_eq).arrange(DOWN, buff=0.35)
        left_group.shift(LEFT * 3.3 + UP * 0.8)

        right_title = Text("随伴：観測関数の時間発展", color=RED, font_size=25)
        right_eq = MathTex(
            r"\frac{\partial}{\partial t} \phi(\mathbf{x}, t) = \mathcal{L}^{\dagger}\, \phi(\mathbf{x}, t)",
            font_size=38, color=RED,
        )
        right_group = VGroup(right_title, right_eq).arrange(DOWN, buff=0.35)
        right_group.shift(RIGHT * 3.3 + UP * 0.8)

        arrow_switch = MathTex(r"\Longleftrightarrow", font_size=50, color=GOLD)
        arrow_switch.shift(UP * 0.5)

        self.play(Write(left_title), Write(left_eq), run_time=0.9)
        self.play(Write(arrow_switch), run_time=0.4)
        self.play(Write(right_title), Write(right_eq), run_time=0.9)
        self.wait(0.4)

        right_box = SurroundingRectangle(right_eq, color=YELLOW, buff=0.2)
        self.play(Create(right_box), run_time=0.5)
        self.wait(0.3)

        merit1 = Text(
            "そして、状態変数の次元よりも観測変数の次元の方が小さいことが多い",
            color=WHITE, font_size=26,
        )
        merit2 = Text(
            "→ 観測関数の時間発展は単純で、計算負荷を大幅に抑えられる",
            color=GOLD, font_size=26, weight=BOLD,
        )
        merits = VGroup(merit1, merit2).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        merits.shift(DOWN * 1.9)
        for m in merits:
            self.play(Write(m), run_time=0.7)
        self.wait(1.8)

        self.play(
            FadeOut(left_title), FadeOut(left_eq), FadeOut(arrow_switch),
            FadeOut(right_title), FadeOut(right_eq), FadeOut(right_box),
            FadeOut(merits),
        )
        self.wait(0.3)

        # ============================================================
        # Part 10: フォッカー・プランク作用素とその随伴
        # ============================================================
        subtitle10 = Text("フォッカー・プランク作用素と、その随伴", font_size=28, color=PURPLE)
        subtitle10.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle10), run_time=0.5)
        self.wait(0.3)

        fp_intro = Text(
            "4部で登場したフォッカー・プランク方程式での具体例：",
            color=WHITE, font_size=25,
        )
        fp_intro.shift(UP * 1.9)
        self.play(Write(fp_intro), run_time=0.8)
        self.wait(0.3)

        fp_title = Text("フォッカー・プランク作用素（確率密度関数に作用）", color=BLUE, font_size=24)
        fp_eq = MathTex(
            r"\mathcal{L} = -\sum_{d=1}^{D} \frac{\partial}{\partial x_d} a_d(\mathbf{x})"
            r"\;+\; \frac{1}{2}\sum_{d, d'} \frac{\partial^2}{\partial x_d \partial x_{d'}}"
            r"\bigl[\mathbf{B}(\mathbf{x})\mathbf{B}(\mathbf{x})^{\top}\bigr]_{dd'}",
            font_size=34, color=BLUE,
        )
        fp_group = VGroup(fp_title, fp_eq).arrange(DOWN, buff=0.25)
        if fp_eq.width > config.frame_width - 1.0:
            fp_eq.scale_to_fit_width(config.frame_width - 1.0)
        fp_group.shift(UP * 0.65)
        self.play(Write(fp_title), run_time=0.5)
        self.play(Write(fp_eq), run_time=1.1)
        self.wait(0.4)

        adj_title = Text("その随伴作用素（観測関数に作用）", color=RED, font_size=24)
        adj_fp_eq = MathTex(
            r"\mathcal{L}^{\dagger} = \sum_{d=1}^{D} a_d(\mathbf{x})\frac{\partial}{\partial x_d}"
            r"\;+\; \frac{1}{2}\sum_{d, d'} \bigl[\mathbf{B}(\mathbf{x})\mathbf{B}(\mathbf{x})^{\top}\bigr]_{dd'}"
            r"\frac{\partial^2}{\partial x_d \partial x_{d'}}",
            font_size=34, color=RED,
        )
        adj_group = VGroup(adj_title, adj_fp_eq).arrange(DOWN, buff=0.27)
        if adj_fp_eq.width > config.frame_width - 1.0:
            adj_fp_eq.scale_to_fit_width(config.frame_width - 1.0)
        adj_group.shift(DOWN * 1.35)
        adj_fp_box = SurroundingRectangle(adj_fp_eq, color=YELLOW, buff=0.2)
        self.play(Write(adj_title), run_time=0.5)
        self.play(Write(adj_fp_eq), Create(adj_fp_box), run_time=1.1)
        self.wait(1.8)

        # fp_note = Text(
        #     "部分積分の要領で、微分が観測関数側へ移り、発散形が消えている",
        #     color=TEAL, font_size=23,
        # )
        # fp_note.shift(DOWN * 2.9)
        # self.play(Write(fp_note), run_time=0.8)
        # self.wait(2.0)

        self.play(
            FadeOut(fp_intro), FadeOut(fp_title), FadeOut(fp_eq),
            FadeOut(adj_title), FadeOut(adj_fp_eq), FadeOut(adj_fp_box),
            # FadeOut(fp_note),
        )
        self.wait(0.3)

        # ============================================================
        # Part 11: まとめ
        # ============================================================
        subtitle11 = Text("まとめ", font_size=34, color=TEAL)
        subtitle11.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle11), run_time=0.6)
        self.wait(0.3)

        summary = VGroup(
            Text("• 求めたいのは、状態を時刻 t 遷移させた観測値の期待値 𝔼[ϕ(𝐗)]",
                 color=WHITE, font_size=25),
            Text("• 素直には、確率密度関数の時間発展を解けばよい",
                 color=WHITE, font_size=25),
            Text("• 随伴作用素 A†：⟨𝐲, A𝐱⟩ = ⟨A†𝐲, 𝐱⟩（作用素を内積の相手側へ移す）",
                 color=WHITE, font_size=25),
            Text("• 関数空間の内積＝積分。部分積分で作用素を ϕ 側へ移せる",
                 color=WHITE, font_size=25),
            Text("• 問題は『観測関数の時間発展』∂ϕ/∂t = 𝓛†ϕ に置き換わる",
                 color=WHITE, font_size=25),
            Text("• 観測の次元は小さいことが多く、計算負荷を大幅に削減できる",
                 color=GOLD, font_size=25, weight=BOLD),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        summary.shift(DOWN * 0.1)

        for row in summary:
            self.play(Write(row), run_time=0.55)
            self.wait(0.15)
        self.wait(2.0)

        self.play(
            FadeOut(VGroup(title, subtitle, summary)),
            run_time=1.0,
        )
        self.wait(0.5)
