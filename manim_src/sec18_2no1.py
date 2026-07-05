from manim import *
import numpy as np


class PCAAndEigenvalues(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        title = Text("主成分分析と固有値の関係", font_size=36, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.7)

        # ============================================================
        # Part 1: 固有ベクトルと固有値の定義
        # ============================================================
        subtitle1 = Text("固有ベクトルと固有値", font_size=28, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)

        eigen_intro = Text(
            "正方行列には特別な性質を持つベクトルとスカラーが存在する",
            color=WHITE, font_size=28,
        )
        eigen_intro.shift(UP * 1.8)
        self.play(Write(eigen_intro), run_time=0.7)
        self.wait(0.5)

        # 固有値・固有ベクトルの定義
        eigen_def = MathTex(
            r"A\boldsymbol{v}_i = \lambda_i \boldsymbol{v}_i",
            color=YELLOW,
            font_size=48,
        )
        eigen_def.shift(UP * 0.7)
        self.play(Write(eigen_def), run_time=0.7)
        self.wait(0.5)

        eigen_label_a = VGroup(
            MathTex(r"A:", color=WHITE, font_size=32),
            Text("正方行列", color=WHITE, font_size=26),
        ).arrange(RIGHT, buff=0.2)
        
        eigen_label_v = VGroup(
            MathTex(r"\boldsymbol{v}_i:", color=TEAL, font_size=32),
            Text("固有ベクトル（特別な方向）", color=TEAL, font_size=26),
        ).arrange(RIGHT, buff=0.2)
        
        eigen_label_lambda = VGroup(
            MathTex(r"\lambda_i:", color=ORANGE, font_size=32),
            Text("固有値（スケール倍率）", color=ORANGE, font_size=26),
        ).arrange(RIGHT, buff=0.2)
        
        eigen_labels = VGroup(eigen_label_a, eigen_label_v, eigen_label_lambda)
        eigen_labels.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        eigen_labels.shift(DOWN * 0.5)

        for label in eigen_labels:
            self.play(Write(label), run_time=0.5)
            self.wait(0.2)

        eigen_note = Text(
            "つまり、行列Aをかけても方向が変わらない特別なベクトル",
            color=GREEN, font_size=28,
        )
        eigen_note.shift(DOWN * 2.2)
        self.play(Write(eigen_note), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(eigen_intro), FadeOut(eigen_def),
            FadeOut(eigen_labels), FadeOut(eigen_note),
            FadeOut(subtitle1),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: 主成分分析の目的とトイデータでの視覚化
        # ============================================================
        subtitle2 = Text("主成分分析の目的", font_size=28, color=GOLD)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2), run_time=0.6)

        pca_intro = VGroup(
            Text("データの特徴をより「扱いやすい」軸で表現したい", color=WHITE, font_size=26),
            Text("※「扱いやすい」の定義は目的によって変わる（アート的）", color=YELLOW, font_size=22),
            Text("ここでは「データのばらつきをよく捉える」軸を考える", color=GREEN, font_size=26),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        pca_intro.shift(UP * 1.5)

        for line in pca_intro:
            self.play(Write(line), run_time=0.5)
            self.wait(0.2)
        self.wait(0.5)

        # トイデータの視覚化
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=5,
            y_length=5,
            axis_config={"color": GREY, "include_tip": False},
        ).scale(0.6)
        axes.shift(DOWN)

        # データ点の生成（楕円状の分布）
        np.random.seed(42)
        # 相関のあるデータを生成
        n_points = 30
        theta = np.pi / 6  # 30度回転
        mean = np.array([0, 0])
        # 共分散行列（対角でない）
        cov_original = np.array([[2.0, 1.5], [1.5, 0.5]])
        data = np.random.multivariate_normal(mean, cov_original, n_points)
        
        dots = VGroup(*[
            Dot(axes.c2p(point[0], point[1]), radius=0.04, color=BLUE)
            for point in data
        ])

        # 元の軸（x, y）
        x_axis_arrow = Arrow(
            axes.c2p(0, 0), axes.c2p(2.5, 0),
            buff=0, color=WHITE, stroke_width=3,
        )
        y_axis_arrow = Arrow(
            axes.c2p(0, 0), axes.c2p(0, 2.5),
            buff=0, color=WHITE, stroke_width=3,
        )
        x_label = MathTex(r"x_1", color=WHITE, font_size=24).next_to(x_axis_arrow, RIGHT)
        y_label = MathTex(r"x_2", color=WHITE, font_size=24).next_to(y_axis_arrow, UP)

        self.play(Create(axes), run_time=0.5)
        self.play(
            Create(x_axis_arrow), Create(y_axis_arrow),
            Write(x_label), Write(y_label),
            run_time=0.5
        )
        self.play(Create(dots), run_time=0.7)
        self.wait(0.5)

        # 主成分軸を計算して表示
        X_centered = data - np.mean(data, axis=0)
        cov_matrix = (X_centered.T @ X_centered) / n_points
        eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
        # 固有値の大きい順にソート
        idx = eigenvalues.argsort()[::-1]
        eigenvalues = eigenvalues[idx]
        eigenvectors = eigenvectors[:, idx]

        # 第1主成分（最大分散方向）
        pc1_direction = eigenvectors[:, 0] * np.sqrt(eigenvalues[0]) * 1.5
        pc1_arrow = Arrow(
            axes.c2p(0, 0), axes.c2p(pc1_direction[0], pc1_direction[1]),
            buff=0, color=YELLOW, stroke_width=5,
        )
        pc1_label = MathTex(r"\boldsymbol{w}_1", color=YELLOW, font_size=28).next_to(
            axes.c2p(pc1_direction[0], pc1_direction[1]), RIGHT
        )

        # 第2主成分
        pc2_direction = eigenvectors[:, 1] * np.sqrt(eigenvalues[1]) * 1.5
        pc2_arrow = Arrow(
            axes.c2p(0, 0), axes.c2p(pc2_direction[0], pc2_direction[1]),
            buff=0, color=ORANGE, stroke_width=5,
        )
        pc2_label = MathTex(r"\boldsymbol{w}_2", color=ORANGE, font_size=28).next_to(
            axes.c2p(pc2_direction[0], pc2_direction[1]), UP
        )

        pca_note = Text(
            "データのばらつきが最も大きい方向が第1主成分（黄色）",
            color=YELLOW, font_size=26,
        )
        pca_note.shift(DOWN * 3.0)

        self.play(Create(pc1_arrow), Write(pc1_label), run_time=0.6)
        self.play(Write(pca_note), run_time=0.5)
        self.wait(0.8)

        pca_note2 = Text(
            "第2主成分（橙色）は第1主成分と直交し、残りの分散を捉える",
            color=ORANGE, font_size=24,
        )
        pca_note2.next_to(pca_note, DOWN, buff=0.1)
        self.play(Create(pc2_arrow), Write(pc2_label), run_time=0.6)
        self.play(Write(pca_note2), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(pca_intro), FadeOut(axes), FadeOut(dots),
            FadeOut(x_axis_arrow), FadeOut(y_axis_arrow),
            FadeOut(x_label), FadeOut(y_label),
            FadeOut(pc1_arrow), FadeOut(pc1_label),
            FadeOut(pc2_arrow), FadeOut(pc2_label),
            FadeOut(pca_note), FadeOut(pca_note2),
            FadeOut(subtitle2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: 分散最大化の定式化
        # ============================================================
        subtitle3 = Text("新しい軸での分散を最大化する", font_size=28, color=TEAL)
        subtitle3.next_to(title, DOWN)
        self.play(Write(subtitle3), run_time=0.6)

        formulation_intro = VGroup(
            Text("17話で見たように、新しい軸は元の基底の線形和で作れるので、それを", color=WHITE, font_size=26),
            MathTex(r"\boldsymbol{w}", color=WHITE, font_size=34),
            Text("とする", color=WHITE, font_size=26),
            # Text("簡単のため2次元で考える", color=YELLOW, font_size=22),
        ).arrange(RIGHT, buff=0.5, aligned_edge=RIGHT)
        formulation_intro.shift(UP * 1.8)
        self.play(Write(formulation_intro), run_time=0.7)
        self.wait(0.5)

        # データを中心化
        centering_note = Text(
            "データ行列Xを予め中心化しておくと、新しい1軸目（w₁方向）での座標の分散は…", color=WHITE, font_size=26,
        )
        centering_note.shift(UP * 1.2)
        self.play(Write(centering_note), run_time=0.6)
        self.wait(0.3)

        # 分散の式
        variance_formula = MathTex(
            r"\sigma_1^2 = \frac{1}{N}(X\boldsymbol{w}_1)^{\top}(X\boldsymbol{w}_1)",
            color=YELLOW,
            font_size=40,
        )
        variance_formula.shift(UP * 0.3)
        self.play(Write(variance_formula), run_time=0.7)
        self.wait(0.5)

        # variance_note = Text(
        #     "新しい1軸目（w₁方向）での座標の分散",
        #     color=GREEN, font_size=24,
        # )
        # variance_note.next_to(variance_formula, DOWN, buff=0.3)
        # self.play(Write(variance_note), run_time=0.5)
        # self.wait(0.7)

        # 制約条件
        constraint_formula = VGroup(
            MathTex(r"\Rightarrow\quad \|\boldsymbol{w}_1\| = 1", color=ORANGE, font_size=32),
            Text("という制約を課す（正規基底という自然な制約）", color=ORANGE, font_size=26),
        ).arrange(RIGHT, buff=0.2)
        
        constraint_intro = VGroup(
            Text("この値を最大化するw₁を探したい", color=WHITE, font_size=26),
            Text("ただし、何も制約がなければ無限に大きくできる", color=RED, font_size=24),
            constraint_formula,
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        constraint_intro.shift(DOWN * 1.0)

        for line in constraint_intro:
            self.play(Write(line), run_time=0.5)
            self.wait(0.2)
        self.wait(0.5)

        # ラグランジュ未定乗数法
        lagrange_note = Text(
            "この最適化問題をラグランジュの未定乗数法を使って解く（詳細は次の動画）",
            color=YELLOW, font_size=26,
        )
        lagrange_note.shift(DOWN * 2.3)
        self.play(Write(lagrange_note), run_time=0.6)
        self.wait(1.0)

        self.play(
            FadeOut(formulation_intro), FadeOut(centering_note),
            FadeOut(variance_formula),
            FadeOut(constraint_intro), FadeOut(lagrange_note),
        )
        self.wait(0.3)

        # 導出結果
        result_intro = Text("すると、以下の式が導かれる", color=WHITE, font_size=26)
        result_intro.shift(UP * 1.5)
        self.play(Write(result_intro), run_time=0.6)

        result_eq = MathTex(
            r"\left(\frac{1}{N}X^{\top}X\right)\boldsymbol{w}_1 = \lambda_1\boldsymbol{w}_1",
            color=YELLOW,
            font_size=44,
        )
        result_eq.shift(UP * 0.4)
        result_box = SurroundingRectangle(result_eq, color=YELLOW, buff=0.2)
        self.play(Write(result_eq), run_time=0.8)
        self.play(Create(result_box), run_time=0.4)
        self.wait(0.8)

        result_note = VGroup(
            Text("この式をよく見てみよう…", color=WHITE, font_size=26),
        )
        result_note.shift(DOWN * 0.8)
        self.play(Write(result_note), run_time=0.5)
        self.wait(1.2)

        self.play(
            FadeOut(result_intro), FadeOut(result_eq), FadeOut(result_box),
            FadeOut(result_note), FadeOut(subtitle3),
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: 固有値問題との関係
        # ============================================================
        subtitle4 = Text("固有値問題との関係", font_size=28, color=BLUE)
        subtitle4.next_to(title, DOWN)
        self.play(Write(subtitle4), run_time=0.6)

        # 2つの式を並べて比較
        comparison_title = Text("2つの式を比べてみる", color=WHITE, font_size=26)
        comparison_title.shift(UP * 2.0)
        self.play(Write(comparison_title), run_time=0.6)

        eigen_eq_again = MathTex(
            r"A\boldsymbol{v}_i = \lambda_i \boldsymbol{v}_i",
            color=TEAL,
            font_size=38,
        )
        eigen_eq_again.shift(UP * 1.0)
        eigen_label = Text("固有値・固有ベクトルの定義", color=TEAL, font_size=22)
        eigen_label.next_to(eigen_eq_again, RIGHT, buff=0.3)

        pca_eq_again = MathTex(
            r"\left(\frac{1}{N}X^{\top}X\right)\boldsymbol{w}_1 = \lambda_1\boldsymbol{w}_1",
            color=ORANGE,
            font_size=38,
        )
        pca_eq_again.shift(DOWN * 0.1)
        pca_label = Text("主成分分析で導出された式", color=ORANGE, font_size=22)
        pca_label.next_to(pca_eq_again, RIGHT, buff=0.3)

        self.play(Write(eigen_eq_again), Write(eigen_label), run_time=0.7)
        self.play(Write(pca_eq_again), Write(pca_label), run_time=0.7)
        self.wait(0.8)

        # 対応関係
        correspondence = VGroup(
            MathTex(
                r"A = \frac{1}{N}X^{\top}X,\quad",
                r"\boldsymbol{v}_i = \boldsymbol{w}_i",
                color=YELLOW, font_size=32,
            ),
            Text("と置き換えれる。つまり、両者は等価な式！", color=YELLOW, font_size=28, weight=BOLD),
        ).arrange(DOWN, buff=0.5)
        correspondence.shift(DOWN * 1.7)

        for line in correspondence:
            self.play(Write(line), run_time=0.6)
            self.wait(0.2)
        self.wait(1.0)

        self.play(
            FadeOut(comparison_title), FadeOut(eigen_eq_again), FadeOut(eigen_label),
            FadeOut(pca_eq_again), FadeOut(pca_label), FadeOut(correspondence),
        )
        self.wait(0.3)

        # 結論
        conclusion_intro = Text(
            "結局、データの特徴を捉えやすい軸を取るには…",
            color=WHITE, font_size=26,
        )
        conclusion_intro.shift(UP * 1.8)
        self.play(Write(conclusion_intro), run_time=0.6)

        conclusion_main = VGroup(
            MathTex(r"X^{\top}X", color=GREEN, font_size=40),
            Text("の固有ベクトルを用いるとよい", color=GREEN, font_size=30),
        ).arrange(RIGHT, buff=0.2)
        conclusion_main.shift(UP * 0.9)
        conclusion_box = SurroundingRectangle(conclusion_main, color=GREEN, buff=0.2)
        self.play(Write(conclusion_main), run_time=0.7)
        self.play(Create(conclusion_box), run_time=0.4)
        self.wait(0.8)

        # 補足
        additional_notes = VGroup(
            Text("補足：", color=WHITE, font_size=24, weight=BOLD),
            Text("・固有値・固有ベクトルは一つの正方行列に対して複数存在する", color=WHITE, font_size=24),
            Text("・固有値の大きい順に「第一固有値・固有ベクトル」「第二…」と呼ぶ", color=WHITE, font_size=24),
            Text("・固有値が大きいほど、その方向の分散が大きい（次の動画で詳細）", color=YELLOW, font_size=24),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        additional_notes.shift(DOWN * 1.0)

        for note in additional_notes:
            self.play(Write(note), run_time=0.5)
            self.wait(0.15)
        self.wait(1.5)

        self.play(
            FadeOut(conclusion_intro), FadeOut(conclusion_main), FadeOut(conclusion_box),
            FadeOut(additional_notes), FadeOut(subtitle4),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: まとめ
        # ============================================================
        subtitle_end = Text("まとめ", font_size=36, color=GOLD, weight=BOLD)
        subtitle_end.next_to(title, DOWN)
        self.play(Write(subtitle_end), run_time=0.7)

        summary = VGroup(
            Text("1. 固有ベクトルは行列をかけても方向が変わらない特別なベクトル", color=WHITE, font_size=28),
            Text("2. 主成分分析では「データのばらつきを最大化する」軸を探す", color=WHITE, font_size=28),
            Text("3. 分散最大化を制約条件下で解くと固有値問題に帰着する", color=WHITE, font_size=28),
            Text("4. すると、XᵀX の固有ベクトルが主成分となる", color=WHITE, font_size=28),
            Text("5. 固有値の大きさが分散の大きさに対応（次の動画で詳しく）", color=YELLOW, font_size=28),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        summary.scale(0.90)
        summary.shift(DOWN * 0.4)

        for row in summary:
            self.play(Write(row), run_time=0.6)
            self.wait(0.15)

        self.wait(1.5)
        self.play(FadeOut(VGroup(title, subtitle_end, summary)), run_time=1.0)
        self.wait(0.5)
