from manim import *
import numpy as np

class OrthogonalPolynomials(Scene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"
        
        # タイトル
        title = Text("多項式の基底: 直交多項式", font_size=40, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)
        
        # === イントロ ===
        intro_text = VGroup(
            Text("単項式の基底 {1, x, x², ...} 以外にも", color=WHITE, font_size=32, weight=BOLD),
            Text("様々な多項式の基底が存在する", color=YELLOW, font_size=32),
        ).arrange(DOWN, buff=0.4)
        intro_text.shift(DOWN * 0.5)
        
        self.play(Write(intro_text), run_time=1.2)
        self.wait(1.5)
        
        self.play(FadeOut(intro_text))
        self.wait(0.3)
        
        # === パート1: エルミート多項式の紹介 ===
        subtitle1 = Text("エルミート多項式（確率論者版）", font_size=32, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.5)
        
        # 説明
        hermite_intro = Text(
            "確率論・統計学でよく使われる多項式の基底",
            color=WHITE, font_size=26, slant=ITALIC
        )
        hermite_intro.shift(UP * 2.2)
        self.play(Write(hermite_intro), run_time=0.8)
        self.wait(0.8)
        
        # 漸化式の表示
        recurrence_label = Text("漸化式で定義:", color=YELLOW, font_size=24, weight=BOLD)
        recurrence_label.shift(UP * 1.4 + LEFT * 4)
        self.play(Write(recurrence_label), run_time=0.5)
        self.wait(0.3)
        
        recurrence_formula = MathTex(
            r"H_{n+1}(x) = 2xH_n(x) - 2nH_{n-1}(x)",
            color=BLUE, font_size=32
        )
        recurrence_formula.next_to(recurrence_label, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(recurrence_formula), run_time=0.9)
        self.wait(0.8)
        
        # 初期条件
        initial_label = Text("初期条件:", color=YELLOW, font_size=24, weight=BOLD)
        initial_label.next_to(recurrence_formula, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(Write(initial_label), run_time=0.5)
        self.wait(0.3)
        
        initial_cond = MathTex(
            r"H_0(x) = 1, \quad H_1(x) = 2x",
            color=BLUE, font_size=32
        )
        initial_cond.next_to(initial_label, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(initial_cond), run_time=0.7)
        self.wait(1.0)
        
        self.play(
            FadeOut(hermite_intro), FadeOut(recurrence_label), 
            FadeOut(recurrence_formula), FadeOut(initial_label), FadeOut(initial_cond)
        )
        self.wait(0.3)
        
        # 具体的な式を表示
        formulas_label = Text("最初のいくつか:", color=YELLOW, font_size=26, weight=BOLD)
        formulas_label.shift(UP * 2 + LEFT * 4.5)
        self.play(Write(formulas_label), run_time=0.5)
        self.wait(0.3)
        
        hermite_formulas = VGroup(
            MathTex(r"H_0(x) = 1", color=BLUE, font_size=28),
            MathTex(r"H_1(x) = 2x", color=BLUE, font_size=28),
            MathTex(r"H_2(x) = 4x^2 - 2", color=BLUE, font_size=28),
            MathTex(r"H_3(x) = 8x^3 - 12x", color=BLUE, font_size=28),
            MathTex(r"H_4(x) = 16x^4 - 48x^2 + 12", color=BLUE, font_size=28),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        hermite_formulas.next_to(formulas_label, DOWN, buff=0.3, aligned_edge=LEFT)
        
        for formula in hermite_formulas:
            self.play(Write(formula), run_time=0.5)
            self.wait(0.3)
        
        self.wait(0.8)
        
        # プロットの準備
        plot_label = Text("グラフで見てみよう:", color=YELLOW, font_size=26, weight=BOLD)
        plot_label.shift(UP * 2 + RIGHT * 2)
        self.play(Write(plot_label), run_time=0.5)
        self.wait(0.3)
        
        # 座標軸の作成
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-10, 10, 5],
            x_length=5,
            y_length=4,
            axis_config={"color": GRAY, "include_numbers": False},
            tips=False,
        )
        axes.shift(RIGHT * 2.5 + DOWN * 0.5)
        
        # 軸ラベル
        x_label = MathTex("x", font_size=24, color=GRAY).next_to(axes.x_axis.get_right(), DOWN)
        y_label = MathTex("H_n(x)", font_size=24, color=GRAY).next_to(axes.y_axis.get_top(), LEFT)
        
        self.play(Create(axes), Write(x_label), Write(y_label), run_time=0.8)
        self.wait(0.5)
        
        # エルミート多項式の定義（確率論者版）
        def hermite(n, x):
            if n == 0:
                return np.ones_like(x)
            elif n == 1:
                return 2*x
            elif n == 2:
                return 4*x**2 - 2
            elif n == 3:
                return 8*x**3 - 12*x
            elif n == 4:
                return 16*x**4 - 48*x**2 + 12
            return np.zeros_like(x)
        
        # グラフの色
        colors = [RED, YELLOW, GREEN, PURPLE, ORANGE]
        
        # グラフのプロット
        graphs = []
        labels = []
        for n in range(5):
            graph = axes.plot(lambda x, n=n: hermite(n, x), 
                            x_range=[-2.5, 2.5], 
                            color=colors[n], 
                            stroke_width=3)
            graphs.append(graph)
            
            # ラベル
            label = MathTex(f"H_{n}", font_size=20, color=colors[n])
            if n == 0:
                label.move_to(axes.c2p(2.5, 1))
            elif n == 1:
                label.move_to(axes.c2p(2.2, 2.2))
            elif n == 2:
                label.move_to(axes.c2p(2.5, 5))
            elif n == 3:
                label.move_to(axes.c2p(2.0, -6))
            else:  # n == 4
                label.move_to(axes.c2p(2.5, 8))
            labels.append(label)
            
            self.play(Create(graph), Write(label), run_time=0.6)
            self.wait(0.4)
        
        self.wait(1.5)
        
        # フェードアウト
        self.play(
            FadeOut(formulas_label), FadeOut(hermite_formulas),
            FadeOut(plot_label), FadeOut(axes), FadeOut(x_label), FadeOut(y_label),
            *[FadeOut(g) for g in graphs], *[FadeOut(l) for l in labels],
            FadeOut(subtitle1)
        )
        self.wait(0.3)
        
        # === パート2: ルジャンドル多項式の紹介 ===
        subtitle2 = Text("ルジャンドル多項式", font_size=32, color=GREEN)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)
        
        # 説明
        legendre_intro = Text(
            "物理学（球面調和関数など）でよく使われる多項式",
            color=WHITE, font_size=26, slant=ITALIC
        )
        legendre_intro.shift(UP * 2.2)
        self.play(Write(legendre_intro), run_time=0.8)
        self.wait(0.8)
        
        # 注意書き
        domain_note = Text(
            "※ 定義域: -1 ≤ x ≤ 1",
            color=RED, font_size=24, weight=BOLD
        )
        domain_note.next_to(legendre_intro, DOWN, buff=0.3)
        self.play(Write(domain_note), run_time=0.7)
        self.wait(0.8)
        
        # 漸化式の表示
        recurrence_label2 = Text("漸化式で定義:", color=YELLOW, font_size=24, weight=BOLD)
        recurrence_label2.shift(UP * 0.8 + LEFT * 4)
        self.play(Write(recurrence_label2), run_time=0.5)
        self.wait(0.3)
        
        recurrence_formula2 = MathTex(
            r"(n+1)P_{n+1}(x) = (2n+1)xP_n(x) - nP_{n-1}(x)",
            color=GREEN, font_size=32
        )
        recurrence_formula2.next_to(recurrence_label2, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(recurrence_formula2), run_time=0.9)
        self.wait(0.8)
        
        # 初期条件
        initial_label2 = Text("初期条件:", color=YELLOW, font_size=24, weight=BOLD)
        initial_label2.next_to(recurrence_formula2, DOWN, buff=0.4, aligned_edge=LEFT)
        self.play(Write(initial_label2), run_time=0.5)
        self.wait(0.3)
        
        initial_cond2 = MathTex(
            r"P_0(x) = 1, \quad P_1(x) = x",
            color=GREEN, font_size=32
        )
        initial_cond2.next_to(initial_label2, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(initial_cond2), run_time=0.7)
        self.wait(1.0)
        
        self.play(
            FadeOut(legendre_intro), FadeOut(domain_note),
            FadeOut(recurrence_label2), FadeOut(recurrence_formula2),
            FadeOut(initial_label2), FadeOut(initial_cond2)
        )
        self.wait(0.3)
        
        # 具体的な式を表示
        formulas_label2 = Text("最初のいくつか:", color=YELLOW, font_size=26, weight=BOLD)
        formulas_label2.shift(UP * 2 + LEFT * 4.5)
        self.play(Write(formulas_label2), run_time=0.5)
        self.wait(0.3)
        
        legendre_formulas = VGroup(
            MathTex(r"P_0(x) = 1", color=GREEN, font_size=28),
            MathTex(r"P_1(x) = x", color=GREEN, font_size=28),
            MathTex(r"P_2(x) = \frac{1}{2}(3x^2 - 1)", color=GREEN, font_size=28),
            MathTex(r"P_3(x) = \frac{1}{2}(5x^3 - 3x)", color=GREEN, font_size=28),
            MathTex(r"P_4(x) = \frac{1}{8}(35x^4 - 30x^2 + 3)", color=GREEN, font_size=28),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        legendre_formulas.next_to(formulas_label2, DOWN, buff=0.3, aligned_edge=LEFT)
        
        for formula in legendre_formulas:
            self.play(Write(formula), run_time=0.5)
            self.wait(0.3)
        
        self.wait(0.8)
        
        # プロットの準備
        plot_label2 = Text("グラフで見てみよう:", color=YELLOW, font_size=26, weight=BOLD)
        plot_label2.shift(UP * 2 + RIGHT * 2)
        self.play(Write(plot_label2), run_time=0.5)
        self.wait(0.3)
        
        # 座標軸の作成
        axes2 = Axes(
            x_range=[-1.2, 1.2, 0.5],
            y_range=[-1.2, 1.2, 0.5],
            x_length=5,
            y_length=4,
            axis_config={"color": GRAY, "include_numbers": False},
            tips=False,
        )
        axes2.shift(RIGHT * 2.5 + DOWN * 0.5)
        
        # 定義域を示す縦線
        domain_line_left = DashedLine(
            axes2.c2p(-1, -1.2), axes2.c2p(-1, 1.2),
            color=RED, stroke_width=2
        )
        domain_line_right = DashedLine(
            axes2.c2p(1, -1.2), axes2.c2p(1, 1.2),
            color=RED, stroke_width=2
        )
        
        # 軸ラベル
        x_label2 = MathTex("x", font_size=24, color=GRAY).next_to(axes2.x_axis.get_right(), DOWN)
        y_label2 = MathTex("P_n(x)", font_size=24, color=GRAY).next_to(axes2.y_axis.get_top(), LEFT)
        
        self.play(
            Create(axes2), Write(x_label2), Write(y_label2),
            Create(domain_line_left), Create(domain_line_right),
            run_time=0.8
        )
        self.wait(0.5)
        
        # ルジャンドル多項式の定義
        def legendre(n, x):
            if n == 0:
                return np.ones_like(x)
            elif n == 1:
                return x
            elif n == 2:
                return 0.5 * (3*x**2 - 1)
            elif n == 3:
                return 0.5 * (5*x**3 - 3*x)
            elif n == 4:
                return 0.125 * (35*x**4 - 30*x**2 + 3)
            return np.zeros_like(x)
        
        # グラフの色
        colors2 = [RED, YELLOW, BLUE, PURPLE, ORANGE]
        
        # グラフのプロット
        graphs2 = []
        labels2 = []
        for n in range(5):
            graph = axes2.plot(lambda x, n=n: legendre(n, x), 
                             x_range=[-1, 1], 
                             color=colors2[n], 
                             stroke_width=3)
            graphs2.append(graph)
            
            # ラベル
            label = MathTex(f"P_{n}", font_size=20, color=colors2[n])
            if n == 0:
                label.move_to(axes2.c2p(0.7, 1.0))
            elif n == 1:
                label.move_to(axes2.c2p(0.8, 0.8))
            elif n == 2:
                label.move_to(axes2.c2p(0.5, 0.3))
            elif n == 3:
                label.move_to(axes2.c2p(0.9, -0.9))
            else:  # n == 4
                label.move_to(axes2.c2p(0.3, -0.8))
            labels2.append(label)
            
            self.play(Create(graph), Write(label), run_time=0.6)
            self.wait(0.4)
        
        self.wait(1.5)
        
        # フェードアウト
        self.play(
            FadeOut(formulas_label2), FadeOut(legendre_formulas),
            FadeOut(plot_label2), FadeOut(axes2), FadeOut(x_label2), FadeOut(y_label2),
            FadeOut(domain_line_left), FadeOut(domain_line_right),
            *[FadeOut(g) for g in graphs2], *[FadeOut(l) for l in labels2],
            FadeOut(subtitle2)
        )
        self.wait(0.3)
        
        # === まとめ ===
        summary_subtitle = Text("まとめ", font_size=32, color=GOLD, weight=BOLD)
        summary_subtitle.next_to(title, DOWN)
        self.play(Write(summary_subtitle), run_time=0.6)
        self.wait(0.5)
        
        # まとめのポイント
        summary_points = VGroup(
            VGroup(
                Text("1.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("エルミート多項式とルジャンドル多項式は", color=WHITE, font_size=24),
                    Text("それぞれ多項式空間の基底になる", color=YELLOW, font_size=24, weight=BOLD),
                ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            
            VGroup(
                Text("2.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("どちらも漸化式で定義される", color=WHITE, font_size=24),
                    Text("多項式の系列", color=BLUE, font_size=24, weight=BOLD),
                ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            
            VGroup(
                Text("3.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("エルミート多項式: 確率論・統計学で重要", color=WHITE, font_size=24),
                    Text("ルジャンドル多項式: 物理学で重要", color=GREEN, font_size=24, weight=BOLD),
                ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            
            VGroup(
                Text("4.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("単項式の場合 {1, x, x², ...} とは", color=WHITE, font_size=24),
                    Text("異なる見た目と性質を持つ", color=ORANGE, font_size=24, weight=BOLD),
                ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        summary_points.scale(0.9)
        summary_points.shift(UP * 0.1)
        
        for point in summary_points:
            self.play(Write(point), run_time=0.9)
            self.wait(0.6)
        
        self.wait(1.5)
        
        # 最終メッセージ
        final_message = Text(
            "これらの多項式の詳しい性質は次回以降で!",
            color=YELLOW, font_size=28, weight=BOLD, slant=ITALIC
        )
        final_message.shift(DOWN * 2.5)
        final_box = SurroundingRectangle(final_message, color=YELLOW, buff=0.25)
        self.play(Write(final_message), Create(final_box), run_time=1.0)
        self.wait(2.0)
        
        # フェードアウト
        self.play(
            FadeOut(summary_points), FadeOut(final_message), FadeOut(final_box),
            FadeOut(summary_subtitle)
        )
        self.wait(0.3)
        
        # === 付録: 物理学者版との比較 ===
        subtitle_appendix = Text("付録: 物理学者版との比較", font_size=32, color=PURPLE)
        subtitle_appendix.next_to(title, DOWN)
        self.play(Write(subtitle_appendix), run_time=0.6)
        self.wait(0.5)
        
        # 説明
        # comparison_note = Text(
        #     "物理学では別の定義（He_n）がよく使われる",
        #     color=WHITE, font_size=26, slant=ITALIC
        # )
        # comparison_note.shift(UP * 2.5)
        # self.play(Write(comparison_note), run_time=0.8)
        # self.wait(0.8)
        
        # 左側: 確率論者版
        prob_label = Text("確率論者版 (H_n)", color=BLUE, font_size=26, weight=BOLD)
        prob_label.shift(UP * 1.8 + LEFT * 3.2)
        
        # 右側: 物理学者版
        phys_label = Text("物理学者版 (He_n)", color=PURPLE, font_size=26, weight=BOLD)
        phys_label.shift(UP * 1.8 + RIGHT * 3.2)
        
        self.play(Write(prob_label), Write(phys_label), run_time=0.7)
        self.wait(0.5)
        
        # 左側の座標軸（確率論者版）
        axes_prob = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-10, 10, 5],
            x_length=4.5,
            y_length=3.5,
            axis_config={"color": GRAY, "include_numbers": False},
            tips=False,
        )
        axes_prob.shift(LEFT * 3.2 + DOWN * 0.3)
        
        x_label_prob = MathTex("x", font_size=20, color=GRAY).next_to(axes_prob.x_axis.get_right(), DOWN)
        y_label_prob = MathTex("H_n", font_size=20, color=BLUE).next_to(axes_prob.y_axis.get_top(), LEFT)
        
        # 右側の座標軸（物理学者版）
        axes_phys = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-10, 10, 5],
            x_length=4.5,
            y_length=3.5,
            axis_config={"color": GRAY, "include_numbers": False},
            tips=False,
        )
        axes_phys.shift(RIGHT * 3.2 + DOWN * 0.3)
        
        x_label_phys = MathTex("x", font_size=20, color=GRAY).next_to(axes_phys.x_axis.get_right(), DOWN)
        y_label_phys = MathTex(r"\text{He}_n", font_size=20, color=PURPLE).next_to(axes_phys.y_axis.get_top(), LEFT)
        
        self.play(
            Create(axes_prob), Write(x_label_prob), Write(y_label_prob),
            Create(axes_phys), Write(x_label_phys), Write(y_label_phys),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 確率論者版エルミート多項式の定義
        def hermite_prob(n, x):
            if n == 0:
                return np.ones_like(x)
            elif n == 1:
                return 2*x
            elif n == 2:
                return 4*x**2 - 2
            elif n == 3:
                return 8*x**3 - 12*x
            elif n == 4:
                return 16*x**4 - 48*x**2 + 12
            return np.zeros_like(x)
        
        # 物理学者版エルミート多項式の定義
        def hermite_phys(n, x):
            if n == 0:
                return np.ones_like(x)
            elif n == 1:
                return x
            elif n == 2:
                return x**2 - 1
            elif n == 3:
                return x**3 - 3*x
            elif n == 4:
                return x**4 - 6*x**2 + 3
            return np.zeros_like(x)
        
        # グラフの色
        colors_comp = [RED, YELLOW, GREEN, PURPLE, ORANGE]
        
        # グラフのプロット（同時に描画）
        graphs_prob = []
        graphs_phys = []
        labels_comp = []
        
        for n in range(5):
            # 確率論者版
            graph_prob = axes_prob.plot(lambda x, n=n: hermite_prob(n, x), 
                                       x_range=[-2.2, 2.2], 
                                       color=colors_comp[n], 
                                       stroke_width=2.5)
            graphs_prob.append(graph_prob)
            
            # 物理学者版
            graph_phys = axes_phys.plot(lambda x, n=n: hermite_phys(n, x), 
                                       x_range=[-2.2, 2.2], 
                                       color=colors_comp[n], 
                                       stroke_width=2.5)
            graphs_phys.append(graph_phys)
            
            # ラベル（中央下に配置）
            label = MathTex(f"n={n}", font_size=18, color=colors_comp[n])
            if n == 0:
                label.shift(DOWN * 2.3 + LEFT * 2.4)
            elif n == 1:
                label.shift(DOWN * 2.3 + LEFT * 1.2)
            elif n == 2:
                label.shift(DOWN * 2.3)
            elif n == 3:
                label.shift(DOWN * 2.3 + RIGHT * 1.2)
            else:  # n == 4
                label.shift(DOWN * 2.3 + RIGHT * 2.4)
            labels_comp.append(label)
            
            self.play(
                Create(graph_prob), Create(graph_phys), Write(label),
                run_time=0.5
            )
            self.wait(0.3)
        
        self.wait(1.0)
        
        # 関係式の表示
        relation_formula = MathTex(
            r"H_n(x) = 2^{n/2} \text{He}_n\left(\frac{x}{\sqrt{2}}\right)",
            color=ORANGE, font_size=26
        )
        relation_formula.shift(DOWN * 3.0)
        relation_box = SurroundingRectangle(relation_formula, color=ORANGE, buff=0.2)
        
        self.play(Write(relation_formula), Create(relation_box), run_time=0.9)
        self.wait(1.5)
        
        # フェードアウト
        all_appendix = VGroup(
            # comparison_note,
            prob_label, phys_label,
            axes_prob, x_label_prob, y_label_prob,
            axes_phys, x_label_phys, y_label_phys,
            *graphs_prob, *graphs_phys, *labels_comp,
            relation_formula, relation_box,
            subtitle_appendix, title
        )
        self.play(FadeOut(all_appendix), run_time=1.0)
        self.wait(0.5)
