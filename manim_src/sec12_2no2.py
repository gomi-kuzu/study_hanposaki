from manim import *
import numpy as np

class FourierTransform(Scene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"

        # タイトル
        title = Text("フーリエ変換", font_size=34, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)

        # === Part 1: 前回の復習 ===
        subtitle1 = Text("さっきの復習: 三角関数の直交性", font_size=30, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.5)

        # 前回の復習
        prev_result = VGroup(
            Text("12話前半で学んだこと:", color=YELLOW, font_size=24, weight=BOLD),
            Text("周波数の異なる波同士は直交する", color=WHITE, font_size=24),
        ).arrange(DOWN, buff=0.3)
        prev_result.shift(UP * 1.3)
        self.play(Write(prev_result), run_time=0.7)
        self.wait(0.4)

        # 直交性の式
        orthogonal_eq = VGroup(
            MathTex(r"\langle \sin_n | \sin_m \rangle = \frac{T}{2} \delta_{nm}", color=TEAL, font_size=30),
            MathTex(r"\langle \cos_n | \cos_m \rangle = \frac{T}{2} \delta_{nm}", color=TEAL, font_size=30),
            MathTex(r"\langle \sin_n | \cos_m \rangle = 0", color=TEAL, font_size=30),
        ).arrange(DOWN, buff=0.2)
        orthogonal_eq.shift(DOWN * 0.6)
        orthogonal_box = SurroundingRectangle(orthogonal_eq, color=TEAL, buff=0.15)
        self.play(Write(orthogonal_eq), Create(orthogonal_box), run_time=0.9)
        self.wait(0.5)

        # これを発展させる
        develop_note = Text("→ これを発展させて「フーリエ変換」を導く", color=ORANGE, font_size=22)
        develop_note.shift(DOWN * 2.4)
        self.play(Write(develop_note), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(prev_result), FadeOut(orthogonal_eq), FadeOut(orthogonal_box),
            FadeOut(develop_note), FadeOut(subtitle1)
        )
        self.wait(0.3)

        # === Part 2: 基底分解の復習 ===
        subtitle2 = Text("11話の復習: 基底による関数の分解", font_size=30, color=PURPLE)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)

        # 11話の内容
        basis_intro = VGroup(
            Text("11話で学んだこと:", color=YELLOW, font_size=24, weight=BOLD),
            Text("任意の関数は基底で分解できる", color=WHITE, font_size=24),
        ).arrange(DOWN, buff=0.2)
        basis_intro.shift(UP * 1.4)
        self.play(Write(basis_intro), run_time=0.7)
        self.wait(0.4)

        # 分解の式
        decomposition = MathTex(
            r"|f\rangle = \sum_n c_n |e_n\rangle",
            color=WHITE, font_size=32
        )
        decomposition.shift(UP * 0.5)
        self.play(Write(decomposition), run_time=0.7)
        self.wait(0.4)

        # 係数の意味
        coeff_meaning = VGroup(
            MathTex(r"c_n", color=WHITE, font_size=30),
            Text("は基底", color=WHITE, font_size=24),
            MathTex(r"|e_n\rangle", color=WHITE, font_size=30),
            Text("方向の成分（係数）", color=WHITE, font_size=24),
        ).arrange(RIGHT, buff=0.15)
        coeff_meaning.shift(DOWN * 0.3)
        self.play(Write(coeff_meaning), run_time=0.7)
        self.wait(0.4)

        # 今回のアイデア
        idea_box = VGroup(
            Text("今回のアイデア:", color=ORANGE, font_size=24, weight=BOLD),
            Text("波（周波数）を基底として信号を分解する", color=ORANGE, font_size=24),
            Text("→ これがフーリエ変換！", color=YELLOW, font_size=26, weight=BOLD),
        ).arrange(DOWN, buff=0.2)
        idea_box.shift(DOWN * 2.0)
        idea_rect = SurroundingRectangle(idea_box, color=ORANGE, buff=0.2)
        self.play(Write(idea_box), Create(idea_rect), run_time=0.9)
        self.wait(1.0)

        self.play(
            FadeOut(basis_intro), FadeOut(decomposition),
            FadeOut(coeff_meaning), FadeOut(idea_box), FadeOut(idea_rect),
            FadeOut(subtitle2)
        )
        self.wait(0.3)

        # === Part 3: 複素正弦波の導入 ===
        subtitle3 = Text("準備①: 複素正弦波の導入", font_size=30, color=GREEN)
        subtitle3.next_to(title, DOWN)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.5)

        # オイラーの公式
        euler_intro = Text("新たな基底として複素正弦波を導入する", color=WHITE, font_size=24)
        euler_intro.shift(UP * 1.6)
        self.play(Write(euler_intro), run_time=0.6)
        self.wait(0.4)

        euler_title = Text("オイラーの公式:", color=YELLOW, font_size=24, weight=BOLD)
        euler_title.shift(UP * 1.0 + LEFT * 4)
        self.play(Write(euler_title), run_time=0.4)

        euler_formula = MathTex(
            r"e^{j\omega t} = \cos \omega t + j \sin \omega t",
            color=YELLOW, font_size=32
        )
        euler_formula.shift(UP * 0.4)
        euler_box = SurroundingRectangle(euler_formula, color=YELLOW, buff=0.15)
        self.play(Write(euler_formula), Create(euler_box), run_time=0.8)
        self.wait(0.5)

        # 複素正弦波の意味
        complex_meaning = VGroup(
            Text("複素正弦波は cos と sin を同時に表現", color=TEAL, font_size=24),
            Text("→ 計算が簡潔になり、位相情報も扱える", color=TEAL, font_size=24),
        ).arrange(DOWN, buff=0.15)
        complex_meaning.shift(DOWN * 0.5)
        self.play(Write(complex_meaning), run_time=0.7)
        self.wait(0.5)

        # j について
        j_note = VGroup(
            Text("※ j は虚数単位（", color=GRAY, font_size=22),
            MathTex(r"j^2 = -1", color=GRAY, font_size=22),
            Text("）、工学では j を使うことが多い", color=GRAY, font_size=22),
        ).arrange(RIGHT, buff=0.1)
        j_note.shift(DOWN * 1.3)
        self.play(Write(j_note), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(euler_intro), FadeOut(euler_title),
            FadeOut(euler_formula), FadeOut(euler_box),
            FadeOut(complex_meaning), FadeOut(j_note),
            FadeOut(subtitle3)
        )
        self.wait(0.3)

        # === Part 4: 複素関数の内積 ===
        subtitle4 = Text("準備②: 複素関数の内積", font_size=30, color=GOLD)
        subtitle4.next_to(title, DOWN)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.5)

        # 複素関数の内積
        inner_intro = Text("複素関数の内積は複素共役を使って定義する", color=WHITE, font_size=24)
        inner_intro.shift(UP * 1.6)
        self.play(Write(inner_intro), run_time=0.7)
        self.wait(0.4)

        # 内積の定義
        inner_def = MathTex(
            r"\langle g | f \rangle = \int_{-\infty}^{\infty} f(t) \, \overline{g(t)} \, dt",
            color=YELLOW, font_size=32
        )
        inner_def.shift(UP * 0.7)
        inner_def_box = SurroundingRectangle(inner_def, color=YELLOW, buff=0.15)
        self.play(Write(inner_def), Create(inner_def_box), run_time=0.8)
        self.wait(0.5)

        # 複素共役の説明
        conj_explain = VGroup(
            MathTex(r"\overline{g(t)}", color=TEAL, font_size=30),
            Text("は", color=TEAL, font_size=22),
            MathTex(r"g(t)", color=TEAL, font_size=30),
            Text("の複素共役", color=TEAL, font_size=22),
        ).arrange(RIGHT, buff=0.2)
        conj_explain.shift(DOWN * 0.2)
        self.play(Write(conj_explain), run_time=0.6)
        self.wait(0.4)

        # 複素共役の例
        conj_example = MathTex(
            r"\overline{e^{jm\omega_0 t}} = e^{-jm\omega_0 t}",
            color=TEAL, font_size=32
        )
        conj_example.shift(DOWN * 1.0)
        self.play(Write(conj_example), run_time=0.6)
        self.wait(0.5)

        # なぜ複素共役？
        why_conj = Text("（複素共役を使うことで、非負を返すという内積の性質を保つ）", color=GRAY, font_size=22)
        why_conj.shift(DOWN * 1.7)
        self.play(Write(why_conj), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(inner_intro), FadeOut(inner_def), FadeOut(inner_def_box),
            FadeOut(conj_explain), FadeOut(conj_example), FadeOut(why_conj),
            FadeOut(subtitle4)
        )
        self.wait(0.3)

        # === Part 5: 複素正弦波の直交性 ===
        subtitle5 = Text("準備③: 複素正弦波の直交性", font_size=30, color=BLUE)
        subtitle5.next_to(title, DOWN)
        self.play(Write(subtitle5), run_time=0.6)
        self.wait(0.5)

        # 直交性の計算
        orthog_title = Text("複素正弦波の内積を計算してみる:", color=YELLOW, font_size=24, weight=BOLD)
        orthog_title.shift(UP * 1.8 + LEFT * 2)
        self.play(Write(orthog_title), run_time=0.5)

        # 1周期での積分として説明
        period_note = Text("（1周期 T での積分を考える）", color=GRAY, font_size=20)
        period_note.shift(UP)
        self.play(Write(period_note), run_time=0.4)

        orthog_calc1 = MathTex(
            r"\langle m | n \rangle = \int_0^T e^{jn\omega_0 t} \, \overline{e^{jm\omega_0 t}} \, dt",
            color=WHITE, font_size=30
        )
        orthog_calc1.shift(UP * 0.4)
        self.play(Write(orthog_calc1), run_time=0.8)
        self.wait(0.4)

        # 計算過程
        orthog_calc2 = MathTex(
            r"= \int_0^T e^{jn\omega_0 t} \, e^{-jm\omega_0 t} \, dt",
            color=WHITE, font_size=30
        )
        orthog_calc2.shift(DOWN * 0.4)
        self.play(Write(orthog_calc2), run_time=0.7)
        self.wait(0.3)

        orthog_calc3 = MathTex(
            r"= \int_0^T e^{j(n-m)\omega_0 t} \, dt",
            color=YELLOW, font_size=30
        )
        orthog_calc3.shift(DOWN * 1.2)
        self.play(Write(orthog_calc3), run_time=0.7)
        self.wait(0.5)

        # 結果
        orthog_result = VGroup(
            MathTex(r"n \neq m", color=RED, font_size=30),
            Text("のとき: 振動して打ち消し合う →", color=RED, font_size=26),
            MathTex(r"0", color=RED, font_size=30),
        ).arrange(RIGHT, buff=0.15)
        orthog_result.shift(DOWN * 2.5)
        self.play(Write(orthog_result), run_time=0.7)
        self.wait(0.4)

        # === 打ち消し合うイメージのアニメーション ===
        self.play(
            FadeOut(orthog_title), FadeOut(period_note), FadeOut(orthog_calc1), FadeOut(orthog_calc2),
            FadeOut(orthog_calc3), FadeOut(orthog_result)
        )
        self.wait(0.2)

        # n≠mの場合の説明
        cancel_title = Text("n ≠ m のとき、なぜ積分が0になる？", color=YELLOW, font_size=24, weight=BOLD)
        cancel_title.shift(UP * 2.0 )
        self.play(Write(cancel_title), run_time=0.6)
        self.wait(0.3)

        # 複素指数関数の実部（cos）を可視化
        cancel_explain = MathTex(
            r"e^{j(n-m)\omega_0 t} = \cos((n-m)\omega_0 t) + j\sin((n-m)\omega_0 t)",
            color=WHITE, font_size=24
        )
        cancel_explain.shift(UP * 1.5)
        self.play(Write(cancel_explain), run_time=0.7)
        self.wait(0.3)

        real_part_note = Text("実部 cos((n-m)ω₀t) を見てみると...", color=TEAL, font_size=22)
        real_part_note.shift(UP * 1)
        self.play(Write(real_part_note), run_time=0.5)
        self.wait(0.3)

        # グラフの軸を作成
        cancel_axes = Axes(
            x_range=[0, 4 * PI, PI],
            y_range=[-1.5, 1.5, 0.5],
            x_length=10,
            y_length=3,
            axis_config={"color": GRAY},
            x_axis_config={"include_tip": True},
            y_axis_config={"include_tip": True},
        ).scale(0.6)
        cancel_axes.shift(DOWN * 0.3)

        x_label_cancel = MathTex(r"t", color=WHITE, font_size=22)
        x_label_cancel.next_to(cancel_axes.x_axis, RIGHT, buff=0.1)
        
        # 0ライン
        zero_line = cancel_axes.plot(lambda x: 0, color=GRAY, stroke_width=1)

        self.play(Create(cancel_axes), Write(x_label_cancel), Create(zero_line), run_time=0.6)
        self.wait(0.2)

        # cos波を描画（n-m = 2 の例）
        cos_wave = cancel_axes.plot(
            lambda x: np.cos(2 * x),
            color=WHITE,
            stroke_width=2
        )
        cos_label = MathTex(r"\cos(2\omega_0 t)", color=WHITE, font_size=22)
        cos_label.next_to(cancel_axes, UP, buff=0.1).shift(RIGHT * 3)

        self.play(Create(cos_wave), Write(cos_label), run_time=0.8)
        self.wait(0.4)

        # 正の部分（青）と負の部分（赤）を塗りつぶし
        positive_area = cancel_axes.get_area(
            cos_wave,
            x_range=[0, PI/4],
            color=BLUE,
            opacity=0.5
        )
        negative_area1 = cancel_axes.get_area(
            cos_wave,
            x_range=[PI/4, 3*PI/4],
            color=RED,
            opacity=0.5
        )
        positive_area2 = cancel_axes.get_area(
            cos_wave,
            x_range=[3*PI/4, 5*PI/4],
            color=BLUE,
            opacity=0.5
        )
        negative_area2 = cancel_axes.get_area(
            cos_wave,
            x_range=[5*PI/4, 7*PI/4],
            color=RED,
            opacity=0.5
        )
        positive_area3 = cancel_axes.get_area(
            cos_wave,
            x_range=[7*PI/4, 9*PI/4],
            color=BLUE,
            opacity=0.5
        )
        negative_area3 = cancel_axes.get_area(
            cos_wave,
            x_range=[9*PI/4, 11*PI/4],
            color=RED,
            opacity=0.5
        )
        positive_area4 = cancel_axes.get_area(
            cos_wave,
            x_range=[11*PI/4, 13*PI/4],
            color=BLUE,
            opacity=0.5
        )
        negative_area4 = cancel_axes.get_area(
            cos_wave,
            x_range=[13*PI/4, 15*PI/4],
            color=RED,
            opacity=0.5
        )
        positive_area5 = cancel_axes.get_area(
            cos_wave,
            x_range=[15*PI/4, 4*PI],
            color=BLUE,
            opacity=0.5
        )

        # 凡例
        legend = VGroup(
            VGroup(
                Rectangle(width=0.4, height=0.3, color=BLUE, fill_opacity=0.5),
                Text("正の部分", color=BLUE, font_size=18),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Rectangle(width=0.4, height=0.3, color=RED, fill_opacity=0.5),
                Text("負の部分", color=RED, font_size=18),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(RIGHT, buff=0.5)
        legend.shift(DOWN * 1.8)

        self.play(
            FadeIn(positive_area), FadeIn(negative_area1), 
            FadeIn(positive_area2), FadeIn(negative_area2),
            FadeIn(positive_area3), FadeIn(negative_area3),
            FadeIn(positive_area4), FadeIn(negative_area4),
            FadeIn(positive_area5),
            Write(legend),
            run_time=0.8
        )
        self.wait(0.5)

        # 打ち消し合うことを説明
        cancel_text = VGroup(
            Text("1周期で積分すると、正と負の面積が", color=WHITE, font_size=22),
            Text("完全に打ち消し合う → 積分 = 0", color=YELLOW, font_size=24, weight=BOLD),
        ).arrange(DOWN, buff=0.15)
        cancel_text.shift(DOWN * 3.0)
        cancel_box = SurroundingRectangle(cancel_text, color=YELLOW, buff=0.1)
        self.play(Write(cancel_text), Create(cancel_box), run_time=0.7)
        self.wait(1.5)

        # クリーンアップ
        self.play(
            FadeOut(cancel_title), FadeOut(cancel_explain), FadeOut(real_part_note),
            FadeOut(cancel_axes), FadeOut(x_label_cancel), FadeOut(zero_line),
            FadeOut(cos_wave), FadeOut(cos_label),
            FadeOut(positive_area), FadeOut(negative_area1),
            FadeOut(positive_area2), FadeOut(negative_area2), FadeOut(positive_area3),
            FadeOut(negative_area3), FadeOut(positive_area4), FadeOut(negative_area4),
            FadeOut(positive_area5),
            FadeOut(legend), FadeOut(cancel_text), FadeOut(cancel_box)
        )
        self.wait(0.3)

        # === n = m の場合 ===
        equal_title = Text("n = m のとき", color=GREEN, font_size=26, weight=BOLD)
        equal_title.shift(UP*2)
        self.play(Write(equal_title), run_time=0.5)
        self.wait(0.3)

        equal_explain = MathTex(
            r"e^{j(n-n)\omega_0 t} = e^{0} = 1",
            color=WHITE, font_size=28
        )
        equal_explain.shift(UP)
        self.play(Write(equal_explain), run_time=0.6)
        self.wait(0.3)

        # 定数1のグラフ
        equal_axes = Axes(
            x_range=[0, 4 * PI, PI],
            y_range=[-0.5, 1.5, 0.5],
            x_length=10,
            y_length=2.5,
            axis_config={"color": GRAY},
        ).scale(0.6)
        equal_axes.shift(DOWN * 0.2)

        const_line = equal_axes.plot(lambda x: 1, color=GREEN, stroke_width=3)
        const_label = MathTex(r"1", color=GREEN, font_size=24)
        const_label.next_to(equal_axes, UP, buff=0.1).shift(LEFT * 4)

        const_area = equal_axes.get_area(
            const_line,
            x_range=[0, 4 * PI],
            color=GREEN,
            opacity=0.4
        )

        self.play(Create(equal_axes), run_time=0.5)
        self.play(Create(const_line), Write(const_label), FadeIn(const_area), run_time=0.7)
        self.wait(0.4)

        equal_result = VGroup(
            Text("常に正なので、1周期で積分すると", color=WHITE, font_size=22),
            MathTex(r"\int_0^T 1 \, dt = T", color=GREEN, font_size=28),
        ).arrange(DOWN, buff=0.15)
        equal_result.shift(DOWN * 2.0)
        equal_box = SurroundingRectangle(equal_result, color=GREEN, buff=0.1)
        self.play(Write(equal_result), Create(equal_box), run_time=0.7)
        self.wait(1.5)

        # クリーンアップ
        self.play(
            FadeOut(equal_title), FadeOut(equal_explain),
            FadeOut(equal_axes), FadeOut(const_line), FadeOut(const_label),
            FadeOut(const_area), FadeOut(equal_result), FadeOut(equal_box)
        )
        self.wait(0.3)

        # 結論
        orthog_conclusion = MathTex(
            r"\langle m | n \rangle = T \delta_{nm}",
            color=YELLOW, font_size=32
        )
        orthog_conclusion.shift(UP * 1.0)
        orthog_conclusion_box = SurroundingRectangle(orthog_conclusion, color=YELLOW, buff=0.15)
        self.play(Write(orthog_conclusion), Create(orthog_conclusion_box), run_time=0.7)
        self.wait(0.5)

        orthog_meaning = Text("→ 複素正弦波も直交基底として使える！", color=YELLOW, font_size=24, weight=BOLD)
        orthog_meaning.shift(UP * 0.2)
        self.play(Write(orthog_meaning), run_time=0.6)
        self.wait(1.0)

        # 補足：フーリエ変換への橋渡し
        bridge_note = VGroup(
            Text("※ フーリエ変換では非周期信号を扱うため", color=WHITE, font_size=22),
            Text("積分区間は -∞ ~ ∞ になるが、直交性の本質は同じ", color=WHITE, font_size=22),
        ).arrange(DOWN, buff=0.1)
        bridge_note.shift(DOWN * 0.8)
        self.play(Write(bridge_note), run_time=0.8)
        self.wait(0.5)

        key_point = Text("実は、クロネッカーのデルタの前のTがnやmに依存しないのがポイント！", color=YELLOW, font_size=22, weight=BOLD)
        key_point.shift(DOWN * 1.8)
        self.play(Write(key_point), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(orthog_conclusion), FadeOut(orthog_conclusion_box),
            FadeOut(orthog_meaning), FadeOut(bridge_note), FadeOut(key_point), FadeOut(subtitle5)
        )
        self.wait(0.3)

        # === Part 6: 内積の意味（射影）の復習 ===
        subtitle6 = Text("準備④: 内積の幾何学的意味", font_size=30, color=PURPLE)
        subtitle6.next_to(title, DOWN)
        self.play(Write(subtitle6), run_time=0.6)
        self.wait(0.5)

        # 6話と11話の復習
        recall_intro = VGroup(
            Text("6話・11話で学んだ内積の意味:", color=YELLOW, font_size=24, weight=BOLD),
        )
        recall_intro.shift(UP * 1.6)
        self.play(Write(recall_intro), run_time=0.6)
        self.wait(0.4)

        # 内積の意味
        inner_meaning = VGroup(
            Text("内積", color=WHITE, font_size=24),
            MathTex(r"\langle e | f \rangle", color=WHITE, font_size=30),
            Text("は", color=WHITE, font_size=24),
            MathTex(r"|f\rangle", color=TEAL, font_size=30),
            Text("を", color=WHITE, font_size=24),
            MathTex(r"|e \rangle ", color=ORANGE, font_size=30),
            Text("で「観測」するイメージ", color=WHITE, font_size=24),
        ).arrange(RIGHT, buff=0.1)
        inner_meaning.shift(UP * 0.8)
        self.play(Write(inner_meaning), run_time=0.8)
        self.wait(0.5)

        # 射影のイメージ
        projection_text = VGroup(
            MathTex(r"|e \rangle", color=ORANGE, font_size=28),
            Text("方向への", color=WHITE, font_size=24),
            MathTex(r"|f\rangle", color=TEAL, font_size=28),
            Text("の「射影」（", color=WHITE, font_size=24),
            MathTex(r"|e \rangle", color=ORANGE, font_size=28),
            Text("に垂直に降りる", color=WHITE, font_size=24),
            MathTex(r"|f\rangle", color=TEAL, font_size=28),
            Text("の影の長さ×", color=WHITE, font_size=24),
            MathTex(r"|e \rangle", color=ORANGE, font_size=28),
            Text("のノルム）", color=WHITE, font_size=24),

        ).arrange(RIGHT, buff=0.1)
        projection_text.shift(UP * 0.0)
        self.play(Write(projection_text), run_time=0.7)
        self.wait(0.5)

        # 視覚的イメージ（簡単なベクトル図）
        arrow_f = Arrow(ORIGIN, RIGHT * 2.5 + UP * 1.5, color=TEAL, buff=0)
        arrow_f.shift(DOWN * 2.5 + LEFT * 2)
        label_f = MathTex(r"|f\rangle", color=TEAL, font_size=24)
        label_f.next_to(arrow_f.get_end(), RIGHT, buff=0.1)

        arrow_g = Arrow(ORIGIN, RIGHT * 3, color=ORANGE, buff=0)
        arrow_g.shift(DOWN * 2.5 + LEFT * 2)
        label_g = MathTex(r"|g\rangle", color=ORANGE, font_size=24)
        label_g.next_to(arrow_g.get_end(), DOWN, buff=0.1)

        # 射影
        proj_line = DashedLine(
            arrow_f.get_end(),
            arrow_f.get_start() + RIGHT * 2.5,
            color=GRAY
        )
        proj_arrow = Arrow(
            arrow_f.get_start(),
            arrow_f.get_start() + RIGHT * 2.5,
            color=GREEN, buff=0, stroke_width=4
        )
        proj_label = Text("垂直に降りる影", color=GREEN, font_size=20)
        proj_label.next_to(proj_arrow, DOWN, buff=0.1)

        self.play(Create(arrow_f), Write(label_f), run_time=0.5)
        self.play(Create(arrow_g), Write(label_g), run_time=0.5)
        self.play(Create(proj_line), Create(proj_arrow), Write(proj_label), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(recall_intro), FadeOut(inner_meaning), FadeOut(projection_text),
            FadeOut(arrow_f), FadeOut(label_f), FadeOut(arrow_g), FadeOut(label_g),
            FadeOut(proj_line), FadeOut(proj_arrow), FadeOut(proj_label),
            FadeOut(subtitle6)
        )
        self.wait(0.3)

        # === Part 7: フーリエ変換の導出 ===
        subtitle7 = Text("フーリエ変換の導出", font_size=30, color=RED)
        subtitle7.next_to(title, DOWN)
        self.play(Write(subtitle7), run_time=0.6)
        self.wait(0.5)

        # アイデアの説明
        idea_text = VGroup(
            Text("信号 f(t) と複素正弦波の内積を計算すると...", color=WHITE, font_size=24),
        )
        idea_text.shift(UP * 1.6)
        self.play(Write(idea_text), run_time=0.7)
        self.wait(0.4)

        # 何を求めているか
        meaning_text = VGroup(
            Text("f(t) の中の「周波数 ω の波の成分」がわかる！", color=YELLOW, font_size=24, weight=BOLD),
        )
        meaning_text.shift(UP * 1.0)
        self.play(Write(meaning_text), run_time=0.7)
        self.wait(0.5)

        # フーリエ変換の式
        ft_formula_title = Text("フーリエ変換:", color=GREEN, font_size=24, weight=BOLD)
        ft_formula_title.shift(UP * 0.3 + LEFT * 4.5)
        self.play(Write(ft_formula_title), run_time=0.4)

        ft_formula = MathTex(
            r"F(\omega) = \langle \omega | f \rangle = \int_{-\infty}^{\infty} f(t) \, e^{-j\omega t} \, dt",
            color=GREEN, font_size=30
        )
        ft_formula.shift(DOWN * 0.4)
        ft_formula_box = SurroundingRectangle(ft_formula, color=GREEN, buff=0.2)
        self.play(Write(ft_formula), Create(ft_formula_box), run_time=0.9)
        self.wait(0.6)

        # 各部分の説明
        parts_explain = VGroup(
            VGroup(
                MathTex(r"F(\omega)", color=ORANGE, font_size=26),
                Text(": 周波数 ω の成分の強さ（スペクトル）", color=ORANGE, font_size=20),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                MathTex(r"f(t)", color=TEAL, font_size=26),
                Text(": 時間領域の信号", color=TEAL, font_size=20),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                MathTex(r"e^{j\omega t}", color=PURPLE, font_size=26),
                Text(": 周波数 ω の複素正弦波（基底）", color=PURPLE, font_size=20),
            ).arrange(RIGHT, buff=0.15),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        parts_explain.shift(DOWN * 1.8)
        self.play(Write(parts_explain), run_time=0.9)
        self.wait(1.5)

        self.play(
            FadeOut(idea_text), FadeOut(meaning_text),
            FadeOut(ft_formula_title), FadeOut(ft_formula), FadeOut(ft_formula_box),
            FadeOut(parts_explain), FadeOut(subtitle7)
        )
        self.wait(0.3)

        # === Part 8: スペクトルの概念 ===
        subtitle8 = Text("スペクトルとは", font_size=30, color=ORANGE)
        subtitle8.next_to(title, DOWN)
        self.play(Write(subtitle8), run_time=0.6)
        self.wait(0.5)

        # スペクトルの説明
        spectrum_intro = VGroup(
            Text("フーリエ変換の結果 F(ω) を", color=WHITE, font_size=24),
            Text("スペクトル", color=YELLOW, font_size=28, weight=BOLD),
            Text("と呼ぶ", color=WHITE, font_size=24),
        ).arrange(RIGHT, buff=0.15)
        spectrum_intro.shift(UP * 1.6)
        self.play(Write(spectrum_intro), run_time=0.7)
        self.wait(0.4)

        # スペクトルの意味
        spectrum_meaning = VGroup(
            Text("スペクトル = 信号の「周波数組成」", color=TEAL, font_size=26, weight=BOLD),
            Text("どの周波数成分がどれだけ含まれているか", color=TEAL, font_size=22),
        ).arrange(DOWN, buff=0.2)
        spectrum_meaning.shift(UP * 0.7)
        spectrum_box = SurroundingRectangle(spectrum_meaning, color=TEAL, buff=0.15)
        self.play(Write(spectrum_meaning), Create(spectrum_box), run_time=0.8)
        self.wait(0.5)

        # 視覚的なイメージ（スペクトルのグラフ）
        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 1.5, 0.5],
            x_length=8,
            y_length=2.5,
            axis_config={"color": GRAY},
        ).scale(0.7)
        axes.shift(DOWN * 1.2)

        x_label = MathTex(r"\omega", color=WHITE, font_size=24)
        x_label.next_to(axes.x_axis, RIGHT)
        y_label = MathTex(r"|F(\omega)|", color=WHITE, font_size=24)
        y_label.next_to(axes.y_axis, UP)

        # スペクトルのバー
        bars = VGroup()
        bar_heights = [0.3, 0.8, 1.2, 0.6, 0.4, 0.2, 0.1]
        bar_colors = [BLUE, GREEN, YELLOW, ORANGE, RED, PURPLE, PINK]
        for i, (h, c) in enumerate(zip(bar_heights, bar_colors)):
            bar = Rectangle(width=0.4, height=h * 1.5, color=c, fill_opacity=0.7)
            bar.move_to(axes.c2p(i + 1.5, h * 0.75))
            bars.add(bar)

        self.play(Create(axes), Write(x_label), Write(y_label), run_time=0.6)
        self.play(LaggedStart(*[GrowFromEdge(bar, DOWN) for bar in bars], lag_ratio=0.1), run_time=0.8)
        self.wait(0.5)

        spectrum_note = Text("各周波数の成分の強さがわかる", color=GREEN, font_size=20)
        spectrum_note.shift(DOWN * 3.0)
        self.play(Write(spectrum_note), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(spectrum_intro), FadeOut(spectrum_meaning), FadeOut(spectrum_box),
            FadeOut(axes), FadeOut(x_label), FadeOut(y_label), FadeOut(bars),
            FadeOut(spectrum_note), FadeOut(subtitle8)
        )
        self.wait(0.3)

        # === Part 8.5: なぜ内積が「成分の強さ」なのか ===
        subtitle8_5 = Text("スペクトルについて考える", font_size=30, color=PURPLE)
        subtitle8_5.next_to(title, DOWN)
        self.play(Write(subtitle8_5), run_time=0.6)
        self.wait(0.5)

        # 疑問の提示
        question_text = Text("なぜ ⟨ω|f⟩ を「成分の強さ」と呼んでよいのか？", color=YELLOW, font_size=24, weight=BOLD)
        question_text.shift(UP * 2)
        self.play(Write(question_text), run_time=0.7)
        self.wait(0.5)

        # 準備③の復習
        recall_orthog = Text("準備③で学んだこと: 複素正弦波は直交する", color=WHITE, font_size=24)
        recall_orthog.shift(UP * 1.5)
        self.play(Write(recall_orthog), run_time=0.6)
        self.wait(0.4)

        # 直交性の式を再掲
        orthog_recap = MathTex(
            r"\langle \omega_m | \omega_n \rangle = T \delta_{mn}",
            color=TEAL, font_size=28
        )
        orthog_recap.shift(UP * 0.8)
        orthog_recap_box = SurroundingRectangle(orthog_recap, color=TEAL, buff=0.15)
        self.play(Write(orthog_recap), Create(orthog_recap_box), run_time=0.8)
        self.wait(0.5)

        # 直交するからこそ分離できる
        separation_text = VGroup(
            Text("直交するからこそ、各周波数成分を", color=ORANGE, font_size=22),
            Text("きれいに分離できる↓", color=ORANGE, font_size=24, weight=BOLD),
        ).arrange(DOWN, buff=0.1)
        separation_text.shift(DOWN * 0.1)
        decomp_formula = MathTex(
            r"|f\rangle = \sum_\omega \frac{\langle \omega | f \rangle}{\sqrt{T}} |\omega \rangle",
            color=GREEN, font_size=32
        )
        decomp_formula.shift(DOWN * 1.7)
        decomp_formula_box = SurroundingRectangle(decomp_formula, color=GREEN, buff=0.2)

        self.play(Write(separation_text), Write(decomp_formula), Create(decomp_formula_box), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(recall_orthog), FadeOut(orthog_recap), FadeOut(orthog_recap_box),
            FadeOut(separation_text), FadeOut(question_text)
        )
        self.wait(0.3)

        # 基底のノルムについて
        # norm_title = Text("基底のノルムを調べてみる", color=YELLOW, font_size=24, weight=BOLD)
        # norm_title.shift(UP * 1.6)
        # self.play(Write(norm_title), run_time=0.6)
        # self.wait(0.4)

        # # ノルムの計算
        # norm_calc = MathTex(
        #     r"\| |\omega \rangle \| = \sqrt{\langle \omega | \omega \rangle} = \sqrt{T}",
        #     color=WHITE, font_size=30
        # )
        # norm_calc.shift(UP * 0.8)
        # self.play(Write(norm_calc), run_time=0.7)
        # self.wait(0.5)

        # # 重要なポイント
        # norm_point = VGroup(
        #     Text("ポイント:", color=YELLOW, font_size=22, weight=BOLD),
        #     Text("√T は積分区間の長さで決まり、", color=WHITE, font_size=22),
        #     Text("周波数には依存しない定数！", color=ORANGE, font_size=24, weight=BOLD),
        # ).arrange(DOWN, buff=0.15)
        # norm_point.shift(UP * 0.0)
        # norm_point_box = SurroundingRectangle(norm_point, color=ORANGE, buff=0.15)
        # self.play(Write(norm_point), Create(norm_point_box), run_time=0.8)
        # self.wait(0.6)

        # self.play(
        #     FadeOut(norm_title), FadeOut(norm_calc),
        #     FadeOut(norm_point), FadeOut(norm_point_box)
        # )
        # self.wait(0.3)

        # 信号の基底分解
        # decomp_title = Text("信号 f(t) を周波数基底で分解すると", color=YELLOW, font_size=24, weight=BOLD)
        # decomp_title.shift(UP * 1.6)
        # self.play(Write(decomp_title), run_time=0.6)
        # self.wait(0.4)

        # 分解の式
        # decomp_formula = MathTex(
        #     r"|f\rangle = \sum_\omega \frac{\langle \omega | f \rangle}{\sqrt{T}} |\omega \rangle",
        #     color=GREEN, font_size=32
        # )
        # decomp_formula.shift(UP * 0.7)
        # decomp_formula_box = SurroundingRectangle(decomp_formula, color=GREEN, buff=0.2)
        # self.play(Write(decomp_formula), Create(decomp_formula_box), run_time=0.9)
        # self.wait(0.5)

        # 各部分の説明
        # decomp_parts = VGroup(
        #     VGroup(
        #         MathTex(r"\langle \omega | f \rangle", color=ORANGE, font_size=26),
        #         Text(": 基底 |ω⟩ 方向への射影", color=ORANGE, font_size=20),
        #     ).arrange(RIGHT, buff=0.15),
        #     VGroup(
        #         MathTex(r"\frac{1}{\sqrt{T}}", color=TEAL, font_size=26),
        #         Text(": 基底の長さで割って正規化", color=TEAL, font_size=20),
        #     ).arrange(RIGHT, buff=0.15),
        # ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        # decomp_parts.shift(DOWN * 0.5)
        # self.play(Write(decomp_parts), run_time=0.8)
        # self.wait(0.6)

        # self.play(
        #     FadeOut(decomp_title), FadeOut(decomp_formula), FadeOut(decomp_formula_box),
        #     FadeOut(decomp_parts)
        # )
        # self.wait(0.3)

        # 結論
        conclusion_title = Text("成分の強さの意味", color=YELLOW, font_size=26, weight=BOLD)
        conclusion_title.shift(UP *2.1)
        self.play(Write(conclusion_title), run_time=0.6)
        self.wait(0.4)

        # 強さは相対的
        relative_text = VGroup(
            Text("成分の「強さ」は相対的な関係性（順序）", color=WHITE, font_size=24),
            Text("→ 定数 √T を除いて考えてよい", color=TEAL, font_size=24),
        ).arrange(DOWN, buff=0.2)
        relative_text.shift(UP * 1.2)
        self.play(Write(relative_text), run_time=0.7)
        self.wait(0.5)

        # 結論の式
        conclusion_formula = VGroup(
            Text("結局、スペクトル", color=WHITE, font_size=24),
            MathTex(r"\langle \omega | f \rangle", color=YELLOW, font_size=30),
            Text("が", color=WHITE, font_size=24),
            Text("成分の強さそのもの", color=YELLOW, font_size=26, weight=BOLD),
            Text("となる！", color=WHITE, font_size=24),
        ).arrange(RIGHT, buff=0.15)
        conclusion_formula.shift(UP * 0.1)
        conclusion_box = SurroundingRectangle(conclusion_formula, color=YELLOW, buff=0.2)
        self.play(Write(conclusion_formula), Create(conclusion_box), run_time=0.9)
        self.wait(0.6)

        # 補足
        supplement = Text("※フーリエ変換の定義上積分区間は無限だが、通常f(t) が有限区間で定義されているので同様の議論が成り立つ", color=GRAY, font_size=18)
        supplement.shift(DOWN * 0.6)
        self.play(Write(supplement), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(question_text), FadeOut(conclusion_title),
            FadeOut(relative_text), FadeOut(conclusion_formula), FadeOut(conclusion_box),
            FadeOut(supplement), FadeOut(subtitle8_5),FadeOut(decomp_formula),
            FadeOut(decomp_formula_box)
        )
        self.wait(0.3)

        # === Part 9: 応用例 ===
        subtitle9 = Text("フーリエ変換の応用", font_size=30, color=TEAL)
        subtitle9.next_to(title, DOWN)
        self.play(Write(subtitle9), run_time=0.6)
        self.wait(0.5)

        # 応用の説明
        app_intro = Text("信号の周波数組成がわかると...", color=WHITE, font_size=24)
        app_intro.shift(UP * 1.6)
        self.play(Write(app_intro), run_time=0.6)
        self.wait(0.4)

        # 応用例のリスト
        applications = VGroup(
            VGroup(
                Text("✓", color=GREEN, font_size=26),
                Text("ローパスフィルタのカットオフ周波数の決定", color=WHITE, font_size=22),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("✓", color=GREEN, font_size=26),
                Text("ノイズ成分の特定と除去", color=WHITE, font_size=22),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("✓", color=GREEN, font_size=26),
                Text("音声認識・音楽の周波数解析", color=WHITE, font_size=22),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("✓", color=GREEN, font_size=26),
                Text("画像処理（2次元フーリエ変換）", color=WHITE, font_size=22),
            ).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        applications.shift(UP * 0.3)

        for app in applications:
            self.play(Write(app), run_time=0.5)
            self.wait(0.2)
        self.wait(0.5)

        # ローパスフィルタの例
        lpf_example = VGroup(
            Text("例: ローパスフィルタ", color=ORANGE, font_size=22, weight=BOLD),
            Text("「どの周波数以上をカットするか」を", color=ORANGE, font_size=20),
            Text("スペクトルを見て判断できる", color=ORANGE, font_size=20),
        ).arrange(DOWN, buff=0.1)
        lpf_example.shift(DOWN * 1.8)
        lpf_box = SurroundingRectangle(lpf_example, color=ORANGE, buff=0.15)
        self.play(Write(lpf_example), Create(lpf_box), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(app_intro), FadeOut(applications),
            FadeOut(lpf_example), FadeOut(lpf_box),
            FadeOut(subtitle9)
        )
        self.wait(0.3)

        # === Part 10: 時間領域と周波数領域 ===
        # subtitle10 = Text("時間領域と周波数領域", font_size=30, color=PURPLE)
        # subtitle10.next_to(title, DOWN)
        # self.play(Write(subtitle10), run_time=0.6)
        # self.wait(0.5)

        # # 2つの見方
        # two_views = VGroup(
        #     Text("同じ信号を2つの視点で見る:", color=YELLOW, font_size=24, weight=BOLD),
        # )
        # two_views.shift(UP * 1.6)
        # self.play(Write(two_views), run_time=0.6)
        # self.wait(0.4)

        # # 左: 時間領域
        # time_side = VGroup(
        #     Text("時間領域", color=BLUE, font_size=24, weight=BOLD),
        #     MathTex(r"f(t)", color=BLUE, font_size=28),
        #     Text("時間とともに値が変化", color=GRAY, font_size=18),
        # ).arrange(DOWN, buff=0.2)
        # time_side.shift(LEFT * 3.5 + UP * 0.5)

        # # 右: 周波数領域
        # freq_side = VGroup(
        #     Text("周波数領域", color=RED, font_size=24, weight=BOLD),
        #     MathTex(r"F(\omega)", color=RED, font_size=28),
        #     Text("各周波数成分の大きさ", color=GRAY, font_size=18),
        # ).arrange(DOWN, buff=0.2)
        # freq_side.shift(RIGHT * 3.5 + UP * 0.5)

        # # 矢印
        # arrow_ft = Arrow(LEFT * 1.5 + UP * 0.5, RIGHT * 1.5 + UP * 0.5, color=GREEN)
        # arrow_label = Text("フーリエ変換", color=GREEN, font_size=20)
        # arrow_label.next_to(arrow_ft, UP, buff=0.1)

        # self.play(Write(time_side), run_time=0.7)
        # self.play(Create(arrow_ft), Write(arrow_label), run_time=0.5)
        # self.play(Write(freq_side), run_time=0.7)
        # self.wait(0.5)

        # # 逆変換
        # arrow_ift = Arrow(RIGHT * 1.5 + DOWN * 0.5, LEFT * 1.5 + DOWN * 0.5, color=ORANGE)
        # arrow_ift_label = Text("逆フーリエ変換", color=ORANGE, font_size=20)
        # arrow_ift_label.next_to(arrow_ift, DOWN, buff=0.1)

        # self.play(Create(arrow_ift), Write(arrow_ift_label), run_time=0.6)
        # self.wait(0.5)

        # # 補足
        # dual_note = Text("両方の表現は等価（情報は失われない）", color=TEAL, font_size=22, weight=BOLD)
        # dual_note.shift(DOWN * 2.0)
        # self.play(Write(dual_note), run_time=0.6)
        # self.wait(1.0)

        # self.play(
        #     FadeOut(two_views), FadeOut(time_side), FadeOut(freq_side),
        #     FadeOut(arrow_ft), FadeOut(arrow_label),
        #     FadeOut(arrow_ift), FadeOut(arrow_ift_label),
        #     FadeOut(dual_note), FadeOut(subtitle10)
        # )
        # self.wait(0.3)

        # === まとめ ===
        subtitle_end = Text("まとめ", font_size=36, color=GOLD, weight=BOLD)
        subtitle_end.next_to(title, DOWN)
        self.play(Write(subtitle_end), run_time=0.7)
        self.wait(0.5)

        summary = VGroup(
            VGroup(
                Text("1.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("複素正弦波を基底として導入", color=WHITE, font_size=28),
                    MathTex(r"e^{j\omega t} = \cos\omega t + j\sin\omega t", color=TEAL, font_size=28),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("2.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("複素正弦波は直交基底", color=WHITE, font_size=28),
                    MathTex(r"\int_0^T e^{j(n-m)\omega_0 t} dt = T\delta_{nm}", color=YELLOW, font_size=28),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("3.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("内積で各周波数成分を抽出（射影）", color=WHITE, font_size=28),
                    MathTex(r"F(\omega) = \int f(t) e^{-j\omega t} dt", color=GREEN, font_size=28),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("4.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("スペクトルで周波数組成がわかる", color=WHITE, font_size=28),
                    Text("→ フィルタ設計などに応用", color=RED, font_size=28),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        summary.scale(0.85)
        summary.shift(UP * 0.1)

        for point in summary:
            self.play(Write(point), run_time=0.7)
            self.wait(0.4)

        self.wait(1.5)

        all_final = VGroup(summary, subtitle_end, title)
        self.play(FadeOut(all_final), run_time=1.0)
        self.wait(0.5)
