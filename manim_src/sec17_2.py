from manim import *
import numpy as np


class LowRankApproximation(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        title = Text("削ってもだいたい合っている", font_size=36, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.7)

        # ============================================================
        # Part 1: U, Σ, V^T を成分表示で並べる
        # ============================================================
        subtitle1 = Text("前回と同じ行列を特異値分解", font_size=28, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)

        x_label = Text("データ行列 X（前回と同じ）", color=WHITE, font_size=24)
        x_label.shift(UP * 1.7 + LEFT * 4.0)
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
        x_mat.shift(LEFT * 4.0)

        svd_intro = VGroup(
            MathTex(r"X = U\Sigma V^{\top}", color=YELLOW, font_size=30),
            Text("を今回は中心化せずに特異値分解すると…", color=YELLOW, font_size=26),
        ).arrange( RIGHT, buff=0.15)
        svd_intro.shift(RIGHT * 2.2)

        self.play(Write(x_label), Write(x_mat), run_time=0.7)
        self.play(Write(svd_intro), run_time=0.6)
        self.wait(1.2)
        self.play(
            FadeOut(x_label), FadeOut(x_mat),
            FadeOut(svd_intro), FadeOut(subtitle1),
        )
        self.wait(0.2)

        # ── 3行列を横並びで表示 ──
        subtitle1b = Text("分解された各行列の成分", font_size=28, color=TEAL)
        subtitle1b.next_to(title, DOWN)
        self.play(Write(subtitle1b), run_time=0.6)

        u_label = MathTex(r"U\;(5\times 4)", color=TEAL, font_size=28)
        u_label.shift(UP * 2.05 + LEFT * 4.6)
        u_mat = MathTex(
            r"\begin{bmatrix}"
            r"-0.535 &  0.013 & -0.408 & -0.696 \\\\"
            r"-0.582 &  0.012 &  0.797 &  0.037 \\\\"
            r"-0.611 &  0.020 & -0.407 &  0.585 \\\\"
            r"-0.030 & -0.748 &  0.118 & -0.272 \\\\"
            r"-0.005 & -0.663 & -0.139 &  0.312"
            r"\end{bmatrix}",
            color=TEAL,
            font_size=22,
        )
        u_mat.next_to(u_label, DOWN, buff=0.1)

        sigma_label = MathTex(r"\Sigma\;(4\times 4)", color=ORANGE, font_size=28)
        sigma_label.shift(UP * 2.05)
        sigma_mat = MathTex(
            r"\begin{bmatrix}"
            r"22.728 & 0 & 0 & 0 \\\\"
            r"0 & 12.055 & 0 & 0 \\\\"
            r"0 & 0 & 1.701 & 0 \\\\"
            r"0 & 0 & 0 & 1.101"
            r"\end{bmatrix}",
            color=ORANGE,
            font_size=22,
        )
        sigma_mat.next_to(sigma_label, DOWN, buff=0.1)

        vt_label = MathTex(r"V^{\top}\;(4\times 4)", color=GREEN_B, font_size=28)
        vt_label.shift(UP * 2.05 + RIGHT * 4.6)
        vt_mat = MathTex(
            r"\begin{bmatrix}"
            r"-0.610 & -0.561 & -0.559 & -0.014 \\\\"
            r" 0.030 &  0.027 & -0.036 & -0.999 \\\\"
            r"-0.791 &  0.397 &  0.465 & -0.029 \\\\"
            r"-0.041 &  0.726 & -0.685 &  0.043"
            r"\end{bmatrix}",
            color=GREEN_B,
            font_size=22,
        )
        vt_mat.next_to(vt_label, DOWN, buff=0.1)

        self.play(
            Write(u_label), Write(u_mat),
            Write(sigma_label), Write(sigma_mat),
            Write(vt_label), Write(vt_mat),
            run_time=1.2,
        )
        self.wait(0.8)

        # ── Σ に注目 → 対角成分の偏りを指摘 ──
        sigma_box = SurroundingRectangle(
            VGroup(sigma_label, sigma_mat), color=YELLOW, buff=0.12, stroke_width=3,
        )
        self.play(Create(sigma_box), run_time=0.4)

        sigma_display = MathTex(
            r"\Sigma = \mathrm{diag}(\,\underbrace{22.728}_{\large\sigma_1},\;"
            r"\underbrace{12.055}_{\large\sigma_2},\;"
            r"\underbrace{1.701}_{\large\sigma_3},\;"
            r"\underbrace{1.101}_{\large\sigma_4}\,)",
            color=ORANGE,
            font_size=30,
        )
        sigma_display.shift(DOWN)

        sigma_remark = VGroup(
            Text("σ₁ と σ₂ が際立って大きい！", color=YELLOW, font_size=25, weight=BOLD),
            Text("→ 上位2つの特異値だけで再構成してみよう", color=GREEN, font_size=23),
        ).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        sigma_remark.shift(DOWN * 2)

        self.play(Write(sigma_display), run_time=0.7)
        self.play(Write(sigma_remark), run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(u_label), FadeOut(u_mat),
            FadeOut(sigma_label), FadeOut(sigma_mat),
            FadeOut(vt_label), FadeOut(vt_mat),
            FadeOut(sigma_box),
            FadeOut(sigma_display), FadeOut(sigma_remark),
            FadeOut(subtitle1b),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: ランク2近似 — 再構成行列と元行列の比較
        # ============================================================
        subtitle2 = Text("上位2成分だけで行列を再構成する", font_size=28, color=GOLD)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2), run_time=0.6)

        rank2_formula = MathTex(
            r"\hat{X}"
            r"= U\,\mathrm{diag}(\sigma_1,\sigma_2,0,0)\,V^{\top}",
            color=YELLOW,
            font_size=32,
        )
        rank2_formula.shift(UP * 2.0)
        self.play(Write(rank2_formula), run_time=0.7)
        self.wait(0.3)

        # 元の行列
        orig_label = Text("元の行列 X", color=WHITE, font_size=22)
        orig_label.shift(UP * 1.5 + LEFT * 3.8)
        orig_mat = MathTex(
            r"\begin{bmatrix}"
            r"8 & 6 & 7 & 0 \\"
            r"7 & 8 & 8 & 0 \\"
            r"9 & 8 & 7 & 0 \\"
            r"0 & 0 & 1 & 9 \\"
            r"0 & 0 & 0 & 8"
            r"\end{bmatrix}",
            color=WHITE,
            font_size=30,
        )
        orig_mat.shift(UP * 0.15 + LEFT * 3.8)

        approx_label = Text("ランク2近似 X̂", color=TEAL, font_size=22)
        approx_label.shift(UP * 1.5 + RIGHT * 2.6)
        approx_mat = MathTex(
            r"\begin{bmatrix}"
            r"7.42 & 6.83 & 6.80 & 0.01 \\"
            r"8.07 & 7.43 & 7.40 & 0.04 \\"
            r"8.48 & 7.81 & 7.76 & -0.05 \\"
            r"0.15 & 0.14 & 0.70 & 9.02 \\"
            r"-0.17 & -0.16 & 0.34 & 7.98"
            r"\end{bmatrix}",
            color=TEAL,
            font_size=30,
        )
        approx_mat.shift(UP * 0.15 + RIGHT * 2.6)

        approx_arrow = MathTex(r"\approx", color=YELLOW, font_size=48)
        approx_arrow.move_to(
            (orig_mat.get_right() + approx_mat.get_left()) / 2
        )

        self.play(FadeIn(orig_label), FadeIn(orig_mat), run_time=0.6)
        self.play(Write(approx_arrow), run_time=0.3)
        self.play(FadeIn(approx_label), FadeIn(approx_mat), run_time=0.7)
        self.wait(0.5)

        similar_note = Text(
            "成分がよく一致している → ランク2でもとの行列を近似できている",
            color=GREEN, font_size=26,
        )
        similar_note.shift(DOWN*1.1)
        self.play(Write(similar_note), run_time=0.6)
        self.wait(0.8)

        storage_note = VGroup(
            Text("保存するデータ量の比較", color=GOLD, font_size=22, weight=BOLD),
            MathTex(
                r"N\times D\;\text{values}"
                r"\quad\longrightarrow\quad"
                r"(N+D+1)\times R\;\text{values (rank-}R\text{)}",
                color=WHITE,
                font_size=26,
            ),
            Text(
                "5x4だと同じだが、大きい行列になるほど情報量の削減効果は大きくなる",
                color=YELLOW, font_size=22,
            ),
            Text(
                "※この低ランク近似の考え方は第5部でも重要な役割を果たす",
                color=GREEN, font_size=20,
            ),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        storage_note.shift(DOWN * 2.3)
        for item in storage_note:
            self.play(Write(item), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(rank2_formula),
            FadeOut(orig_label), FadeOut(orig_mat),
            FadeOut(approx_arrow),
            FadeOut(approx_label), FadeOut(approx_mat),
            FadeOut(similar_note), FadeOut(storage_note),
            FadeOut(subtitle2),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: なぜランクが下がるのか — 外積展開によるランク確認
        # ============================================================
        subtitle3 = Text("本当にランクが下がっているか", font_size=28, color=BLUE)
        subtitle3.next_to(title, DOWN)
        self.play(Write(subtitle3), run_time=0.6)

        # 列ベクトルによる展開式
        expand_step1 = MathTex(
            r"\hat{X}=[\boldsymbol{u}_1\ \boldsymbol{u}_2\ \boldsymbol{u}_3\ \boldsymbol{u}_4]"
            r"\begin{bmatrix}\sigma_1&0&0&0\\0&\sigma_2&0&0\\0&0&0&0\\0&0&0&0\end{bmatrix}"
            r"\begin{bmatrix}\boldsymbol{v}_1^{\top}\\\boldsymbol{v}_2^{\top}\\\boldsymbol{v}_3^{\top}\\\boldsymbol{v}_4^{\top}\end{bmatrix}",
            color=WHITE,
            font_size=26,
        )
        expand_step1.shift(UP * 1.5)

        eq_sign = MathTex(r"=", color=WHITE, font_size=30)
        eq_sign.next_to(expand_step1, DOWN, buff=0.18)

        expand_step2 = MathTex(
            r"\sigma_1\,\boldsymbol{u}_1\boldsymbol{v}_1^{\top}"
            r"+\sigma_2\,\boldsymbol{u}_2\boldsymbol{v}_2^{\top}",
            color=YELLOW,
            font_size=34,
        )
        expand_step2.next_to(eq_sign, DOWN, buff=0.18)

        self.play(Write(expand_step1), run_time=0.9)
        self.play(Write(eq_sign), Write(expand_step2), run_time=0.7)
        self.wait(0.5)

        # 第1項のランク説明
        term1_box = SurroundingRectangle(
            expand_step2[0][0:13], color=TEAL, buff=0.08, stroke_width=2,
        )
        term1_note = VGroup(
            MathTex(
                r"\sigma_1\,\boldsymbol{u}_1\boldsymbol{v}_1^{\top}"
                r"=\sigma_1\begin{bmatrix}u_{11}\\u_{21}\\u_{31}\\u_{41}\\u_{51}\end{bmatrix}"
                r"\boldsymbol{v}_1^{\top}",
                color=TEAL, font_size=24,
            ),
            Text(
                "列ベクトル u₁ × 行ベクトル v₁ᵀ → ランク1",
                color=TEAL, font_size=24,
            ),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        term1_note.shift(DOWN * 1.5 + LEFT * 1.0)

        self.play(Create(term1_box), run_time=0.4)
        self.play(Write(term1_note), run_time=0.7)
        self.wait(0.8)
        self.play(FadeOut(term1_box), FadeOut(term1_note))

        # 第2項のランク説明
        term2_note = VGroup(
            Text("第2項 σ₂ u₂ v₂ᵀ も同様にランク1", color=ORANGE, font_size=22),
            Text(
                "U, V は直交行列 → u₁ ⊥ u₂, v₁ ⊥ v₂",
                color=WHITE, font_size=24,
            ),
            Text(
                "であり、2つの項は本質的に独立（同じ方向を含まない）",
                color=WHITE, font_size=24,
            ),
            Text(
                "∴ ランク1 ＋ ランク1（独立）= ランク2 →もとの4から落ちている",
                color=GREEN, font_size=26, weight=BOLD,
            ),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        term2_note.shift(DOWN * 1.5)

        for item in term2_note:
            self.play(Write(item), run_time=0.5)
        self.wait(1.5)

        self.play(
            FadeOut(expand_step1), FadeOut(eq_sign), FadeOut(expand_step2),
            FadeOut(term2_note), FadeOut(subtitle3),
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: 一般化 — 外積和表記とブラケット表記
        # ============================================================
        subtitle4 = Text("特異値分解を外積和・ブラケットで書く", font_size=28, color=GOLD)
        subtitle4.next_to(title, DOWN)
        self.play(Write(subtitle4), run_time=0.6)

        # 一般的な外積和表記
        outer_sum = MathTex(
            r"X = \sum_{r=1}^{R}\sigma_r\,\boldsymbol{u}_r\boldsymbol{v}_r^{\top}",
            color=YELLOW,
            font_size=42,
        )
        outer_sum.shift(UP * 1.4)
        # outer_box = SurroundingRectangle(outer_sum, color=YELLOW, buff=0.2)

        outer_note = VGroup(
            # Text("各項は『方向 uᵣ に投影し σᵣ 倍してから方向 vᵣᵀ に配置する』操作", color=WHITE, font_size=22),
            Text("特異値が小さい項は寄与が小さく、省いてもほぼ影響がないことがわかる", color=GREEN, font_size=26),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        outer_note.shift(UP * 0.3)

        self.play(Write(outer_sum), run_time=0.8)
        self.play(Write(outer_note), run_time=0.7)
        self.wait(0.5)

        # ブラケット表記
        bracket_label = Text("ブラケット記法で書くと：", color=WHITE, font_size=24)
        bracket_label.shift(DOWN * 0.5)

        bracket_eq = MathTex(
            r"X = \sum_{r=1}^{R}\sigma_r\,|\boldsymbol{u}_r\rangle\langle\boldsymbol{v}_r|",
            color=TEAL,
            font_size=42,
        )
        bracket_eq.shift(DOWN * 1.4)
        # bracket_box = SurroundingRectangle(bracket_eq, color=TEAL, buff=0.2)

        bracket_note = VGroup(
            # MathTex(
            #     r"\langle\boldsymbol{v}_r|\;=\;\boldsymbol{v}_r^{\top}",
            #     color=WHITE, font_size=24,
            # ),
            Text(
                "⟨vᵣ| は入力ベクトルを vᵣ 方向へ射影する操作を表す(6話のはなし)",
                color=ORANGE, font_size=26,
            ),
            Text(
                "射影 (⟨vᵣ|) → スケール（σᵣ）→ 出力空間に配置、という流れが見える",
                color=WHITE, font_size=24,
            ),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        bracket_note.shift(DOWN * 2.8)

        self.play(Write(bracket_label), run_time=0.4)
        self.play(Write(bracket_eq), run_time=0.7)
        self.play(Write(bracket_note), run_time=0.8)
        self.wait(1.8)

        self.play(
            FadeOut(outer_sum),
            FadeOut(outer_note),
            FadeOut(bracket_label),
            FadeOut(bracket_eq),
            FadeOut(bracket_note),
            FadeOut(subtitle4),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: まとめ
        # ============================================================
        subtitle_end = Text("まとめ", font_size=36, color=GOLD, weight=BOLD)
        subtitle_end.next_to(title, DOWN)
        self.play(Write(subtitle_end), run_time=0.7)

        summary = VGroup(
            Text("1. 小さい特異値を0にして再構成しても、もとの行列を近似できる", color=WHITE, font_size=28),
            Text("→これが低ランク近似：情報をうまく削減する手法", color=WHITE, font_size=26),
            Text("2. ランクが下がる理由は外積 uᵣvᵣᵀ がランク1であることと直交性", color=WHITE, font_size=28),
            Text("3. SVDは Σ σᵣ|uᵣ⟩⟨vᵣ| と書け ⟨vᵣ| が射影操作を表現している", color=WHITE, font_size=28),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        summary.scale(0.88)
        summary.shift(DOWN * 0.5)

        for row in summary:
            self.play(Write(row), run_time=0.6)
            self.wait(0.15)

        self.wait(1.5)
        self.play(FadeOut(VGroup(title, subtitle_end, summary)), run_time=1.0)
        self.wait(0.5)
