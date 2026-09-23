from manim import *
import numpy as np


class StochasticDifferentialEquationOverview(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        title = Text("状態量の確率微分方程式の概要", font_size=36, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)

        # ============================================================
        # Part 1: 前回までの振り返りと今回のテーマ
        # ============================================================
        subtitle1 = Text("前回との違い", font_size=28, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.5)
        self.wait(0.3)

        recap1 = Text(
            "22,23話では、確率密度関数 p(x, t) の時間発展を詳しく見てきた",
            color=WHITE, font_size=26,
        )
        recap1.shift(UP * 1.8)
        self.play(Write(recap1), run_time=0.8)
        self.wait(0.3)

        recap2 = Text(
            "今回：密度関数ではなく、",
            color=GOLD, font_size=28, weight=BOLD,
        )
        recap3 = Text(
            "状態ベクトル 𝐗(t) 自身の確率的な時間発展を記述する方法を見る",
            color=GOLD, font_size=28, weight=BOLD,
        )
        recap2.shift(UP * 0.5)
        recap3.next_to(recap2, DOWN, buff=0.2)
        self.play(Write(recap2), run_time=0.7)
        self.play(Write(recap3), run_time=0.7)
        self.wait(0.5)

        recap4 = Text(
            "その上で、確率密度関数の時間発展との関係を整理する",
            color=WHITE, font_size=26,
        )
        recap4.shift(DOWN * 0.9)
        self.play(Write(recap4), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(recap1), FadeOut(recap2), FadeOut(recap3), FadeOut(recap4),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: 確率微分方程式（SDE）
        # ============================================================
        subtitle2 = Text("状態ベクトルの確率微分方程式", font_size=28, color=GOLD)
        subtitle2.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle2), run_time=0.5)
        self.wait(0.3)

        sde_intro = Text(
            "状態ベクトルの確率的な時間発展は、次の形の確率微分方程式で表される",
            color=WHITE, font_size=26,
        )
        sde_intro.shift(UP * 1.8)
        self.play(Write(sde_intro), run_time=0.8)
        self.wait(0.3)

        sde_eq = MathTex(
            r"d\mathbf{X}(t) = "
            r"\mathbf{a}(\mathbf{X}(t))\,dt "
            r"+ \mathbf{B}(\mathbf{X}(t))\,d\mathbf{W}(t)",
            color=YELLOW, font_size=44,
        )
        sde_eq.shift(UP * 0.7)
        sde_box = SurroundingRectangle(sde_eq, color=YELLOW, buff=0.25)
        self.play(Write(sde_eq), Create(sde_box), run_time=1.0)
        self.wait(0.5)

        expl1 = Text(
            "• 𝐗(t)：確率変数（状態ベクトル）",
            color=WHITE, font_size=24,
        )
        expl2 = Text(
            "• d𝐖(t)：ウィナー過程から導かれるゆらぎ（ノイズ）",
            color=WHITE, font_size=24,
        )
        expl3 = Text(
            "• ウィナー過程は微分できないため d/dt では書けず、形式的に d で記述",
            color=WHITE, font_size=24,
        )
        exps = VGroup(expl1, expl2, expl3).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        exps.shift(DOWN * 1.5)
        for e in exps:
            self.play(Write(e), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(sde_intro), FadeOut(sde_eq), FadeOut(sde_box),
            FadeOut(exps),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: 確定的微分方程式との比較
        # ============================================================
        subtitle3 = Text("確定的な微分方程式との違い", font_size=28, color=TEAL)
        subtitle3.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle3), run_time=0.5)
        self.wait(0.3)

        det_label = Text("19〜21話：確定的な微分方程式", color=BLUE, font_size=24)
        det_eq = MathTex(
            r"d\mathbf{x}(t) = \mathbf{a}(\mathbf{x}(t))\,dt",
            color=WHITE, font_size=38,
        )
        det_group = VGroup(det_label, det_eq).arrange(DOWN, buff=0.25)
        det_group.shift(UP * 1.5)
        self.play(Write(det_label), Write(det_eq), run_time=0.9)
        self.wait(0.3)

        sto_label = Text("今回：確率微分方程式", color=GOLD, font_size=24)
        sto_eq = MathTex(
            r"d\mathbf{X}(t) = \mathbf{a}(\mathbf{X}(t))\,dt ",
            r"+ \mathbf{B}(\mathbf{X}(t))\,d\mathbf{W}(t)",
            font_size=38,
        )
        sto_eq[0].set_color(WHITE)
        sto_eq[1].set_color(YELLOW)
        sto_group = VGroup(sto_label, sto_eq).arrange(DOWN, buff=0.25)
        sto_group.shift(DOWN * 0.3)
        self.play(Write(sto_label), Write(sto_eq), run_time=1.0)
        added_note = Text("↑ 追加された項", color=YELLOW, font_size=22)
        added_note.next_to(sto_eq[1], DOWN, buff=0.2)
        self.play(Write(added_note), run_time=0.6)
        self.wait(0.5)

        correspond = Text(
            "この 𝐁(𝐗)d𝐖 の項が22話フォッカー・プランクの方程式の",
            color=GOLD, font_size=24,
        )
        correspond2 = Text(
            "「拡散項」に、𝐚(𝐗)dt の項が「ドリフト項」に対応する",
            color=GOLD, font_size=24,
        )
        correspond.shift(DOWN * 2.0)
        correspond2.next_to(correspond, DOWN, buff=0.15)
        self.play(Write(correspond), run_time=0.8)
        self.play(Write(correspond2), run_time=0.8)
        self.wait(1.8)

        self.play(
            FadeOut(det_label), FadeOut(det_eq),
            FadeOut(sto_label), FadeOut(sto_eq), FadeOut(added_note),
            FadeOut(correspond), FadeOut(correspond2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: 状態ベクトルを得るには？
        # ============================================================
        subtitle4 = Text("任意時刻の状態ベクトルを得るには", font_size=28, color=ORANGE)
        subtitle4.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle4), run_time=0.5)
        self.wait(0.3)

        way_intro = Text(
            "SDE から任意時刻 t の 𝐗(t) の値が欲しい場合：",
            color=WHITE, font_size=26,
        )
        way_intro.shift(UP * 1.8)
        self.play(Write(way_intro), run_time=0.7)
        self.wait(0.3)

        way1 = Text(
            "① 初期値から出発し、単位時刻ずつ SDE に従って逐次更新する",
            color=WHITE, font_size=25,
        )
        way2 = Text(
            "② あるいは「確率積分」という操作を行う",
            color=WHITE, font_size=25,
        )
        ways = VGroup(way1, way2).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        ways.shift(UP * 0.6)
        for w in ways:
            self.play(Write(w), run_time=0.7)
        self.wait(0.4)

        # 簡単な模式図：単位時刻ごとに揺らぎつつ進む1本のサンプルパス
        axes4 = Axes(
            x_range=[0, 5, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=7.0,
            y_length=2.4,
            axis_config={"color": WHITE, "include_tip": False, "stroke_width": 2},
        )
        axes4.shift(DOWN * 1.8)
        t_lab = MathTex("t", color=WHITE, font_size=26).next_to(axes4.x_axis.get_end(), RIGHT, buff=0.1)
        x_lab = MathTex(r"X(t)", color=WHITE, font_size=26).next_to(axes4.y_axis.get_end(), UP, buff=0.1)

        rng = np.random.default_rng(3)
        n_steps = 60
        ts = np.linspace(0, 5, n_steps + 1)
        xs = np.zeros(n_steps + 1)
        dt = ts[1] - ts[0]
        for k in range(n_steps):
            xs[k + 1] = xs[k] - 0.3 * xs[k] * dt + 0.5 * np.sqrt(dt) * rng.standard_normal()
        pts = [axes4.c2p(ts[k], xs[k]) for k in range(n_steps + 1)]
        path = VMobject(color=YELLOW, stroke_width=2.5)
        path.set_points_as_corners(pts)

        self.play(Create(axes4), Write(t_lab), Write(x_lab), run_time=0.7)
        self.play(Create(path), run_time=1.6)
        self.wait(1.5)

        self.play(
            FadeOut(way_intro), FadeOut(ways),
            FadeOut(axes4), FadeOut(t_lab), FadeOut(x_lab), FadeOut(path),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: 密度関数経由の方が楽
        # ============================================================
        subtitle5 = Text("確率密度関数の時間発展との関係", font_size=28, color=PURPLE)
        subtitle5.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle5), run_time=0.5)
        self.wait(0.3)

        rel1 = Text(
            "本質的には、状態ベクトルの時間発展と確率密度関数の時間発展は同じ現象",
            color=WHITE, font_size=26,
        )
        rel1.shift(UP * 1.95)
        self.play(Write(rel1), run_time=0.8)
        self.wait(0.3)

        rel2 = Text(
            "分布から状態量をドローできるなら、",
            color=GOLD, font_size=26, weight=BOLD,
        )
        rel3 = Text(
            "対応する密度関数の時間発展を作用素で解いた方が楽",
            color=GOLD, font_size=26, weight=BOLD,
        )
        rel2.shift(UP * 1.2)
        rel3.next_to(rel2, DOWN, buff=0.2)
        self.play(Write(rel2), run_time=0.7)
        self.play(Write(rel3), run_time=0.7)
        self.wait(0.4)

        op_eq = MathTex(
            r"\frac{\partial}{\partial t} p(\mathbf{x}, t) "
            r"= \mathcal{L}\, p(\mathbf{x}, t)",
            color=YELLOW, font_size=44,
        )
        op_eq.shift(DOWN * 0.8)
        op_box = SurroundingRectangle(op_eq, color=YELLOW, buff=0.25)
        self.play(Write(op_eq), Create(op_box), run_time=0.9)
        self.wait(0.4)

        flow = Text(
            "→ 作用素 ℒ から一般解を導き、そこから状態ベクトルをドローする",
            color=TEAL, font_size=24,
        )
        flow.shift(DOWN * 2.0)
        self.play(Write(flow), run_time=0.9)
        self.wait(1.5)

        self.play(
            FadeOut(rel1), FadeOut(rel2), FadeOut(rel3),
            FadeOut(op_eq), FadeOut(op_box), FadeOut(flow),
        )
        self.wait(0.3)

        # ============================================================
        # Part 6: 作用素を使うメリット（線形性）
        # ============================================================
        subtitle6 = Text("作用素を使うメリット：線形性", font_size=28, color=GREEN)
        subtitle6.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle6), run_time=0.5)
        self.wait(0.3)

        merit1 = Text(
            "状態変数の領域では非線形でも、",
            color=WHITE, font_size=26,
        )
        merit2 = Text(
            "状態変数の関数（確率密度関数）の時間発展として捉えると線形性を満たしやすい",
            color=WHITE, font_size=26,
        )
        merit1.shift(UP * 1.8)
        merit2.next_to(merit1, DOWN, buff=0.2)
        self.play(Write(merit1), run_time=0.7)
        self.play(Write(merit2), run_time=0.7)
        self.wait(0.3)

        merit3 = Text(
            "→ 線形性を満たすと、強力な線形系の解析ツール群が使える",
            color=GOLD, font_size=26, weight=BOLD,
        )
        merit3.shift(UP * 0.5)
        self.play(Write(merit3), run_time=0.8)
        self.wait(0.5)

        example_label = Text("例：状態変数側では非線形な時間発展", color=WHITE, font_size=24)
        example_eq = MathTex(
            r"\frac{d}{dt}x(t) = a(x(t)) = \bigl(x(t)\bigr)^2",
            color=YELLOW, font_size=40,
        )
        ex_group = VGroup(example_label, example_eq).arrange(DOWN, buff=0.2)
        ex_group.shift(DOWN)
        self.play(Write(example_label), Write(example_eq), run_time=0.9)
        self.wait(0.4)

        nonlin_note = MathTex(
            r"a(x + x') \neq a(x) + a(x')",
            color=RED, font_size=38,
        )
        nonlin_label = Text("（非線形）", color=RED, font_size=24)
        nonlin_group = VGroup(nonlin_note, nonlin_label).arrange(RIGHT, buff=0.25)
        nonlin_group.shift(DOWN * 2.4)
        self.play(Write(nonlin_note), Write(nonlin_label), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(merit1), FadeOut(merit2), FadeOut(merit3),
            FadeOut(example_label), FadeOut(example_eq), FadeOut(nonlin_group),
        )
        self.wait(0.3)

        # ============================================================
        # Part 7: 対応するフォッカー・プランクは線形
        # ============================================================
        subtitle7 = Text("対応する作用素は線形", font_size=28, color=YELLOW)
        subtitle7.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle7), run_time=0.5)
        self.wait(0.3)

        fp_intro = Text(
            "先ほどの非線形な a(x) に対応するフォッカー・プランク方程式",
            color=WHITE, font_size=25,
        )
        fp_intro.shift(UP * 2)
        self.play(Write(fp_intro), run_time=0.7)
        self.wait(0.3)

        fp_eq = MathTex(
            r"\frac{\partial}{\partial t}p(x, t) "
            r"= \frac{\partial}{\partial x}\bigl[a(x)\,p(x, t)\bigr]",
            color=YELLOW, font_size=38,
        )
        fp_eq.shift(UP * 1.2)
        self.play(Write(fp_eq), run_time=0.9)
        self.wait(0.3)

        check_label = Text("作用素として線形性を確認：", color=GREEN, font_size=24)
        # check_label.shift(UP * 0.1)
        self.play(Write(check_label), run_time=0.6)

        lin_eq = MathTex(
            r"\frac{\partial}{\partial x}\bigl[a(x)(p(x, t) + p'(x, t))\bigr]",
            r"=",
            r"\frac{\partial}{\partial x}\bigl[a(x)\,p(x, t)\bigr] "
            r"+ \frac{\partial}{\partial x}\bigl[a(x)\,p'(x, t)\bigr]",
            color=GREEN, font_size=34,
        )
        lin_eq.shift(DOWN)
        self.play(Write(lin_eq), run_time=1.2)
        self.wait(0.4)

        key = Text(
            "ポイント：線形作用素は x には作用せず、関数 a や p のみに作用する",
            color=GOLD, font_size=24, weight=BOLD,
        )
        key.shift(DOWN * 2.1)
        self.play(Write(key), run_time=0.9)
        self.wait(0.4)

        reach = Text(
            "→ 適当な表現行列化すれば、線形代数のツールで扱える",
            color=TEAL, font_size=24,
        )
        reach.shift(DOWN * 2.6)
        self.play(Write(reach), run_time=0.8)
        self.wait(1.8)

        self.play(
            FadeOut(fp_intro), FadeOut(fp_eq),
            FadeOut(check_label), FadeOut(lin_eq),
            FadeOut(key), FadeOut(reach),
        )
        self.wait(0.3)

        # ============================================================
        # Part 8: 視点の変更と過去回への接続
        # ============================================================
        subtitle8 = Text("視点を変えると線形/非線形が変わる", font_size=28, color=ORANGE)
        subtitle8.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle8), run_time=0.5)
        self.wait(0.3)

        view1 = Text(
            "状態変数 x そのものに着目 → 非線形",
            color=RED, font_size=28,
        )
        view2 = Text(
            "状態変数の関数 p(x, t) に着目 → 線形",
            color=GREEN, font_size=28,
        )
        view1.shift(UP * 1.4)
        view2.next_to(view1, DOWN, buff=0.4)
        self.play(Write(view1), run_time=0.7)
        self.play(Write(view2), run_time=0.7)
        self.wait(0.5)

        connect = Text(
            "視点を変えるだけで線形/非線形が変わるのは、",
            color=WHITE, font_size=26,
        )
        connect2 = Text(
            "15話などで扱った線形回帰の議論と似た構図",
            color=WHITE, font_size=26,
        )
        connect.shift(DOWN * 0.5)
        connect2.next_to(connect, DOWN, buff=0.2)
        self.play(Write(connect), run_time=0.8)
        self.play(Write(connect2), run_time=0.8)
        self.wait(1.8)

        self.play(
            FadeOut(view1), FadeOut(view2),
            FadeOut(connect), FadeOut(connect2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 9: まとめ
        # ============================================================
        subtitle9 = Text("まとめ", font_size=36, color=TEAL)
        subtitle9.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle9), run_time=0.6)
        self.wait(0.3)

        summary = VGroup(
            Text("• 状態ベクトルの確率的な時間発展は SDE：d𝐗 = 𝐚(𝐗)dt + 𝐁(𝐗)d𝐖 で表される", color=WHITE, font_size=24),
            Text("• d𝐖 はウィナー過程由来のゆらぎ。微分できないので形式的に d を用いる", color=WHITE, font_size=24),
            Text("• 𝐚(𝐗)dt がドリフト項、𝐁(𝐗)d𝐖 が拡散項（FP方程式のそれと対応）", color=WHITE, font_size=24),
            Text("• 任意時刻の 𝐗(t) は逐次更新か確率積分で得られる", color=WHITE, font_size=24),
            Text("• 本質は密度関数の時間発展と同じ → ∂p/∂t = ℒp を解いてドローする方が楽", color=WHITE, font_size=24),
            Text("• 状態変数側で非線形でも、密度関数の時間発展は線形になり得る", color=WHITE, font_size=24),
            Text("• 線形性が得られれば強力な線形系の解析ツールが使える（15話の線形回帰と類似）", color=WHITE, font_size=24),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        # summary.shift(UP * 0.1)

        for row in summary:
            self.play(Write(row), run_time=0.55)
            self.wait(0.2)
        self.wait(2.0)

        self.play(
            FadeOut(VGroup(title, subtitle1, summary)),
            run_time=1.0,
        )
        self.wait(0.5)
