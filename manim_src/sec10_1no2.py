from manim import *
import numpy as np

class PolynomialGramSchmidt(Scene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"
        
        # タイトル
        title = Text("多項式空間でグラム-シュミット直交化", font_size=38, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)
        
        # === イントロ: 問題設定 ===
        intro_subtitle = Text("今回の設定", font_size=32, color=YELLOW)
        intro_subtitle.next_to(title, DOWN)
        self.play(Write(intro_subtitle), run_time=0.6)
        self.wait(0.5)
        
        setup = VGroup(
            Text("4話で学んだグラム-シュミット法を多項式に適用！", color=WHITE, font_size=24, slant=ITALIC),
            VGroup(
                Text("定義域:", color=WHITE, font_size=26),
                MathTex(r"[-1, \, 1]", color=WHITE, font_size=28),
                Text("、最大次数 2 の多項式空間", color=WHITE, font_size=26),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                Text("内積: ", color=ORANGE, font_size=28),
                MathTex(r"\langle f | g \rangle = \int_{-1}^{1} f(x) \, g(x) \, dx", color=ORANGE, font_size=28),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("生成元:", color=YELLOW, font_size=26, weight=BOLD),
                MathTex(
                    r"\{ \, |1\rangle, \; |x\rangle, \; |x^2\rangle \, \}",
                    color=YELLOW, font_size=30
                ),
            ).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.35)
        setup.shift(DOWN * 0.3)
        
        self.play(Write(setup), run_time=1.2)
        self.wait(1.2)
        
        # 目標
        goal = VGroup(
            Text("目標:", color=GREEN, font_size=28, weight=BOLD),
            Text("ここから直交基底を構成する", color=GREEN, font_size=26),
        ).arrange(RIGHT, buff=0.3)
        goal.shift(DOWN * 2.5)
        goal_box = SurroundingRectangle(goal, color=GREEN, buff=0.15)
        
        self.play(Write(goal), Create(goal_box), run_time=0.8)
        self.wait(1.2)
        
        self.play(FadeOut(setup), FadeOut(goal), FadeOut(goal_box), FadeOut(intro_subtitle))
        self.wait(0.3)
        
        # === グラム-シュミット法の手順おさらい ===
        subtitle_gs = Text("グラム-シュミット法のおさらい", font_size=32, color=BLUE)
        subtitle_gs.next_to(title, DOWN)
        self.play(Write(subtitle_gs), run_time=0.6)
        self.wait(0.5)
        
        gs_procedure = VGroup(
            VGroup(
                Text("Step 1:", color=GREEN, font_size=26, weight=BOLD),
                Text("最初のベクトルをそのまま採用", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("Step 2:", color=GREEN, font_size=26, weight=BOLD),
                Text("2番目から1番目への射影を引く", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("Step 3:", color=GREEN, font_size=26, weight=BOLD),
                Text("3番目から1番目・2番目への射影を引く", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        gs_procedure.shift(UP * 0.8)
        
        for step in gs_procedure:
            self.play(Write(step), run_time=0.6)
            self.wait(0.3)
        
        self.wait(0.5)
        
        gs_formula_general = VGroup(
            Text("射影: ", color=ORANGE, font_size=28),
            MathTex(
                r"\text{proj}_{|u\rangle} |v\rangle"
                r" = \frac{\langle u | v \rangle}{\langle u | u \rangle} \, |u\rangle",
                color=ORANGE, font_size=32
            ),
        ).arrange(RIGHT, buff=0.1)
        gs_formula_general.shift(DOWN * 1.2)
        gs_box = SurroundingRectangle(gs_formula_general, color=ORANGE, buff=0.2)
        
        self.play(Write(gs_formula_general), Create(gs_box), run_time=0.8)
        self.wait(0.5)
        
        key_idea = Text(
            "ベクトルと全く同じ手順！ 内積の定義だけが違う",
            color=YELLOW, font_size=24, weight=BOLD, slant=ITALIC
        )
        key_idea.shift(DOWN * 2.5)
        self.play(Write(key_idea), run_time=0.7)
        self.wait(1.0)
        
        self.play(
            FadeOut(gs_procedure), FadeOut(gs_formula_general), FadeOut(gs_box),
            FadeOut(key_idea), FadeOut(subtitle_gs)
        )
        self.wait(0.3)
        
        # === パート1: Step 1 - |1⟩ から始める ===
        subtitle1 = Text("Step 1: 最初のベクトル |1⟩", font_size=32, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.5)
        
        # グラム-シュミットの最初のステップ
        step1_text = VGroup(
            MathTex(r"|u_1\rangle = |1\rangle", color=BLUE, font_size=30),
            Text("（そのまま採用）", color=BLUE, font_size=26),
        ).arrange(RIGHT, buff=0.3)
        step1_text.shift(UP * 1.8)
        self.play(Write(step1_text), run_time=0.7)
        self.wait(0.6)
        
        # |1⟩ は正規化されてそう
        naive_text = Text(
            "|1⟩ は定数関数 f(x)=1 ... 正規化されてそうに見えるが？",
            color=WHITE, font_size=24, slant=ITALIC
        )
        naive_text.shift(UP * 0.8)
        self.play(Write(naive_text), run_time=0.8)
        self.wait(0.8)
        
        # ノルムを計算
        norm_label = Text("ノルムを計算してみよう:", color=YELLOW, font_size=24, weight=BOLD)
        norm_label.shift(UP * 0.0 + LEFT * 4)
        self.play(Write(norm_label), run_time=0.5)
        self.wait(0.3)
        
        norm_calc1 = MathTex(
            r"\langle 1 | 1 \rangle = \int_{-1}^{1} 1 \cdot 1 \, dx"
            r" = \Big[ x \Big]_{-1}^{1} = 1 - (-1) = 2",
            color=WHITE, font_size=26
        )
        norm_calc1.shift(DOWN * 0.7)
        self.play(Write(norm_calc1), run_time=0.9)
        self.wait(0.6)
        
        norm_calc2 = MathTex(
            r"\| \, |1\rangle \, \| = \sqrt{\langle 1 | 1 \rangle} = \sqrt{2}",
            color=WHITE, font_size=28
        )
        norm_calc2.shift(DOWN * 1.5)
        self.play(Write(norm_calc2), run_time=0.7)
        self.wait(0.8)
        
        # 驚き！
        surprise = VGroup(
            MathTex(r"\sqrt{2} \neq 1", color=RED, font_size=34),
            Text("正規化されていない！", color=RED, font_size=28, weight=BOLD),
        ).arrange(RIGHT, buff=0.5)
        surprise.shift(DOWN * 2.5)
        surprise_box = SurroundingRectangle(surprise, color=RED, buff=0.2)
        
        self.play(Write(surprise), Create(surprise_box), run_time=0.8)
        self.wait(1.2)
        
        self.play(
            FadeOut(step1_text), FadeOut(naive_text), FadeOut(norm_label),
            FadeOut(norm_calc1), FadeOut(norm_calc2),
            FadeOut(surprise), FadeOut(surprise_box)
        )
        self.wait(0.3)
        
        # 正規化
        normalize_label = Text("正規化する:", color=GREEN, font_size=26, weight=BOLD)
        normalize_label.shift(UP * 1.8 + LEFT * 4)
        self.play(Write(normalize_label), run_time=0.5)
        self.wait(0.3)
        
        normalize_formula = MathTex(
            r"|\hat{e}_1\rangle = \frac{|1\rangle}{\| \, |1\rangle \, \|}"
            r" = \frac{1}{\sqrt{2}}",
            color=GREEN, font_size=32
        )
        normalize_formula.shift(UP * 0.7)
        e1_box = SurroundingRectangle(normalize_formula, color=GREEN, buff=0.2)
        
        self.play(Write(normalize_formula), Create(e1_box), run_time=0.8)
        self.wait(0.5)
        
        # 検算
        check_norm = VGroup(
            Text("検算: ", color=GREEN, font_size=26),
            MathTex(
                r"\langle \hat{e}_1 | \hat{e}_1 \rangle"
                r" = \int_{-1}^{1} \frac{1}{2} \, dx = 1 \; \checkmark",
                color=GREEN, font_size=26
            ),
        ).arrange(RIGHT, buff=0.1)
        check_norm.shift(DOWN * 0.3)
        self.play(Write(check_norm), run_time=0.7)
        self.wait(0.8)
        
        # ポイント
        point1 = Text(
            "※ 内積の定義が変わればノルムも変わる！",
            color=ORANGE, font_size=24, slant=ITALIC
        )
        point1.shift(DOWN * 1.3)
        self.play(Write(point1), run_time=0.6)
        self.wait(0.5)
        
        # 以降の注記
        note_unnorm = Text(
            "※この動画では以降の直交化は正規化前の u₁ = |1⟩ のまま進める",
            color=GRAY, font_size=32
        )
        note_unnorm.shift(DOWN * 2.2)
        self.play(Write(note_unnorm), run_time=0.5)
        self.wait(1.0)
        
        self.play(
            FadeOut(normalize_label), FadeOut(normalize_formula), FadeOut(e1_box),
            FadeOut(check_norm), FadeOut(point1), FadeOut(note_unnorm),
            FadeOut(subtitle1)
        )
        self.wait(0.3)
        
        # === パート2: Step 2 - |x⟩ を直交化 ===
        subtitle2 = Text("Step 2: |x⟩ を直交化", font_size=32, color=GREEN)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)
        
        # 公式
        gs_formula2 = MathTex(
            r"|u_2\rangle = |x\rangle"
            r" - \frac{\langle u_1 | x \rangle}{\langle u_1 | u_1 \rangle}"
            r" \, |u_1\rangle",
            color=WHITE, font_size=28
        )
        gs_formula2.shift(UP * 1.8)
        self.play(Write(gs_formula2), run_time=0.8)
        self.wait(0.6)
        
        # 射影成分の計算
        calc2_label = Text("射影成分を計算:", color=YELLOW, font_size=24, weight=BOLD)
        calc2_label.shift(UP * 0.8 + LEFT * 5)
        self.play(Write(calc2_label), run_time=0.5)
        self.wait(0.3)
        
        calc2_inner = MathTex(
            r"\langle u_1 | x \rangle = \int_{-1}^{1} 1 \cdot x \, dx"
            r" = \left[ \frac{x^2}{2} \right]_{-1}^{1}"
            r" = \frac{1}{2} - \frac{1}{2} = 0",
            color=BLUE, font_size=24
        )
        calc2_inner.shift(UP * 0.1)
        self.play(Write(calc2_inner), run_time=0.9)
        self.wait(0.5)
        
        calc2_note = Text(
            "(被積分関数 x は奇関数 → 対称区間 [-1,1] で積分 0)",
            color=GRAY, font_size=18
        )
        calc2_note.next_to(calc2_inner, DOWN, buff=0.2)
        self.play(Write(calc2_note), run_time=0.6)
        self.wait(0.6)
        
        # 結果
        result2 = MathTex(
            r"\therefore \;\; |u_2\rangle = |x\rangle"
            r" - \frac{0}{2} \, |1\rangle = |x\rangle",
            color=GREEN, font_size=30
        )
        result2.shift(DOWN * 1.5)
        result2_box = SurroundingRectangle(result2, color=GREEN, buff=0.15)
        
        self.play(Write(result2), Create(result2_box), run_time=0.8)
        self.wait(0.8)
        
        # 解釈
        interpretation2 = Text(
            "|x⟩ はもとから |1⟩ と直交していた！ 修正不要",
            color=YELLOW, font_size=26, weight=BOLD
        )
        interpretation2.shift(DOWN * 2.6)
        self.play(Write(interpretation2), run_time=0.7)
        self.wait(1.0)
        
        self.play(
            FadeOut(gs_formula2), FadeOut(calc2_label),
            FadeOut(calc2_inner), FadeOut(calc2_note),
            FadeOut(result2), FadeOut(result2_box),
            FadeOut(interpretation2), FadeOut(subtitle2)
        )
        self.wait(0.3)
        
        # === パート3: Step 3 - |x²⟩ を直交化 ===
        subtitle3 = Text("Step 3: |x²⟩ を直交化", font_size=32, color=PURPLE)
        subtitle3.next_to(title, DOWN)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.5)
        
        # 公式
        gs_formula3 = MathTex(
            r"|u_3\rangle = |x^2\rangle"
            r" - \frac{\langle u_1 | x^2 \rangle}{\langle u_1 | u_1 \rangle}"
            r" \, |u_1\rangle"
            r" - \frac{\langle u_2 | x^2 \rangle}{\langle u_2 | u_2 \rangle}"
            r" \, |u_2\rangle",
            color=WHITE, font_size=24
        )
        gs_formula3.shift(UP * 2.0)
        self.play(Write(gs_formula3), run_time=0.9)
        self.wait(0.6)
        
        # 各内積を計算
        calc3_label = Text("各内積を計算:", color=YELLOW, font_size=24, weight=BOLD)
        calc3_label.shift(UP * 1.0 + LEFT * 5.5)
        self.play(Write(calc3_label), run_time=0.5)
        self.wait(0.3)
        
        calc3_item1 = MathTex(
            r"\langle u_1 | x^2 \rangle = \int_{-1}^{1} x^2 \, dx"
            r" = \left[ \frac{x^3}{3} \right]_{-1}^{1}"
            r" = \frac{1}{3} - \left(-\frac{1}{3}\right) = \frac{2}{3}",
            color=BLUE, font_size=22
        )
        calc3_item1.shift(UP * 1.3)
        self.play(Write(calc3_item1), run_time=0.8)
        self.wait(0.4)
        
        calc3_item2 = MathTex(
            r"\langle u_1 | u_1 \rangle = 2 \quad (\text{from Step 1})",
            color=BLUE, font_size=22
        )
        calc3_item2.next_to(calc3_item1, DOWN, buff=0.25, aligned_edge=LEFT)
        self.play(Write(calc3_item2), run_time=0.6)
        self.wait(0.3)
        
        calc3_item3 = MathTex(
            r"\langle u_2 | x^2 \rangle = \int_{-1}^{1} x \cdot x^2 \, dx"
            r" = \int_{-1}^{1} x^3 \, dx = 0",
            color=BLUE, font_size=22
        )
        calc3_item3.next_to(calc3_item2, DOWN, buff=0.25, aligned_edge=LEFT)
        
        calc3_odd_note = Text("(奇関数)", color=GRAY, font_size=16)
        calc3_odd_note.next_to(calc3_item3, RIGHT, buff=0.2)
        
        self.play(Write(calc3_item3), Write(calc3_odd_note), run_time=0.7)
        self.wait(0.5)
        
        # 代入
        substitution = MathTex(
            r"|u_3\rangle = |x^2\rangle"
            r" - \frac{2/3}{2} \, |1\rangle - 0 \cdot |x\rangle"
            r" = x^2 - \frac{1}{3}",
            color=WHITE, font_size=26
        )
        substitution.shift(DOWN * 1.2)
        self.play(Write(substitution), run_time=0.8)
        self.wait(0.6)
        
        # 結果を強調
        result3 = MathTex(
            r"|u_3\rangle = x^2 - \frac{1}{3}",
            color=PURPLE, font_size=34
        )
        result3.shift(DOWN * 2.3)
        result3_box = SurroundingRectangle(result3, color=PURPLE, buff=0.2)
        
        self.play(Write(result3), Create(result3_box), run_time=0.8)
        self.wait(1.2)
        
        self.play(
            FadeOut(gs_formula3), FadeOut(calc3_label),
            FadeOut(calc3_item1), FadeOut(calc3_item2),
            FadeOut(calc3_item3), FadeOut(calc3_odd_note),
            FadeOut(substitution), FadeOut(result3), FadeOut(result3_box),
            FadeOut(subtitle3)
        )
        self.wait(0.3)
        
        # === パート4: 直交性の確認 ===
        subtitle4 = Text("直交性を確認しよう", font_size=32, color=ORANGE)
        subtitle4.next_to(title, DOWN)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.5)
        
        # 得られた基底を再掲
        basis_result = VGroup(
            Text("得られた直交基底:", color=YELLOW, font_size=26, weight=BOLD),
            MathTex(
                r"|u_1\rangle = 1, \qquad"
                r"|u_2\rangle = x, \qquad"
                r"|u_3\rangle = x^2 - \frac{1}{3}",
                color=WHITE, font_size=26
            ),
        ).arrange(DOWN, buff=0.3)
        basis_result.shift(UP*1.5)
        
        self.play(Write(basis_result), run_time=0.8)
        self.wait(0.6)
        
        # 全ペアの内積
        check_label = Text("全ての組で内積 = 0 を確認:", color=ORANGE, font_size=24, weight=BOLD)
        check_label.shift(UP * 0.8 + LEFT * 3.5)
        self.play(Write(check_label), run_time=0.5)
        self.wait(0.3)
        
        check1 = MathTex(
            r"\langle u_1 | u_2 \rangle"
            r" = \int_{-1}^{1} 1 \cdot x \, dx = 0 \; \checkmark",
            color=GREEN, font_size=24
        )
        check1.shift(UP * 0.1 + LEFT * 1)
        self.play(Write(check1), run_time=0.6)
        self.wait(0.3)
        
        check2 = MathTex(
            r"\langle u_1 | u_3 \rangle"
            r" = \int_{-1}^{1} \!\left(x^2 - \frac{1}{3}\right) dx"
            r" = \frac{2}{3} - \frac{2}{3} = 0 \; \checkmark",
            color=GREEN, font_size=24
        )
        check2.next_to(check1, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(check2), run_time=0.7)
        self.wait(0.3)
        
        check3 = MathTex(
            r"\langle u_2 | u_3 \rangle"
            r" = \int_{-1}^{1} x \!\left(x^2 - \frac{1}{3}\right) dx"
            r" = 0 \; \checkmark",
            color=GREEN, font_size=24
        )
        check3.next_to(check2, DOWN, buff=0.3, aligned_edge=LEFT)
        
        check3_note = Text("(奇関数)", color=GRAY, font_size=16)
        check3_note.next_to(check3, RIGHT, buff=0.2)
        
        self.play(Write(check3), Write(check3_note), run_time=0.7)
        self.wait(0.6)
        
        # 成功
        success = Text(
            "すべて直交！！",
            color=GREEN, font_size=28, weight=BOLD
        )
        success.shift(DOWN * 2.5)
        success_box = SurroundingRectangle(success, color=GREEN, buff=0.15)
        self.play(Write(success), Create(success_box), run_time=0.8)
        self.wait(1.2)
        
        self.play(
            FadeOut(basis_result), FadeOut(check_label),
            FadeOut(check1), FadeOut(check2), FadeOut(check3), FadeOut(check3_note),
            FadeOut(success), FadeOut(success_box),
            FadeOut(subtitle4)
        )
        self.wait(0.3)
        
        # === パート5: グラフで可視化 ===
        subtitle5 = Text("直交基底をグラフで見る", font_size=32, color=TEAL)
        subtitle5.next_to(title, DOWN)
        self.play(Write(subtitle5), run_time=0.6)
        self.wait(0.5)
        
        # グラフ
        axes = Axes(
            x_range=[-1.4, 1.4, 0.5],
            y_range=[-0.8, 1.5, 0.5],
            x_length=8,
            y_length=4,
            axis_config={"color": GREY, "include_numbers": True, "font_size": 18},
            tips=False,
        )
        axes.shift(DOWN * 0.3)
        
        x_label = axes.get_x_axis_label(MathTex("x", font_size=24), direction=RIGHT)
        
        self.play(Create(axes), Write(x_label), run_time=0.8)
        self.wait(0.3)
        
        # 3つの多項式をプロット
        graph1 = axes.plot(lambda x: 1, x_range=[-1, 1], color=RED, stroke_width=3)
        graph2 = axes.plot(lambda x: x, x_range=[-1, 1], color=BLUE, stroke_width=3)
        graph3 = axes.plot(
            lambda x: x**2 - 1/3, x_range=[-1, 1], color=PURPLE, stroke_width=3
        )
        
        label1 = MathTex(r"|u_1\rangle = 1", color=RED, font_size=22)
        label1.next_to(axes.c2p(1.05, 1), RIGHT, buff=0.15)
        
        label2 = MathTex(r"|u_2\rangle = x", color=BLUE, font_size=22)
        label2.next_to(axes.c2p(1.05, 1), RIGHT, buff=0.15).shift(UP * 0.5)
        
        label3 = MathTex(r"|u_3\rangle = x^2 - \tfrac{1}{3}", color=PURPLE, font_size=20)
        label3.next_to(axes.c2p(1.05, 2/3), RIGHT, buff=0.15).shift(DOWN * 0.4)
        
        self.play(Create(graph1), Write(label1), run_time=0.7)
        self.wait(0.3)
        self.play(Create(graph2), Write(label2), run_time=0.7)
        self.wait(0.3)
        self.play(Create(graph3), Write(label3), run_time=0.7)
        self.wait(0.8)
        
        graph_note = Text(
            "これらは互いに「直交」した関数（積分するとゼロ）",
            color=YELLOW, font_size=22, slant=ITALIC
        )
        graph_note.shift(DOWN * 3.0)
        self.play(Write(graph_note), run_time=0.7)
        self.wait(1.2)
        
        self.play(
            FadeOut(axes), FadeOut(x_label),
            FadeOut(graph1), FadeOut(graph2), FadeOut(graph3),
            FadeOut(label1), FadeOut(label2), FadeOut(label3),
            FadeOut(graph_note), FadeOut(subtitle5)
        )
        self.wait(0.3)
        
        # === パート6: ルジャンドル多項式との関連 ===
        subtitle6 = Text("ルジャンドル多項式との関連", font_size=32, color=GOLD)
        subtitle6.next_to(title, DOWN)
        self.play(Write(subtitle6), run_time=0.6)
        self.wait(0.5)
        
        compare_intro = Text(
            "得られた結果を知られた多項式と比べてみると...",
            color=WHITE, font_size=26, slant=ITALIC
        )
        compare_intro.shift(UP * 1.8)
        self.play(Write(compare_intro), run_time=0.7)
        self.wait(0.5)
        
        # 左: 今回の結果
        our_title = Text("今回の直交基底", color=BLUE, font_size=24, weight=BOLD)
        our_title.shift(UP * 1.0 + LEFT * 3.5)
        
        our_items = VGroup(
            MathTex(r"|u_1\rangle = 1", color=BLUE, font_size=26),
            MathTex(r"|u_2\rangle = x", color=BLUE, font_size=26),
            MathTex(r"|u_3\rangle = x^2 - \frac{1}{3}", color=BLUE, font_size=26),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        our_items.next_to(our_title, DOWN, buff=0.3, aligned_edge=LEFT)
        
        # 右: ルジャンドル多項式
        leg_title = Text("ルジャンドル多項式", color=GOLD, font_size=24, weight=BOLD)
        leg_title.shift(UP * 1.0 + RIGHT * 3)
        
        leg_items = VGroup(
            MathTex(r"P_0(x) = 1", color=GOLD, font_size=26),
            MathTex(r"P_1(x) = x", color=GOLD, font_size=26),
            MathTex(r"P_2(x) = \frac{3x^2 - 1}{2}", color=GOLD, font_size=26),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        leg_items.next_to(leg_title, DOWN, buff=0.3, aligned_edge=LEFT)
        
        self.play(Write(our_title), Write(our_items), run_time=0.9)
        self.wait(0.5)
        self.play(Write(leg_title), Write(leg_items), run_time=0.9)
        self.wait(0.8)
        
        # 対応を矢印で示す
        arrows = VGroup()
        for i in range(3):
            arr = Arrow(
                our_items[i].get_right() + RIGHT * 0.15,
                leg_items[i].get_left() + LEFT * 0.15,
                color=YELLOW, stroke_width=3, buff=0.1,
                max_tip_length_to_length_ratio=0.15,
            )
            arrows.add(arr)
        
        self.play(*[Create(a) for a in arrows], run_time=0.6)
        self.wait(0.6)
        
        # 関係式
        relation = MathTex(
            r"x^2 - \frac{1}{3} = \frac{2}{3} \, P_2(x)",
            color=YELLOW, font_size=28
        )
        relation.shift(DOWN * 1.5)
        self.play(Write(relation), run_time=0.8)
        self.wait(0.5)
        
        conclusion6 = VGroup(
            Text("定数倍の違いを除いてルジャンドル多項式と一致！", color=YELLOW, font_size=24, weight=BOLD),
            Text("[-1,1] 上の積分 + 重み1 → ルジャンドル多項式が自然に現れる", color=WHITE, font_size=20),
        ).arrange(DOWN, buff=0.2)
        conclusion6.shift(DOWN * 2.5)
        self.play(Write(conclusion6), run_time=0.9)
        self.wait(1.2)
        
        self.play(
            FadeOut(compare_intro),
            FadeOut(our_title), FadeOut(our_items),
            FadeOut(leg_title), FadeOut(leg_items),
            FadeOut(arrows), FadeOut(relation), FadeOut(conclusion6),
            FadeOut(subtitle6)
        )
        self.wait(0.3)
        
        # === まとめ ===
        subtitle_end = Text("まとめ", font_size=36, color=GOLD, weight=BOLD)
        subtitle_end.next_to(title, DOWN)
        self.play(Write(subtitle_end), run_time=0.7)
        self.wait(0.5)
        
        summary = VGroup(
            VGroup(
                Text("1.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("|1⟩ のノルムは √2（正規化されていない！）", color=WHITE, font_size=24),
                    Text("内積の定義でノルムが決まる", color=YELLOW, font_size=22),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("2.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("グラム-シュミット法で直交基底を構成できた", color=WHITE, font_size=24),
                    MathTex(
                        r"\{1, \; x, \; x^2 - \tfrac{1}{3}\}",
                        color=GREEN, font_size=24
                    ),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("3.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("奇関数×偶関数の性質で計算が簡略化された", color=WHITE, font_size=24),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("4.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("結果はルジャンドル多項式に一致", color=WHITE, font_size=24),
                    Text("ベクトルと同じ手法が多項式空間でも使える！", color=ORANGE, font_size=24, weight=BOLD),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        summary.scale(0.9)
        summary.shift(UP * 0.3)
        
        for point in summary:
            self.play(Write(point), run_time=0.7)
            self.wait(0.4)
        
        self.wait(1.5)
        
        # フェードアウト
        all_final = VGroup(summary, subtitle_end, title)
        self.play(FadeOut(all_final), run_time=1.0)
        self.wait(0.5)
