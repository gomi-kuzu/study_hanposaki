from manim import *
import numpy as np

class ModelMathExpression(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        # タイトル
        title = Text("モデルの数式表現", font_size=34, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)

        # ============================================================
        # Part 1: 前回の復習 - モデルとは関数である
        # ============================================================
        subtitle1 = Text("前回の復習", font_size=30, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.5)

        review_text = VGroup(
            Text("モデルとは", color=WHITE, font_size=26),
            Text("パラメータを持った関数である", color=YELLOW, font_size=26, weight=BOLD),
        ).arrange(DOWN, buff=0.15)
        review_text.shift(UP * 1.0)
        self.play(Write(review_text), run_time=0.7)
        self.wait(0.3)

        model_formula = MathTex(
            r"y = f_{\theta}(x)", color=TEAL, font_size=42
        )
        model_formula.shift(UP * 0.0)
        model_box = SurroundingRectangle(model_formula, color=TEAL, buff=0.2)
        self.play(Write(model_formula), Create(model_box), run_time=0.7)
        self.wait(0.5)

        parts_desc = VGroup(
            VGroup(
                MathTex(r"x", color=ORANGE, font_size=30),
                Text(": 入力", color=WHITE, font_size=22),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                MathTex(r"y", color=GREEN, font_size=30),
                Text(": 出力", color=WHITE, font_size=22),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                MathTex(r"\theta", color=YELLOW, font_size=30),
                Text(": パラメータ", color=WHITE, font_size=22),
            ).arrange(RIGHT, buff=0.15),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        parts_desc.shift(DOWN * 1.2)
        self.play(Write(parts_desc), run_time=0.8)
        self.wait(1.0)

        self.play(
            FadeOut(review_text), FadeOut(model_formula), FadeOut(model_box),
            FadeOut(parts_desc), FadeOut(subtitle1),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: 関数系は自由に設計できる
        # ============================================================
        subtitle2 = Text("関数系は目的に応じて自由に設計", font_size=30, color=GREEN)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)

        design_text = VGroup(
            Text("モデルの関数形は解析者が決める", color=WHITE, font_size=24),
            Text("データの特性や目的に応じて様々な選択肢がある", color=WHITE, font_size=24),
        ).arrange(DOWN, buff=0.15)
        design_text.shift(UP * 1.3)
        self.play(Write(design_text), run_time=0.7)
        self.wait(0.5)

        # 具体例を3つ並べる
        example1 = VGroup(
            RoundedRectangle(width=3.5, height=1.4, corner_radius=0.15, color=BLUE, fill_opacity=0.1),
            VGroup(
                Text("線形モデル", color=BLUE, font_size=20, weight=BOLD),
                MathTex(r"f(x) = w_0 + w_1 x", color=BLUE, font_size=22),
            ).arrange(DOWN, buff=0.12),
        )
        example1[1].move_to(example1[0])

        example2 = VGroup(
            RoundedRectangle(width=3.5, height=1.4, corner_radius=0.15, color=ORANGE, fill_opacity=0.1),
            VGroup(
                Text("多項式モデル", color=ORANGE, font_size=20, weight=BOLD),
                MathTex(r"f(x) = w_0 + w_1 x + w_2 x^2", color=ORANGE, font_size=20),
            ).arrange(DOWN, buff=0.12),
        )
        example2[1].move_to(example2[0])

        example3 = VGroup(
            RoundedRectangle(width=3.5, height=1.4, corner_radius=0.15, color=RED, fill_opacity=0.1),
            VGroup(
                Text("ガウス基底", color=RED, font_size=20, weight=BOLD),
                MathTex(r"f(x) = \sum_i w_i e^{-(x-\mu_i)^2}", color=RED, font_size=19),
            ).arrange(DOWN, buff=0.12),
        )
        example3[1].move_to(example3[0])

        examples = VGroup(example1, example2, example3).arrange(DOWN, buff=0.35)
        examples.shift(DOWN * 0.3)
        self.play(FadeIn(examples, lag_ratio=0.3), run_time=1.0)
        self.wait(0.5)

        note_freedom = Text("→ 選択の自由度が解析者の腕の見せ所", color=YELLOW, font_size=22, weight=BOLD)
        note_freedom.shift(DOWN * 2.5)
        self.play(Write(note_freedom), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(design_text), FadeOut(examples), FadeOut(note_freedom),
            FadeOut(subtitle2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: 多項式モデルの具体例
        # ============================================================
        subtitle3 = Text("例：多項式モデル", font_size=30, color=ORANGE)
        subtitle3.next_to(title, DOWN)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.5)

        poly_intro = VGroup(
            Text("第2部（7~12話）で扱ったような多項式も", color=WHITE, font_size=24),
            Text("パラメータ付きモデルの一例である", color=WHITE, font_size=24),
        ).arrange(DOWN, buff=0.15)
        poly_intro.shift(UP * 1.5)
        self.play(Write(poly_intro), run_time=0.7)
        self.wait(0.5)

        poly_formula = MathTex(
            r"f(x) = w_0 + w_1 x + w_2 x^2",
            color=ORANGE, font_size=38
        )
        poly_formula.shift(UP * 0.5)
        poly_box = SurroundingRectangle(poly_formula, color=ORANGE, buff=0.18)
        self.play(Write(poly_formula), Create(poly_box), run_time=0.7)
        self.wait(0.5)

        # パラメータの説明
        param_desc = VGroup(
            MathTex(r"\theta = (w_0, w_1, w_2)", color=YELLOW, font_size=28),
            Text("がパラメータ（未知数）", color=WHITE, font_size=22),
        ).arrange(RIGHT, buff=0.2)
        param_desc.shift(DOWN * 0.2)
        self.play(Write(param_desc), run_time=0.6)
        self.wait(0.5)

        # グラフでの可視化
        axes = Axes(
            x_range=[-2, 2, 1], y_range=[-1, 3, 1],
            x_length=5, y_length=3,
            axis_config={"color": GRAY, "include_tip": True},
        ).scale(0.7)
        axes.shift(DOWN * 1.5)

        # データ点（ノイズ入り）
        np.random.seed(42)
        n_data = 10
        x_data = np.linspace(-1.5, 1.5, n_data)
        y_true = 0.5 + 0.3 * x_data + 0.4 * x_data**2
        y_data = y_true + np.random.normal(0, 0.15, n_data)
        data_dots = VGroup(*[
            Dot(axes.c2p(x_data[i], y_data[i]), color=YELLOW, radius=0.06)
            for i in range(n_data)
        ])

        # フィット曲線
        poly_curve = axes.plot(
            lambda x: 0.5 + 0.3 * x + 0.4 * x**2,
            x_range=[-1.8, 1.8], color=ORANGE, stroke_width=3.5
        )

        self.play(Create(axes), FadeIn(data_dots, lag_ratio=0.2), run_time=0.8)
        self.play(Create(poly_curve), run_time=0.9)
        self.wait(0.5)

        curve_label = Text("パラメータを調整してデータにフィット", color=ORANGE, font_size=20)
        curve_label.next_to(axes, DOWN, buff=0.1)
        self.play(Write(curve_label), run_time=0.6)
        self.wait(1.2)

        self.play(
            FadeOut(poly_intro), FadeOut(poly_formula), FadeOut(poly_box),
            FadeOut(param_desc), FadeOut(axes), FadeOut(data_dots),
            FadeOut(poly_curve), FadeOut(curve_label),
            FadeOut(subtitle3),
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: ベクトル空間との対応
        # ============================================================
        subtitle4 = Text("ベクトル空間との対応", font_size=30, color=PURPLE)
        subtitle4.next_to(title, DOWN)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.5)

        vector_intro = VGroup(
            Text("第2部で学んだように", color=WHITE, font_size=24),
            Text("多項式もベクトル空間と対応させることができる", color=YELLOW, font_size=24, weight=BOLD),
        ).arrange(DOWN, buff=0.15)
        vector_intro.shift(UP * 1.6)
        self.play(Write(vector_intro), run_time=0.7)
        self.wait(0.5)

        # 多項式の式
        poly_eq = MathTex(
            r"f(x) = w_0 + w_1 x + w_2 x^2",
            color=WHITE, font_size=34
        )
        poly_eq.shift(UP * 0.7)
        self.play(Write(poly_eq), run_time=0.6)
        self.wait(0.3)

        # 矢印
        arrow_down = Arrow(UP * 0.4, DOWN * 0.0, color=TEAL, buff=0.1)
        correspond_text = Text("対応", color=TEAL, font_size=20)
        correspond_text.next_to(arrow_down, RIGHT, buff=0.15)
        self.play(Create(arrow_down), Write(correspond_text), run_time=0.5)
        self.wait(0.3)

        # ベクトル表現
        vector_eq = MathTex(
            r"\mathbf{w} = \begin{pmatrix} w_0 \\ w_1 \\ w_2 \end{pmatrix}",
            color=TEAL, font_size=36
        )
        vector_eq.shift(DOWN * 0.8)
        vector_box = SurroundingRectangle(vector_eq, color=TEAL, buff=0.15)
        self.play(Write(vector_eq), Create(vector_box), run_time=0.7)
        self.wait(0.5)

        # 基底の説明
        basis_desc = VGroup(
            Text("基底関数:", color=YELLOW, font_size=22, weight=BOLD),
            MathTex(r"\{1, x, x^2\}", color=YELLOW, font_size=26),
        ).arrange(RIGHT, buff=0.2)
        basis_desc.shift(DOWN * 1.8)
        self.play(Write(basis_desc), run_time=0.6)
        self.wait(1.0)

        self.play(
            FadeOut(vector_intro), FadeOut(poly_eq), FadeOut(arrow_down),
            FadeOut(correspond_text), FadeOut(vector_eq), FadeOut(vector_box),
            FadeOut(basis_desc), FadeOut(subtitle4),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: ベクトル表現のメリット
        # ============================================================
        subtitle5 = Text("ベクトル表現のメリット", font_size=30, color=GOLD)
        subtitle5.next_to(title, DOWN)
        self.play(Write(subtitle5), run_time=0.6)
        self.wait(0.5)

        merit_text = Text("ベクトルで表現できると何が嬉しいのか？", color=WHITE, font_size=26, weight=BOLD)
        merit_text.shift(UP * 1.3)
        self.play(Write(merit_text), run_time=0.6)
        self.wait(0.4)

        # メリットのリスト
        merit_list = VGroup(
            VGroup(
                Text("1.", color=TEAL, font_size=26, weight=BOLD),
                Text("コンピュータでの計算が容易になる", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("2.", color=TEAL, font_size=26, weight=BOLD),
                Text("線形代数の豊富なツールを利用できる", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("3.", color=TEAL, font_size=26, weight=BOLD),
                Text("最適化・勾配計算が効率的に行える", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        merit_list.shift(DOWN * 0.0)
        self.play(Write(merit_list[0]), run_time=0.7)
        self.wait(0.3)
        self.play(Write(merit_list[1]), run_time=0.7)
        self.wait(0.3)
        self.play(Write(merit_list[2]), run_time=0.7)
        self.wait(0.8)

        # 強調ボックス
        highlight = VGroup(
            Text("特にメリット1、2が実用上大きい:", color=YELLOW, font_size=22, weight=BOLD),
            Text("ノイマン型コンピュータや数値計算ライブラリとの親和性が高い", color=YELLOW, font_size=22),
        ).arrange(DOWN, buff=0.1)
        highlight.shift(DOWN * 2.2)
        highlight_box = SurroundingRectangle(highlight, color=YELLOW, buff=0.12)
        self.play(Write(highlight), Create(highlight_box), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(merit_text), FadeOut(merit_list),
            FadeOut(highlight), FadeOut(highlight_box),
            FadeOut(subtitle5),
        )
        self.wait(0.3)

        # ============================================================
        # Part 6: 次回予告 - 線形回帰へ
        # ============================================================
        subtitle6 = Text("この先の話の展望", font_size=32, color=RED, weight=BOLD)
        subtitle6.next_to(title, DOWN)
        self.play(Write(subtitle6), run_time=0.7)
        self.wait(0.5)

        preview_intro = VGroup(
            Text("ここで重要な事実:", color=WHITE, font_size=24),
            Text("変数xに対しては非線形でも", color=YELLOW, font_size=24, weight=BOLD),
            Text("基底をうまくとれば線形代数の範疇となる", color=YELLOW, font_size=24, weight=BOLD),
        ).arrange(DOWN, buff=0.15)
        preview_intro.shift(UP * 1.0)
        self.play(Write(preview_intro), run_time=0.8)
        self.wait(0.6)

        # 具体例
        example_nonlinear = MathTex(
            r"f(x) = w_0 + w_1 x + w_2 x^2",
            color=ORANGE, font_size=32
        )
        example_nonlinear.shift(UP * 0.0)
        self.play(Write(example_nonlinear), run_time=0.6)
        self.wait(0.3)

        arrow_transform = Arrow(LEFT * 0.0 + DOWN * 0.3, LEFT * 0.0 + DOWN * 0.8, color=TEAL, buff=0.05)
        transform_text = Text("基底変換", color=TEAL, font_size=18)
        transform_text.next_to(arrow_transform, RIGHT, buff=0.1)
        self.play(Create(arrow_transform), Write(transform_text), run_time=0.5)
        self.wait(0.2)

        # 線形表現
        linear_form = MathTex(
            r"\mathbf{y} = \mathbf{X} \mathbf{w}",
            color=TEAL, font_size=36
        )
        linear_form.shift(DOWN * 1.3)
        linear_box = SurroundingRectangle(linear_form, color=TEAL, buff=0.15)
        self.play(Write(linear_form), Create(linear_box), run_time=0.7)
        self.wait(0.5)

        linear_note = Text("パラメータwについては線形！", color=TEAL, font_size=22, weight=BOLD)
        linear_note.next_to(linear_form, DOWN, buff=0.3)
        self.play(Write(linear_note), run_time=0.6)
        self.wait(1.0)

        self.play(
            FadeOut(preview_intro), FadeOut(example_nonlinear),
            FadeOut(arrow_transform), FadeOut(transform_text),
            FadeOut(linear_form), FadeOut(linear_box), FadeOut(linear_note),
        )
        self.wait(0.3)

        # 線形回帰の紹介
        lr_title = Text("線形回帰（Linear Regression）", font_size=28, color=GREEN, weight=BOLD)
        lr_title.shift(UP * 0.8)
        self.play(Write(lr_title), run_time=0.6)
        self.wait(0.4)

        lr_desc = VGroup(
            Text("このアプローチを利用した代表的な手法が", color=WHITE, font_size=24),
            Text("「線形回帰」である", color=GREEN, font_size=26, weight=BOLD),
        ).arrange(DOWN, buff=0.15)
        lr_desc.shift(UP * 0.0)
        self.play(Write(lr_desc), run_time=0.7)
        self.wait(0.6)

        lr_features = VGroup(
            VGroup(
                Text("●", color=GREEN, font_size=22),
                Text("解析的に解ける（最小二乗法）", color=WHITE, font_size=22),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                Text("●", color=GREEN, font_size=22),
                Text("実装が容易で計算も高速", color=WHITE, font_size=22),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                Text("●", color=GREEN, font_size=22),
                Text("様々な拡張が可能（正則化など）", color=WHITE, font_size=22),
            ).arrange(RIGHT, buff=0.15),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        lr_features.shift(DOWN * 1.2)
        self.play(Write(lr_features), run_time=0.8)
        self.wait(1.0)

        next_episode = Text("詳しくは次回以降で！", color=RED, font_size=24, weight=BOLD)
        next_episode.shift(DOWN * 2.5)
        next_box = SurroundingRectangle(next_episode, color=RED, buff=0.12)
        self.play(Write(next_episode), Create(next_box), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(lr_title), FadeOut(lr_desc), FadeOut(lr_features),
            FadeOut(next_episode), FadeOut(next_box),
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
                Text("1.", color=WHITE, font_size=24, weight=BOLD),
                VGroup(
                    Text("モデルの関数形は目的に応じて自由に設計できる", color=WHITE, font_size=26),
                    Text("多項式モデルはその代表例の一つ", color=ORANGE, font_size=24),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("2.", color=WHITE, font_size=24, weight=BOLD),
                VGroup(
                    Text("関数をベクトル空間と対応させることができる", color=WHITE, font_size=26),
                    Text("コンピュータ計算が容易になる", color=TEAL, font_size=24),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("3.", color=WHITE, font_size=24, weight=BOLD),
                VGroup(
                    Text("基底をうまくとれば線形代数の範疇で扱える", color=WHITE, font_size=26),
                    Text("線形回帰は次回以降で詳しく学ぶ", color=GREEN, font_size=24),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        summary.scale(0.85)
        summary.shift(DOWN * 0.2)

        for point in summary:
            self.play(Write(point), run_time=0.7)
            self.wait(0.3)

        self.wait(1.5)

        all_final = VGroup(summary, subtitle_end, title)
        self.play(FadeOut(all_final), run_time=1.0)
        self.wait(0.5)
