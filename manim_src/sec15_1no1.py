from manim import *
import numpy as np

class RegressionAndCost(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        # タイトル
        title = Text("回帰問題のいち解法", font_size=34, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)

        # ============================================================
        # Part 1: データサイエンスの基本的な問題
        # ============================================================
        subtitle1 = Text("データサイエンスの基本的な問題", font_size=30, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.5)

        ds_intro = VGroup(
            Text("データから「入力→出力」の関係を学習する", color=WHITE, font_size=26),
            Text("これが機械学習・データサイエンスのひとつの目的", color=YELLOW, font_size=26, weight=BOLD),
        ).arrange(DOWN, buff=0.15)
        ds_intro.shift(UP * 1.5)
        self.play(Write(ds_intro), run_time=0.7)
        self.wait(0.6)

        ds_examples = VGroup(
            VGroup(
                Text("●", color=TEAL, font_size=22),
                Text("住宅の広さ・立地 → 価格の予測", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("●", color=TEAL, font_size=22),
                Text("患者のデータ → 病気のリスク推定", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("●", color=TEAL, font_size=22),
                Text("気象データ → 気温の予測", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        ds_examples.shift(DOWN * 0.2)
        for item in ds_examples:
            self.play(Write(item), run_time=0.5)
            self.wait(0.2)

        problem_type = VGroup(
            Text("出力が連続値の場合 → ", color=WHITE, font_size=26),
            Text("回帰問題（Regression）", color=ORANGE, font_size=26, weight=BOLD),
        ).arrange(RIGHT, buff=0.1)
        problem_type.shift(DOWN * 1.5)
        self.play(Write(problem_type), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(ds_intro), FadeOut(ds_examples), FadeOut(problem_type),
            FadeOut(subtitle1),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: 線形回帰と最小二乗法の概観（グラフ）
        # ============================================================
        subtitle2 = Text("線形回帰と最小二乗法の概観", font_size=30, color=ORANGE)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)

        overview_text = Text("データへの「直線当てはめ」が線形回帰の基本イメージ", color=WHITE, font_size=26)
        overview_text.shift(UP * 1.7)
        self.play(Write(overview_text), run_time=0.6)
        self.wait(0.4)

        # 散布図 + 回帰直線
        axes = Axes(
            x_range=[0, 5, 1], y_range=[0, 6, 1],
            x_length=5.0, y_length=3.5,
            axis_config={"color": GRAY, "include_tip": True},
            x_axis_config={"include_numbers": True},
            y_axis_config={"include_numbers": True},
        ).scale(0.78)
        axes.shift(DOWN * 0.8 + LEFT * 2.5)

        x_label = axes.get_x_axis_label(MathTex(r"x", font_size=28), direction=RIGHT)
        y_label = axes.get_y_axis_label(MathTex(r"y", font_size=28), direction=UP)

        # 散布データ（疑似的な線形関係）
        np.random.seed(42)
        raw_xs = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]
        raw_ys = [0.8, 1.3, 1.9, 2.6, 3.0, 3.4, 3.8, 4.6, 4.9]
        scatter_dots = VGroup(*[
            Dot(axes.c2p(x, y), color=YELLOW, radius=0.08)
            for x, y in zip(raw_xs, raw_ys)
        ])

        # 回帰直線 y = 1.04x + 0.25（上のデータのほぼ最小二乗直線）
        reg_line = axes.plot(lambda x: 1.04 * x + 0.25, x_range=[0, 4.8], color=ORANGE, stroke_width=3)
        reg_label = MathTex(r"f(x) = w_0 + w_1 x", color=ORANGE, font_size=30)
        reg_label.next_to(axes, RIGHT, buff=0.2).shift(UP * 0.5)

        # 残差（縦線）
        residual_lines = VGroup(*[
            DashedLine(
                axes.c2p(x, y),
                axes.c2p(x, 1.04 * x + 0.25),
                color=RED, stroke_width=2, dash_length=0.08
            )
            for x, y in zip(raw_xs, raw_ys)
        ])
        residual_label = VGroup(
            Text("残差を二乗して足した量を最小化する直線を探す", color=RED, font_size=22),
        ).arrange(DOWN, buff=0.08)
        residual_label.next_to(axes, RIGHT, buff=0.2).shift(DOWN * 0.4)

        self.play(Create(axes), Write(x_label), Write(y_label), run_time=0.6)
        self.play(FadeIn(scatter_dots), run_time=0.5)
        self.wait(0.4)
        self.play(Create(reg_line), Write(reg_label), run_time=0.7)
        self.wait(0.3)
        self.play(Create(residual_lines), Write(residual_label), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(overview_text), FadeOut(axes), FadeOut(x_label), FadeOut(y_label),
            FadeOut(scatter_dots), FadeOut(reg_line), FadeOut(reg_label),
            FadeOut(residual_lines), FadeOut(residual_label),
            FadeOut(subtitle2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: 全体の流れ（一覧）
        # ============================================================
        subtitle3 = Text("問題を解く流れ", font_size=30, color=TEAL)
        subtitle3.next_to(title, DOWN)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.5)

        flow_intro = Text("以下の4ステップで最適なモデルパラメータを探す", color=WHITE, font_size=26)
        flow_intro.shift(UP * 1.5)
        self.play(Write(flow_intro), run_time=0.6)
        self.wait(0.3)

        flow_items = VGroup(
            VGroup(
                Text("[1]", color=GOLD, font_size=26, weight=BOLD),
                Text("データを記号で表現する", color=WHITE, font_size=26),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("[2]", color=GOLD, font_size=26, weight=BOLD),
                Text("モデルを設計する", color=WHITE, font_size=26),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("[3]", color=GOLD, font_size=26, weight=BOLD),
                Text("コスト関数を設定する", color=WHITE, font_size=26),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("[4]", color=GOLD, font_size=26, weight=BOLD),
                Text("コストを最小にするパラメータを探す", color=WHITE, font_size=26),
            ).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        flow_items.shift(DOWN * 0.2)

        for item in flow_items:
            self.play(Write(item), run_time=0.5)
            self.wait(0.3)
        self.wait(1.5)

        self.play(
            FadeOut(flow_intro), FadeOut(flow_items),
            FadeOut(subtitle3),
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: [1] データを記号で表現
        # ============================================================
        subtitle4 = Text("[1]  データを記号で表現する", font_size=30, color=GOLD)
        subtitle4.next_to(title, DOWN)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.5)

        data_intro = Text("N 個のデータを観測したとする。n 番目のデータを次のように表す：", color=WHITE, font_size=26)
        data_intro.shift(UP * 1.7)
        self.play(Write(data_intro), run_time=0.6)
        self.wait(0.4)

        data_notation = VGroup(
            VGroup(
                Text("入力（特徴ベクトル）：", color=WHITE, font_size=24),
                MathTex(r"\mathbf{x}_n \in \mathbb{R}^D", color=TEAL, font_size=32),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("出力（ターゲット）：", color=WHITE, font_size=24),
                MathTex(r"y_n \in \mathbb{R}", color=YELLOW, font_size=32),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        data_notation.shift(UP * 0.6)
        for item in data_notation:
            self.play(Write(item), run_time=0.6)
            self.wait(0.3)
        self.wait(0.3)

        data_set_expr = MathTex(
            r"\mathcal{D} = \{(\mathbf{x}_n,\, y_n)\}_{n=1}^{N}",
            color=WHITE, font_size=28
        )
        data_set_expr.shift(DOWN * 0.3)
        data_set_box = SurroundingRectangle(data_set_expr, color=TEAL, buff=0.15)
        self.play(Write(data_set_expr), Create(data_set_box), run_time=0.6)
        self.wait(0.5)

        data_dim_note = VGroup(
            # MathTex(r"D", color=TEAL, font_size=26),
            Text("D：入力の次元数（特徴の数）、N：データ点の総数", color=WHITE, font_size=22),
            # MathTex(r"N", color=YELLOW, font_size=26),
            # Text("：データ点の総数", color=WHITE, font_size=22),
        ).arrange(RIGHT, buff=0.1)
        data_dim_note.shift(DOWN * 1.1)
        self.play(Write(data_dim_note), run_time=0.6)
        self.wait(0.3)

        data_example = VGroup(
            Text("例：住宅価格予測であれば", color=WHITE, font_size=21),
        )
        data_example.shift(DOWN * 1.7)
        self.play(Write(data_example), run_time=0.5)
        self.wait(0.2)

        data_example2 = VGroup(
            MathTex(r"\mathbf{x}_n = \begin{pmatrix} \mathrm{area} \\ \mathrm{age} \\ \mathrm{distance} \end{pmatrix},\quad y_n = \mathrm{price}", color=WHITE, font_size=24),
        )
        data_example2.shift(DOWN * 2.7)
        self.play(Write(data_example2), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(data_intro), FadeOut(data_notation),
            FadeOut(data_set_expr), FadeOut(data_set_box),
            FadeOut(data_dim_note), FadeOut(data_example), FadeOut(data_example2),
            FadeOut(subtitle4),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: [2] モデルを設計する
        # ============================================================
        subtitle5 = Text("[2]  モデルを設計する", font_size=30, color=GOLD)
        subtitle5.next_to(title, DOWN)
        self.play(Write(subtitle5), run_time=0.6)
        self.wait(0.5)

        model_design_note = VGroup(
            Text("モデルは「与えられるもの」ではなく、設計者が仮定や経験をもとに「設計するもの」", color=YELLOW, font_size=26, weight=BOLD),
        ).arrange(DOWN, buff=0.12)
        model_design_note.shift(UP * 1.7)
        self.play(Write(model_design_note), run_time=0.7)
        self.wait(0.5)

        model_design_detail = VGroup(
            VGroup(
                Text("●", color=TEAL, font_size=22),
                Text("データを俯瞰して傾向を掴む", color=WHITE, font_size=23),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("●", color=TEAL, font_size=22),
                Text("計算コスト・解釈性・汎化性能 などの要因も考慮", color=WHITE, font_size=23),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("●", color=TEAL, font_size=22),
                Text("13話で強調した通り、モデルは世界の近似に過ぎない", color=WHITE, font_size=23),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        model_design_detail.shift(UP * 0.6)
        for item in model_design_detail:
            self.play(Write(item), run_time=0.5)
            self.wait(0.2)
        self.wait(0.3)

        model_today = Text("今回の例：線形モデル（基底の空間上の平面を仮定）", color=ORANGE, font_size=23, weight=BOLD)
        model_today.shift(DOWN * 0.3)
        self.play(Write(model_today), run_time=0.6)
        self.wait(0.3)

        linear_model = MathTex(
            r"f(\mathbf{x}) = w_0 + \sum_{d=1}^{D} w_d x_d",
            color=TEAL, font_size=36
        )
        linear_model.shift(DOWN * 1.05)
        # linear_model_box = SurroundingRectangle(linear_model, color=TEAL, buff=0.18)
        self.play(Write(linear_model), run_time=0.8)
        self.wait(0.5)

        param_desc = VGroup(
            VGroup(
                MathTex(r"w_0", color=YELLOW, font_size=28),
                Text("：バイアス（切片）", color=WHITE, font_size=22),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                MathTex(r"w_1, \ldots, w_D", color=YELLOW, font_size=28),
                Text("：各特徴への重み", color=WHITE, font_size=22),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(RIGHT, buff=0.5)
        param_desc.shift(DOWN * 2.2)
        self.play(Write(param_desc), run_time=0.6)
        self.wait(0.5)

        param_vec = VGroup(
            Text("これらをまとめてパラメータベクトル", color=WHITE, font_size=22),
            MathTex(r"\mathbf{w} = (w_0, w_1, \ldots, w_D)^\top", color=YELLOW, font_size=26),
            Text("と書く", color=WHITE, font_size=22),
        ).arrange(RIGHT, buff=0.15)
        param_vec.shift(DOWN * 2.7)
        self.play(Write(param_vec), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(model_design_note), FadeOut(model_design_detail),
            FadeOut(model_today), FadeOut(linear_model), #FadeOut(linear_model_box),
            FadeOut(param_desc), FadeOut(param_vec),
            FadeOut(subtitle5),
        )
        self.wait(0.3)

        # ============================================================
        # Part 6: [3] コスト関数を設定する
        # ============================================================
        subtitle6 = Text("[3]  コスト関数を設定する", font_size=30, color=GOLD)
        subtitle6.next_to(title, DOWN)
        self.play(Write(subtitle6), run_time=0.6)
        self.wait(0.5)

        cost_intro = VGroup(
            Text("「データへの当てはまりの良さ」をどう数値化するか", color=WHITE, font_size=24),
            Text("この基準も設計者が選択・設計するものである", color=YELLOW, font_size=24, weight=BOLD),
        ).arrange(DOWN, buff=0.12)
        cost_intro.shift(UP * 1.7)
        self.play(Write(cost_intro), run_time=0.7)
        self.wait(0.5)

        cost_names = VGroup(
            Text("この「当てはまりの基準」を表す関数を以下のように呼ぶ（文脈によって変わる）", color=WHITE, font_size=23),
        )
        cost_names.shift(UP * 0.9)
        self.play(Write(cost_names), run_time=0.5)
        self.wait(0.2)

        cost_name_list = VGroup(
            VGroup(Text("● コスト関数 (cost function)", color=ORANGE, font_size=23)).arrange(RIGHT, buff=0.2),
            VGroup(Text("● 誤差関数 (loss function)", color=ORANGE, font_size=23)).arrange(RIGHT, buff=0.2),
            VGroup(Text("● 目的関数 (objective function)", color=ORANGE, font_size=23)).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        # cost_name_list.shift(UP * 0.2)
        self.play(Write(cost_name_list), run_time=0.6)
        self.wait(0.4)

        cost_today = Text("今回の例：二乗誤差（squared error）を使う", color=WHITE, font_size=23, weight=BOLD)
        cost_today.shift(DOWN)
        self.play(Write(cost_today), run_time=0.6)
        self.wait(0.3)

        cost_func = MathTex(
            r"J(\mathbf{w}) = \sum_{n=1}^{N} \left( y_n - f(\mathbf{x}_n) \right)^2",
            color=ORANGE, font_size=34
        )
        cost_func.shift(DOWN * 1.7)
        # cost_func_box = SurroundingRectangle(cost_func, color=ORANGE, buff=0.18)
        self.play(Write(cost_func), run_time=0.8)
        self.wait(0.5)

        lsq_note = VGroup(
            Text("この二乗誤差を最小化する手法を", color=WHITE, font_size=22),
            Text("最小二乗法（Least Squares Method）", color=YELLOW, font_size=22, weight=BOLD),
            Text("と呼ぶ", color=WHITE, font_size=22),
        ).arrange(RIGHT, buff=0.12)
        lsq_note.shift(DOWN * 2.65)
        self.play(Write(lsq_note), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(cost_intro), FadeOut(cost_names), FadeOut(cost_name_list),
            FadeOut(cost_today), FadeOut(cost_func), #FadeOut(cost_func_box),
            FadeOut(lsq_note),
            FadeOut(subtitle6),
        )
        self.wait(0.3)

        # ============================================================
        # Part 7: [4] コスト関数の行列表現へ
        # ============================================================
        subtitle7 = Text("[4]  コスト関数を行列で表現する", font_size=30, color=GOLD)
        subtitle7.next_to(title, DOWN)
        self.play(Write(subtitle7), run_time=0.6)
        self.wait(0.5)

        matrix_goal = VGroup(
            Text("※この動画では", color=WHITE, font_size=26),
            Text("コスト関数をベクトル・行列で表現", color=TEAL, font_size=26, weight=BOLD),
            Text("するところまでを説明する", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.12)
        matrix_goal.shift(UP * 1.7)
        self.play(Write(matrix_goal), run_time=0.6)
        self.wait(0.3)

        next_note_preview = Text("（パラメータの解き方は次の動画で！）", color=GREEN, font_size=21)
        next_note_preview.shift(UP * 1.2)
        self.play(Write(next_note_preview), run_time=0.5)
        self.wait(0.4)

        # ステップ1: バイアス挿入
        step1_title = Text("Step 1：入力ベクトルにバイアス項を追加", color=WHITE, font_size=23, weight=BOLD)
        step1_title.shift(UP * 0.6)
        self.play(Write(step1_title), run_time=0.5)
        self.wait(0.2)

        step1_expr = MathTex(
            r"\mathbf{x}_n' = \begin{pmatrix} 1 \\ x_{n1} \\ \vdots \\ x_{nD} \end{pmatrix} \in \mathbb{R}^{D+1}",
            color=TEAL, font_size=30
        )
        step1_expr.shift(DOWN * 0.5)

        step1_note = VGroup(
            Text("先頭に 1 を追加することで、バイアス", color=WHITE, font_size=21),
            MathTex(r"w_0", color=YELLOW, font_size=24),
            Text("も重みベクトルに組み込める", color=WHITE, font_size=21),
        ).arrange(RIGHT, buff=0.1)
        step1_note.shift(DOWN * 1.6)

        self.play(Write(step1_expr), run_time=0.6)
        self.play(Write(step1_note), run_time=0.5)
        self.wait(0.5)

        step1_fw = MathTex(
            r"f(\mathbf{x}_n) = w_0 + \sum_{d=1}^{D} w_d x_{nd} = \mathbf{x}_n^{\prime\top} \mathbf{w}",
            color=ORANGE, font_size=28
        )
        step1_fw.shift(DOWN * 2.4)
        step1_fw_box = SurroundingRectangle(step1_fw, color=ORANGE, buff=0.12)
        self.play(Write(step1_fw), Create(step1_fw_box), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(step1_title), FadeOut(step1_expr), FadeOut(step1_note),
            FadeOut(step1_fw), FadeOut(step1_fw_box), FadeOut(next_note_preview),
            FadeOut(matrix_goal)
        )
        self.wait(0.2)

        # ステップ2: データ行列の定義
        step2_title = Text("Step 2：全データを並べたデータ行列を定義する", color=WHITE, font_size=23, weight=BOLD)
        step2_title.shift(UP * 1.1)
        self.play(Write(step2_title), run_time=0.5)
        self.wait(0.2)

        step2_expr = MathTex(
            r"X = \begin{pmatrix} \mathbf{x}_1^{\prime\top} \\ \mathbf{x}_2^{\prime\top} \\ \vdots \\ \mathbf{x}_N^{\prime\top} \end{pmatrix}"
            r"= \begin{pmatrix} 1 & x_{11} & \cdots & x_{1D} \\ 1 & x_{21} & \cdots & x_{2D} \\ \vdots & \vdots & \ddots & \vdots \\ 1 & x_{N1} & \cdots & x_{ND} \end{pmatrix}"
            r"\in \mathbb{R}^{N \times (D+1)}",
            color=TEAL, font_size=30
        )
        step2_expr.shift(DOWN * 0.3)

        step2_note = VGroup(
            MathTex(r"N", color=YELLOW, font_size=26),
            Text("行", color=WHITE, font_size=22),
            MathTex(r"(D+1)", color=TEAL, font_size=26),
            Text("列の行列（各行が1サンプル）", color=WHITE, font_size=22),
        ).arrange(RIGHT, buff=0.1)
        step2_note.shift(DOWN * 2.1)

        self.play(Write(step2_expr), run_time=0.8)
        self.play(Write(step2_note), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(step2_title), FadeOut(step2_expr), FadeOut(step2_note))
        self.wait(0.2)

        # ステップ3: 出力ベクトル
        step3_title = Text("Step 3：出力をまとめたベクトルを定義する", color=WHITE, font_size=23, weight=BOLD)
        step3_title.shift(UP * 0.8)
        self.play(Write(step3_title), run_time=0.5)
        self.wait(0.2)

        step3_expr = MathTex(
            r"\mathbf{y} = \begin{pmatrix} y_1 \\ y_2 \\ \vdots \\ y_N \end{pmatrix} \in \mathbb{R}^N",
            color=YELLOW, font_size=34
        )
        step3_expr.shift(DOWN * 0.7)

        self.play(Write(step3_expr), run_time=0.6)
        self.wait(1.0)

        self.play(FadeOut(step3_title), FadeOut(step3_expr))
        self.wait(0.2)

        # ステップ4: コスト関数の行列表現（式展開）
        step4_title = Text("Step 4：コスト関数を行列で表現する", color=WHITE, font_size=23, weight=BOLD)
        step4_title.shift(UP * 1.8)
        self.play(Write(step4_title), run_time=0.5)
        self.wait(0.2)

        derive_label = Text("まず予測誤差ベクトルを考えると…", color=WHITE, font_size=22)
        derive_label.shift(UP * 1.15)
        self.play(Write(derive_label), run_time=0.4)
        self.wait(0.2)

        # X w の各行は x'_n^T w = f(x_n) なので誤差ベクトルは y - Xw
        err_vec = MathTex(
            r"\mathbf{y} - X\mathbf{w} = \begin{pmatrix} y_1 - \mathbf{x}_1^{\prime\top}\mathbf{w} \\ \vdots \\ y_N - \mathbf{x}_N^{\prime\top}\mathbf{w} \end{pmatrix}"
            r"= \begin{pmatrix} y_1 - f(\mathbf{x}_1) \\ \vdots \\ y_N - f(\mathbf{x}_N) \end{pmatrix}",
            color=WHITE, font_size=30
        )
        err_vec.shift(DOWN * 0.3)
        self.play(Write(err_vec), run_time=0.8)
        self.wait(0.8)

        self.play(FadeOut(derive_label), FadeOut(err_vec))
        self.wait(0.1)

        derive_label2 = Text("このベクトルの「二乗ノルム」がコスト関数！", color=YELLOW, font_size=30, weight=BOLD)
        derive_label2.shift(UP * 1.0)
        self.play(Write(derive_label2), run_time=0.5)
        self.wait(0.2)

        cost_expand = MathTex(
            r"J(\mathbf{w})"
            r"= \sum_{n=1}^{N}(y_n - f(\mathbf{x}_n))^2",
            color=WHITE, font_size=30
        )
        cost_expand.shift(UP * 0.2)
        self.play(Write(cost_expand), run_time=0.6)
        self.wait(0.4)

        cost_expand2 = MathTex(
            r"= \|\mathbf{y} - X\mathbf{w}\|^2",
            color=WHITE, font_size=30
        )
        cost_expand2.shift(DOWN * 0.5)
        self.play(Write(cost_expand2), run_time=0.5)
        self.wait(0.3)

        cost_final = MathTex(
            r"= (\mathbf{y} - X\mathbf{w})^\top (\mathbf{y} - X\mathbf{w})",
            color=ORANGE, font_size=30
        )
        cost_final.shift(DOWN * 1.3)
        cost_final_box = SurroundingRectangle(cost_final, color=ORANGE, buff=0.15)
        self.play(Write(cost_final), Create(cost_final_box), run_time=0.7)
        self.wait(0.5)

        norm_note = VGroup(
            # Text("（", color=WHITE, font_size=21),
            MathTex(r"\because \|\mathbf{v}\|^2 = \mathbf{v}^\top \mathbf{v}", color=TEAL, font_size=24),
            # Text("であることを利用）", color=WHITE, font_size=21),
        ).arrange(RIGHT, buff=0.1)
        norm_note.shift(DOWN * 2.1)
        self.play(Write(norm_note), run_time=0.5)
        self.wait(1.5)

        # 最終形を強調
        self.play(
            FadeOut(cost_expand), FadeOut(cost_expand2), FadeOut(norm_note),
            FadeOut(derive_label2),
        )
        self.wait(0.2)

        final_title = Text("コスト関数の行列表現（まとめ）", color=WHITE, font_size=24, weight=BOLD)
        final_title.shift(UP * 1.35)
        self.play(Write(final_title), run_time=0.5)
        self.wait(0.2)

        final_cost = MathTex(
            r"J(\mathbf{w}) = (\mathbf{y} - X\mathbf{w})^\top (\mathbf{y} - X\mathbf{w})",
            color=ORANGE, font_size=36
        )
        final_cost.shift(UP * 0.4)
        final_cost_box2 = SurroundingRectangle(final_cost, color=ORANGE, buff=0.18)
        self.play(
            Transform(cost_final, final_cost),
            Transform(cost_final_box, final_cost_box2),
            run_time=0.7
        )
        self.wait(0.5)

        final_labels = VGroup(
            VGroup(
                MathTex(r"\mathbf{y}", color=YELLOW, font_size=26),
                Text("：観測出力ベクトル、　", color=WHITE, font_size=21),
                MathTex(r"X", color=TEAL, font_size=26),
                Text("：データ行列（バイアス列を含む）、　", color=WHITE, font_size=21),
                MathTex(r"\mathbf{w}", color=YELLOW, font_size=26),
                Text("：パラメータベクトル", color=WHITE, font_size=21),
            ).arrange(RIGHT, buff=0.1),
        )
        final_labels.shift(DOWN * 0.5)
        self.play(Write(final_labels), run_time=0.6)
        self.wait(0.5)

        next_step_note = VGroup(
            Text("この形を使って最小化するパラメータ", color=WHITE, font_size=26),
            MathTex(r"\hat{\mathbf{w}}", color=ORANGE, font_size=28),
            Text("を求める方法は次の動画へ！", color=GREEN, font_size=26, weight=BOLD),
        ).arrange(RIGHT, buff=0.1)
        next_step_note.shift(DOWN * 1.3)
        self.play(Write(next_step_note), run_time=0.6)
        self.wait(1.5)

        self.play(
            # FadeOut(matrix_goal), #FadeOut(next_note_preview),
            FadeOut(step4_title),
            FadeOut(cost_final), FadeOut(cost_final_box),
            FadeOut(final_title),
            FadeOut(final_labels), FadeOut(next_step_note),
            FadeOut(subtitle7),
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
                Text("[1]", color=GOLD, font_size=28, weight=BOLD),
                Text("データを記号で表現：入力", color=WHITE, font_size=28),
                MathTex(r"\mathbf{x}_n", color=TEAL, font_size=30),
                Text("、出力", color=WHITE, font_size=28),
                MathTex(r"y_n", color=YELLOW, font_size=30),
            ).arrange(RIGHT, buff=0.15, aligned_edge=DOWN),
            VGroup(
                Text("[2]", color=GOLD, font_size=28, weight=BOLD),
                VGroup(
                    Text("モデルを設計（今回は線形モデル）", color=WHITE, font_size=28),
                    Text("モデルは設計者が仮定・経験をもとに選ぶもの", color=ORANGE, font_size=24),
                ).arrange(DOWN, buff=0.08, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.25, aligned_edge=UP),
            VGroup(
                Text("[3]", color=GOLD, font_size=28, weight=BOLD),
                VGroup(
                    Text("コスト関数を設定（今回は二乗誤差）", color=WHITE, font_size=28),
                    Text("→ 最小二乗法 : 二乗誤差を最小化する手法", color=ORANGE, font_size=24),
                ).arrange(DOWN, buff=0.08, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.25, aligned_edge=UP),
            VGroup(
                Text("[4]", color=GOLD, font_size=28, weight=BOLD),
                VGroup(
                    MathTex(r"J(\mathbf{w}) = (\mathbf{y} - X\mathbf{w})^\top (\mathbf{y} - X\mathbf{w})", color=TEAL, font_size=30),
                    Text("最適解の求め方は次の動画へ！", color=GREEN, font_size=26, weight=BOLD),
                ).arrange(DOWN, buff=0.08, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.25, aligned_edge=UP),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        summary.scale(0.9)
        summary.shift(DOWN * 0.3)

        for point in summary:
            self.play(Write(point), run_time=0.7)
            self.wait(0.3)

        self.wait(1.5)

        all_final = VGroup(summary, subtitle_end, title)
        self.play(FadeOut(all_final), run_time=1.0)
        self.wait(0.5)
