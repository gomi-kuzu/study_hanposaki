from manim import *
import numpy as np

class LeastSquaresAnalyticalSolution(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        # タイトル
        title = Text("最小二乗法の解析解とモデリングのアート性", font_size=32, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)

        # ============================================================
        # Part 1: 前回の復習
        # ============================================================
        subtitle1 = Text("前回のまとめ：コスト関数の行列表現", font_size=28, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.4)

        recap_intro = Text("前回導出したコスト関数（行列形式）：", color=WHITE, font_size=26)
        recap_intro.shift(UP * 1.6)
        self.play(Write(recap_intro), run_time=0.5)
        self.wait(0.3)

        recap_cost = MathTex(
            r"J(\mathbf{w}) = (\mathbf{y} - X\mathbf{w})^\top (\mathbf{y} - X\mathbf{w})",
            color=ORANGE, font_size=34
        )
        recap_cost.shift(UP * 0.8)
        recap_cost_box = SurroundingRectangle(recap_cost, color=ORANGE, buff=0.15)
        self.play(Write(recap_cost), Create(recap_cost_box), run_time=0.7)
        self.wait(0.4)

        recap_labels = VGroup(
            MathTex(r"\mathbf{y} \in \mathbb{R}^N", color=YELLOW, font_size=24),
            Text("：観測出力、　", color=WHITE, font_size=20),
            MathTex(r"X \in \mathbb{R}^{N \times (D+1)}", color=TEAL, font_size=24),
            Text("：データ行列、　", color=WHITE, font_size=20),
            MathTex(r"\mathbf{w} \in \mathbb{R}^{D+1}", color=YELLOW, font_size=24),
            Text("：パラメータ", color=WHITE, font_size=20),
        ).arrange(RIGHT, buff=0.1)
        recap_labels.shift(UP * 0.05)
        self.play(Write(recap_labels), run_time=0.6)
        self.wait(0.4)

        recap_goal = VGroup(
            Text("目標：この", color=WHITE, font_size=26),
            MathTex(r"J(\mathbf{w})", color=ORANGE, font_size=30),
            Text("を最小にする", color=WHITE, font_size=26),
            MathTex(r"\hat{\mathbf{w}}", color=YELLOW, font_size=30),
            Text("を求める", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.1)
        recap_goal.shift(DOWN * 0.7)
        self.play(Write(recap_goal), run_time=0.6)
        self.wait(0.3)

        recap_method = VGroup(
            Text("14話で学んだ偏微分=0 の条件を使う！", color=GREEN, font_size=23, weight=BOLD),
        )
        recap_method.shift(DOWN * 1.3)
        self.play(Write(recap_method), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(recap_intro), FadeOut(recap_cost), FadeOut(recap_cost_box),
            FadeOut(recap_labels), FadeOut(recap_goal), FadeOut(recap_method),
            FadeOut(subtitle1),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: 偏微分による最小化（導出）
        # ============================================================
        subtitle2 = Text("偏微分によるコスト最小化の導出", font_size=28, color=ORANGE)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.4)

        deriv_intro = Text("J(w) を w で偏微分し、0 と置くことで最適解を求める", color=WHITE, font_size=26)
        deriv_intro.shift(UP * 1.7)
        self.play(Write(deriv_intro), run_time=0.6)
        self.wait(0.3)

        # 展開ステップ
        step_expand_title = Text("Step 1：コスト関数を展開する", color=TEAL, font_size=22, weight=BOLD)
        step_expand_title.shift(UP * 1.1)
        self.play(Write(step_expand_title), run_time=0.4)
        self.wait(0.2)

        expand1 = MathTex(
            r"J(\mathbf{w}) = \mathbf{y}^\top\mathbf{y}"
            r"- 2\mathbf{w}^\top X^\top \mathbf{y}"
            r"+ \mathbf{w}^\top X^\top X \mathbf{w}",
            color=WHITE, font_size=30
        )
        expand1.shift(UP * 0.35)
        self.play(Write(expand1), run_time=0.7)
        self.wait(0.5)

        expand_hint = VGroup(
            Text("（", color=WHITE, font_size=20),
            MathTex(r"(\mathbf{a}-\mathbf{b})^\top(\mathbf{a}-\mathbf{b})"
                    r"= \mathbf{a}^\top\mathbf{a} - 2\mathbf{b}^\top\mathbf{a} + \mathbf{b}^\top\mathbf{b}",
                    color=GRAY, font_size=20),
            Text("を利用）", color=WHITE, font_size=20),
        ).arrange(RIGHT, buff=0.1)
        expand_hint.shift(DOWN * 0.3)
        self.play(Write(expand_hint), run_time=0.5)
        self.wait(0.5)

        # 偏微分ステップ
        step_diff_title = Text("Step 2：w で偏微分する", color=TEAL, font_size=22, weight=BOLD)
        step_diff_title.shift(DOWN * 0.9)
        self.play(Write(step_diff_title), run_time=0.4)
        self.wait(0.2)

        diff_expr = MathTex(
            r"\frac{\partial J}{\partial \mathbf{w}}"
            r"= -2 X^\top \mathbf{y} + 2 X^\top X \mathbf{w}",
            color=WHITE, font_size=30
        )
        diff_expr.shift(DOWN * 1.6)
        self.play(Write(diff_expr), run_time=0.6)
        self.wait(0.5)

        # =0 とおく
        set_zero = MathTex(
            r"\frac{\partial J}{\partial \mathbf{w}} = \mathbf{0}",
            color=YELLOW, font_size=30
        )
        set_zero.shift(DOWN * 2.4)
        set_zero_arr = MathTex(r"\Longrightarrow", color=WHITE, font_size=30)
        set_zero_arr.next_to(set_zero, RIGHT, buff=0.2)
        normal_eq = MathTex(
            r"X^\top X \mathbf{w} = X^\top \mathbf{y}",
            color=ORANGE, font_size=30
        )
        normal_eq.next_to(set_zero_arr, RIGHT, buff=0.2)
        normal_eq_label = Text("（正規方程式）", color=ORANGE, font_size=24)
        normal_eq_label.next_to(normal_eq, RIGHT, buff=0.2)
        self.play(Write(set_zero), run_time=0.4)
        self.play(Write(set_zero_arr), Write(normal_eq), Write(normal_eq_label), run_time=0.6)
        self.wait(1.2)

        self.play(
            FadeOut(deriv_intro), FadeOut(step_expand_title),
            FadeOut(expand1), FadeOut(expand_hint),
            FadeOut(step_diff_title), FadeOut(diff_expr),
            FadeOut(set_zero), FadeOut(set_zero_arr),
            FadeOut(normal_eq), FadeOut(normal_eq_label),
            FadeOut(subtitle2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: 解析解の導出
        # ============================================================
        subtitle3 = Text("解析解の導出", font_size=28, color=TEAL)
        subtitle3.next_to(title, DOWN)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.4)

        normal_recap = MathTex(
            r"X^\top X \mathbf{w} = X^\top \mathbf{y}",
            color=ORANGE, font_size=30
        )
        normal_recap.shift(UP * 1.5)
        # normal_recap_label = Text("正規方程式", color=ORANGE, font_size=20)
        # normal_recap_label.next_to(normal_recap, RIGHT, buff=0.3)
        self.play(Write(normal_recap), run_time=0.5)
        self.wait(0.3)

        # 逆行列で解く
        solve_note = VGroup(
            Text("両辺に左から", color=WHITE, font_size=22),
            MathTex(r"(X^\top X)^{-1}", color=WHITE, font_size=26),
            Text("を掛けると…", color=WHITE, font_size=22)
        ).arrange(RIGHT, buff=0.15)
        solve_note.shift(UP * 0.7)
        self.play(Write(solve_note), run_time=0.5)
        self.wait(0.3)

        solution = MathTex(
            r"\hat{\mathbf{w}} = (X^\top X)^{-1} X^\top \mathbf{y}",
            color=YELLOW, font_size=38
        )
        solution.shift(DOWN * 0.1)
        solution_box = SurroundingRectangle(solution, color=YELLOW, buff=0.2)
        self.play(Write(solution), Create(solution_box), run_time=0.8)
        self.wait(0.6)

        pseudo_note = VGroup(
            MathTex(r"(X^\top X)^{-1} X^\top", color=TEAL, font_size=26),
            Text("← ※これは", color=WHITE, font_size=21),
            Text("左疑似逆行列", color=TEAL, font_size=21, weight=BOLD),
        ).arrange(RIGHT, buff=0.15)
        pseudo_note.shift(DOWN * 1.0)
        self.play(Write(pseudo_note), run_time=0.6)
        self.wait(0.5)

        pseudo_notation = MathTex(
            r"X^+ \equiv (X^\top X)^{-1} X^\top \quad \Rightarrow \quad \hat{\mathbf{w}} = X^+ \mathbf{y}",
            color=TEAL, font_size=26
        )
        pseudo_notation.shift(DOWN * 1.7)
        self.play(Write(pseudo_notation), run_time=0.6)
        self.wait(0.5)

        future_notes = VGroup(
            VGroup(
                Text("●", color=GRAY, font_size=20),
                Text("疑似逆行列の詳細は 18話 で扱う", color=GRAY, font_size=21),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("●", color=GRAY, font_size=20),
                MathTex(r"X^\top X", color=GRAY, font_size=22),
                Text("の逆行列が存在する条件は 16話 で扱う", color=GRAY, font_size=21),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        future_notes.shift(DOWN * 2.55)
        for item in future_notes:
            self.play(Write(item), run_time=0.5)
            self.wait(0.2)
        self.wait(1.2)

        self.play(
            FadeOut(normal_recap), #FadeOut(normal_recap_label),
            FadeOut(solve_note),
            FadeOut(solution), FadeOut(solution_box),
            FadeOut(pseudo_note), FadeOut(pseudo_notation),
            FadeOut(future_notes),
            FadeOut(subtitle3),
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: この解は必ず最小値
        # ============================================================
        subtitle4 = Text("この解は必ず最小値を与える", font_size=28, color=GREEN)
        subtitle4.next_to(title, DOWN)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.4)

        min_intro = Text("二乗誤差コスト J(w) はパラメータ w の凸関数！", color=WHITE, font_size=26)
        min_intro.shift(UP * 1.75)
        self.play(Write(min_intro), run_time=0.6)
        self.wait(0.4)

        # 凸関数のイメージ（放物面の断面）
        ax_conv = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[0, 5, 1],
            x_length=5.0, y_length=2.8,
            axis_config={"color": GRAY, "include_tip": True},
        ).scale(0.8)
        ax_conv.shift(DOWN * 0.4 + LEFT * 2.3)
        conv_curve = ax_conv.plot(lambda w: w**2 + 0.3, color=ORANGE, stroke_width=3)
        conv_min_dot = Dot(ax_conv.c2p(0, 0.3), color=YELLOW, radius=0.1)
        conv_min_label = MathTex(r"\hat{\mathbf{w}}", color=YELLOW, font_size=24)
        conv_min_label.next_to(conv_min_dot, DOWN, buff=0.15)
        w_ax_label = ax_conv.get_x_axis_label(MathTex(r"w", font_size=24), direction=RIGHT)
        j_ax_label = ax_conv.get_y_axis_label(MathTex(r"J(w)", font_size=24), direction=UP)

        self.play(Create(ax_conv), Write(w_ax_label), Write(j_ax_label), run_time=0.5)
        self.play(Create(conv_curve), run_time=0.5)
        self.play(FadeIn(conv_min_dot), Write(conv_min_label), run_time=0.4)
        self.wait(0.3)

        convex_props = VGroup(

            VGroup(
                Text("●", color=TEAL, font_size=20),
                Text("凸関数の停留点（∂J/∂w = 0）は必ず大域最小", color=WHITE, font_size=22),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("●", color=TEAL, font_size=20),
                Text("制約なしの場合、正規方程式の解が唯一の最小解", color=WHITE, font_size=22),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        convex_props.shift(RIGHT * 2.3 + DOWN * 0.3)
        for item in convex_props:
            self.play(Write(item), run_time=0.5)
            self.wait(0.2)
        self.wait(1.2)

        self.play(
            FadeOut(min_intro),
            FadeOut(ax_conv), FadeOut(w_ax_label), FadeOut(j_ax_label),
            FadeOut(conv_curve), FadeOut(conv_min_dot), FadeOut(conv_min_label),
            FadeOut(convex_props),
            FadeOut(subtitle4),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: モデリングのアート性 ── 他のノルムとの比較
        # ============================================================
        subtitle5 = Text("モデリングの「アート性」：コスト関数の選択", font_size=27, color=ORANGE)
        subtitle5.next_to(title, DOWN)
        self.play(Write(subtitle5), run_time=0.6)
        self.wait(0.4)

        art_intro = VGroup(
            Text("二乗誤差（L2 ノルム）は「唯一の正解」ではない", color=YELLOW, font_size=26, weight=BOLD),
            Text("回帰のコスト関数には複数の選択肢がある", color=WHITE, font_size=26),
        ).arrange(DOWN, buff=0.12)
        art_intro.shift(UP * 1.75)
        self.play(Write(art_intro), run_time=0.7)
        self.wait(0.5)

        # 3つのノルムを比較するグラフ
        ax_norm = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[0, 4, 1],
            x_length=5.0, y_length=4.0,
            axis_config={"color": GRAY, "include_tip": True},
            x_axis_config={"include_numbers": True},
            y_axis_config={"include_numbers": True},
        ).scale(0.75)
        ax_norm.shift(DOWN * 0.9 + LEFT * 1.8)

        e_label = ax_norm.get_x_axis_label(MathTex(r"e = y_n - f(\mathbf{x}_n)", font_size=24), direction=RIGHT)
        cost_label = ax_norm.get_y_axis_label(MathTex(r"|e|^p", font_size=24), direction=UP)

        # L2 ノルム: e^2
        l2_curve = ax_norm.plot(lambda e: e**2, x_range=[-2, 2], color=ORANGE, stroke_width=3)
        l2_label = MathTex(r"L_2:\ |e|^2", color=ORANGE, font_size=24)
        l2_label.next_to(ax_norm, RIGHT, buff=0.2).shift(UP * 0.8)

        # L1 ノルム: |e|
        l1_curve = ax_norm.plot(lambda e: abs(e), x_range=[-2, 2], color=BLUE, stroke_width=3)
        l1_label = MathTex(r"L_1:\ |e|", color=BLUE, font_size=24)
        l1_label.next_to(l2_label, DOWN, buff=0.3)

        # L1/2 ノルム: |e|^(1/2)
        eps = 0.01
        l_half_curve = ax_norm.plot(
            lambda e: abs(e)**0.5, x_range=[-2, 2], color=GREEN, stroke_width=3
        )
        l_half_label = MathTex(r"L_{1/2}:\ |e|^{1/2}", color=GREEN, font_size=24)
        l_half_label.next_to(l1_label, DOWN, buff=0.3)

        self.play(Create(ax_norm), Write(e_label), Write(cost_label), run_time=0.5)
        self.play(Create(l2_curve), Write(l2_label), run_time=0.6)
        self.wait(0.3)
        self.play(Create(l1_curve), Write(l1_label), run_time=0.6)
        self.wait(0.3)
        self.play(Create(l_half_curve), Write(l_half_label), run_time=0.6)
        self.wait(0.5)

        # 原点付近を強調する矢印
        origin_arrow = Arrow(
            ax_norm.c2p(0.8, 1.5), ax_norm.c2p(0.05, 0.22),
            color=WHITE, buff=0.05, stroke_width=2, max_tip_length_to_length_ratio=0.2
        )
        origin_note = Text("原点付近での挙動が異なる", color=WHITE, font_size=19)
        origin_note.move_to(ax_norm.c2p(-4.0, 1.0))
        self.play(Create(origin_arrow), Write(origin_note), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(ax_norm), FadeOut(e_label), FadeOut(cost_label),
            FadeOut(l2_curve), FadeOut(l2_label),
            FadeOut(l1_curve), FadeOut(l1_label),
            FadeOut(l_half_curve), FadeOut(l_half_label),
            FadeOut(origin_arrow), FadeOut(origin_note),
        )
        self.wait(0.2)

        # 各ノルムの特性比較テキスト
        norm_compare = VGroup(
            VGroup(
                MathTex(r"L_2", color=ORANGE, font_size=26),
                Text("：微分可能、解析解あり、外れ値に敏感（二乗で増大）", color=WHITE, font_size=21),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                MathTex(r"L_1", color=BLUE, font_size=26),
                Text("：原点で微分不可、外れ値にロバスト（中央値回帰 = LAD 回帰に相当）", color=WHITE, font_size=21),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                MathTex(r"L_{1/2}", color=GREEN, font_size=26),
                Text("：原点で微分不可、小さい誤差に特に敏感（原点付近で勾配→∞）", color=WHITE, font_size=21),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        norm_compare.shift(UP * 0.3)
        for item in norm_compare:
            self.play(Write(item), run_time=0.5)
            self.wait(0.2)
        self.wait(0.5)

        nondiff_note = VGroup(
            Text("●", color=RED, font_size=20),
            MathTex(r"L_1,\ L_{1/2}", color=RED, font_size=23),
            Text("は原点周辺で微分不可 → 正規方程式での閉形式解が得られない", color=WHITE, font_size=21),
        ).arrange(RIGHT, buff=0.15)
        nondiff_note.shift(DOWN * 1.1)
        sensitive_note = VGroup(
            Text("●", color=GREEN, font_size=20),
            Text("一方、原点付近の小さい誤差に対して L2 より敏感 → この性質を活かしたい場面もある", color=WHITE, font_size=21),
        ).arrange(RIGHT, buff=0.15)
        sensitive_note.shift(DOWN * 1.7)
        self.play(Write(nondiff_note), run_time=0.5)
        self.wait(0.3)
        self.play(Write(sensitive_note), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(art_intro),
            FadeOut(norm_compare),
            FadeOut(nondiff_note), FadeOut(sensitive_note),
            FadeOut(subtitle5),
        )
        self.wait(0.3)

        # ============================================================
        # Part 6: "アート" としてのモデリング
        # ============================================================
        subtitle6 = Text("モデリングはデータサイエンスの「アート」", font_size=27, color=YELLOW)
        subtitle6.next_to(title, DOWN)
        self.play(Write(subtitle6), run_time=0.6)
        self.wait(0.4)

        art_message = VGroup(
            Text("何を基準とするかは、経験と直感で人が選ぶ", color=YELLOW, font_size=24, weight=BOLD),
            Text("これがデータサイエンスで「アート」と呼ばれる所以", color=WHITE, font_size=23),
        ).arrange(DOWN, buff=0.15)
        art_message.shift(UP * 1.5)
        self.play(Write(art_message), run_time=0.7)
        self.wait(0.5)

        art_points = VGroup(
            VGroup(
                Text("●", color=TEAL, font_size=22),
                Text("数学的に厳密な解が得られる場合でも", color=WHITE, font_size=26),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("　", color=TEAL, font_size=22),
                Text("その「準備段階（コスト関数・モデルの選択）」は一意ではない", color=ORANGE, font_size=26),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("●", color=TEAL, font_size=22),
                Text("同じ L2 コストでも、異なるモデル設計により解は変わる", color=WHITE, font_size=26),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("●", color=TEAL, font_size=22),
                Text("データの背景・ドメイン知識を踏まえた選択が本質的", color=WHITE, font_size=26),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        art_points.shift(DOWN * 0.4)
        for item in art_points:
            self.play(Write(item), run_time=0.5)
            self.wait(0.2)
        self.wait(0.5)

        art_final = VGroup(
            Text("「解が求まること」と「正しい解を求めること」は別の話", color=YELLOW, font_size=24, weight=BOLD),
        )
        art_final.shift(DOWN * 2.3)
        self.play(Write(art_final), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(art_message), FadeOut(art_points), FadeOut(art_final),
            FadeOut(subtitle6),
        )
        self.wait(0.3)

        # ============================================================
        # Part 7: まとめ
        # ============================================================
        subtitle_end = Text("まとめ", font_size=36, color=GOLD, weight=BOLD)
        subtitle_end.next_to(title, DOWN)
        self.play(Write(subtitle_end), run_time=0.7)
        self.wait(0.5)

        summary = VGroup(
            VGroup(
                Text("1.", color=GOLD, font_size=26, weight=BOLD),
                VGroup(
                    Text("正規方程式を偏微分=0 から導出", color=WHITE, font_size=28),
                    MathTex(r"X^\top X \mathbf{w} = X^\top \mathbf{y}", color=ORANGE, font_size=30),
                ).arrange(DOWN, buff=0.08, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("2.", color=GOLD, font_size=26, weight=BOLD),
                VGroup(
                    Text("解析解（疑似逆行列が現れる）", color=WHITE, font_size=28),
                    MathTex(r"\hat{\mathbf{w}} = (X^\top X)^{-1} X^\top \mathbf{y}", color=YELLOW, font_size=30),
                    Text("詳細：疑似逆行列→18話 / 逆行列の存在条件→16話", color=GRAY, font_size=26),
                ).arrange(DOWN, buff=0.08, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("3.", color=GOLD, font_size=26, weight=BOLD),
                VGroup(
                    Text("J(w) は凸関数 → 停留点は必ず大域最小", color=WHITE, font_size=28),
                ).arrange(DOWN, buff=0.08, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("4.", color=GOLD, font_size=26, weight=BOLD),
                VGroup(
                    Text("コスト関数の選択はモデリングの「アート」", color=ORANGE, font_size=28),
                    Text("L1/L½は解析解なし、しかし小誤差に敏感という利点も", color=WHITE, font_size=26),
                    Text("→ データの背景を見て最善の選択を！", color=GREEN, font_size=26, weight=BOLD),
                ).arrange(DOWN, buff=0.08, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        summary.scale(0.88)
        summary.shift(DOWN * 0.3)

        for point in summary:
            self.play(Write(point), run_time=0.7)
            self.wait(0.3)

        self.wait(1.5)

        all_final = VGroup(summary, subtitle_end, title)
        self.play(FadeOut(all_final), run_time=1.0)
        self.wait(0.5)
