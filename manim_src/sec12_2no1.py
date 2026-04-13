from manim import *
import numpy as np

class WaveDecomposition(Scene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"

        # タイトル
        title = Text("波の理解・分解・再構築", font_size=34, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)

        # === Part 1: 多項式から波へ ===
        subtitle1 = Text("多項式の話を波に拡張する", font_size=30, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.5)

        # 前回の復習
        prev_result = VGroup(
            Text("前回までは多項式を基底で分解した", color=WHITE, font_size=24),
            Text("同じアイデアが「波」にも適用できる！", color=YELLOW, font_size=24, weight=BOLD),
        ).arrange(DOWN, buff=0.3)
        prev_result.shift(UP * 1.3)
        self.play(Write(prev_result), run_time=0.8)
        self.wait(0.5)

        # 周期関数の定義
        periodic_def = VGroup(
            Text("周期関数の定義:", color=TEAL, font_size=24, weight=BOLD),
            MathTex(r"f(t + T) = f(t)", color=TEAL, font_size=32),
            Text("（周期Tで同じ値を繰り返す関数）", color=GRAY, font_size=20),
        ).arrange(DOWN, buff=0.2)
        periodic_def.shift(DOWN * 0.5)
        periodic_box = SurroundingRectangle(periodic_def, color=TEAL, buff=0.2)
        self.play(Write(periodic_def), Create(periodic_box), run_time=0.8)
        self.wait(0.5)

        # 波のイメージ
        wave_note = Text("→ これは「波」を数学的に表したもの", color=ORANGE, font_size=22)
        wave_note.shift(DOWN * 1.8)
        self.play(Write(wave_note), run_time=0.6)
        self.wait(1.0)

        self.play(
            FadeOut(prev_result), FadeOut(periodic_def), FadeOut(periodic_box),
            FadeOut(wave_note), FadeOut(subtitle1)
        )
        self.wait(0.3)

        # === Part 2: 三角関数を基底に使う理由 ===
        subtitle2 = Text("なぜ三角関数を基底に使うのか？", font_size=30, color=PURPLE)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)

        # 理由の説明
        reason = VGroup(
            Text("波を分解するには、同じ「波」を使うのが効率的", color=WHITE, font_size=24),
            Text("↓", color=WHITE, font_size=28),
            Text("三角関数 sin, cos は周期関数の代表格！", color=YELLOW, font_size=26, weight=BOLD),
        ).arrange(DOWN, buff=0.3)
        reason.shift(UP * 1.0)
        self.play(Write(reason), run_time=0.9)
        self.wait(0.5)

        # sin と cos のグラフを表示
        axes = Axes(
            x_range=[0, 4 * PI, PI],
            y_range=[-1.5, 1.5, 0.5],
            x_length=10,
            y_length=2.5,
            axis_config={"color": GRAY},
        ).scale(0.7)
        axes.shift(DOWN * 1.5)

        sin_graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        cos_graph = axes.plot(lambda x: np.cos(x), color=RED)
        
        sin_label = MathTex(r"\sin(t)", color=BLUE, font_size=24).next_to(axes, RIGHT, buff=0.3).shift(UP * 0.3)
        cos_label = MathTex(r"\cos(t)", color=RED, font_size=24).next_to(axes, RIGHT, buff=0.3).shift(DOWN * 0.3)

        self.play(Create(axes), run_time=0.6)
        self.play(Create(sin_graph), Write(sin_label), run_time=0.7)
        self.play(Create(cos_graph), Write(cos_label), run_time=0.7)
        self.wait(1.0)

        self.play(
            FadeOut(reason), FadeOut(axes), FadeOut(sin_graph), FadeOut(cos_graph),
            FadeOut(sin_label), FadeOut(cos_label), FadeOut(subtitle2)
        )
        self.wait(0.3)

        # === Part 3: フーリエ級数展開 ===
        subtitle3 = Text("フーリエ級数展開", font_size=30, color=GREEN)
        subtitle3.next_to(title, DOWN)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.5)

        # フーリエ級数の導入
        fourier_intro = Text("任意の周期関数は三角関数の和で表せる", color=YELLOW, font_size=24, weight=BOLD)
        fourier_intro.shift(UP * 1.6)
        self.play(Write(fourier_intro), run_time=0.7)
        self.wait(0.4)

        # フーリエ級数の式
        fourier_formula = MathTex(
            r"f(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left( a_n \cos\frac{2\pi n t}{T} + b_n \sin\frac{2\pi n t}{T} \right)",
            color=WHITE, font_size=28
        )
        fourier_formula.shift(UP * 0.7)
        fourier_box = SurroundingRectangle(fourier_formula, color=GREEN, buff=0.15)
        self.play(Write(fourier_formula), Create(fourier_box), run_time=1.0)
        self.wait(0.6)

        # 各項の説明
        terms_explain = VGroup(
            VGroup(
                MathTex(r"\frac{a_0}{2}", color=ORANGE, font_size=26),
                Text(": 定数項（平均値）", color=ORANGE, font_size=20),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                MathTex(r"a_n \cos\frac{2\pi n t}{T}", color=RED, font_size=26),
                Text(": コサイン成分", color=RED, font_size=20),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                MathTex(r"b_n \sin\frac{2\pi n t}{T}", color=BLUE, font_size=26),
                Text(": サイン成分", color=BLUE, font_size=20),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        terms_explain.shift(DOWN * 1.1)
        self.play(Write(terms_explain), run_time=0.9)
        self.wait(1.0)

        self.play(
            FadeOut(fourier_intro), FadeOut(fourier_formula), FadeOut(fourier_box),
            FadeOut(terms_explain), FadeOut(subtitle3)
        )
        self.wait(0.3)

        # === Part 4: 波の合成（視覚的デモ） ===
        subtitle4 = Text("波の合成（重ね合わせの原理）を視覚的に理解する", font_size=30, color=GOLD)
        subtitle4.next_to(title, DOWN)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.5)

        # グラフ用の軸
        axes2 = Axes(
            x_range=[0, 2 * PI, PI / 2],
            y_range=[-2.5, 2.5, 1],
            x_length=10,
            y_length=4,
            axis_config={"color": GRAY},
        ).scale(0.65)
        axes2.shift(DOWN * 0.8)

        # 基本波
        wave1 = axes2.plot(lambda x: np.sin(x), color=BLUE)
        wave1_label = MathTex(r"\sin(t)", color=BLUE, font_size=28)
        wave1_label.next_to(axes2, UP*3.0, buff=0.1).shift(LEFT * 3.4)

        self.play(Create(axes2), run_time=0.5)
        self.play(Create(wave1), Write(wave1_label), run_time=0.6)
        self.wait(0.3)

        # 2倍周波数の波を追加
        wave2 = axes2.plot(lambda x: 0.5 * np.sin(2 * x), color=RED)
        wave2_label = MathTex(r"+ \frac{1}{2}\sin(2t)", color=RED, font_size=28)
        wave2_label.next_to(wave1_label, RIGHT, buff=0.3)

        self.play(Create(wave2), Write(wave2_label), run_time=0.6)
        self.wait(0.3)

        # 3倍周波数の波を追加
        wave3 = axes2.plot(lambda x: 0.3 * np.sin(3 * x), color=PURPLE)
        wave3_label = MathTex(r"+ \frac{1}{3}\sin(3t)", color=PURPLE, font_size=28)
        wave3_label.next_to(wave2_label, RIGHT, buff=0.3)

        self.play(Create(wave3), Write(wave3_label), run_time=0.6)
        self.wait(0.4)

        # 合成波
        combined_wave = axes2.plot(
            lambda x: np.sin(x) + 0.5 * np.sin(2 * x) + 0.3 * np.sin(3 * x),
            color=YELLOW,
            stroke_width=3
        )
        combined_label = Text("= 合成波", color=YELLOW, font_size=26, weight=BOLD)
        combined_label.next_to(wave3_label, RIGHT, buff=0.3)

        self.play(
            FadeOut(wave1), FadeOut(wave2), FadeOut(wave3),
            Create(combined_wave), Write(combined_label),
            run_time=0.8
        )
        self.wait(0.5)

        # 強調
        synthesis_note = Text("異なる周波数の波を重ね合わせて、複雑な波形を作れる！", color=GREEN, font_size=24, weight=BOLD)
        synthesis_note.shift(DOWN * 2.8)
        self.play(Write(synthesis_note), run_time=0.7)
        self.wait(1.0)

        self.play(
            FadeOut(axes2), FadeOut(combined_wave),
            FadeOut(wave1_label), FadeOut(wave2_label), FadeOut(wave3_label), FadeOut(combined_label),
            FadeOut(synthesis_note), FadeOut(subtitle4)
        )
        self.wait(0.3)

        # === Part 5: 疑問提起 ===
        subtitle5 = Text("ここで一つの疑問", font_size=30, color=RED)
        subtitle5.next_to(title, DOWN)
        self.play(Write(subtitle5), run_time=0.6)
        self.wait(0.5)

        # 疑問
        question = VGroup(
            Text("sin や cos は本当に", color=WHITE, font_size=28),
            Text("1次独立", color=RED, font_size=32, weight=BOLD),
            Text("なのか？", color=WHITE, font_size=28),
        ).arrange(RIGHT, buff=0.15)
        question.shift(UP * 1.2)
        q_box = SurroundingRectangle(question, color=RED, buff=0.2)
        self.play(Write(question), Create(q_box), run_time=0.8)
        self.wait(0.6)

        # 補足
        supplement = VGroup(
            Text("基底として使うなら、1次独立でなければならない", color=GRAY, font_size=22),
            Text("（どれかが他の線形結合で表せてはダメ）", color=GRAY, font_size=20),
        ).arrange(DOWN, buff=0.15)
        supplement.shift(DOWN * 0.3)
        self.play(Write(supplement), run_time=0.7)
        self.wait(0.5)

        # 結論予告
        conclusion_preview = VGroup(
            Text("結論:", color=GREEN, font_size=26, weight=BOLD),
            Text("1次独立なだけでなく、周波数ごとに", color=GREEN, font_size=26),
            Text("直交", color=YELLOW, font_size=30, weight=BOLD),
            Text("している！", color=GREEN, font_size=26),
        ).arrange(RIGHT, buff=0.15)
        conclusion_preview.shift(DOWN * 1.5)
        conclusion_box = SurroundingRectangle(conclusion_preview, color=GREEN, buff=0.2)
        self.play(Write(conclusion_preview), Create(conclusion_box), run_time=0.9)
        self.wait(1.2)

        self.play(
            FadeOut(question), FadeOut(q_box),
            FadeOut(supplement),
            FadeOut(conclusion_preview), FadeOut(conclusion_box),
            FadeOut(subtitle5)
        )
        self.wait(0.3)

        # === Part 6: 内積の定義 ===
        subtitle6 = Text("内積の定義", font_size=30, color=PURPLE)
        subtitle6.next_to(title, DOWN)
        self.play(Write(subtitle6), run_time=0.6)
        self.wait(0.5)

        # 内積の導入
        inner_intro = Text("直交性を確かめるために、周期関数の内積を定義する", color=WHITE, font_size=24)
        inner_intro.shift(UP * 1.6)
        self.play(Write(inner_intro), run_time=0.7)
        self.wait(0.4)

        # 内積の定義式
        inner_def = MathTex(
            r"\langle h | g \rangle = \int_0^T h(t) \, g(t) \, dt",
            color=YELLOW, font_size=32
        )
        inner_def.shift(UP * 0.7)
        inner_def_box = SurroundingRectangle(inner_def, color=YELLOW, buff=0.15)
        self.play(Write(inner_def), Create(inner_def_box), run_time=0.8)
        self.wait(0.5)

        # 直交の意味
        orthogonal_meaning = VGroup(
            Text("直交の定義:", color=TEAL, font_size=24, weight=BOLD),
            MathTex(r"\langle h | g \rangle = 0", color=TEAL, font_size=28),
            Text("のとき、h と g は直交する", color=TEAL, font_size=22),
        ).arrange(DOWN, buff=0.2)
        orthogonal_meaning.shift(DOWN * 0.7)
        self.play(Write(orthogonal_meaning), run_time=0.8)
        self.wait(0.5)

        # フーリエ級数の基底
        basis_note = VGroup(
            Text("フーリエ級数の基底:", color=ORANGE, font_size=22, weight=BOLD),
            MathTex(r"1, \quad \cos\frac{2\pi n t}{T}, \quad \sin\frac{2\pi n t}{T}", color=ORANGE, font_size=26),
            Text("（n = 1, 2, 3, ...）", color=GRAY, font_size=18),
        ).arrange(DOWN, buff=0.15)
        basis_note.shift(DOWN * 2.2)
        self.play(Write(basis_note), run_time=0.7)
        self.wait(1.0)

        self.play(
            FadeOut(inner_intro), FadeOut(inner_def), FadeOut(inner_def_box),
            FadeOut(orthogonal_meaning), FadeOut(basis_note),
            FadeOut(subtitle6)
        )
        self.wait(0.3)

        # === Part 7: sin同士の内積 ===
        subtitle7 = Text("sin同士の内積", font_size=30, color=BLUE)
        subtitle7.next_to(title, DOWN)
        self.play(Write(subtitle7), run_time=0.6)
        self.wait(0.5)

        # 計算
        sin_sin_title = Text("sin同士の内積を計算:", color=YELLOW, font_size=24, weight=BOLD)
        sin_sin_title.shift(UP * 1.8 + LEFT * 3)
        self.play(Write(sin_sin_title), run_time=0.5)

        sin_sin_calc = MathTex(
            r"\left\langle \sin\frac{2\pi n t}{T} \middle| \sin\frac{2\pi m t}{T} \right\rangle = \int_0^T \sin\frac{2\pi n t}{T} \sin\frac{2\pi m t}{T} \, dt",
            color=WHITE, font_size=24
        )
        sin_sin_calc.shift(UP * 1.0)
        self.play(Write(sin_sin_calc), run_time=0.9)
        self.wait(0.4)

        # 結果
        sin_sin_result = MathTex(
            r"= \frac{T}{2} \delta_{nm}",
            color=GREEN, font_size=32
        )
        sin_sin_result.shift(UP * 0.2)
        sin_sin_result_box = SurroundingRectangle(sin_sin_result, color=GREEN, buff=0.15)
        self.play(Write(sin_sin_result), Create(sin_sin_result_box), run_time=0.7)
        self.wait(0.5)

        # クロネッカーのデルタの説明
        delta_explain = VGroup(
            Text("クロネッカーのデルタ:", color=TEAL, font_size=22, weight=BOLD),
            MathTex(r"\delta_{nm} = \begin{cases} 1 & (n = m) \\ 0 & (n \neq m) \end{cases}", color=TEAL, font_size=26),
        ).arrange(DOWN, buff=0.2)
        delta_explain.shift(DOWN * 1.0)
        self.play(Write(delta_explain), run_time=0.7)
        self.wait(0.5)

        # 意味
        sin_meaning = Text("→ 周波数が異なれば直交、同じなら内積はT/2", color=ORANGE, font_size=26)
        sin_meaning.shift(DOWN * 2.3)
        self.play(Write(sin_meaning), run_time=0.6)
        self.wait(1.0)

        self.play(
            FadeOut(sin_sin_title), FadeOut(sin_sin_calc),
            FadeOut(sin_sin_result), FadeOut(sin_sin_result_box),
            FadeOut(delta_explain), FadeOut(sin_meaning),
            FadeOut(subtitle7)
        )
        self.wait(0.3)

        # === Part 8: cos同士の内積 ===
        subtitle8 = Text("cos同士の内積", font_size=30, color=RED)
        subtitle8.next_to(title, DOWN)
        self.play(Write(subtitle8), run_time=0.6)
        self.wait(0.5)

        # 計算
        cos_cos_title = Text("cos同士の内積を計算:", color=YELLOW, font_size=24, weight=BOLD)
        cos_cos_title.shift(UP * 1.8 + LEFT * 3)
        self.play(Write(cos_cos_title), run_time=0.5)

        cos_cos_calc = MathTex(
            r"\left\langle \cos\frac{2\pi n t}{T} \middle| \cos\frac{2\pi m t}{T} \right\rangle = \int_0^T \cos\frac{2\pi n t}{T} \cos\frac{2\pi m t}{T} \, dt",
            color=WHITE, font_size=24
        )
        cos_cos_calc.shift(UP * 1.0)
        self.play(Write(cos_cos_calc), run_time=0.9)
        self.wait(0.4)

        # 結果
        cos_cos_result = MathTex(
            r"= \frac{T}{2} \delta_{nm}",
            color=GREEN, font_size=32
        )
        cos_cos_result.shift(UP * 0.2)
        cos_cos_result_box = SurroundingRectangle(cos_cos_result, color=GREEN, buff=0.15)
        self.play(Write(cos_cos_result), Create(cos_cos_result_box), run_time=0.7)
        self.wait(0.5)

        # 意味
        cos_meaning = VGroup(
            Text("sin同士と同じ結果！", color=TEAL, font_size=24, weight=BOLD),
            Text("→ 周波数が異なれば直交、同じなら内積はT/2", color=ORANGE, font_size=26),
        ).arrange(DOWN, buff=0.2)
        cos_meaning.shift(DOWN * 0.8)
        self.play(Write(cos_meaning), run_time=0.7)
        self.wait(1.0)

        self.play(
            FadeOut(cos_cos_title), FadeOut(cos_cos_calc),
            FadeOut(cos_cos_result), FadeOut(cos_cos_result_box),
            FadeOut(cos_meaning),
            FadeOut(subtitle8)
        )
        self.wait(0.3)

        # === Part 9: sinとcosの内積 ===
        subtitle9 = Text("sinとcosの内積", font_size=30, color=PURPLE)
        subtitle9.next_to(title, DOWN)
        self.play(Write(subtitle9), run_time=0.6)
        self.wait(0.5)

        # 計算
        sin_cos_title = Text("sinとcosの内積を計算:", color=YELLOW, font_size=24, weight=BOLD)
        sin_cos_title.shift(UP * 1.8 + LEFT * 3)
        self.play(Write(sin_cos_title), run_time=0.5)

        sin_cos_calc = MathTex(
            r"\left\langle \sin\frac{2\pi n t}{T} \middle| \cos\frac{2\pi m t}{T} \right\rangle = \int_0^T \sin\frac{2\pi n t}{T} \cos\frac{2\pi m t}{T} \, dt",
            color=WHITE, font_size=24
        )
        sin_cos_calc.shift(UP * 1.0)
        self.play(Write(sin_cos_calc), run_time=0.9)
        self.wait(0.4)

        # 結果
        sin_cos_result = MathTex(
            r"= 0",
            color=RED, font_size=40
        )
        sin_cos_result.shift(UP * 0.2)
        sin_cos_result_box = SurroundingRectangle(sin_cos_result, color=RED, buff=0.2)
        self.play(Write(sin_cos_result), Create(sin_cos_result_box), run_time=0.7)
        self.wait(0.5)

        # 強調
        sin_cos_note = VGroup(
            Text("任意の n, m に対して常にゼロ！", color=YELLOW, font_size=24, weight=BOLD),
            Text("→ sinとcosは常に直交している", color=GREEN, font_size=24, weight=BOLD),
        ).arrange(DOWN, buff=0.2)
        sin_cos_note.shift(DOWN * 0.8)
        note_box = SurroundingRectangle(sin_cos_note, color=YELLOW, buff=0.15)
        self.play(Write(sin_cos_note), Create(note_box), run_time=0.8)
        self.wait(1.0)

        self.play(
            FadeOut(sin_cos_title), FadeOut(sin_cos_calc),
            FadeOut(sin_cos_result), FadeOut(sin_cos_result_box),
            FadeOut(sin_cos_note), FadeOut(note_box),
            FadeOut(subtitle9)
        )
        self.wait(0.3)

        # === Part 10: 定数項との内積 ===
        subtitle10 = Text("定数項との内積", font_size=30, color=ORANGE)
        subtitle10.next_to(title, DOWN)
        self.play(Write(subtitle10), run_time=0.6)
        self.wait(0.5)

        # 定数とsinの内積
        const_sin_title = Text("定数とsinの内積:", color=BLUE, font_size=24, weight=BOLD)
        const_sin_title.shift(UP * 1.6 + LEFT * 4)
        self.play(Write(const_sin_title), run_time=0.5)

        const_sin_calc = MathTex(
            r"\langle 1 | \sin\frac{2\pi n t}{T} \rangle = \int_0^T \sin\frac{2\pi n t}{T} \, dt = 0",
            color=BLUE, font_size=26
        )
        const_sin_calc.shift(UP * 0.9)
        self.play(Write(const_sin_calc), run_time=0.8)
        self.wait(0.4)

        # 定数とcosの内積
        const_cos_title = Text("定数とcosの内積:", color=RED, font_size=24, weight=BOLD)
        const_cos_title.shift(DOWN * 0.0 + LEFT * 4)
        self.play(Write(const_cos_title), run_time=0.5)

        const_cos_calc = MathTex(
            r"\langle 1 | \cos\frac{2\pi n t}{T} \rangle = \int_0^T \cos\frac{2\pi n t}{T} \, dt = 0",
            color=RED, font_size=26
        )
        const_cos_calc.shift(DOWN * 0.7)
        self.play(Write(const_cos_calc), run_time=0.8)
        self.wait(0.4)

        # 結論
        const_conclusion = VGroup(
            Text("定数項は sin, cos のどちらとも直交！", color=GREEN, font_size=24, weight=BOLD),
        )
        const_conclusion.shift(DOWN * 1.7)
        const_box = SurroundingRectangle(const_conclusion, color=GREEN, buff=0.15)
        self.play(Write(const_conclusion), Create(const_box), run_time=0.7)
        self.wait(0.5)

        # 補足
        note_const = Text("（n ≥ 1 の場合。1周期分積分すると打ち消し合う）", color=GRAY, font_size=18)
        note_const.shift(DOWN * 2.5)
        self.play(Write(note_const), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(const_sin_title), FadeOut(const_sin_calc),
            FadeOut(const_cos_title), FadeOut(const_cos_calc),
            FadeOut(const_conclusion), FadeOut(const_box),
            FadeOut(note_const),
            FadeOut(subtitle10)
        )
        self.wait(0.3)

        # === Part 11: 直交性のまとめ ===
        subtitle11 = Text("直交性のまとめ", font_size=30, color=TEAL)
        subtitle11.next_to(title, DOWN)
        self.play(Write(subtitle11), run_time=0.6)
        self.wait(0.5)

        # まとめの表
        orthogonal_summary = VGroup(
            VGroup(
                MathTex(r"\langle \sin_n | \sin_m \rangle", color=BLUE, font_size=26),
                MathTex(r"= \frac{T}{2} \delta_{nm}", color=WHITE, font_size=26),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                MathTex(r"\langle \cos_n | \cos_m \rangle", color=RED, font_size=26),
                MathTex(r"= \frac{T}{2} \delta_{nm}", color=WHITE, font_size=26),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                MathTex(r"\langle \sin_n | \cos_m \rangle", color=PURPLE, font_size=26),
                MathTex(r"= 0", color=WHITE, font_size=26),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                MathTex(r"\langle 1 | \sin_n \rangle", color=BLUE, font_size=26),
                MathTex(r"= 0", color=WHITE, font_size=26),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                MathTex(r"\langle 1 | \cos_n \rangle", color=RED, font_size=26),
                MathTex(r"= 0", color=WHITE, font_size=26),
            ).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        orthogonal_summary.shift(UP * 0.5)
        
        for item in orthogonal_summary:
            self.play(Write(item), run_time=0.5)
            self.wait(0.2)
        self.wait(0.5)

        # 最終結論
        final_conclusion = VGroup(
            Text("各基底は互いに直交している！", color=YELLOW, font_size=28, weight=BOLD),
            Text("→ フーリエ級数の基底は正規直交系", color=GREEN, font_size=24),
        ).arrange(DOWN, buff=0.2)
        final_conclusion.shift(DOWN * 2.0)
        final_box = SurroundingRectangle(final_conclusion, color=YELLOW, buff=0.2)
        self.play(Write(final_conclusion), Create(final_box), run_time=0.9)
        self.wait(1.2)

        self.play(
            FadeOut(orthogonal_summary),
            FadeOut(final_conclusion), FadeOut(final_box),
            FadeOut(subtitle11)
        )
        self.wait(0.3)

        # === まとめ ===
        subtitle_end = Text("まとめ", font_size=36, color=GOLD, weight=BOLD)
        subtitle_end.next_to(title, DOWN)
        self.play(Write(subtitle_end), run_time=0.7)
        self.wait(0.5)

        summary = VGroup(
            VGroup(
                Text("1.", color=WHITE, font_size=28, weight=BOLD),
                VGroup(
                    Text("周期関数（波）も基底で分解できる", color=WHITE, font_size=28),
                    MathTex(r"f(t+T) = f(t)", color=TEAL, font_size=30),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("2.", color=WHITE, font_size=28, weight=BOLD),
                VGroup(
                    Text("三角関数を基底に使う（フーリエ級数）", color=WHITE, font_size=28),
                    MathTex(r"f(t) = \frac{a_0}{2} + \sum_{n} (a_n \cos + b_n \sin)", color=YELLOW, font_size=30),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("3.", color=WHITE, font_size=28, weight=BOLD),
                VGroup(
                    Text("内積を定義して直交性を確認", color=WHITE, font_size=28),
                    MathTex(r"\langle h | g \rangle = \int_0^T h(t) g(t) dt", color=GREEN, font_size=30),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("4.", color=WHITE, font_size=28, weight=BOLD),
                VGroup(
                    Text("sin, cos, 定数は互いに直交！", color=WHITE, font_size=28),
                    MathTex(r"\langle \sin_n | \cos_m \rangle = 0, \quad \langle \sin_n | \sin_m \rangle = \frac{T}{2}\delta_{nm}", color=RED, font_size=30),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        summary.scale(0.85)
        summary.shift(-UP * 0.1)

        for point in summary:
            self.play(Write(point), run_time=0.7)
            self.wait(0.4)

        self.wait(1.5)

        all_final = VGroup(summary, subtitle_end, title)
        self.play(FadeOut(all_final), run_time=1.0)
        self.wait(0.5)
