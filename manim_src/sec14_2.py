from manim import *
import numpy as np

class OptimalSearch(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        # タイトル
        title = Text("関数の最適な場所の探し方", font_size=34, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)

        # ============================================================
        # Part 1: 前回のモチベーション
        # ============================================================
        subtitle1 = Text("前回のモチベーション", font_size=30, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.5)

        motiv_text = VGroup(
            Text("前節、少し唐突にベクトルによる微分を学んだが", color=WHITE, font_size=24),
            Text("そもそも今後、何のために微分が必要なのか？", color=YELLOW, font_size=24, weight=BOLD),
        ).arrange(DOWN, buff=0.15)
        motiv_text.shift(UP * 1.3)
        self.play(Write(motiv_text), run_time=0.7)
        self.wait(0.6)

        ml_context = VGroup(
            VGroup(
                Text("●", color=TEAL, font_size=22),
                Text("機械学習では関数の最大・最小を探すことが頻出", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("●", color=TEAL, font_size=22),
                Text("その常套手段が「勾配を登る・下る」", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("●", color=TEAL, font_size=22),
                Text("この勾配の計算に微分が用いられる", color=YELLOW, font_size=24, weight=BOLD),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        ml_context.shift(DOWN * 0.3)
        for item in ml_context:
            self.play(Write(item), run_time=0.6)
            self.wait(0.3)

        next_note = Text("最適化についてより詳しくは次回以降で！", color=GREEN, font_size=22, weight=BOLD)
        next_note.shift(DOWN * 2.0)
        self.play(Write(next_note), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(motiv_text), FadeOut(ml_context), FadeOut(next_note),
            FadeOut(subtitle1),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: 最大値・最小値を持たない関数
        # ============================================================
        subtitle2 = Text("最大値・最小値を持たない関数", font_size=30, color=ORANGE)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)

        no_max_note = VGroup(
            Text("最大値や最小値を持たない関数も存在する", color=WHITE, font_size=24),
            Text("まずはこの点を確認しておこう", color=WHITE, font_size=24),
        ).arrange(DOWN, buff=0.12)
        no_max_note.shift(UP * 1.5)
        self.play(Write(no_max_note), run_time=0.7)
        self.wait(1.0)

        # 単調増加関数の例
        axes_mono = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[-3, 3, 1],
            x_length=4.5, y_length=3.2,
            axis_config={"color": GRAY, "include_tip": True},
        ).scale(0.85)
        axes_mono.shift(DOWN * 0.5)

        mono_curve = axes_mono.plot(
            lambda x: x, x_range=[-2.3, 2.3], color=ORANGE, stroke_width=3
        )
        mono_label = MathTex(r"f(x) = x", color=ORANGE, font_size=32)
        mono_label.next_to(axes_mono, RIGHT, buff=0.2).shift(UP * 0.5)

        mono_note = VGroup(
            Text("→ どこまでも大きく・小さくなる（最大値も最小値も存在しない）", color=ORANGE, font_size=26),
        )
        mono_note.next_to(axes_mono, DOWN, buff=0.15)

        self.play(Create(axes_mono), run_time=0.6)
        self.play(Create(mono_curve), Write(mono_label), run_time=0.7)
        self.play(Write(mono_note), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(no_max_note), FadeOut(axes_mono), FadeOut(mono_curve),
            FadeOut(mono_label), FadeOut(mono_note),
            FadeOut(subtitle2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: 上限・上界の説明
        # ============================================================
        subtitle3 = Text("上限・上界とは", font_size=30, color=PURPLE)
        subtitle3.next_to(title, DOWN)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.5)

        upper_intro = VGroup(
            Text("上界（upper bound）：関数のすべての値 f(x) 以上となる値 M", color=RED, font_size=26, weight=BOLD),
        ).arrange(DOWN, buff=0.12)
        upper_intro.shift(UP * 1.9)
        self.play(Write(upper_intro), run_time=0.7)
        self.wait(0.2)

        upper_def = MathTex(
            r"f(x) \leq M \quad \text{for all } x",
            color=RED, font_size=30
        )
        upper_def.shift(UP * 1.3)
        upper_box = SurroundingRectangle(upper_def, color=RED, buff=0.15)
        self.play(Write(upper_def), Create(upper_box), run_time=0.6)
        self.wait(1.2)

        sup_intro = VGroup(
            Text("上限（supremum）：上界の中で最小のもの", color=GOLD, font_size=26, weight=BOLD),
        ).arrange(DOWN, buff=0.12)
        sup_intro.shift(UP * 0.7)
        self.play(Write(sup_intro), run_time=0.7)
        self.wait(0.2)


        # 図示
        axes_sup = Axes(
            x_range=[0, 1.4, 0.5], y_range=[0, 1.4, 0.5],
            x_length=4.5, y_length=3.5,
            axis_config={"color": GRAY, "include_tip": True},
            x_axis_config={"include_numbers": True},
            y_axis_config={"include_numbers": True},
        ).scale(0.75)
        axes_sup.shift(DOWN * 1.0 + LEFT * 4)

        # f(x) = x, x ∈ [0, 1) （開区間）
        sup_curve = axes_sup.plot(
            lambda x: x, x_range=[0, 0.97], color=TEAL, stroke_width=3
        )
        sup_curve_label = MathTex(r"f(x) = x,\ x \in [0,\, 1)", color=TEAL, font_size=30)
        sup_curve_label.next_to(axes_sup, RIGHT, buff=0.15).shift(UP * 0.2 )

        # 右端の開点（x=1に到達しない）
        open_dot = Circle(radius=0.08, color=TEAL, stroke_width=2.5)
        open_dot.move_to(axes_sup.c2p(1.0, 1.0))

        # 上限の水平線（y=1）
        sup_bound_line = DashedVMobject(
            axes_sup.plot(lambda x: 1.0, x_range=[0, 1.3], color=GOLD, stroke_width=2.5),
            num_dashes=18
        )
        sup_label = VGroup(
            MathTex(r"\sup f = 1", color=GOLD, font_size=26),
            Text("（上限）", color=GOLD, font_size=22),
        ).arrange(RIGHT, buff=0.08)
        sup_label.next_to(axes_sup, RIGHT, buff=0.15).shift(DOWN * 0.4 )

        # 上界の例（y=1.2）
        upper_bound_line = DashedVMobject(
            axes_sup.plot(lambda x: 1.2, x_range=[0, 1.3], color=RED, stroke_width=2.0),
            num_dashes=18
        )
        M_label = VGroup(
            MathTex(r"M = 1.2", color=RED, font_size=26),
            Text("（上界の一例）", color=RED, font_size=22),
        ).arrange(RIGHT, buff=0.08)
        M_label.next_to(axes_sup, RIGHT, buff=0.15).shift(DOWN * 1.0 )

        self.play(Create(axes_sup), run_time=0.5)
        self.play(Create(sup_curve), Write(sup_curve_label), run_time=0.6)
        self.play(FadeIn(open_dot), run_time=0.4)
        self.wait(0.3)
        self.play(Create(upper_bound_line), Write(M_label), run_time=0.6)
        self.wait(0.5)

        sup_explain = VGroup(
            Text("上界は複数存在しうる", color=RED, font_size=22),
            Text("（例：1.2, 1.5, 100, ...）", color=RED, font_size=22),
            Text("その中で最小のものが上限", color=GOLD, font_size=22, weight=BOLD),
        ).arrange(DOWN, buff=0.1)
        sup_explain.shift( DOWN *1.5 +RIGHT * 3.5)
        self.play(Write(sup_explain), run_time=0.7)
        self.wait(0.5)

        self.play(Create(sup_bound_line), Write(sup_label), run_time=0.6)
        self.wait(1.5)

        # 最大値との違い
        max_diff = Text("1 には届かない → 最大値は存在しないが、上限 sup f = 1 は存在する", color=WHITE, font_size=22)
        max_diff.shift(DOWN*3.1)
        self.play(Write(max_diff), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(upper_intro), FadeOut(upper_def), FadeOut(upper_box),
            FadeOut(axes_sup), FadeOut(sup_curve), FadeOut(sup_curve_label),
            FadeOut(open_dot), FadeOut(sup_intro),
            FadeOut(upper_bound_line), FadeOut(M_label),
            FadeOut(sup_bound_line), FadeOut(sup_label),
            FadeOut(sup_explain), FadeOut(max_diff),
            FadeOut(subtitle3),
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: 下限（簡易説明）
        # ============================================================
        subtitle4 = Text("下限について", font_size=30, color=PURPLE)
        subtitle4.next_to(title, DOWN)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.5)

        inf_intro = VGroup(
            Text("下限（infimum）とは", color=TEAL, font_size=26, weight=BOLD),
            Text("上界・上限の「最大と最小を入れ替えた」概念", color=WHITE, font_size=24),
        ).arrange(DOWN, buff=0.15)
        inf_intro.shift(UP * 1.0)
        self.play(Write(inf_intro), run_time=0.7)
        self.wait(0.5)

        inf_compare = VGroup(
            VGroup(
                MathTex(r"\sup f", color=GOLD, font_size=28),
                Text("：最小の上界（上限）", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                MathTex(r"\inf f", color=TEAL, font_size=28),
                Text("：最大の下界（下限）", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        inf_compare.shift(DOWN * 0.1)
        self.play(Write(inf_compare[0]), run_time=0.6)
        self.wait(0.3)
        self.play(Write(inf_compare[1]), run_time=0.6)
        self.wait(1.0)

        inf_note = Text("最小値が存在するとき inf f = min f", color=TEAL, font_size=22)
        inf_note.shift(DOWN * 1.3)
        self.play(Write(inf_note), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(inf_intro), FadeOut(inf_compare), FadeOut(inf_note),
            FadeOut(subtitle4),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: 極大・極小
        # ============================================================
        subtitle5 = Text("極大値・極小値", font_size=30, color=ORANGE)
        subtitle5.next_to(title, DOWN)
        self.play(Write(subtitle5), run_time=0.6)
        self.wait(0.5)

        local_intro = VGroup(
            Text("最大・最小の前に「極大・極小」を理解しよう", color=WHITE, font_size=24),
        )
        local_intro.shift(UP * 1.6)
        self.play(Write(local_intro), run_time=0.7)
        self.wait(0.5)

        # 極大・極小の定義
        local_defs = VGroup(
            VGroup(
                Text("極大値：", color=RED, font_size=24, weight=BOLD),
                Text("微分 = 0　かつ　2次微分 < 0", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("極小値：", color=BLUE, font_size=24, weight=BOLD),
                Text("微分 = 0　かつ　2次微分 > 0", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        local_defs.shift(UP * 0.8)
        self.play(Write(local_defs[0]), run_time=0.6)
        self.wait(0.3)
        self.play(Write(local_defs[1]), run_time=0.6)
        self.wait(0.5)

        # グラフ
        axes_local = Axes(
            x_range=[-3.2, 3.2, 1], y_range=[-2.5, 2.5, 1],
            x_length=5.5, y_length=3.0,
            axis_config={"color": GRAY, "include_tip": True},
        ).scale(0.75)
        axes_local.shift(DOWN * 1.3)

        def f_local(x):
            return 0.3 * x**3 - 1.5 * x

        local_curve = axes_local.plot(
            f_local, x_range=[-2.8, 2.8], color=ORANGE, stroke_width=3
        )

        # 極大点 x=-√(5/3)≈-1.29, 極小点 x=√(5/3)≈1.29
        x_max = -np.sqrt(5/3)
        x_min = np.sqrt(5/3)

        dot_max = Dot(axes_local.c2p(x_max, f_local(x_max)), color=RED, radius=0.1)
        dot_min = Dot(axes_local.c2p(x_min, f_local(x_min)), color=BLUE, radius=0.1)

        label_max = Text("極大", color=RED, font_size=20)
        label_max.next_to(dot_max, UP, buff=0.15)
        label_min = Text("極小", color=BLUE, font_size=20)
        label_min.next_to(dot_min, DOWN, buff=0.15)

        self.play(Create(axes_local), Create(local_curve), run_time=0.7)
        self.play(
            FadeIn(dot_max), Write(label_max),
            FadeIn(dot_min), Write(label_min),
            run_time=0.7
        )
        self.wait(0.6)

        local_note = VGroup(
            Text("極大値が必ずしも最大値とは限らない", color=YELLOW, font_size=22, weight=BOLD),
            Text("が、最大・最小を探す手がかりとして極大・極小を探すことは有効", color=WHITE, font_size=20),
        ).arrange(DOWN, buff=0.1)
        local_note.next_to(axes_local, DOWN, buff=0.15)
        self.play(Write(local_note), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(local_intro), FadeOut(local_defs),
            FadeOut(axes_local), FadeOut(local_curve),
            FadeOut(dot_max), FadeOut(label_max),
            FadeOut(dot_min), FadeOut(label_min),
            FadeOut(local_note), FadeOut(subtitle5),
        )
        self.wait(0.3)

        # ============================================================
        # Part 6: 二次形式の微分
        # ============================================================
        subtitle6 = Text("二次形式の微分", font_size=30, color=TEAL)
        subtitle6.next_to(title, DOWN)
        self.play(Write(subtitle6), run_time=0.6)
        self.wait(0.5)

        quad_intro = VGroup(
            Text("非線形なベクトル関数の微分の例として次の二次形式を考える", color=WHITE, font_size=24),
        ).arrange(DOWN, buff=0.12)
        quad_intro.shift(UP * 1.6)
        self.play(Write(quad_intro), run_time=0.7)
        self.wait(0.5)

        quad_form = MathTex(
            r"f(\mathbf{x}) = \mathbf{x}^{\top} S \mathbf{x}",
            color=TEAL, font_size=40
        )
        quad_form.shift(UP * 0.8)
        quad_box = SurroundingRectangle(quad_form, color=TEAL, buff=0.18)
        self.play(Write(quad_form), Create(quad_box), run_time=0.7)
        self.wait(0.5)

        # Sの説明
        S_desc = VGroup(
            MathTex(r"S", color=YELLOW, font_size=28),
            Text("：対称行列（", color=WHITE, font_size=24),
            MathTex(r"S = S^{\top}", color=YELLOW, font_size=26),
            Text("）", color=WHITE, font_size=24),
        ).arrange(RIGHT, buff=0.1)
        S_desc.shift(UP * 0.1)
        self.play(Write(S_desc), run_time=0.6)
        self.wait(0.4)

        # 微分結果
        quad_diff_label = Text("これをxで微分すると：", color=WHITE, font_size=24)
        quad_diff_label.shift(DOWN * 0.3)
        self.play(Write(quad_diff_label), run_time=0.6)
        self.wait(0.3)

        quad_diff = MathTex(
            r"\frac{\partial f}{\partial \mathbf{x}} = 2S\mathbf{x}",
            color=ORANGE, font_size=38
        )
        quad_diff.shift(DOWN * 1.5)
        quad_diff_box = SurroundingRectangle(quad_diff, color=ORANGE, buff=0.18)
        self.play(Write(quad_diff), Create(quad_diff_box), run_time=0.7)
        self.wait(1.5)

        quad_note = Text("この結果は第15話以降で活用する", color=GREEN, font_size=22, weight=BOLD)
        quad_note.shift(DOWN * 2.5)
        self.play(Write(quad_note), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(quad_intro), FadeOut(quad_form), FadeOut(quad_box),
            FadeOut(S_desc), FadeOut(quad_diff_label),
            FadeOut(quad_diff), FadeOut(quad_diff_box),
            FadeOut(quad_note), FadeOut(subtitle6),
        )
        self.wait(0.3)

        # ============================================================
        # Part 7: 正定値行列と最小値の保証
        # ============================================================
        subtitle7 = Text("正定値行列と最小値の保証", font_size=30, color=GOLD)
        subtitle7.next_to(title, DOWN)
        self.play(Write(subtitle7), run_time=0.6)
        self.wait(0.5)

        pd_def_intro = Text("正定値行列の定義：", color=WHITE, font_size=24, weight=BOLD)
        pd_def_intro.shift(UP * 1.7)
        self.play(Write(pd_def_intro), run_time=0.6)
        self.wait(0.4)

        pd_def = MathTex(
            r"\mathbf{x}^{\top} H \mathbf{x} > 0 \quad \text{for all } \mathbf{x} \neq \mathbf{0}",
            color=GOLD, font_size=32
        )
        pd_def.shift(UP * 1.0)
        pd_def_box = SurroundingRectangle(pd_def, color=GOLD, buff=0.18)
        pd_sym_note = Text("（H は対称行列）", color=WHITE, font_size=20)
        pd_sym_note.next_to(pd_def_box, RIGHT, buff=0.2)
        self.play(Write(pd_def), Create(pd_def_box), Write(pd_sym_note), run_time=0.8)
        self.wait(1.2)

        # 重要な性質
        pd_prop_title = Text("重要な性質：", color=YELLOW, font_size=24, weight=BOLD)
        pd_prop_title.shift(UP * 0.3)
        self.play(Write(pd_prop_title), run_time=0.5)
        self.wait(0.3)

        pd_prop = VGroup(
            Text("二次形式", color=WHITE, font_size=24),
            MathTex(r"f(\mathbf{x}) = \mathbf{x}^{\top} H \mathbf{x}", color=TEAL, font_size=26),
            Text("において", color=WHITE, font_size=24),
        ).arrange(RIGHT, buff=0.15)
        pd_prop.shift(DOWN * 0.2)
        self.play(Write(pd_prop), run_time=0.6)
        self.wait(0.3)

        pd_result = VGroup(
            MathTex(r"\frac{\partial f}{\partial \mathbf{x}} = 2H\mathbf{x} = \mathbf{0}", color=ORANGE, font_size=28),
            Text("を解いて得られる", color=WHITE, font_size=24),
            MathTex(r"\mathbf{x}", color=ORANGE, font_size=28),
            Text("は", color=WHITE, font_size=24),
        ).arrange(RIGHT, buff=0.15)
        pd_result.shift(DOWN * 0.8)
        self.play(Write(pd_result), run_time=0.7)
        self.wait(0.3)

        pd_guarantee = VGroup(
            Text("必ず", color=RED, font_size=28, weight=BOLD),
            Text("最小値", color=RED, font_size=28, weight=BOLD),
            Text("を与える！", color=WHITE, font_size=28),
        ).arrange(RIGHT, buff=0.1)
        pd_guarantee.shift(DOWN * 1.4)
        pd_guarantee_box = SurroundingRectangle(pd_guarantee, color=RED, buff=0.15)
        self.play(Write(pd_guarantee), Create(pd_guarantee_box), run_time=0.7)
        self.wait(1.5)

        pd_intuition = VGroup(
            Text("直観：H が正定値 ⟺ 関数が「下に凸の椀型」", color=WHITE, font_size=21),
            Text("→ 微分が0になる点は一意な大域最小値", color=TEAL, font_size=21),
        ).arrange(DOWN, buff=0.1)
        pd_intuition.shift(DOWN * 2.3)
        self.play(Write(pd_intuition), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(pd_def_intro), FadeOut(pd_def), FadeOut(pd_def_box), FadeOut(pd_sym_note),
            FadeOut(pd_prop_title), FadeOut(pd_prop), FadeOut(pd_result),
            FadeOut(pd_guarantee), FadeOut(pd_guarantee_box),
            FadeOut(pd_intuition), FadeOut(subtitle7),
        )
        self.wait(0.3)

        # ============================================================
        # Part 8: まとめ
        # ============================================================
        subtitle_end = Text("まとめ", font_size=36, color=GOLD, weight=BOLD)
        subtitle_end.next_to(title, DOWN)
        self.play(Write(subtitle_end), run_time=0.7)
        self.wait(0.5)

        summary = VGroup(
            VGroup(
                Text("1.", color=WHITE, font_size=30, weight=BOLD),
                Text("勾配を使った最大・最小探索が機械学習の基本（詳しくは次回）", color=WHITE, font_size=28),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("2.", color=WHITE, font_size=30, weight=BOLD),
                VGroup(
                    Text("上限・下限：関数値の「限界」を表す概念", color=WHITE, font_size=28),
                    Text("上限 = 最小の上界、下限 = 最大の下界", color=ORANGE, font_size=26),
                ).arrange(DOWN, buff=0.08, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("3.", color=WHITE, font_size=30, weight=BOLD),
                VGroup(
                    Text("極大・極小（1変数）：「微分=0 かつ 2次微分の符号」で判定", color=WHITE, font_size=28),
                    Text("最大・最小の手がかりとなる", color=ORANGE, font_size=26),
                ).arrange(DOWN, buff=0.08, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("4.", color=WHITE, font_size=30, weight=BOLD),
                VGroup(
                    MathTex(r"\mathbf{x}^{\top} H \mathbf{x}", color=TEAL, font_size=32),
                    Text("の停留点は、H が正定値なら一意な大域最小値", color=WHITE, font_size=28),
                ).arrange(RIGHT, buff=0.1),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        summary.scale(0.88)
        summary.shift(DOWN * 0.2)

        for point in summary:
            self.play(Write(point), run_time=0.7)
            self.wait(0.3)

        self.wait(1.5)

        all_final = VGroup(summary, subtitle_end, title)
        self.play(FadeOut(all_final), run_time=1.0)
        self.wait(0.5)
