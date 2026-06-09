from manim import *
import numpy as np


class DataPreprocessing(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        # タイトル
        title = Text("データの前処理", font_size=32, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)

        # ============================================================
        # Part 1: 前処理の概要
        # ============================================================
        subtitle1 = Text("なぜ前処理が必要か？", font_size=28, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.4)

        overview = VGroup(
            Text("機械学習では、各特徴量のスケールや分布が大きく異なることがある", color=WHITE, font_size=24),
            Text("例：身長（150〜180 cm） vs 年収（200万〜1000万円）", color=YELLOW, font_size=23),
            Text("→ そのままでは計算が不安定になったり、学習がうまく進まない", color=RED, font_size=23),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        overview.shift(UP * 0.8)
        self.play(Write(overview[0]), run_time=0.5)
        self.play(Write(overview[1]), run_time=0.5)
        self.play(Write(overview[2]), run_time=0.5)
        self.wait(0.5)

        three_methods = VGroup(
            Text("主な前処理の方法：", color=GOLD, font_size=26, weight=BOLD),
            VGroup(
                Text("① 標準化（Standardization）", color=TEAL, font_size=25),
                Text("② 中心化（Mean Centering）", color=ORANGE, font_size=25),
                Text("③ 正規化（Normalization）", color=GREEN, font_size=25),
            ).arrange(DOWN, buff=0.18, aligned_edge=LEFT),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        three_methods.shift(DOWN * 1.4)
        self.play(Write(three_methods[0]), run_time=0.4)
        self.play(Write(three_methods[1]), run_time=0.7)
        self.wait(1.5)

        self.play(FadeOut(overview), FadeOut(three_methods), FadeOut(subtitle1))
        self.wait(0.3)

        # ============================================================
        # Part 2: 標準化
        # ============================================================
        subtitle2 = Text("① 標準化（Standardization）", font_size=28, color=TEAL)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.4)

        # 記法の定義
        notation = VGroup(
            Text("記法：", color=GOLD, font_size=24, weight=BOLD),
            VGroup(
                MathTex(r"x_{nd}", color=WHITE, font_size=30),
                Text("：データ点 n、特徴量次元 d の値　（", color=WHITE, font_size=24),
                MathTex(r"n=1,\ldots,N,\quad d=1,\ldots,D", color=GRAY, font_size=24),
                Text("）", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                MathTex(r"\bar{x}_d = \frac{1}{N}\sum_{n=1}^{N} x_{nd}", color=TEAL, font_size=30),
                Text("：特徴量 d の平均", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.4),
            VGroup(
                MathTex(
                    r"\sigma_d = \sqrt{\frac{1}{N}\sum_{n=1}^{N}(x_{nd}-\bar{x}_d)^2}",
                    color=ORANGE, font_size=30
                ),
                Text("：特徴量 d の標準偏差", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.4),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        notation.shift(UP * 1.0 + LEFT * 0.5)
        self.play(Write(notation), run_time=1.0)
        self.wait(0.5)

        # 標準化の式
        std_formula = MathTex(
            r"x'_{nd} = \frac{x_{nd} - \bar{x}_d}{\sigma_d}",
            color=YELLOW, font_size=40
        )
        std_formula.shift(DOWN * 1.3)
        # std_box = SurroundingRectangle(std_formula, color=YELLOW, buff=0.2)
        std_label = Text("標準化後：", color=YELLOW, font_size=26)
        std_label.next_to(std_formula, LEFT, buff=0.3)
        self.play(Write(std_label), Write(std_formula), run_time=0.8)
        self.wait(0.5)

        # 標準化の結果
        std_results = VGroup(
            VGroup(
                Text("変換後は：", color=WHITE, font_size=24),
                MathTex(r"\frac{1}{N}\sum_{n=1}^N x'_{nd} = 0", color=TEAL, font_size=28),
                Text("（平均が 0 になる）", color=TEAL, font_size=23),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("　　　　　", font_size=24),
                MathTex(r"\frac{1}{N}\sum_{n=1}^N (x'_{nd})^2 = 1", color=ORANGE, font_size=28),
                Text("（分散が 1 になる）", color=ORANGE, font_size=23),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        std_results.shift(DOWN * 2.5)
        self.play(Write(std_results), run_time=0.7)
        self.wait(1.0)

        self.play(
            FadeOut(notation), FadeOut(std_label), FadeOut(std_formula),
            FadeOut(std_results),
        )
        self.wait(0.2)

        # --- 標準化の嬉しい効果 ---
        effect_title = Text("標準化の嬉しい効果", color=TEAL, font_size=27, weight=BOLD)
        effect_title.shift(UP * 1.8)
        self.play(Write(effect_title), run_time=0.5)
        self.wait(0.3)

        effects = VGroup(
            VGroup(
                Text("Ⅰ.", color=GOLD, font_size=26, weight=BOLD),
                VGroup(
                    Text("スケールが揃って計算が安定化する", color=WHITE, font_size=28, weight=BOLD),
                    Text("特徴量ごとに単位やスケールが異なっても、標準化すれば", color=GRAY, font_size=24),
                    Text("すべての次元が同じスケールになり、勾配降下法などが安定する", color=GRAY, font_size=24),
                ).arrange(DOWN, buff=0.06, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.2, aligned_edge=UP),
            VGroup(
                Text("Ⅱ.", color=GOLD, font_size=26, weight=BOLD),
                VGroup(
                    Text("外れ値の影響が相対的に見やすくなる", color=WHITE, font_size=28),
                    Text("平均0・標準偏差1 の単位で離れた点が外れ値とみなしやすい", color=GRAY, font_size=24),
                ).arrange(DOWN, buff=0.06, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.2, aligned_edge=UP),
            VGroup(
                Text("Ⅲ.", color=GOLD, font_size=26, weight=BOLD),
                VGroup(
                    Text("異なる特徴量の係数（重み）を比較しやすくなる", color=WHITE, font_size=28),
                ).arrange(DOWN, buff=0.06, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.2, aligned_edge=UP),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        effects.shift(DOWN * 0.2)
        effects.scale(0.92)

        for eff in effects:
            self.play(Write(eff), run_time=0.6)
            self.wait(0.2)
        self.wait(1.2)

        self.play(FadeOut(effect_title), FadeOut(effects))
        self.wait(0.2)

        # --- 標準化のグラフ ---
        graph_title = Text("標準化のグラフによるイメージ", color=TEAL, font_size=25)
        graph_title.shift(UP * 1.8)
        self.play(Write(graph_title), run_time=0.5)
        self.wait(0.3)

        np.random.seed(7)
        raw = np.random.normal(loc=50.0, scale=15.0, size=18)
        raw_mean = raw.mean()
        raw_std = raw.std()
        std_data = (raw - raw_mean) / raw_std

        # 元データの軸（左）
        ax_raw = Axes(
            x_range=[0, 20, 5], y_range=[10, 90, 20],
            x_length=3.2, y_length=3.8,
            axis_config={"color": GRAY, "include_tip": True, "include_numbers": True},
        ).scale(0.85)
        ax_raw.shift(LEFT * 3.2 + DOWN * 0.4)
        label_raw = Text("元データ", font_size=21, color=WHITE)
        label_raw.next_to(ax_raw, UP, buff=0.1)

        # 標準化後の軸（右）
        ax_std = Axes(
            x_range=[0, 20, 5], y_range=[-3.5, 3.5, 1],
            x_length=3.2, y_length=3.8,
            axis_config={"color": GRAY, "include_tip": True, "include_numbers": True},
        ).scale(0.85)
        ax_std.shift(RIGHT * 2.6 + DOWN * 0.4)
        label_std = Text("標準化後", font_size=21, color=YELLOW)
        label_std.next_to(ax_std, UP, buff=0.1)

        x_positions = np.linspace(1, 18, len(raw))

        dots_raw = VGroup(*[
            Dot(ax_raw.c2p(x, y), color=ORANGE, radius=0.07)
            for x, y in zip(x_positions, raw)
        ])
        dots_std = VGroup(*[
            Dot(ax_std.c2p(x, y), color=YELLOW, radius=0.07)
            for x, y in zip(x_positions, std_data)
        ])

        # 平均線
        mean_line_raw = DashedLine(
            ax_raw.c2p(0, raw_mean), ax_raw.c2p(20, raw_mean),
            color=TEAL, stroke_width=2
        )
        mean_line_std = DashedLine(
            ax_std.c2p(0, 0), ax_std.c2p(20, 0),
            color=TEAL, stroke_width=2
        )
        mean_label_raw = MathTex(r"\bar{x}", color=TEAL, font_size=20)
        mean_label_raw.next_to(mean_line_raw, RIGHT, buff=0.05)
        mean_label_std = MathTex(r"0", color=TEAL, font_size=20)
        mean_label_std.next_to(mean_line_std, RIGHT, buff=0.05)

        self.play(
            Create(ax_raw), Write(label_raw),
            Create(ax_std), Write(label_std),
            run_time=0.7
        )
        self.play(FadeIn(dots_raw), run_time=0.5)
        self.play(Create(mean_line_raw), Write(mean_label_raw), run_time=0.4)
        self.wait(0.3)

        arrow = Arrow(
            ax_raw.get_right() + RIGHT * 0.1,
            ax_std.get_left() + LEFT * 0.1,
            color=WHITE, buff=0.1, stroke_width=3
        )
        arrow_label = VGroup(
            MathTex(r"x'_{nd} = \frac{x_{nd}-\bar{x}_d}{\sigma_d}", color=YELLOW, font_size=24),
        )
        arrow_label.next_to(arrow, UP, buff=0.1)
        self.play(GrowArrow(arrow), Write(arrow_label), run_time=0.5)

        self.play(FadeIn(dots_std), run_time=0.5)
        self.play(Create(mean_line_std), Write(mean_label_std), run_time=0.4)
        self.wait(0.5)

        note_std = Text(
            "データ点の相対的配置は同じ\n→ 軸のスケールと原点位置が変化",
            color=WHITE, font_size=21
        )
        note_std.shift(DOWN * 2.65)
        self.play(Write(note_std), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(graph_title), FadeOut(ax_raw), FadeOut(label_raw),
            FadeOut(ax_std), FadeOut(label_std),
            FadeOut(dots_raw), FadeOut(dots_std),
            FadeOut(mean_line_raw), FadeOut(mean_label_raw),
            FadeOut(mean_line_std), FadeOut(mean_label_std),
            FadeOut(arrow), FadeOut(arrow_label),
            FadeOut(note_std),
            FadeOut(subtitle2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: 中心化
        # ============================================================
        subtitle3 = Text("② 中心化（Mean Centering）", font_size=28, color=ORANGE)
        subtitle3.next_to(title, DOWN)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.4)

        center_desc = Text("各特徴量から平均を引くだけの操作", color=WHITE, font_size=25)
        center_desc.shift(UP * 1.6)
        self.play(Write(center_desc), run_time=0.5)
        self.wait(0.3)

        center_formula = MathTex(
            r"x^*_{nd} = x_{nd} - \bar{x}_d",
            color=ORANGE, font_size=44
        )
        center_formula.shift(UP * 0.7)
        center_box = SurroundingRectangle(center_formula, color=ORANGE, buff=0.2)
        center_label = Text("中心化後：", color=ORANGE, font_size=26)
        center_label.next_to(center_formula, LEFT, buff=0.3)
        self.play(Write(center_label), Write(center_formula), Create(center_box), run_time=0.7)
        self.wait(0.4)

        center_result = VGroup(
            Text("変換後は：", color=WHITE, font_size=24),
            MathTex(r"\frac{1}{N}\sum_{n=1}^N x^*_{nd} = 0", color=ORANGE, font_size=28),
            Text("（平均が 0 になる）", color=ORANGE, font_size=23),
        ).arrange(RIGHT, buff=0.2)
        center_result.shift(DOWN * 0.5)
        self.play(Write(center_result), run_time=0.5)
        self.wait(0.4)

        center_note = VGroup(
            Text("標準化との違い：", color=YELLOW, font_size=24, weight=BOLD),
            Text("中心化は分散を変えない（スケールはそのまま）", color=WHITE, font_size=24),
        ).arrange(RIGHT, buff=0.2)
        center_note.shift(DOWN * 1.9)
        self.play(Write(center_note), run_time=0.5)
        self.wait(0.8)

        # 画面が詰まりすぎないよう、一度ここまでの説明を退場させる
        self.play(
            FadeOut(center_desc), FadeOut(center_label), FadeOut(center_formula),
            FadeOut(center_box), FadeOut(center_result), FadeOut(center_note),
        )
        self.wait(0.2)

        # 中心化の嬉しい効果
        ceff_title = Text("中心化の嬉しい効果", color=ORANGE, font_size=27, weight=BOLD)
        ceff_title.shift(UP * 1.8)
        self.play(Write(ceff_title), run_time=0.5)
        self.wait(0.3)

        ceff = VGroup(
            VGroup(
                Text("Ⅰ.", color=GOLD, font_size=25, weight=BOLD),
                VGroup(
                    Text("モデルから定数項（バイアス）を除ける", color=WHITE, font_size=28, weight=BOLD),
                    Text(
                        "中心化されたデータでは、線形回帰モデルの切片が 0 になる",
                        color=GRAY, font_size=26
                    ),
                    MathTex(
                        r"\sum_{d=1}^D w_d\, x^*_{nd} \approx y_n - \bar{y}",
                        color=ORANGE, font_size=30
                    ),
                    Text("→ バイアス項を推定する必要がなくなり、式が簡潔になる", color=GRAY, font_size=28),
                ).arrange(DOWN, buff=0.06, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.2, aligned_edge=UP),
            VGroup(
                Text("Ⅱ.", color=GOLD, font_size=25, weight=BOLD),
                VGroup(
                    Text("共分散行列などの計算が簡潔になる", color=WHITE, font_size=26),
                    Text("PCA（主成分分析）では中心化が前提となることが多い", color=GRAY, font_size=26),
                ).arrange(DOWN, buff=0.06, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.2, aligned_edge=UP),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        ceff.shift(DOWN * 0.35)
        ceff.scale(0.9)

        for ce in ceff:
            self.play(Write(ce), run_time=0.6)
            self.wait(0.2)
        self.wait(1.0)

        self.play(FadeOut(ceff_title), FadeOut(ceff))
        self.wait(0.2)

        # --- 中心化のグラフ ---
        cgraph_title = Text("中心化のグラフによるイメージ", color=ORANGE, font_size=25)
        cgraph_title.shift(UP * 1.8)
        self.play(Write(cgraph_title), run_time=0.5)
        self.wait(0.3)

        raw_c = raw.copy()
        cen_data = raw_c - raw_c.mean()

        ax_raw_c = Axes(
            x_range=[0, 20, 5], y_range=[10, 90, 20],
            x_length=3.2, y_length=3.8,
            axis_config={"color": GRAY, "include_tip": True, "include_numbers": True},
        ).scale(0.85)
        ax_raw_c.shift(LEFT * 3.2 + DOWN * 0.4)
        label_raw_c = Text("元データ", font_size=21, color=WHITE)
        label_raw_c.next_to(ax_raw_c, UP, buff=0.1)

        ax_cen = Axes(
            x_range=[0, 20, 5], y_range=[-50, 50, 20],
            x_length=3.2, y_length=3.8,
            axis_config={"color": GRAY, "include_tip": True, "include_numbers": True},
        ).scale(0.85)
        ax_cen.shift(RIGHT * 2.6 + DOWN * 0.4)
        label_cen = Text("中心化後", font_size=21, color=ORANGE)
        label_cen.next_to(ax_cen, UP, buff=0.1)

        dots_raw_c = VGroup(*[
            Dot(ax_raw_c.c2p(x, y), color=ORANGE, radius=0.07)
            for x, y in zip(x_positions, raw_c)
        ])
        dots_cen = VGroup(*[
            Dot(ax_cen.c2p(x, y), color=ORANGE, radius=0.07)
            for x, y in zip(x_positions, cen_data)
        ])

        mean_line_raw_c = DashedLine(
            ax_raw_c.c2p(0, raw_c.mean()), ax_raw_c.c2p(20, raw_c.mean()),
            color=TEAL, stroke_width=2
        )
        mean_line_cen = DashedLine(
            ax_cen.c2p(0, 0), ax_cen.c2p(20, 0),
            color=TEAL, stroke_width=2
        )
        mean_label_raw_c = MathTex(r"\bar{x}", color=TEAL, font_size=20)
        mean_label_raw_c.next_to(mean_line_raw_c, RIGHT, buff=0.05)
        mean_label_cen = MathTex(r"0", color=TEAL, font_size=20)
        mean_label_cen.next_to(mean_line_cen, RIGHT, buff=0.05)

        self.play(
            Create(ax_raw_c), Write(label_raw_c),
            Create(ax_cen), Write(label_cen),
            run_time=0.7
        )
        self.play(FadeIn(dots_raw_c), run_time=0.5)
        self.play(Create(mean_line_raw_c), Write(mean_label_raw_c), run_time=0.4)
        self.wait(0.3)

        arrow_c = Arrow(
            ax_raw_c.get_right() + RIGHT * 0.1,
            ax_cen.get_left() + LEFT * 0.1,
            color=WHITE, buff=0.1, stroke_width=3
        )
        arrow_c_label = MathTex(r"x^*_{nd} = x_{nd}-\bar{x}_d", color=ORANGE, font_size=26)
        arrow_c_label.next_to(arrow_c, UP, buff=0.1)
        self.play(GrowArrow(arrow_c), Write(arrow_c_label), run_time=0.5)

        self.play(FadeIn(dots_cen), run_time=0.5)
        self.play(Create(mean_line_cen), Write(mean_label_cen), run_time=0.4)
        self.wait(0.4)

        note_cen = Text(
            "データ点の散らばり具合（分散）は変わらない\n→ 原点だけが平均の位置に移動",
            color=WHITE, font_size=21
        )
        note_cen.shift(DOWN * 2.65+RIGHT * 2.2)
        self.play(Write(note_cen), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(cgraph_title), FadeOut(ax_raw_c), FadeOut(label_raw_c),
            FadeOut(ax_cen), FadeOut(label_cen),
            FadeOut(dots_raw_c), FadeOut(dots_cen),
            FadeOut(mean_line_raw_c), FadeOut(mean_label_raw_c),
            FadeOut(mean_line_cen), FadeOut(mean_label_cen),
            FadeOut(arrow_c), FadeOut(arrow_c_label),
            FadeOut(note_cen),
            FadeOut(subtitle3),
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: 正規化
        # ============================================================
        subtitle4 = Text("③ 正規化（Normalization）", font_size=28, color=GREEN)
        subtitle4.next_to(title, DOWN)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.4)

        norm_desc = Text(
            "各特徴量の値を一定の範囲（例：0〜1）にスケール変換する操作",
            color=WHITE, font_size=24
        )
        norm_desc.shift(UP * 1.7)
        self.play(Write(norm_desc), run_time=0.5)
        self.wait(0.3)

        # Min-Maxスケーリング
        minmax_label = Text("Min-Max スケーリング（最もよく使われる正規化）：", color=GREEN, font_size=23)
        minmax_label.shift(UP * 1.0)
        self.play(Write(minmax_label), run_time=0.5)

        minmax_formula = MathTex(
            r"\tilde{x}_{nd} = \frac{x_{nd} - \min_n(x_{nd})}{\max_n(x_{nd}) - \min_n(x_{nd})}",
            color=YELLOW, font_size=36
        )
        minmax_formula.shift(UP * 0.05)
        minmax_box = SurroundingRectangle(minmax_formula, color=YELLOW, buff=0.2)
        self.play(Write(minmax_formula), Create(minmax_box), run_time=0.7)
        self.wait(0.4)

        minmax_result = VGroup(
            Text("変換後は：", color=WHITE, font_size=24),
            MathTex(r"0 \leq \tilde{x}_{nd} \leq 1", color=GREEN, font_size=30),
            Text("の範囲に収まる", color=WHITE, font_size=23),
        ).arrange(RIGHT, buff=0.2)
        minmax_result.shift(DOWN * 0.9)
        self.play(Write(minmax_result), run_time=0.5)
        self.wait(0.5)

        # 正規化の嬉しい効果
        norm_effects = VGroup(
            VGroup(
                Text("● ", color=GOLD, font_size=24),
                Text("特徴量ごとのスケールを統一でき、アルゴリズムの収束が速くなる", color=WHITE, font_size=23),
            ).arrange(RIGHT, buff=0.05),
            VGroup(
                Text("● ", color=GOLD, font_size=24),
                Text("外れ値の影響を受けやすい点に注意が必要", color=YELLOW, font_size=23),
            ).arrange(RIGHT, buff=0.05),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        norm_effects.shift(DOWN * 1.8)
        self.play(Write(norm_effects), run_time=0.6)
        self.wait(0.8)

        self.play(
            FadeOut(norm_desc), FadeOut(minmax_label),
            FadeOut(minmax_formula), FadeOut(minmax_box),
            FadeOut(minmax_result), FadeOut(norm_effects),
        )
        self.wait(0.2)

        # --- 注意：ベクトルの正規化との違い ---
        caution_title = Text("注意：「正規化」という言葉の曖昧さ", color=RED, font_size=26, weight=BOLD)
        caution_title.shift(UP * 1.7)
        self.play(Write(caution_title), run_time=0.5)
        self.wait(0.4)

        caution_table = VGroup(
            # ヘッダ
            VGroup(
                Text("用語", color=GOLD, font_size=24, weight=BOLD),
                Text("意味", color=GOLD, font_size=24, weight=BOLD),
                Text("対象", color=GOLD, font_size=24, weight=BOLD),
            ).arrange(RIGHT, buff=1.2),
            Line(LEFT * 4.5, RIGHT * 4.5, color=GRAY, stroke_width=1),
            # 行1：データの正規化
            VGroup(
                Text("正規化", color=GREEN, font_size=23),
                Text("値を特定の範囲に収める", color=WHITE, font_size=23),
                Text("データセット全体の各次元", color=WHITE, font_size=22),
            ).arrange(RIGHT, buff=0.6),
            # 行2：ベクトルの正規化
            VGroup(
                Text("ベクトルの正規化", color=ORANGE, font_size=23),
                MathTex(r"\|\mathbf{v}\|=1", color=ORANGE, font_size=26),
                Text("個々のベクトル", color=WHITE, font_size=22),
            ).arrange(RIGHT, buff=0.6),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        caution_table.shift(UP * 0.4)

        for row in caution_table:
            self.play(Write(row), run_time=0.5)
            self.wait(0.15)
        self.wait(0.5)

        vec_norm_formula = MathTex(
            r"\hat{\mathbf{v}} = \frac{\mathbf{v}}{\|\mathbf{v}\|}",
            color=ORANGE, font_size=34
        )
        vec_norm_formula.shift(DOWN * 1.6)
        vec_norm_text = Text(
            "ベクトルの正規化とは、ベクトルをその大きさで割って",
            color=WHITE, font_size=22
        )
        vec_norm_text2 = Text(
            "長さが 1 の単位ベクトルに変換することを指す（別の概念！）",
            color=ORANGE, font_size=22
        )
        vec_norm_text.next_to(vec_norm_formula, DOWN, buff=0.15)
        vec_norm_text2.next_to(vec_norm_text, DOWN, buff=0.1)
        self.play(Write(vec_norm_formula), run_time=0.5)
        self.play(Write(vec_norm_text), Write(vec_norm_text2), run_time=0.6)
        self.wait(0.5)

        caution_box = SurroundingRectangle(
            VGroup(vec_norm_formula, vec_norm_text, vec_norm_text2),
            color=ORANGE, buff=0.15
        )
        self.play(Create(caution_box), run_time=0.4)
        self.wait(1.5)

        self.play(
            FadeOut(caution_title), FadeOut(caution_table),
            FadeOut(vec_norm_formula), FadeOut(vec_norm_text),
            FadeOut(vec_norm_text2), FadeOut(caution_box),
        )
        self.wait(0.2)

        # --- 正規化のグラフ ---
        ngraph_title = Text("正規化のグラフによるイメージ", color=GREEN, font_size=25)
        ngraph_title.shift(UP * 1.8)
        self.play(Write(ngraph_title), run_time=0.5)
        self.wait(0.3)

        raw_n = raw.copy()
        raw_min = raw_n.min()
        raw_max = raw_n.max()
        norm_data = (raw_n - raw_min) / (raw_max - raw_min)

        ax_raw_n = Axes(
            x_range=[0, 20, 5], y_range=[10, 90, 20],
            x_length=3.2, y_length=3.8,
            axis_config={"color": GRAY, "include_tip": True, "include_numbers": True},
        ).scale(0.85)
        ax_raw_n.shift(LEFT * 3.2 + DOWN * 0.4)
        label_raw_n = Text("元データ", font_size=21, color=WHITE)
        label_raw_n.next_to(ax_raw_n, UP, buff=0.1)

        ax_norm = Axes(
            x_range=[0, 20, 5], y_range=[-0.1, 1.2, 0.5],
            x_length=3.2, y_length=3.8,
            axis_config={"color": GRAY, "include_tip": True, "include_numbers": True},
        ).scale(0.85)
        ax_norm.shift(RIGHT * 2.6 + DOWN * 0.4)
        label_norm = Text("正規化後（0〜1）", font_size=21, color=GREEN)
        label_norm.next_to(ax_norm, UP, buff=0.1)

        dots_raw_n = VGroup(*[
            Dot(ax_raw_n.c2p(x, y), color=ORANGE, radius=0.07)
            for x, y in zip(x_positions, raw_n)
        ])
        dots_norm = VGroup(*[
            Dot(ax_norm.c2p(x, y), color=GREEN, radius=0.07)
            for x, y in zip(x_positions, norm_data)
        ])

        self.play(
            Create(ax_raw_n), Write(label_raw_n),
            Create(ax_norm), Write(label_norm),
            run_time=0.7
        )
        self.play(FadeIn(dots_raw_n), run_time=0.5)
        self.wait(0.3)

        arrow_n = Arrow(
            ax_raw_n.get_right() + RIGHT * 0.1,
            ax_norm.get_left() + LEFT * 0.1,
            color=WHITE, buff=0.1, stroke_width=3
        )
        arrow_n_label = MathTex(
            r"\tilde{x}_{nd} = \frac{x_{nd}-x_{\min}}{x_{\max}-x_{\min}}",
            color=GREEN, font_size=24
        )
        arrow_n_label.next_to(arrow_n, UP, buff=0.1)
        self.play(GrowArrow(arrow_n), Write(arrow_n_label), run_time=0.5)

        self.play(FadeIn(dots_norm), run_time=0.5)
        self.wait(0.4)

        note_norm = Text(
            "データ点の相対的配置は同じ\n→ 軸の範囲が [0, 1] に変化",
            color=WHITE, font_size=21
        )
        note_norm.shift(DOWN * 2.65)
        self.play(Write(note_norm), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(ngraph_title), FadeOut(ax_raw_n), FadeOut(label_raw_n),
            FadeOut(ax_norm), FadeOut(label_norm),
            FadeOut(dots_raw_n), FadeOut(dots_norm),
            FadeOut(arrow_n), FadeOut(arrow_n_label),
            FadeOut(note_norm),
            FadeOut(subtitle4),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: 3つの手法の比較
        # ============================================================
        subtitle5 = Text("3つの前処理の比較", font_size=28, color=GOLD)
        subtitle5.next_to(title, DOWN)
        self.play(Write(subtitle5), run_time=0.6)
        self.wait(0.4)

        # 比較表
        header = VGroup(
            Text("手法", color=GOLD, font_size=24, weight=BOLD),
            Text("式", color=GOLD, font_size=24, weight=BOLD),
            Text("平均", color=GOLD, font_size=24, weight=BOLD),
            Text("分散", color=GOLD, font_size=24, weight=BOLD),
            Text("範囲", color=GOLD, font_size=24, weight=BOLD),
        ).arrange(RIGHT, buff=0.65)
        header.shift(UP * 1.8)

        sep = Line(LEFT * 5.5, RIGHT * 5.5, color=GRAY, stroke_width=1)
        sep.next_to(header, DOWN, buff=0.1)

        row1 = VGroup(
            Text("標準化", color=TEAL, font_size=22),
            MathTex(r"\frac{x_{nd}-\bar{x}_d}{\sigma_d}", color=TEAL, font_size=22),
            Text("0", color=TEAL, font_size=22),
            Text("1", color=TEAL, font_size=22),
            Text("任意", color=GRAY, font_size=22),
        ).arrange(RIGHT, buff=0.75)
        row1.next_to(sep, DOWN, buff=0.2)

        row2 = VGroup(
            Text("中心化", color=ORANGE, font_size=22),
            MathTex(r"x_{nd}-\bar{x}_d", color=ORANGE, font_size=22),
            Text("0", color=ORANGE, font_size=22),
            Text("変わらない", color=ORANGE, font_size=22),
            Text("任意", color=GRAY, font_size=22),
        ).arrange(RIGHT, buff=0.75)
        row2.next_to(row1, DOWN, buff=0.25)

        row3 = VGroup(
            Text("正規化", color=GREEN, font_size=22),
            MathTex(r"\frac{x_{nd}-x_{\min}}{x_{\max}-x_{\min}}", color=GREEN, font_size=22),
            Text("変わらない", color=GRAY, font_size=22),
            Text("変わらない", color=GRAY, font_size=22),
            Text("[0, 1]", color=GREEN, font_size=22),
        ).arrange(RIGHT, buff=0.75)
        row3.next_to(row2, DOWN, buff=0.25)

        self.play(Write(header), Create(sep), run_time=0.5)
        for row in [row1, row2, row3]:
            self.play(Write(row), run_time=0.5)
            self.wait(0.2)
        self.wait(1.0)

        # 使い分けのヒント
        hint = VGroup(
            Text("使い分けのヒント：", color=YELLOW, font_size=26, weight=BOLD),
            VGroup(
                Text("・ データが正規分布に近い場合 → ", color=WHITE, font_size=24),
                Text("標準化", color=TEAL, font_size=24, weight=BOLD),
            ).arrange(RIGHT, buff=0.05),
            VGroup(
                Text("・ 値の範囲を厳密に制限したい場合 → ", color=WHITE, font_size=24),
                Text("正規化", color=GREEN, font_size=24, weight=BOLD),
            ).arrange(RIGHT, buff=0.05),
            VGroup(
                Text("・ スケールは保ちつつ平均を 0 にしたい場合 → ", color=WHITE, font_size=24),
                Text("中心化", color=ORANGE, font_size=24, weight=BOLD),
            ).arrange(RIGHT, buff=0.05),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        hint.next_to(row3, DOWN, buff=0.4)
        hint.scale(0.92)
        self.play(Write(hint), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(header), FadeOut(sep),
            FadeOut(row1), FadeOut(row2), FadeOut(row3),
            FadeOut(hint), FadeOut(subtitle5),
        )
        self.wait(0.3)

        # ============================================================
        # Part 6: まとめ
        # ============================================================
        subtitle_end = Text("まとめ", font_size=36, color=GOLD, weight=BOLD)
        subtitle_end.next_to(title, DOWN)
        self.play(Write(subtitle_end), run_time=0.7)
        self.wait(0.5)

        summary = VGroup(
            VGroup(
                Text("1.", color=GOLD, font_size=26, weight=BOLD),
                VGroup(
                    Text("標準化：平均を引いて標準偏差で割る", color=TEAL, font_size=26),
                    MathTex(
                        r"x'_{nd} = \frac{x_{nd}-\bar{x}_d}{\sigma_d}",
                        color=TEAL, font_size=30
                    ),
                    Text("→ スケールが揃い計算が安定・係数の比較が容易", color=WHITE, font_size=23),
                ).arrange(DOWN, buff=0.06, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("2.", color=GOLD, font_size=26, weight=BOLD),
                VGroup(
                    Text("中心化：平均を引くだけ（分散は不変）", color=ORANGE, font_size=26),
                    MathTex(r"x^*_{nd} = x_{nd} - \bar{x}_d", color=ORANGE, font_size=30),
                    Text("→ 定数項（バイアス）を式から除けて計算が簡潔になる", color=WHITE, font_size=23),
                ).arrange(DOWN, buff=0.06, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("3.", color=GOLD, font_size=26, weight=BOLD),
                VGroup(
                    Text("正規化（Min-Max）：値を [0, 1] に変換", color=GREEN, font_size=26),
                    Text("（※ベクトルの正規化とは別概念に注意）", color=ORANGE, font_size=22),
                    Text("→ 値の範囲を厳密に統一したい場合に有効", color=WHITE, font_size=23),
                ).arrange(DOWN, buff=0.06, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("4.", color=GOLD, font_size=26, weight=BOLD),
                VGroup(
                    Text("グラフ上ではデータ点の相対的配置は変わらない", color=WHITE, font_size=26),
                    Text("→ 変わるのは軸のスケールや原点の位置", color=YELLOW, font_size=23),
                ).arrange(DOWN, buff=0.06, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        summary.scale(0.86)
        summary.shift(DOWN * 0.4)

        for point in summary:
            self.play(Write(point), run_time=0.7)
            self.wait(0.3)

        self.wait(1.5)

        all_final = VGroup(summary, subtitle_end, title)
        self.play(FadeOut(all_final), run_time=1.0)
        self.wait(0.5)
