from manim import *
import numpy as np


class AxisForSeparability(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        title = Text("データを区別しやすい軸", font_size=36, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.7)

        # ============================================================
        # Part 1: 2次元トイデータと軸の取り直し
        # ============================================================
        subtitle1 = Text("2次元特徴量空間での直感", font_size=28, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)

        axes = Axes(
            x_range=[-0.5, 6.5, 1],
            y_range=[-0.5, 6.5, 1],
            x_length=6.0,
            y_length=6.0,
            axis_config={"color": GRAY_B, "include_numbers": True, "include_tip": True},
        ).scale(0.85)
        axes.shift(LEFT * 2.8 + DOWN * 0.35)

        x1_label = MathTex(r"x_1", color=WHITE, font_size=24)
        x1_label.next_to(axes.x_axis, RIGHT, buff=0.08)
        x2_label = MathTex(r"x_2", color=WHITE, font_size=24)
        x2_label.next_to(axes.y_axis, UP, buff=0.08)

        toy_data = np.array(
            [
                [0.9, 1.2],
                [1.3, 1.6],
                [1.8, 2.0],
                [2.2, 2.6],
                [2.7, 3.0],
                [3.0, 3.4],
                [3.4, 3.8],
                [3.9, 4.1],
                [4.3, 4.7],
                [4.7, 5.0],
                [5.1, 5.3],
            ]
        )
        dots = VGroup(*[Dot(axes.c2p(p[0], p[1]), color=YELLOW, radius=0.055) for p in toy_data])

        intro_note = VGroup(
                        Text("こういうデータでは、", color=GREEN, font_size=24),
                        Text("軸を取り直すと1軸で特徴を捉えやすい", color=GREEN, font_size=24),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        intro_note.to_edge(RIGHT).shift(UP)

        self.play(Create(axes), Write(x1_label), Write(x2_label), run_time=0.8)
        self.play(FadeIn(dots, shift=UP * 0.12), run_time=0.8)
        self.play(Write(intro_note), run_time=0.7)
        self.wait(0.6)

        center = axes.c2p(3.0, 3.1)
        z1_dir = np.array([1.0, 1.0, 0.0])
        z1_dir = z1_dir / np.linalg.norm(z1_dir)
        z2_dir = np.array([-1.0, 1.0, 0.0])
        z2_dir = z2_dir / np.linalg.norm(z2_dir)

        z1_axis = Arrow(
            start=center - z1_dir * 2.4,
            end=center + z1_dir * 2.4,
            buff=0,
            color=TEAL,
            stroke_width=6,
            max_stroke_width_to_length_ratio=12,
        )
        z2_axis = Arrow(
            start=center - z2_dir * 1.4,
            end=center + z2_dir * 1.4,
            buff=0,
            color=ORANGE,
            stroke_width=5,
            max_stroke_width_to_length_ratio=12,
        )

        z1_label = MathTex(r"z_1", color=TEAL, font_size=28)
        z1_label.next_to(z1_axis.get_end(), UR, buff=0.05)
        z2_label = MathTex(r"z_2", color=ORANGE, font_size=28)
        z2_label.next_to(z2_axis.get_end(), UL, buff=0.05)

        axis_note = VGroup(
            Text("たとえば、", color=WHITE, font_size=23),
            Text("データに沿って新第1軸を", color=TEAL, font_size=23),
            Text("その直交方向に新第2軸を", color=ORANGE, font_size=23),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        axis_note.next_to(intro_note, DOWN, buff=0.35, aligned_edge=LEFT)

        self.play(Create(z1_axis), Write(z1_label), run_time=0.6)
        self.play(Create(z2_axis), Write(z2_label), run_time=0.5)
        self.play(Write(axis_note), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(axes), FadeOut(x1_label), FadeOut(x2_label), FadeOut(dots),
            FadeOut(z1_axis), FadeOut(z2_axis), FadeOut(z1_label), FadeOut(z2_label),
            FadeOut(intro_note), FadeOut(axis_note), FadeOut(subtitle1),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: 線形結合による変数変換
        # ============================================================
        subtitle2 = Text("元変数の線形結合で新しい変数を作る", font_size=28, color=GOLD)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2), run_time=0.6)

        transform_eqs = VGroup(
            MathTex(r"z_1 = w_{11}x_1 + w_{12}x_2", color=TEAL, font_size=42),
            MathTex(r"z_2 = w_{21}x_1 + w_{22}x_2", color=ORANGE, font_size=42),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        transform_eqs.shift(UP * 0.2)

        transform_note = VGroup(
            Text("係数 w をどう選ぶかで、", color=WHITE, font_size=25),
            Text("『区別しやすい軸』が得られるかが決まる", color=YELLOW, font_size=25),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        transform_note.shift(DOWN * 1.6)

        pca_note = VGroup(
            Text("この係数を " + "データを区別しやすいように" + " 決めるのが主成分分析", color=GREEN, font_size=24),
            Text("主成分分析の本格的な話は第18話で扱う", color=GRAY_B, font_size=22),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        pca_note.shift(DOWN * 2.55)

        self.play(Write(transform_eqs), run_time=0.8)
        self.play(Write(transform_note), run_time=0.6)
        self.play(Write(pca_note), run_time=0.6)
        self.wait(1.5)

        self.play(FadeOut(subtitle2), FadeOut(transform_eqs), FadeOut(transform_note), FadeOut(pca_note))
        self.wait(0.3)

        # ============================================================
        # Part 3: 特異値分解の概要
        # ============================================================
        subtitle3 = Text("ここでは特異値分解（SVD）を詳しく見る", font_size=28, color=BLUE)
        subtitle3.next_to(title, DOWN)
        self.play(Write(subtitle3), run_time=0.6)

        svd_eq = MathTex(r"X = U\Sigma V^{\top}", color=YELLOW, font_size=54)
        svd_eq.shift(UP * 1.0)
        svd_box = SurroundingRectangle(svd_eq, color=YELLOW, buff=0.2)

        shape_note = VGroup(
            MathTex(r"X\in\mathbb{R}^{N\times D}", color=WHITE, font_size=32),
            MathTex(r"U\in\mathbb{R}^{N\times R},\ \Sigma\in\mathbb{R}^{R\times R},\ V^{\top}\in\mathbb{R}^{R\times D}", color=TEAL, font_size=30),
            Text("この動画ではコンパクトSVD（N×R, R×R, R×D）で説明", color=WHITE, font_size=24),
        ).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        shape_note.shift(DOWN * 0.25)

        sigma_note = VGroup(
            MathTex(r"\Sigma=\mathrm{diag}(\sigma_1,\sigma_2,\ldots,\sigma_R),\ \sigma_1\ge\sigma_2\ge\cdots\ge\sigma_R\ge0", color=ORANGE, font_size=30),
            Text("対角成分を特異値と呼ぶ。特異値の数 R は高々 min(N, D)", color=ORANGE, font_size=24),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        sigma_note.shift(DOWN * 1.95)

        self.play(Write(svd_eq), Create(svd_box), run_time=0.8)
        self.play(Write(shape_note), run_time=0.9)
        self.play(Write(sigma_note), run_time=0.8)
        self.wait(1.5)

        self.play(FadeOut(subtitle3), FadeOut(svd_eq), FadeOut(svd_box), FadeOut(shape_note), FadeOut(sigma_note))
        self.wait(0.3)

        # ============================================================
        # Part 4: 具体例（中心化 -> SVD）
        # ============================================================
        subtitle4 = Text("具体例：4次元特徴量を持つ5本データ", font_size=28, color=GOLD)
        subtitle4.next_to(title, DOWN)
        self.play(Write(subtitle4), run_time=0.6)

        x_label = Text("データ行列 X", color=WHITE, font_size=26)
        x_label.shift(UP * 1.85 + LEFT * 4.8)
        x_mat = MathTex(
            r"X=\begin{bmatrix}"
            r"8&6&7&0\\"
            r"7&8&8&0\\"
            r"9&8&7&0\\"
            r"0&0&1&9\\"
            r"0&0&0&8"
            r"\end{bmatrix}",
            color=WHITE,
            font_size=34,
        )
        x_mat.shift(UP * 0.85 + LEFT * 3.5)

        mean_vec = MathTex(
            r"\mu=\left[4.8,\ 4.4,\ 4.6,\ 3.4\right]",
            color=YELLOW,
            font_size=30,
        )
        mean_vec.shift(UP * 1.9 + RIGHT * 2.0)

        centered_label = Text("特徴量ごとに中心化：~X = X - 1\mu", color=WHITE, font_size=24)
        centered_label.shift(UP * 1.3 + RIGHT * 2.0)

        xt_mat = MathTex(
            r"\tilde{X}=\begin{bmatrix}"
            r"3.2&1.6&2.4&-3.4\\"
            r"2.2&3.6&3.4&-3.4\\"
            r"4.2&3.6&2.4&-3.4\\"
            r"-4.8&-4.4&-3.6&5.6\\"
            r"-4.8&-4.4&-4.6&4.6"
            r"\end{bmatrix}",
            color=TEAL,
            font_size=27,
        )
        xt_mat.shift(DOWN * 0.5 + RIGHT * 2.0)

        self.play(Write(x_label), Write(x_mat), run_time=0.8)
        self.play(Write(mean_vec), Write(centered_label), run_time=0.7)
        self.play(Write(xt_mat), run_time=0.9)
        self.wait(0.8)

        svd_small = MathTex(r"\tilde{X}=\tilde{U}\tilde{\Sigma}\tilde{V}^{\top}", color=YELLOW, font_size=38)
        svd_small.shift(DOWN * 2.55)
        self.play(Write(svd_small), run_time=0.6)
        self.wait(1.5)

        self.play(FadeOut(x_label), FadeOut(x_mat), FadeOut(mean_vec), FadeOut(centered_label), FadeOut(xt_mat), FadeOut(svd_small))
        self.wait(0.3)

        # ============================================================
        # Part 4b: 分解行列の成分表示（U, Σ, V^T を横並び）
        # ============================================================
        subtitle4b = Text("分解された各行列の成分", font_size=28, color=TEAL)
        subtitle4b.next_to(title, DOWN)
        self.play(ReplacementTransform(subtitle4, subtitle4b), run_time=0.5)

        u_label_tex = MathTex(r"\tilde{U}\;(5\times 4)", color=TEAL, font_size=24)
        u_label_tex.shift(UP * 2.05 + LEFT * 4.6)
        u_mat_tex = MathTex(
            r"\begin{bmatrix}"
            r"-0.318 &  0.474 & -0.672 &  0.153 \\\\"
            r"-0.370 & -0.773 & -0.123 & -0.223 \\\\"
            r"-0.405 &  0.313 &  0.729 &  0.081 \\\\"
            r" 0.550 & -0.206 &  0.046 &  0.673 \\\\"
            r" 0.543 &  0.192 &  0.021 & -0.684"
            r"\end{bmatrix}",
            color=TEAL,
            font_size=18,
        )
        u_mat_tex.shift(UP * 0.42 + LEFT * 4.6)

        sigma_label_tex = MathTex(r"\tilde{\Sigma}\;(4\times 4)", color=ORANGE, font_size=24)
        sigma_label_tex.shift(UP * 2.05)
        sigma_mat_tex = MathTex(
            r"\begin{bmatrix}"
            r"16.887 & 0 & 0 & 0 \\\\"
            r"0 & 1.736 & 0 & 0 \\\\"
            r"0 & 0 & 1.179 & 0 \\\\"
            r"0 & 0 & 0 & 0.906"
            r"\end{bmatrix}",
            color=ORANGE,
            font_size=18,
        )
        sigma_mat_tex.shift(UP * 0.42)

        vt_label_tex = MathTex(r"\tilde{V}^{\top}\;(4\times 4)", color=GREEN_B, font_size=24)
        vt_label_tex.shift(UP * 2.05 + RIGHT * 4.6)
        vt_mat_tex = MathTex(
            r"\begin{bmatrix}"
            r"-0.520 & -0.480 & -0.443 &  0.550 \\\\"
            r" 0.689 & -0.483 & -0.509 & -0.181 \\\\"
            r" 0.272 &  0.689 & -0.460 &  0.489 \\\\"
            r" 0.426 & -0.246 &  0.577 &  0.652"
            r"\end{bmatrix}",
            color=GREEN_B,
            font_size=18,
        )
        vt_mat_tex.shift(UP * 0.42 + RIGHT * 4.6)

        vt_note = Text(
            "V^T の各行が新しい軸の方向ベクトル（第1行が第1主成分方向）",
            color=WHITE, font_size=22,
        )
        vt_note.shift(DOWN * 1.85)

        self.play(
            Write(u_label_tex), Write(u_mat_tex),
            Write(sigma_label_tex), Write(sigma_mat_tex),
            Write(vt_label_tex), Write(vt_mat_tex),
            run_time=1.3,
        )
        self.play(Write(vt_note), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(u_label_tex), FadeOut(u_mat_tex),
            FadeOut(sigma_label_tex), FadeOut(sigma_mat_tex),
            FadeOut(vt_label_tex), FadeOut(vt_mat_tex),
            FadeOut(vt_note), FadeOut(subtitle4b),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: SVDの結果からPCAの意味を読み解く（行列を再表示してハイライト）
        # ============================================================
        subtitle5 = Text("SVDの結果からPCAの意味を読み解く", font_size=28, color=BLUE)
        subtitle5.next_to(title, DOWN)
        self.play(Write(subtitle5), run_time=0.6)

        # 行列を画面上部に再表示（コンパクト）
        u5_label = MathTex(r"\tilde{U}", color=TEAL, font_size=20)
        u5_label.shift(UP * 2.1 + LEFT * 4.7)
        u5_mat = MathTex(
            r"\begin{bmatrix}"
            r"-0.318 &  0.474 & -0.672 &  0.153 \\"
            r"-0.370 & -0.773 & -0.123 & -0.223 \\"
            r"-0.405 &  0.313 &  0.729 &  0.081 \\"
            r" 0.550 & -0.206 &  0.046 &  0.673 \\"
            r" 0.543 &  0.192 &  0.021 & -0.684"
            r"\end{bmatrix}",
            color=TEAL, font_size=15,
        )
        u5_mat.next_to(u5_label, DOWN, buff=0.06)

        sig5_label = MathTex(r"\tilde{\Sigma}", color=ORANGE, font_size=20)
        sig5_label.shift(UP * 2.1)
        sig5_mat = MathTex(
            r"\begin{bmatrix}"
            r"16.887 & 0 & 0 & 0 \\"
            r"0 & 1.736 & 0 & 0 \\"
            r"0 & 0 & 1.179 & 0 \\"
            r"0 & 0 & 0 & 0.906"
            r"\end{bmatrix}",
            color=ORANGE, font_size=15,
        )
        sig5_mat.next_to(sig5_label, DOWN, buff=0.06)

        vt5_label = MathTex(r"\tilde{V}^{\top}", color=GREEN_B, font_size=20)
        vt5_label.shift(UP * 2.1 + RIGHT * 4.7)
        vt5_mat = MathTex(
            r"\begin{bmatrix}"
            r"-0.520 & -0.480 & -0.443 &  0.550 \\"
            r" 0.689 & -0.483 & -0.509 & -0.181 \\"
            r" 0.272 &  0.689 & -0.460 &  0.489 \\"
            r" 0.426 & -0.246 &  0.577 &  0.652"
            r"\end{bmatrix}",
            color=GREEN_B, font_size=15,
        )
        vt5_mat.next_to(vt5_label, DOWN, buff=0.06)

        self.play(
            FadeIn(VGroup(u5_label, u5_mat)),
            FadeIn(VGroup(sig5_label, sig5_mat)),
            FadeIn(VGroup(vt5_label, vt5_mat)),
            run_time=0.8,
        )
        self.wait(0.3)

        # ─── Step 1: Σ をハイライト → σ₁が突出 ───
        sig5_box = SurroundingRectangle(sig5_mat, color=YELLOW, buff=0.1, stroke_width=3)
        sigma_step = VGroup(
            MathTex(
                r"\sigma_1=16.887\;\gg\;\sigma_2=1.736,\ \sigma_3=1.179,\ \sigma_4=0.906",
                color=YELLOW, font_size=27,
            ),
            Text("第1特異値が圧倒的に大きい → 第1軸1本で大部分の情報を表せる",
                 color=GREEN, font_size=23),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        sigma_step.move_to(DOWN * 1.8)

        self.play(Create(sig5_box), run_time=0.4)
        self.play(Write(sigma_step), run_time=0.7)
        self.wait(1.2)
        self.play(FadeOut(sig5_box), FadeOut(sigma_step))
        self.wait(0.2)

        # ─── Step 2: V^T をハイライト → 第1行が第1主成分方向 ───
        vt5_box = SurroundingRectangle(vt5_mat, color=GREEN_B, buff=0.1, stroke_width=3)
        # 行列の高さを4等分して第1行の位置を推定
        vt5_row_h = vt5_mat.height / 4.0
        vt5_row1_hl = Rectangle(
            width=vt5_mat.width * 0.86, height=vt5_row_h * 0.78,
            color=GREEN_B, fill_color=GREEN_B, fill_opacity=0.22, stroke_width=2,
        ).move_to([vt5_mat.get_center()[0],
                   vt5_mat.get_top()[1] - vt5_row_h * 0.57, 0])

        vt_row_eq = MathTex(
            r"\tilde{v}_1^{\top}=[-0.520,\ -0.480,\ -0.443,\ 0.550]",
            color=GREEN_B, font_size=28,
        )
        vt_row_eq.move_to(DOWN * 1.35)
        vt_row_note = Text(
            "V\u1d40 の第1行 = 新しい第1軸の方向（x\u2081〜x\u2084 それぞれへの重み係数）",
            color=WHITE, font_size=22,
        )
        vt_row_note.next_to(vt_row_eq, DOWN, buff=0.12)

        self.play(Create(vt5_box), FadeIn(vt5_row1_hl), run_time=0.5)
        self.play(Write(vt_row_eq), run_time=0.6)
        self.play(Write(vt_row_note), run_time=0.5)
        self.wait(1.2)
        self.play(
            FadeOut(vt5_box), FadeOut(vt5_row1_hl),
            FadeOut(vt_row_eq), FadeOut(vt_row_note),
        )
        self.wait(0.2)

        # ─── Step 3: U をハイライト → 第1列×σ₁ = 各データの第1軸座標 ───
        u5_box = SurroundingRectangle(u5_mat, color=TEAL, buff=0.1, stroke_width=3)
        # 行列の幅を4等分して第1列の位置を推定
        u5_col_w = u5_mat.width / 4.0
        u5_col1_hl = Rectangle(
            width=u5_col_w * 0.68, height=u5_mat.height * 0.86,
            color=TEAL, fill_color=TEAL, fill_opacity=0.22, stroke_width=2,
        ).move_to([u5_mat.get_left()[0] + u5_col_w * 0.56,
                   u5_mat.get_center()[1], 0])

        u_col_eq = MathTex(
            r"\tilde{u}_1=[-0.318,\ -0.370,\ -0.405,\ 0.550,\ 0.543]^{\top}",
            color=TEAL, font_size=27,
        )
        u_col_eq.move_to(DOWN * 1.05)

        score_eq = MathTex(
            r"t_1=\sigma_1\,\tilde{u}_1\approx[-5.37,\ -6.25,\ -6.85,\ 9.29,\ 9.18]^{\top}",
            color=TEAL, font_size=26,
        )
        score_eq.next_to(u_col_eq, DOWN, buff=0.14)

        score_note = Text(
            "1〜3本目は負（−）・4〜5本目は正（＋）→ 第1軸の符号でデータが2群に分かれる",
            color=YELLOW, font_size=22,
        )
        score_note.next_to(score_eq, DOWN, buff=0.1)

        self.play(Create(u5_box), FadeIn(u5_col1_hl), run_time=0.5)
        self.play(Write(u_col_eq), run_time=0.6)
        self.play(Write(score_eq), run_time=0.6)
        self.play(Write(score_note), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(u5_label), FadeOut(u5_mat),
            FadeOut(sig5_label), FadeOut(sig5_mat),
            FadeOut(vt5_label), FadeOut(vt5_mat),
            FadeOut(u5_box), FadeOut(u5_col1_hl),
            FadeOut(u_col_eq), FadeOut(score_eq),
            FadeOut(score_note), FadeOut(subtitle5),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: まとめ
        # ============================================================
        subtitle_end = Text("まとめ", font_size=36, color=GOLD, weight=BOLD)
        subtitle_end.next_to(title, DOWN)
        self.play(Write(subtitle_end), run_time=0.7)

        summary = VGroup(
            Text("1. 軸を変えると特徴を捉えやすくなることがある", color=WHITE, font_size=28),
            Text("2. 新軸は z = Wx（元変数の線形結合）で作れる", color=WHITE, font_size=28),
            Text("3. SVD: X=UΣV^T（この動画は N×R, R×R, R×D の分解）", color=WHITE, font_size=28),
            Text("4. 特異値が偏ると、少数軸で特徴を表現しやすい", color=WHITE, font_size=28),
            Text("5. 特異値分解と主成分分析は密接な関係がある", color=GREEN, font_size=28),
            Text("主成分分析の話は第18話でもう一度扱う", color=ORANGE, font_size=25),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        summary.scale(0.85)
        summary.shift(DOWN * 0.45)

        for row in summary:
            self.play(Write(row), run_time=0.6)
            self.wait(0.2)

        self.wait(1.5)
        self.play(FadeOut(VGroup(title, subtitle_end, summary)), run_time=1.0)
        self.wait(0.5)
