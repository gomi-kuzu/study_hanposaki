from manim import *
import numpy as np

class WorldDataModel(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        # タイトル
        title = Text("世界とデータとモデル", font_size=34, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)

        # ============================================================
        # Part 1: データは世界の一部
        # ============================================================
        subtitle1 = Text("データは世界の一部である", font_size=30, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.5)

        # 世界の大きな円
        world_circle = Circle(radius=2.5, color=TEAL, fill_opacity=0.08, stroke_width=2)
        world_circle.shift(DOWN * 0.5)
        world_label = Text("世界（神のみぞ知る真の状態）", color=TEAL, font_size=20)
        world_label.next_to(world_circle, UP, buff=0.1)

        # データの小さな円（世界の部分集合）
        data_circle = Circle(radius=0.9, color=YELLOW, fill_opacity=0.15, stroke_width=2)
        data_circle.shift(DOWN * 0.8 + RIGHT * 0.5)
        data_label = Text("データ", color=YELLOW, font_size=20, weight=BOLD)
        data_label.next_to(data_circle, DOWN, buff=0.1)

        self.play(Create(world_circle), Write(world_label), run_time=0.8)
        self.wait(0.3)
        self.play(Create(data_circle), Write(data_label), run_time=0.7)
        self.wait(0.3)

        part1_note = VGroup(
            Text("世界には膨大な情報が存在するが、", color=WHITE, font_size=22),
            Text("人間が観測できるのはその極一部にすぎない", color=WHITE, font_size=22),
        ).arrange(DOWN, buff=0.15)
        part1_note.shift(DOWN * 2.8)
        self.play(Write(part1_note), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(world_circle), FadeOut(world_label),
            FadeOut(data_circle), FadeOut(data_label),
            FadeOut(part1_note), FadeOut(subtitle1),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: センサによる観測と情報劣化
        # ============================================================
        subtitle2 = Text("センサによる観測と情報劣化", font_size=30, color=GREEN)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)

        obs_intro = VGroup(
            Text("神のみぞ知る世界の状態変化を", color=WHITE, font_size=22),
            Text("何らかのセンサで観測して初めて人間はデータを得る", color=WHITE, font_size=22),
        ).arrange(DOWN, buff=0.15)
        obs_intro.shift(UP * 1.5)
        self.play(Write(obs_intro), run_time=0.7)
        self.wait(0.5)

        # フロー図: 世界 → センサ → データ
        box_world = VGroup(
            RoundedRectangle(width=2.2, height=1.0, corner_radius=0.15, color=TEAL, fill_opacity=0.15),
            Text("世界の状態", color=TEAL, font_size=22, weight=BOLD),
        )
        box_world[1].move_to(box_world[0])
        box_world.shift(LEFT * 4.5 + DOWN * 0.1)

        box_sensor = VGroup(
            RoundedRectangle(width=2.2, height=1.0, corner_radius=0.15, color=ORANGE, fill_opacity=0.15),
            Text("センシング", color=ORANGE, font_size=22),
        )
        box_sensor[1].move_to(box_sensor[0])
        box_sensor.shift(DOWN * 0.1)

        box_data = VGroup(
            RoundedRectangle(width=2.2, height=1.0, corner_radius=0.15, color=YELLOW, fill_opacity=0.15),
            Text("データ", color=YELLOW, font_size=22, weight=BOLD),
        )
        box_data[1].move_to(box_data[0])
        box_data.shift(RIGHT * 4.5 + DOWN * 0.1)

        arrow1 = Arrow(box_world[0].get_right(), box_sensor[0].get_left(), buff=0.15, color=GRAY)
        arrow2 = Arrow(box_sensor[0].get_right(), box_data[0].get_left(), buff=0.15, color=GRAY)

        self.play(
            FadeIn(box_world), FadeIn(box_sensor), FadeIn(box_data),
            Create(arrow1), Create(arrow2),
            run_time=0.8,
        )
        self.wait(0.5)

        # 情報劣化の2要素
        degrade_title = Text("この過程で必ず情報劣化が生じる:", color=RED, font_size=26, weight=BOLD)
        degrade_title.shift(DOWN * 1.2)
        self.play(Write(degrade_title), run_time=0.5)
        self.wait(0.3)

        degrade_items = VGroup(
            VGroup(
                Text("①", color=RED, font_size=26),
                Text("未観測情報の喪失", color=WHITE, font_size=26, weight=BOLD),
                # Text("（次元の落ちた部分空間への射影）", color=GRAY, font_size=18),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                Text("②", color=RED, font_size=26),
                Text("ノイズの混入", color=WHITE, font_size=26, weight=BOLD),
                # Text("（電気信号変換時の誤差）", color=GRAY, font_size=18),
            ).arrange(RIGHT, buff=0.15),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        degrade_items.shift(DOWN * 2.0)
        self.play(Write(degrade_items), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(obs_intro),
            FadeOut(box_world), FadeOut(box_sensor), FadeOut(box_data),
            FadeOut(arrow1), FadeOut(arrow2),
            FadeOut(degrade_title), FadeOut(degrade_items),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2b: 車とフォトカプラの具体例アニメーション
        # ============================================================
        example_title = Text("例：車の接近をフォトカプラ距離センサで計測", font_size=24, color=ORANGE)
        example_title.next_to(subtitle2, DOWN, buff=0.3)
        self.play(Write(example_title), run_time=0.6)
        self.wait(0.3)

        # --- 左側: ユークリッド空間の事象（2D/3Dの車の動き）---
        left_label = Text("世界（ユークリッド空間）", color=TEAL, font_size=20, weight=BOLD)
        left_label.shift(UP * 1.2 + LEFT * 4)
        self.play(Write(left_label), run_time=0.4)

        # 簡易的な道路
        road = Rectangle(width=4, height=0.6, color=GRAY, fill_opacity=0.2, stroke_width=1)
        road.shift(LEFT * 4 + DOWN * 0.2)
        sensor_dot = Dot(LEFT * 2 + DOWN * 0.2, color=ORANGE, radius=0.12)
        sensor_label_small = Text("センサ", color=ORANGE, font_size=14)
        sensor_label_small.next_to(sensor_dot, DOWN, buff=0.1)

        # 車（簡易的な四角形）
        car = VGroup(
            Rectangle(width=0.7, height=0.35, color=BLUE, fill_opacity=0.6),
            Text("車", color=WHITE, font_size=12),
        )
        car[1].move_to(car[0])
        car.move_to(LEFT * 6 + DOWN * 0.2)

        self.play(FadeIn(road), FadeIn(sensor_dot), Write(sensor_label_small), FadeIn(car), run_time=0.5)
        self.wait(0.2)

        # --- 右側: 1次元の距離データ（時系列グラフ）---
        right_label = Text("データ（1次元 距離値）", color=YELLOW, font_size=20, weight=BOLD)
        right_label.shift(UP * 1.2 + RIGHT * 3.5)
        self.play(Write(right_label), run_time=0.4)

        data_axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 4, 1],
            x_length=4,
            y_length=2.5,
            axis_config={"color": GRAY, "include_tip": True},
        ).scale(0.7)
        data_axes.shift(RIGHT * 3.5 + DOWN * 0.5)
        x_lab = MathTex("t", font_size=18, color=WHITE).next_to(data_axes.x_axis, RIGHT, buff=0.05)
        y_lab = Text("距離", font_size=14, color=WHITE).next_to(data_axes.y_axis, UP, buff=0.05)
        self.play(Create(data_axes), Write(x_lab), Write(y_lab), run_time=0.5)

        # 理想距離曲線（ノイズなし）
        ideal_curve = data_axes.plot(
            lambda t: 3.5 - 0.8 * t,
            x_range=[0, 3.8],
            color=TEAL, stroke_width=1.5,
        )
        ideal_label = Text("真の距離", color=TEAL, font_size=14)
        ideal_label.next_to(data_axes, DOWN, buff=0.05).shift(LEFT * 0.8)

        # ノイズ付き計測値をドットで表示（事前に計算）
        np.random.seed(42)
        n_points = 16
        t_vals = np.linspace(0.2, 3.6, n_points)
        d_ideal = 3.5 - 0.8 * t_vals
        noise = np.random.normal(0, 0.25, n_points)
        d_noisy = np.clip(d_ideal + noise, 0.1, 4.0)

        noisy_dots = VGroup(*[
            Dot(data_axes.c2p(t_vals[i], d_noisy[i]), color=YELLOW, radius=0.04)
            for i in range(n_points)
        ])
        noisy_label = Text("計測値（ノイズ混入）", color=YELLOW, font_size=14)
        noisy_label.next_to(ideal_label, DOWN, buff=0.1)

        # --- アニメーション：車が近づく → データ点が打たれる ---
        self.play(Create(ideal_curve), Write(ideal_label), run_time=0.5)

        # 車の移動アニメーション + ドット追加を同時進行
        car_target = LEFT * 2.3 + DOWN * 0.2
        self.play(
            car.animate.move_to(car_target),
            run_time=2.0,
            rate_func=linear,
        )
        self.play(FadeIn(noisy_dots, lag_ratio=0.3), Write(noisy_label), run_time=1.0)
        self.wait(0.3)

        # 情報劣化の注釈
        annot = VGroup(
            Text("ユークリッド空間の事象 → 1次元の距離値に情報が落ちる", color=WHITE, font_size=19),
            Text("+電気信号変換でノイズが混入する", color=RED, font_size=19),
        ).arrange(DOWN, buff=0.15)
        annot.shift(DOWN * 2.5)
        annot_box = SurroundingRectangle(annot, color=RED, buff=0.1)
        self.play(Write(annot), Create(annot_box), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(example_title), FadeOut(left_label), FadeOut(right_label),
            FadeOut(road), FadeOut(sensor_dot), FadeOut(sensor_label_small), FadeOut(car),
            FadeOut(data_axes), FadeOut(x_lab), FadeOut(y_lab),
            FadeOut(ideal_curve), FadeOut(ideal_label),
            FadeOut(noisy_dots), FadeOut(noisy_label),
            FadeOut(annot), FadeOut(annot_box),
            FadeOut(subtitle2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: センサの状態への注意
        # ============================================================
        subtitle3 = Text("観測の設計が重要", font_size=30, color=GOLD)
        subtitle3.next_to(title, DOWN)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.5)

        caution_text = VGroup(
            Text("センサの種類・状態によってもデータは変質する", color=WHITE, font_size=24),
            Text("", font_size=10),
            Text("何を、どんなふうに観測して得られたデータなのかを", color=YELLOW, font_size=24),
            Text("きちんと把握しておくことが大切", color=YELLOW, font_size=24, weight=BOLD),
        ).arrange(DOWN, buff=0.2)
        caution_text.shift(UP * 0.5)
        self.play(Write(caution_text), run_time=0.9)
        self.wait(0.5)

        caution_examples = VGroup(
            VGroup(
                Text("●", color=TEAL, font_size=20),
                Text("計測対象と無関係なバイアスがのっていないか？", color=WHITE, font_size=20),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                Text("●", color=TEAL, font_size=20),
                Text("サンプリング周波数は十分か？（エイリアシング）", color=WHITE, font_size=20),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                Text("●", color=TEAL, font_size=20),
                Text("センサの飽和・非線形性は考慮されているか？", color=WHITE, font_size=20),
            ).arrange(RIGHT, buff=0.15),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        caution_examples.shift(DOWN * 1.5)
        self.play(Write(caution_examples), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(caution_text), FadeOut(caution_examples), FadeOut(subtitle3),
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: モデルとは何か
        # ============================================================
        subtitle4 = Text("モデルとは", font_size=30, color=PURPLE)
        subtitle4.next_to(title, DOWN)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.5)

        model_def = VGroup(
            Text("モデル ＝ パラメータを持った関数", color=YELLOW, font_size=26, weight=BOLD),
            Text("入力を入れると出力を返す", color=WHITE, font_size=22),
        ).arrange(DOWN, buff=0.15)
        model_def.shift(UP * 1.5)
        self.play(Write(model_def), run_time=0.7)
        self.wait(0.4)

        model_formula = MathTex(
            r"y = f_{\theta}(x)", color=TEAL, font_size=38
        )
        model_formula.shift(UP * 0.5)
        model_box = SurroundingRectangle(model_formula, color=TEAL, buff=0.15)

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
                Text(": パラメータ（学習で調整）", color=WHITE, font_size=22),
            ).arrange(RIGHT, buff=0.15),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        parts_desc.shift(DOWN * 0.5)

        self.play(Write(model_formula), Create(model_box), run_time=0.7)
        self.play(Write(parts_desc), run_time=0.8)
        self.wait(0.5)

        ml_note = VGroup(
            Text("機械学習では、データを用いて θ を調整し", color=WHITE, font_size=21),
            Text("未知データにも汎化できるモデルの獲得を目指す", color=YELLOW, font_size=21, weight=BOLD),
        ).arrange(DOWN, buff=0.1)
        ml_note.shift(DOWN * 2.0)
        ml_box = SurroundingRectangle(ml_note, color=YELLOW, buff=0.1)
        self.play(Write(ml_note), Create(ml_box), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(model_def), FadeOut(model_formula), FadeOut(model_box),
            FadeOut(parts_desc), FadeOut(ml_note), FadeOut(ml_box),
            FadeOut(subtitle4),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: モデルの骨格は解析者が設計する
        # ============================================================
        subtitle5 = Text("モデルの設計は解析者の腕の見せ所", font_size=28, color=ORANGE)
        subtitle5.next_to(title, DOWN)
        self.play(Write(subtitle5), run_time=0.6)
        self.wait(0.5)

        design_text = VGroup(
            Text("モデルの骨格（どんな式・どんなパラメータ）を決めるのは解析者", color=WHITE, font_size=22),
            Text("目的やポリシーによって様々な選択肢がある", color=WHITE, font_size=22),
        ).arrange(DOWN, buff=0.15)
        design_text.shift(UP * 1.3)
        self.play(Write(design_text), run_time=0.7)
        self.wait(0.3)

        # 選択肢の例をボックスで並べる
        choice_a = VGroup(
            RoundedRectangle(width=3, height=1.6, corner_radius=0.15, color=BLUE, fill_opacity=0.1),
            VGroup(
                Text("線形回帰", color=BLUE, font_size=20, weight=BOLD),
                MathTex(r"y = w^T x + b", color=BLUE, font_size=22),
            ).arrange(DOWN, buff=0.15),
        )
        choice_a[1].move_to(choice_a[0])

        choice_b = VGroup(
            RoundedRectangle(width=3, height=1.6, corner_radius=0.15, color=GREEN, fill_opacity=0.1),
            VGroup(
                Text("ニューラルネット", color=GREEN, font_size=20, weight=BOLD),
                MathTex(r"y = \sigma(W_2 \sigma(W_1 x))", color=GREEN, font_size=18),
            ).arrange(DOWN, buff=0.15),
        )
        choice_b[1].move_to(choice_b[0])

        choice_c = VGroup(
            RoundedRectangle(width=3, height=1.6, corner_radius=0.15, color=RED, fill_opacity=0.1),
            VGroup(
                Text("ガウス過程", color=RED, font_size=20, weight=BOLD),
                MathTex(r"f \sim \mathcal{GP}(m, k)", color=RED, font_size=22),
            ).arrange(DOWN, buff=0.15),
        )
        choice_c[1].move_to(choice_c[0])

        choices = VGroup(choice_a, choice_b, choice_c).arrange(RIGHT, buff=0.4)
        choices.shift(DOWN * 0.5)
        self.play(FadeIn(choices, lag_ratio=0.3), run_time=1.0)
        self.wait(0.5)

        design_note = Text("→ 問題に適した骨格の選択がモデリングの鍵", color=YELLOW, font_size=22, weight=BOLD)
        design_note.shift(DOWN * 2.3)
        self.play(Write(design_note), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(design_text), FadeOut(choices), FadeOut(design_note),
            FadeOut(subtitle5),
        )
        self.wait(0.3)

        # ============================================================
        # Part 6: 2つのモデリングの方向性（アニメーション）
        # ============================================================
        subtitle6 = Text("モデリングの方向性の種類", font_size=30, color=TEAL)
        subtitle6.next_to(title, DOWN)
        self.play(Write(subtitle6), run_time=0.6)
        self.wait(0.5)

        # --- 左: 識別的モデリング ---
        left_title = Text("① 識別的モデリング", color=BLUE, font_size=22, weight=BOLD)
        left_title.shift(UP * 1.3 + LEFT * 3.5)
        left_desc = Text("入力 → ラベル/値 への変換関数", color=WHITE, font_size=18)
        left_desc.next_to(left_title, DOWN, buff=0.15)
        self.play(Write(left_title), Write(left_desc), run_time=0.6)

        # 識別的モデルのグラフアニメーション（回帰曲線フィッティング）
        disc_axes = Axes(
            x_range=[0, 5, 1], y_range=[0, 4, 1],
            x_length=4, y_length=2.5,
            axis_config={"color": GRAY, "include_tip": True},
        ).scale(0.55)
        disc_axes.shift(LEFT * 3.5 + DOWN * 0.7)

        np.random.seed(7)
        n_disc = 12
        x_disc = np.linspace(0.3, 4.5, n_disc)
        y_disc = 0.5 + 0.6 * x_disc + np.random.normal(0, 0.35, n_disc)
        disc_dots = VGroup(*[
            Dot(disc_axes.c2p(x_disc[i], y_disc[i]), color=YELLOW, radius=0.05)
            for i in range(n_disc)
        ])

        # フィット曲線
        fit_line = disc_axes.plot(lambda x: 0.5 + 0.6 * x, x_range=[0.1, 4.8], color=BLUE, stroke_width=3)
        fit_label = MathTex(r"y = f_\theta(x)", color=BLUE, font_size=22)
        fit_label.next_to(disc_axes, DOWN, buff=0.1)

        self.play(Create(disc_axes), FadeIn(disc_dots, lag_ratio=0.2), run_time=0.7)
        self.play(Create(fit_line), Write(fit_label), run_time=0.8)
        self.wait(0.5)

        # --- 右: 生成的モデリング（ベイズ推論）---
        right_title = Text("② 生成的モデリング", color=RED, font_size=22, weight=BOLD)
        right_title.shift(UP * 1.3 + RIGHT * 3.5)
        right_desc = Text("データが従う確率分布をモデル化", color=WHITE, font_size=18)
        right_desc.next_to(right_title, DOWN, buff=0.15)
        self.play(Write(right_title), Write(right_desc), run_time=0.6)

        # 確率分布のアニメーション（ガウス分布へのフィッティング）
        gen_axes = Axes(
            x_range=[-3, 3, 1], y_range=[0, 0.5, 0.1],
            x_length=4, y_length=2.5,
            axis_config={"color": GRAY, "include_tip": True},
        ).scale(0.55)
        gen_axes.shift(RIGHT * 3.5 + DOWN * 0.7)

        # データ点（ヒストグラム風にドットを並べる）
        np.random.seed(123)
        samples = np.random.normal(0.3, 0.9, 30)
        gen_dots = VGroup(*[
            Dot(gen_axes.c2p(s, 0.02), color=YELLOW, radius=0.04)
            for s in samples
        ])

        # フィットしたガウス分布
        gauss_curve = gen_axes.plot(
            lambda x: 0.44 * np.exp(-0.5 * ((x - 0.3) / 0.9) ** 2),
            x_range=[-3, 3], color=RED, stroke_width=3,
        )
        gauss_label = MathTex(r"p(x|\theta) = \mathcal{N}(\mu, \sigma^2)", color=RED, font_size=20)
        gauss_label.next_to(gen_axes, DOWN, buff=0.1)

        self.play(Create(gen_axes), FadeIn(gen_dots, lag_ratio=0.15), run_time=0.7)
        self.play(Create(gauss_curve), Write(gauss_label), run_time=0.8)
        self.wait(0.5)

        # 下部の比較まとめ
        compare_summary = VGroup(
            VGroup(
                Text("識別的:", color=BLUE, font_size=20, weight=BOLD),
                MathTex(r"x \mapsto y", color=BLUE, font_size=24),
                Text("の写像を直接学習", color=WHITE, font_size=18),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                Text("生成的:", color=RED, font_size=20, weight=BOLD),
                MathTex(r"p(x|\theta)", color=RED, font_size=24),
                Text("データの生成過程を学習", color=WHITE, font_size=18),
            ).arrange(RIGHT, buff=0.15),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        compare_summary.shift(DOWN * 2.7)
        compare_box = SurroundingRectangle(compare_summary, color=YELLOW, buff=0.12)
        self.play(Write(compare_summary), Create(compare_box), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(left_title), FadeOut(left_desc),
            FadeOut(disc_axes), FadeOut(disc_dots), FadeOut(fit_line), FadeOut(fit_label),
            FadeOut(right_title), FadeOut(right_desc),
            FadeOut(gen_axes), FadeOut(gen_dots), FadeOut(gauss_curve), FadeOut(gauss_label),
            FadeOut(compare_summary), FadeOut(compare_box),
            FadeOut(subtitle6),
        )
        self.wait(0.3)

        # ============================================================
        # Part 7: 全体のまとめ
        # ============================================================
        subtitle_end = Text("まとめ", font_size=36, color=GOLD, weight=BOLD)
        subtitle_end.next_to(title, DOWN)
        self.play(Write(subtitle_end), run_time=0.7)
        self.wait(0.5)

        summary = VGroup(
            VGroup(
                Text("1.", color=WHITE, font_size=24, weight=BOLD),
                VGroup(
                    Text("データは世界の一部を観測した結果にすぎない", color=WHITE, font_size=28),
                    Text("情報劣化（次元削減＋ノイズ）が必ず伴う", color=TEAL, font_size=26),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("2.", color=WHITE, font_size=24, weight=BOLD),
                VGroup(
                    Text("何をどう観測したかの理解が解析の出発点", color=WHITE, font_size=28),
                    Text("センサの特性・限界を把握することが重要", color=ORANGE, font_size=26),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("3.", color=WHITE, font_size=24, weight=BOLD),
                VGroup(
                    Text("モデル ＝ パラメータ付き関数、骨格は解析者が設計", color=WHITE, font_size=28),
                    Text("識別的 / 生成的 など多様なアプローチがある", color=YELLOW, font_size=26),
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
