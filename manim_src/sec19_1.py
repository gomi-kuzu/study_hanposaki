from manim import *
import numpy as np


class TimeEvolutionIntro(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        title = Text("時間発展方程式の導入", font_size=36, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.7)

        # ============================================================
        # Part 1: これから学ぶこと
        # ============================================================
        subtitle1 = Text("これから学ぶこと", font_size=28, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)

        intro_text = Text(
            "この先の数話では、状態ベクトルの時間発展を線形代数的に扱う",
            color=WHITE, font_size=26,
        )
        intro_text.shift(UP * 1.8)
        self.play(Write(intro_text), run_time=0.8)
        self.wait(0.5)

        # 状態ベクトルの時間発展
        vector_eq = MathTex(
            r"\frac{d}{dt}\boldsymbol{x}(t) = L\boldsymbol{x}(t)",
            color=YELLOW,
            font_size=42,
        )
        vector_eq.shift(UP * 0.7)
        vector_note = Text(
            "連立微分方程式を行列で表現",
            color=YELLOW, font_size=24,
        )
        vector_note.next_to(vector_eq, DOWN, buff=0.3)

        self.play(Write(vector_eq), run_time=0.8)
        self.play(Write(vector_note), run_time=0.6)
        self.wait(0.7)

        # さらに先の話
        future_text = Text(
            "さらにその先（４部後半）では…",
            color=WHITE, font_size=26,
        )
        future_text.shift(DOWN * 0.6)
        self.play(Write(future_text), run_time=0.7)
        self.wait(0.4)

        # 偏微分方程式
        pde_eq = MathTex(
            r"\frac{\partial}{\partial t}p(\boldsymbol{x},t) = \mathcal{L}p(\boldsymbol{x},t)",
            color=TEAL,
            font_size=42,
        )
        pde_eq.shift(DOWN * 1.5)
        pde_note = Text(
            "状態ベクトルを入力とする関数の時間発展（偏微分方程式）",
            color=TEAL, font_size=24,
        )
        pde_note.next_to(pde_eq, DOWN, buff=0.3)

        self.play(Write(pde_eq), run_time=0.8)
        self.play(Write(pde_note), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(intro_text), FadeOut(vector_eq), FadeOut(vector_note),
            FadeOut(future_text), FadeOut(pde_eq), FadeOut(pde_note),
            FadeOut(subtitle1),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: 具体例の導入
        # ============================================================
        subtitle2 = Text("具体例：化学反応のダンパ系", font_size=28, color=GOLD)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2), run_time=0.6)

        example_intro = Text(
            "化学反応は濃度が濃いほど起きやすい",
            color=WHITE, font_size=26,
        )
        example_intro.shift(DOWN)
        self.play(Write(example_intro), run_time=0.7)
        self.wait(1.5)

        # 時間発展方程式
        damper_eq = MathTex(
            r"\frac{d}{dt}x(t) = -\alpha x(t)",
            color=YELLOW,
            font_size=44,
        )
        damper_eq.shift(UP * 0.9)
        damper_box = SurroundingRectangle(damper_eq, color=YELLOW, buff=0.2)

        self.play(Write(damper_eq), run_time=0.8)
        self.play(Create(damper_box),  run_time=0.4)
        self.wait(0.6)

        # 説明
        explanation = VGroup(
            Text("x(t)：時刻tでの濃度", color=TEAL, font_size=26),
            Text("α：反応速度定数（正の定数）", color=TEAL, font_size=26),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        explanation.shift(DOWN * 0.3)

        for line in explanation:
            self.play(Write(line), run_time=0.5)
            self.wait(0.2)

        # 濃度減少のポンチ絵アニメーション
        self.play(
            FadeOut(damper_eq), FadeOut(damper_box), FadeOut(explanation),
            run_time=0.5
        )
        self.wait(0.2)

        visual_title = Text("濃度の時間変化のイメージ", color=YELLOW, font_size=28)
        visual_title.shift(UP)
        self.play(Write(visual_title), run_time=0.5)
        self.wait(0.3)

        # 容器の枠
        container = Rectangle(width=8, height=4, color=WHITE, stroke_width=3)
        container.shift(DOWN * 0.2)
        self.play(Create(container), run_time=0.5)
        self.wait(0.3)

        # 初期状態：多数の分子を配置
        np.random.seed(42)
        num_molecules = 80
        molecules = VGroup()
        
        for i in range(num_molecules):
            x_pos = np.random.uniform(-3.8, 3.8)
            y_pos = np.random.uniform(-1.8, 1.8)
            molecule = Dot(
                point=container.get_center() + np.array([x_pos, y_pos, 0]),
                radius=0.08,
                color=BLUE,
            )
            molecules.add(molecule)
        
        self.play(FadeIn(molecules), run_time=0.8)
        self.wait(0.5)

        time_label = MathTex("t = 0", font_size=34, color=YELLOW)
        time_label.next_to(container, DOWN, buff=0.4)
        self.play(Write(time_label), run_time=0.4)
        self.wait(0.5)

        # 指数関数的に分子を消していく（4段階）
        alpha_visual = 3
        time_steps = [0.5, 1.0, 1.5, 2.0]
        
        for t in time_steps:
            # 残存率を計算（指数関数的減少）
            survival_rate = np.exp(-alpha_visual * t)
            num_remaining = int(num_molecules * survival_rate)
            
            # ランダムに分子を選んで消す
            num_to_remove = len(molecules) - num_remaining
            if num_to_remove > 0 and len(molecules) > 0:
                # インデックスをランダムに選択
                num_current = len(molecules)
                indices_to_remove = np.random.choice(
                    num_current, 
                    size=min(num_to_remove, num_current), 
                    replace=False
                )
                
                # 選択されたインデックスの分子を取得
                molecules_list = list(molecules)
                molecules_to_remove = VGroup(*[molecules_list[i] for i in indices_to_remove])
                
                # 時刻表示を更新
                new_time_label = MathTex(f"t = {t}", font_size=34, color=YELLOW)
                new_time_label.next_to(container, DOWN, buff=0.4)
                
                self.play(
                    FadeOut(molecules_to_remove),
                    Transform(time_label, new_time_label),
                    run_time=0.8
                )
                
                # 消えた分子をVGroupから除去
                for mol in molecules_to_remove:
                    molecules.remove(mol)
                
                self.wait(0.4)

        self.wait(0.8)

        # ポンチ絵を片付ける
        self.play(
            FadeOut(container), FadeOut(molecules), 
            FadeOut(time_label), FadeOut(visual_title),
            FadeOut(example_intro),
            run_time=0.6
        )
        self.wait(0.3)

        # 元の要素を戻す
        self.play(Write(damper_eq), Create(damper_box), run_time=0.6)
        self.play(Write(explanation), run_time=0.5)
        self.wait(0.4)

        initial_condition = Text(
            "初期状態 x(0) を与えれば、その後の時間発展が全て計算できる",
            color=GREEN, font_size=26, weight=BOLD,
        )
        initial_condition.shift(DOWN * 1.5)
        self.play(Write(initial_condition), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(damper_eq), FadeOut(damper_box),
            FadeOut(explanation), FadeOut(initial_condition), FadeOut(subtitle2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: 通常のプロット
        # ============================================================
        subtitle3 = Text("いくつかの初期値でプロットしてみる", font_size=28, color=BLUE)
        subtitle3.next_to(title, DOWN)
        self.play(Write(subtitle3), run_time=0.6)

        alpha_note = MathTex(r"\alpha = 3", color=YELLOW, font_size=32)
        alpha_note.shift(UP * 2.2 + LEFT * 4.5)
        self.play(Write(alpha_note), run_time=0.5)
        self.wait(0.3)

        # 通常プロット
        axes_normal = Axes(
            x_range=[0, 2, 0.5],
            y_range=[0, 4.5, 1],
            x_length=6,
            y_length=4,
            axis_config={"color": GREY, "include_tip": True},
            tips=True,
        )
        axes_normal.shift(DOWN * 0.3)

        x_label_normal = MathTex("t", font_size=28).next_to(axes_normal.x_axis, RIGHT, buff=0.1)
        y_label_normal = MathTex("x(t)", font_size=28).next_to(axes_normal.y_axis, UP, buff=0.1)

        self.play(Create(axes_normal), Write(x_label_normal), Write(y_label_normal), run_time=0.6)
        self.wait(0.4)

        # プロット（α = 3, 複数の初期値）
        alpha = 3
        initial_values = [1, 2, 3, 4]
        colors = [RED, BLUE, GREEN, ORANGE]
        curves_normal = VGroup()
        
        for x0, color in zip(initial_values, colors):
            curve = axes_normal.plot(
                lambda t, x0=x0: x0 * np.exp(-alpha * t),
                x_range=[0, 2],
                color=color,
                stroke_width=3,
            )
            curves_normal.add(curve)
            
            # 初期値ラベル
            label = MathTex(f"x(0)={x0}", font_size=24, color=color)
            label.next_to(axes_normal.c2p(0, x0), LEFT, buff=0.15)
            curves_normal.add(label)

        self.play(Create(curves_normal), run_time=1.2)
        self.wait(0.8)

        observation1 = Text(
            "一見、初期値によって減少の傾向が異なるように見える",
            color=WHITE, font_size=24,
        )
        observation1.shift(DOWN * 2.8)
        self.play(Write(observation1), run_time=0.7)
        self.wait(1.0)

        self.play(
            FadeOut(axes_normal), FadeOut(x_label_normal), FadeOut(y_label_normal),
            FadeOut(curves_normal), FadeOut(observation1), FadeOut(alpha_note),
            FadeOut(subtitle3),
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: 片対数プロット
        # ============================================================
        subtitle4 = Text("縦軸を対数にした片対数グラフで見ると…", font_size=28, color=TEAL)
        subtitle4.next_to(title, DOWN)
        self.play(Write(subtitle4), run_time=0.6)

        alpha_note2 = MathTex(r"\alpha = 3", color=YELLOW, font_size=32)
        alpha_note2.shift(UP * 2.2 + LEFT * 4.5)
        self.play(Write(alpha_note2), run_time=0.5)
        self.wait(0.3)

        # 片対数プロット（縦軸が対数目盛り）
        axes_log = Axes(
            x_range=[0, 1.5, 0.5],
            y_range=[-2, 1, 1],  # 10^-4 ~ 10^1 の範囲（指数で指定）
            x_length=6,
            y_length=4,
            axis_config={"color": GREY, "include_tip": True},
            y_axis_config={
                "scaling": LogBase(base=10),
            },
            tips=True,
        )
        axes_log.shift(DOWN * 0.3)

        x_label_log = MathTex("t", font_size=28).next_to(axes_log.x_axis, RIGHT, buff=0.1)
        y_label_log = MathTex("x(t)", font_size=28).next_to(axes_log.y_axis, UP, buff=0.1)

        self.play(Create(axes_log), Write(x_label_log), Write(y_label_log), run_time=0.6)
        self.wait(0.4)

        # 片対数プロット
        curves_log = VGroup()
        
        for x0, color in zip(initial_values, colors):
            curve = axes_log.plot(
                lambda t, x0=x0: x0 * np.exp(-alpha * t),
                x_range=[0, 1.5],
                color=color,
                stroke_width=3,
            )
            curves_log.add(curve)
            
            # 初期値ラベル
            label = MathTex(f"x(0)={x0}", font_size=24, color=color)
            label.next_to(axes_log.c2p(0, x0), LEFT, buff=0.15)
            curves_log.add(label)

        self.play(Create(curves_log), run_time=1.2)
        self.wait(0.8)

        observation2 = Text(
            "どれも直線的に減少し、傾きは同じ！",
            color=YELLOW, font_size=26, weight=BOLD,
        )
        observation2.shift(DOWN * 2.6)
        self.play(Write(observation2), run_time=0.7)
        self.wait(0.5)

        conclusion_exp = Text(
            "→ すべて指数関数的な減少をしている",
            color=GREEN, font_size=26, weight=BOLD,
        )
        conclusion_exp.shift(DOWN * 3.1)
        self.play(Write(conclusion_exp), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(axes_log), FadeOut(x_label_log), FadeOut(y_label_log),
            FadeOut(curves_log), FadeOut(observation2), FadeOut(conclusion_exp),
            FadeOut(alpha_note2), FadeOut(subtitle4),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: 解の紹介
        # ============================================================
        subtitle5 = Text("解の形", font_size=28, color=GOLD)
        subtitle5.next_to(title, DOWN)
        self.play(Write(subtitle5), run_time=0.6)

        solution_intro = Text(
            "詳しい話は今後するとして、ここでは解を天下り的に紹介する",
            color=WHITE, font_size=26,
        )
        solution_intro.shift(UP * 2.0)
        self.play(Write(solution_intro), run_time=0.8)
        self.wait(0.5)

        # 微分方程式
        eq_recall = MathTex(
            r"\frac{d}{dt}x(t) = -\alpha x(t)",
            color=YELLOW,
            font_size=38,
        )
        eq_recall.shift(UP * 0.8)
        self.play(Write(eq_recall), run_time=0.7)
        self.wait(0.4)

        arrow_down = MathTex(r"\Downarrow", color=WHITE, font_size=48)
        arrow_down.shift(UP * 0.0)
        self.play(Write(arrow_down), run_time=0.4)
        self.wait(0.3)

        # 解
        solution_eq = MathTex(
            r"x(t) = x(0)e^{-\alpha t}",
            color=ORANGE,
            font_size=48,
        )
        solution_eq.shift(DOWN * 0.8)
        solution_box = SurroundingRectangle(solution_eq, color=ORANGE, buff=0.2)

        self.play(Write(solution_eq), run_time=0.8)
        self.play(Create(solution_box), run_time=0.4)
        self.wait(0.7)

        # 強調
        emphasis = Text(
            "時間発展方程式の解に指数関数が登場する",
            color=GREEN, font_size=28, weight=BOLD,
        )
        emphasis.shift(DOWN * 2.0)
        self.play(Write(emphasis), run_time=0.7)
        self.wait(0.5)

        next_topic = Text(
            "次回以降、この背景にある数学的構造を詳しく見ていく",
            color=TEAL, font_size=26,
        )
        next_topic.shift(DOWN * 2.7)
        self.play(Write(next_topic), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(solution_intro), FadeOut(eq_recall), FadeOut(arrow_down),
            FadeOut(solution_eq), FadeOut(solution_box),
            FadeOut(emphasis), FadeOut(next_topic), FadeOut(subtitle5),
        )
        self.wait(0.3)

        # ============================================================
        # Part 6: まとめ
        # ============================================================
        subtitle_end = Text("まとめ", font_size=36, color=GOLD, weight=BOLD)
        subtitle_end.next_to(title, DOWN)
        self.play(Write(subtitle_end), run_time=0.7)

        summary = VGroup(
            Text("1. 状態ベクトルの時間発展を線形代数で扱う", color=WHITE, font_size=28),
            Text("2. 化学反応などは濃度に比例した微分方程式で記述", color=WHITE, font_size=28),
            Text("3. 初期値を与えれば時間発展が決まる", color=WHITE, font_size=28),
            Text("4. 片対数グラフで見ると減少の傾きが同じ", color=WHITE, font_size=28),
            Text("5. 解は指数関数の形 x(t) = x(0)e⁻ᵅᵗ", color=YELLOW, font_size=28),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        summary.scale(0.90)
        summary.shift(DOWN * 0.4)

        for row in summary:
            self.play(Write(row), run_time=0.6)
            self.wait(0.15)

        self.wait(2)
        self.play(FadeOut(VGroup(title, subtitle_end, summary)), run_time=1.0)
        self.wait(0.5)
