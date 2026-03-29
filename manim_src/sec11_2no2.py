from manim import *
import numpy as np

class SystematicRepresentationMatrix(Scene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"

        # タイトル
        title = Text("表現行列の系統的な求め方", font_size=34, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)

        # === Part 1: 前回の復習 ===
        subtitle1 = Text("前回の復習: 発見的に求めた表現行列", font_size=30, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.5)

        # 前回の結果
        prev_result = VGroup(
            Text("前回はエルミート基底での微分の表現行列を", color=WHITE, font_size=24),
            Text("個別の計算から求めた", color=WHITE, font_size=24),
        ).arrange(DOWN, buff=0.2)
        prev_result.shift(UP * 1.5)
        self.play(Write(prev_result), run_time=0.7)
        self.wait(0.4)

        prev_matrix = MathTex(
            r"L_{\text{Hermite}} = \begin{pmatrix} 0 & 2 & 0 \\ 0 & 0 & 4 \\ 0 & 0 & 0 \end{pmatrix}",
            color=YELLOW, font_size=28
        )
        prev_matrix.shift(UP * 0.3)
        prev_matrix_box = SurroundingRectangle(prev_matrix, color=YELLOW, buff=0.15)
        self.play(Write(prev_matrix), Create(prev_matrix_box), run_time=0.7)
        self.wait(0.5)

        # 問題提起
        question = VGroup(
            Text("これを系統的に導出できないか？", color=RED, font_size=26, weight=BOLD),
            Text("→ 任意の次数・任意の作用素に使える方法", color=ORANGE, font_size=22),
        ).arrange(DOWN, buff=0.2)
        question.shift(DOWN * 1.2)
        q_box = SurroundingRectangle(question, color=RED, buff=0.2)
        self.play(Write(question), Create(q_box), run_time=0.8)
        self.wait(1.0)

        self.play(
            FadeOut(prev_result), FadeOut(prev_matrix), FadeOut(prev_matrix_box),
            FadeOut(question), FadeOut(q_box),
            FadeOut(subtitle1)
        )
        self.wait(0.3)

        # === Part 2: エルミート多項式の内積公式 ===
        subtitle2 = Text("準備①: 内積公式のブラケット表記", font_size=30, color=PURPLE)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)

        # 元の公式
        original_label = Text("エルミート多項式の直交性（第10話）:", color=YELLOW, font_size=22, weight=BOLD)
        original_label.shift(UP * 1.8 + LEFT * 2)
        self.play(Write(original_label), run_time=0.5)
        self.wait(0.3)

        original_formula = MathTex(
            r"\langle H_n | H_m \rangle = \int_{-\infty}^{\infty} H_n(x) H_m(x) e^{-x^2} dx = 2^n n! \sqrt{\pi} \, \delta_{nm}",
            color=WHITE, font_size=24
        )
        original_formula.shift(UP * 1.1)
        self.play(Write(original_formula), run_time=0.8)
        self.wait(0.5)

        # ブラケット表記に書き換え
        braket_label = Text("簡潔なブラケット表記:", color=TEAL, font_size=22, weight=BOLD)
        braket_label.shift(UP * 0.3 + LEFT * 4)
        self.play(Write(braket_label), run_time=0.4)

        braket_formula = MathTex(
            r"\langle n | m \rangle = 2^n n! \sqrt{\pi} \, \delta_{nm}",
            color=TEAL, font_size=28
        )
        braket_formula.shift(DOWN * 0.3)
        braket_box = SurroundingRectangle(braket_formula, color=TEAL, buff=0.15)
        self.play(Write(braket_formula), Create(braket_box), run_time=0.7)
        self.wait(0.5)

        # 正規化定数の導入
        alpha_label = Text("正規化定数を導入:", color=ORANGE, font_size=22, weight=BOLD)
        alpha_label.shift(DOWN * 1.1 + LEFT * 4)
        self.play(Write(alpha_label), run_time=0.4)

        alpha_def = MathTex(
            r"\alpha_n = \frac{1}{2^n n! \sqrt{\pi}}",
            color=ORANGE, font_size=26
        )
        alpha_def.shift(DOWN * 1.8)
        self.play(Write(alpha_def), run_time=0.6)
        self.wait(0.3)

        # 正規化された内積
        normalized = MathTex(
            r"\alpha_n \langle n | m \rangle = \delta_{nm}",
            color=GREEN, font_size=30
        )
        normalized.shift(DOWN * 2.7)
        normalized_box = SurroundingRectangle(normalized, color=GREEN, buff=0.2)
        self.play(Write(normalized), Create(normalized_box), run_time=0.7)
        self.wait(1.0)

        self.play(
            FadeOut(original_label), FadeOut(original_formula),
            FadeOut(braket_label), FadeOut(braket_formula), FadeOut(braket_box),
            FadeOut(alpha_label), FadeOut(alpha_def),
            FadeOut(normalized), FadeOut(normalized_box),
            FadeOut(subtitle2)
        )
        self.wait(0.3)

        # === Part 3: エルミート多項式の微分公式 ===
        subtitle3 = Text("準備②: エルミート多項式の微分公式", font_size=30, color=GREEN)
        subtitle3.next_to(title, DOWN)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.5)

        # エルミート多項式のもう一つの性質
        property_intro = VGroup(
            Text("エルミート多項式にはもう一つ便利な性質がある", color=WHITE, font_size=24),
        )
        property_intro.shift(UP * 1.6)
        self.play(Write(property_intro), run_time=0.6)
        self.wait(0.4)

        # 微分公式
        diff_formula_label = Text("微分公式:", color=YELLOW, font_size=24, weight=BOLD)
        diff_formula_label.shift(UP * 0.9 + LEFT * 5)
        self.play(Write(diff_formula_label), run_time=0.4)

        diff_formula = MathTex(
            r"\frac{d}{dx} H_n(x) = 2n \, H_{n-1}(x)",
            color=YELLOW, font_size=30
        )
        diff_formula.shift(UP * 0.3)
        diff_box = SurroundingRectangle(diff_formula, color=YELLOW, buff=0.15)
        self.play(Write(diff_formula), Create(diff_box), run_time=0.7)
        self.wait(0.5)

        # ケット表記で
        ket_label = Text("ケット表記で:", color=TEAL, font_size=22, weight=BOLD)
        ket_label.shift(DOWN * 0.5 + LEFT * 5)
        self.play(Write(ket_label), run_time=0.4)

        ket_diff = MathTex(
            r"\frac{d}{dx} |n\rangle = 2n |n-1\rangle",
            color=TEAL, font_size=28
        )
        ket_diff.shift(DOWN * 1.1)
        ket_diff_box = SurroundingRectangle(ket_diff, color=TEAL, buff=0.15)
        self.play(Write(ket_diff), Create(ket_diff_box), run_time=0.7)
        self.wait(0.5)

        # 具体例
        examples_label = Text("確認:", color=GRAY, font_size=20)
        examples_label.shift(DOWN * 2.0 + LEFT * 5.5)
        self.play(Write(examples_label), run_time=0.3)

        examples = VGroup(
            MathTex(r"\frac{d}{dx}|1\rangle = 2|0\rangle", color=GRAY, font_size=22),
            MathTex(r"\frac{d}{dx}|2\rangle = 4|1\rangle", color=GRAY, font_size=22),
            MathTex(r"\frac{d}{dx}|3\rangle = 6|2\rangle", color=GRAY, font_size=22),
        ).arrange(RIGHT, buff=0.6)
        examples.shift(DOWN * 2.6)
        self.play(Write(examples), run_time=0.7)
        self.wait(1.0)

        self.play(
            FadeOut(property_intro),
            FadeOut(diff_formula_label), FadeOut(diff_formula), FadeOut(diff_box),
            FadeOut(ket_label), FadeOut(ket_diff), FadeOut(ket_diff_box),
            FadeOut(examples_label), FadeOut(examples),
            FadeOut(subtitle3)
        )
        self.wait(0.3)

        # === Part 4: ブラの役割（射影・成分抽出） ===
        subtitle4 = Text("準備③: ブラの役割 - 成分の抽出", font_size=30, color=GOLD)
        subtitle4.next_to(title, DOWN)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.5)

        # ブラの意味
        bra_meaning = VGroup(
            Text("ブラケット記法における「ブラ」の役割", color=WHITE, font_size=24),
            Text("（第6話で学んだ内容の復習）", color=GRAY, font_size=20),
        ).arrange(DOWN, buff=0.15)
        bra_meaning.shift(UP * 1.6)
        self.play(Write(bra_meaning), run_time=0.7)
        self.wait(0.4)

        # 射影の考え方
        projection_text = VGroup(
            Text("ノルム1のベクトルのブラ → 射影を意味する", color=YELLOW, font_size=24),
        )
        projection_text.shift(UP * 0.8)
        self.play(Write(projection_text), run_time=0.6)
        self.wait(0.4)

        # エルミートの場合
        hermite_case = VGroup(
            Text("エルミート多項式は正規化されていないが...", color=WHITE, font_size=22),
            Text("同様に「ある方向の成分を抽出」と考えられる", color=TEAL, font_size=24, weight=BOLD),
        ).arrange(DOWN, buff=0.2)
        hermite_case.shift(DOWN * 0.1)
        self.play(Write(hermite_case), run_time=0.8)
        self.wait(0.5)

        # 成分抽出の式
        extraction = VGroup(
            MathTex(r"\alpha_n \langle n | f \rangle", color=GREEN, font_size=24),
            Text("＝", color=GREEN, font_size=20),
            MathTex(r"|f\rangle", color=GREEN, font_size=24),
            Text("の", color=GREEN, font_size=20),
            MathTex(r"|n\rangle", color=GREEN, font_size=24),
            Text("方向の成分", color=GREEN, font_size=20),
        ).arrange(RIGHT, buff=0.15)
        extraction.shift(DOWN * 1.2)
        self.play(Write(extraction), run_time=0.7)
        self.wait(1.0)

        self.play(
            FadeOut(bra_meaning), FadeOut(projection_text),
            FadeOut(hermite_case), FadeOut(extraction),
            FadeOut(subtitle4)
        )
        self.wait(0.3)

        # === Part 5: 多項式の展開（単位の分解への準備） ===
        subtitle5 = Text("任意の多項式の基底展開", font_size=30, color=BLUE)
        subtitle5.next_to(title, DOWN)
        self.play(Write(subtitle5), run_time=0.6)
        self.wait(0.5)

        # 展開の説明
        expand_intro = Text("任意の多項式をエルミート多項式で展開する", color=YELLOW, font_size=24, weight=BOLD)
        expand_intro.shift(UP * 1.6)
        self.play(Write(expand_intro), run_time=0.6)
        self.wait(0.4)

        # 展開式
        expansion = MathTex(
            r"|f\rangle = \sum_{n=0}^{\infty} \left( \alpha_n \langle n | f \rangle \right) |n\rangle",
            color=WHITE, font_size=28
        )
        expansion.shift(UP * 0.8)
        self.play(Write(expansion), run_time=0.8)
        self.wait(0.5)

        # スカラーなので順序交換可能
        scalar_note = VGroup(
            MathTex(r"\langle n | f \rangle", color=ORANGE, font_size=26),
            Text("はスカラーなので", color=WHITE, font_size=22),
            Text("積の順番を入れ替えられる", color=WHITE, font_size=22),
        ).arrange(RIGHT, buff=0.2)
        scalar_note.shift(UP * 0.0)
        self.play(Write(scalar_note), run_time=0.7)
        self.wait(0.4)

        # 順序を入れ替えた式
        reordered = MathTex(
            r"|f\rangle = \sum_{n=0}^{\infty} \alpha_n |n\rangle \langle n | f \rangle",
            color=TEAL, font_size=28
        )
        reordered.shift(DOWN * 0.8)
        self.play(Write(reordered), run_time=0.7)
        self.wait(0.5)

        # 両辺を見比べる
        compare_text = Text("両辺をよく見比べると...", color=YELLOW, font_size=24, weight=BOLD)
        compare_text.shift(DOWN * 1.6)
        self.play(Write(compare_text), run_time=0.5)
        self.wait(0.5)

        # 恒等演算子の発見
        identity_discovery = VGroup(
            MathTex(r"\sum_{n=0}^{\infty} \alpha_n |n\rangle \langle n|", color=GREEN, font_size=26),
            Text("は「何もしない作用素」", color=GREEN, font_size=22),
        ).arrange(RIGHT, buff=0.2)
        identity_discovery.shift(DOWN * 2.4)
        identity_box = SurroundingRectangle(identity_discovery, color=GREEN, buff=0.15)
        self.play(Write(identity_discovery), Create(identity_box), run_time=0.9)
        self.wait(1.2)

        self.play(
            FadeOut(expand_intro), FadeOut(expansion),
            FadeOut(scalar_note), FadeOut(reordered),
            FadeOut(compare_text), FadeOut(identity_discovery), FadeOut(identity_box),
            FadeOut(subtitle5)
        )
        self.wait(0.3)

        # === Part 6: 単位の分解 ===
        subtitle6 = Text("単位の分解（恒等演算子の分解）", font_size=30, color=RED)
        subtitle6.next_to(title, DOWN)
        self.play(Write(subtitle6), run_time=0.6)
        self.wait(0.5)

        # 単位の分解の式
        identity_title = Text("恒等演算子（単位演算子）:", color=YELLOW, font_size=24, weight=BOLD)
        identity_title.shift(UP * 1.6 + LEFT * 3)
        self.play(Write(identity_title), run_time=0.5)

        identity_eq = MathTex(
            r"\hat{I} = \sum_{n=0}^{\infty} \alpha_n |n\rangle \langle n|",
            color=YELLOW, font_size=30
        )
        identity_eq.shift(UP * 0.9)
        identity_eq_box = SurroundingRectangle(identity_eq, color=YELLOW, buff=0.15)
        self.play(Write(identity_eq), Create(identity_eq_box), run_time=0.8)
        self.wait(0.6)

        # 利用法の説明
        usage_text = VGroup(
            Text("任意の作用素をこの恒等演算子で「挟んでも」", color=WHITE, font_size=22),
            Text("結果は変わらない", color=WHITE, font_size=22),
        ).arrange(DOWN, buff=0.15)
        usage_text.shift(DOWN * 0.1)
        self.play(Write(usage_text), run_time=0.7)
        self.wait(0.4)

        # 挟む式
        sandwich = MathTex(
            r"\mathcal{L} = \hat{I} \, \mathcal{L} \, \hat{I}",
            color=TEAL, font_size=28
        )
        sandwich.shift(DOWN * 1.0)
        self.play(Write(sandwich), run_time=0.6)
        self.wait(0.5)

        # 展開した式
        expanded_L = MathTex(
            r"\mathcal{L} = \sum_{n,m} \alpha_m |m\rangle \langle m| \mathcal{L} |n\rangle \alpha_n \langle n|",
            color=GREEN, font_size=26
        )
        expanded_L.shift(DOWN * 2.0)
        expanded_L_box = SurroundingRectangle(expanded_L, color=GREEN, buff=0.15)
        self.play(Write(expanded_L), Create(expanded_L_box), run_time=0.9)
        self.wait(1.2)

        self.play(
            FadeOut(identity_title), FadeOut(identity_eq), FadeOut(identity_eq_box),
            FadeOut(usage_text), FadeOut(sandwich),
            FadeOut(expanded_L), FadeOut(expanded_L_box),
            FadeOut(subtitle6)
        )
        self.wait(0.3)

        # === Part 7: 行列要素の計算 ===
        subtitle7 = Text("行列要素の計算", font_size=30, color=PURPLE)
        subtitle7.next_to(title, DOWN)
        self.play(Write(subtitle7), run_time=0.6)
        self.wait(0.5)

        # 計算する要素
        element_title = Text("計算すべきは真ん中の部分:", color=YELLOW, font_size=24, weight=BOLD)
        element_title.shift(UP * 1.8 + LEFT * 3)
        self.play(Write(element_title), run_time=0.5)

        element = MathTex(
            r"\langle m | \mathcal{L} | n \rangle = \langle m | \frac{d}{dx} | n \rangle",
            color=WHITE, font_size=28
        )
        element.shift(UP * 1.1)
        self.play(Write(element), run_time=0.7)
        self.wait(0.5)

        # 微分公式を使う
        use_diff = Text("微分公式を使う:", color=TEAL, font_size=22, weight=BOLD)
        use_diff.shift(UP * 0.4 + LEFT * 5)
        self.play(Write(use_diff), run_time=0.4)

        step1 = MathTex(
            r"\langle m | \frac{d}{dx} | n \rangle = \langle m | 2n | n-1 \rangle = 2n \langle m | n-1 \rangle",
            color=WHITE, font_size=26
        )
        step1.shift(DOWN * 0.2)
        self.play(Write(step1), run_time=0.8)
        self.wait(0.5)

        # デルタ関数を使う
        use_delta = Text("正規化条件より:", color=ORANGE, font_size=22, weight=BOLD)
        use_delta.shift(DOWN * 0.9 + LEFT * 5)
        self.play(Write(use_delta), run_time=0.4)

        step2 = MathTex(
            r"\langle m | n-1 \rangle = \frac{1}{\alpha_m} \delta_{m, n-1}",
            color=WHITE, font_size=26
        )
        step2.shift(DOWN * 1.5)
        self.play(Write(step2), run_time=0.7)
        self.wait(0.4)

        # 最終結果
        result = MathTex(
            r"\langle m | \mathcal{L} | n \rangle = \frac{2n}{\alpha_m} \delta_{m, n-1}",
            color=GREEN, font_size=28
        )
        result.shift(DOWN * 2.4)
        result_box = SurroundingRectangle(result, color=GREEN, buff=0.15)
        self.play(Write(result), Create(result_box), run_time=0.8)
        self.wait(1.2)

        self.play(
            FadeOut(element_title), FadeOut(element),
            FadeOut(use_diff), FadeOut(step1),
            FadeOut(use_delta), FadeOut(step2),
            FadeOut(result), FadeOut(result_box),
            FadeOut(subtitle7)
        )
        self.wait(0.3)

        # === Part 8: 表現行列の成分 ===
        subtitle8 = Text("表現行列の成分", font_size=30, color=ORANGE)
        subtitle8.next_to(title, DOWN)
        self.play(Write(subtitle8), run_time=0.6)
        self.wait(0.5)

        # 作用素の展開式（再掲）
        L_expansion_title = Text("作用素の展開:", color=YELLOW, font_size=22, weight=BOLD)
        L_expansion_title.shift(UP * 1.8 + LEFT * 5)
        self.play(Write(L_expansion_title), run_time=0.4)

        L_expansion = MathTex(
            r"\mathcal{L} = \sum_{n,m} |m\rangle \left( 2n \, \delta_{m, n-1} \right) \alpha_n \langle n|",
            color=WHITE, font_size=26
        )
        L_expansion.shift(UP * 1.1)
        self.play(Write(L_expansion), run_time=0.8)
        self.wait(0.5)

        # 真ん中が表現行列
        matrix_element_title = Text("真ん中の部分が表現行列の成分:", color=TEAL, font_size=22, weight=BOLD)
        matrix_element_title.shift(UP * 0.3 + LEFT * 3)
        self.play(Write(matrix_element_title), run_time=0.5)

        matrix_element = MathTex(
            r"L_{mn} = 2n \, \delta_{m, n-1}",
            color=TEAL, font_size=28
        )
        matrix_element.shift(DOWN * 0.3)
        matrix_element_box = SurroundingRectangle(matrix_element, color=TEAL, buff=0.15)
        self.play(Write(matrix_element), Create(matrix_element_box), run_time=0.7)
        self.wait(0.6)

        # インデックスの補正
        index_note_title = Text("注意: H₀から始まるので添字を調整", color=ORANGE, font_size=20, weight=BOLD)
        index_note_title.shift(DOWN * 1.1 + LEFT * 2.5)
        self.play(Write(index_note_title), run_time=0.5)

        index_note = VGroup(
            MathTex(r"\tilde{m} = m + 1", color=ORANGE, font_size=22),
            Text("行", color=ORANGE, font_size=18),
            MathTex(r"\tilde{n} = n + 1", color=ORANGE, font_size=22),
            Text("列", color=ORANGE, font_size=18),
        ).arrange(RIGHT, buff=0.15)
        index_note.shift(DOWN * 1.7)
        self.play(Write(index_note), run_time=0.6)
        self.wait(0.4)

        # 調整後の公式
        adjusted = MathTex(
            r"L_{\tilde{m}\tilde{n}} = 2(\tilde{n}-1) \, \delta_{\tilde{m}-1, \tilde{n}-2}",
            color=RED, font_size=26
        )
        adjusted.shift(DOWN * 2.5)
        adjusted_box = SurroundingRectangle(adjusted, color=RED, buff=0.15)
        self.play(Write(adjusted), Create(adjusted_box), run_time=0.8)
        self.wait(1.2)

        self.play(
            FadeOut(L_expansion_title), FadeOut(L_expansion),
            FadeOut(matrix_element_title), FadeOut(matrix_element), FadeOut(matrix_element_box),
            FadeOut(index_note_title), FadeOut(index_note),
            FadeOut(adjusted), FadeOut(adjusted_box),
            FadeOut(subtitle8)
        )
        self.wait(0.3)

        # === Part 9: 具体的な行列の構成 ===
        subtitle9 = Text("具体的な行列を構成", font_size=30, color=GREEN)
        subtitle9.next_to(title, DOWN)
        self.play(Write(subtitle9), run_time=0.6)
        self.wait(0.5)

        # 公式の再掲
        formula_recall = MathTex(
            r"L_{mn} = 2n \, \delta_{m, n-1}",
            color=YELLOW, font_size=26
        )
        formula_recall.shift(UP * 1.8)
        self.play(Write(formula_recall), run_time=0.5)
        self.wait(0.3)

        # 具体的な値
        calc_title = Text("m, n = 0, 1, 2 の場合:", color=WHITE, font_size=22, weight=BOLD)
        calc_title.shift(UP * 1.1 + LEFT * 4)
        self.play(Write(calc_title), run_time=0.4)

        # 各成分の計算
        calcs = VGroup(
            MathTex(r"L_{00} = 2 \cdot 0 \cdot \delta_{0,-1} = 0", color=WHITE, font_size=22),
            MathTex(r"L_{01} = 2 \cdot 1 \cdot \delta_{0,0} = 2", color=GREEN, font_size=22),
            MathTex(r"L_{02} = 2 \cdot 2 \cdot \delta_{0,1} = 0", color=WHITE, font_size=22),
            MathTex(r"L_{10} = 2 \cdot 0 \cdot \delta_{1,-1} = 0", color=WHITE, font_size=22),
            MathTex(r"L_{11} = 2 \cdot 1 \cdot \delta_{1,0} = 0", color=WHITE, font_size=22),
            MathTex(r"L_{12} = 2 \cdot 2 \cdot \delta_{1,1} = 4", color=GREEN, font_size=22),
            MathTex(r"L_{20} = 2 \cdot 0 \cdot \delta_{2,-1} = 0", color=WHITE, font_size=22),
            MathTex(r"L_{21} = 2 \cdot 1 \cdot \delta_{2,0} = 0", color=WHITE, font_size=22),
            MathTex(r"L_{22} = 2 \cdot 2 \cdot \delta_{2,1} = 0", color=WHITE, font_size=22),
        )
        
        # 3x3に配置
        calcs_grid = VGroup(
            VGroup(calcs[0], calcs[1], calcs[2]).arrange(RIGHT, buff=0.3),
            VGroup(calcs[3], calcs[4], calcs[5]).arrange(RIGHT, buff=0.3),
            VGroup(calcs[6], calcs[7], calcs[8]).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.2)
        calcs_grid.scale(0.85)
        calcs_grid.shift(DOWN * 0.3)
        
        for row in calcs_grid:
            self.play(Write(row), run_time=0.6)
            self.wait(0.2)
        self.wait(0.5)

        # 結果の行列
        result_matrix = MathTex(
            r"L = \begin{pmatrix} 0 & 2 & 0 \\ 0 & 0 & 4 \\ 0 & 0 & 0 \end{pmatrix}",
            color=GREEN, font_size=32
        )
        result_matrix.shift(DOWN * 2.5)
        result_matrix_box = SurroundingRectangle(result_matrix, color=GREEN, buff=0.2)
        self.play(Write(result_matrix), Create(result_matrix_box), run_time=0.8)
        self.wait(1.0)

        self.play(
            FadeOut(formula_recall), FadeOut(calc_title), FadeOut(calcs_grid),
            FadeOut(result_matrix), FadeOut(result_matrix_box),
            FadeOut(subtitle9)
        )
        self.wait(0.3)

        # === Part 10: 前回の結果との比較 ===
        subtitle10 = Text("前回の結果との一致を確認", font_size=30, color=GOLD)
        subtitle10.next_to(title, DOWN)
        self.play(Write(subtitle10), run_time=0.6)
        self.wait(0.5)

        # 並べて比較
        compare_title = Text("2つの方法で同じ結果！", color=YELLOW, font_size=26, weight=BOLD)
        compare_title.shift(UP * 1.6)
        self.play(Write(compare_title), run_time=0.6)
        self.wait(0.4)

        # 左: 前回（発見的）
        prev_side = VGroup(
            Text("発見的方法（前回）", color=BLUE, font_size=22, weight=BOLD),
            Text("個別に計算して求めた", color=GRAY, font_size=18),
            MathTex(
                r"L = \begin{pmatrix} 0 & 2 & 0 \\ 0 & 0 & 4 \\ 0 & 0 & 0 \end{pmatrix}",
                color=BLUE, font_size=26
            ),
        ).arrange(DOWN, buff=0.25)
        prev_side.shift(LEFT * 3.5 + DOWN * 0.2)

        # 右: 今回（系統的）
        sys_side = VGroup(
            Text("系統的方法（今回）", color=GREEN, font_size=22, weight=BOLD),
            Text("単位の分解から導出", color=GRAY, font_size=18),
            MathTex(
                r"L = \begin{pmatrix} 0 & 2 & 0 \\ 0 & 0 & 4 \\ 0 & 0 & 0 \end{pmatrix}",
                color=GREEN, font_size=26
            ),
        ).arrange(DOWN, buff=0.25)
        sys_side.shift(RIGHT * 3.5 + DOWN * 0.2)

        # 仕切り線
        divider = DashedLine(UP * 1.0, DOWN * 2.0, color=GRAY, stroke_width=2)

        self.play(Write(prev_side), run_time=0.8)
        self.play(Create(divider), run_time=0.3)
        self.play(Write(sys_side), run_time=0.8)
        self.wait(0.6)

        # イコール
        eq_symbol = MathTex(r"=", color=YELLOW, font_size=50)
        eq_symbol.shift(DOWN * 1.0)
        self.play(Write(eq_symbol), run_time=0.5)
        self.wait(0.5)

        # 強調
        match_note = Text("完全に一致！", color=YELLOW, font_size=28, weight=BOLD)
        match_note.shift(DOWN * 2.5)
        match_box = SurroundingRectangle(match_note, color=YELLOW, buff=0.15)
        self.play(Write(match_note), Create(match_box), run_time=0.6)
        self.wait(1.2)

        self.play(
            FadeOut(compare_title), FadeOut(prev_side), FadeOut(sys_side),
            FadeOut(divider), FadeOut(eq_symbol),
            FadeOut(match_note), FadeOut(match_box),
            FadeOut(subtitle10)
        )
        self.wait(0.3)

        # === Part 11: 系統的方法の利点 ===
        subtitle11 = Text("系統的方法の利点", font_size=30, color=TEAL)
        subtitle11.next_to(title, DOWN)
        self.play(Write(subtitle11), run_time=0.6)
        self.wait(0.5)

        # 利点
        advantages = VGroup(
            VGroup(
                Text("✓", color=GREEN, font_size=26),
                Text("任意の次数に拡張可能", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("✓", color=GREEN, font_size=26),
                Text("微分以外の作用素にも適用可能", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("✓", color=GREEN, font_size=26),
                Text("公式から機械的に計算できる", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("✓", color=GREEN, font_size=26),
                Text("量子力学の定式化と同じ考え方", color=YELLOW, font_size=24, weight=BOLD),
            ).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        advantages.shift(UP * 0.4)
        
        for adv in advantages:
            self.play(Write(adv), run_time=0.6)
            self.wait(0.3)
        self.wait(0.5)

        # 強調
        key_insight = VGroup(
            Text("鍵となるアイデア:", color=ORANGE, font_size=24, weight=BOLD),
            Text("「単位の分解」で作用素を基底で展開", color=ORANGE, font_size=24),
        ).arrange(DOWN, buff=0.15)
        key_insight.shift(DOWN * 1.8)
        key_box = SurroundingRectangle(key_insight, color=ORANGE, buff=0.2)
        self.play(Write(key_insight), Create(key_box), run_time=0.8)
        self.wait(1.2)

        self.play(
            FadeOut(advantages), FadeOut(key_insight), FadeOut(key_box),
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
                Text("1.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("内積公式をブラケット表記で整理:", color=WHITE, font_size=22),
                    MathTex(r"\alpha_n \langle n | m \rangle = \delta_{nm}", color=TEAL, font_size=22),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("2.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("エルミート多項式の微分公式:", color=WHITE, font_size=22),
                    MathTex(r"\frac{d}{dx}|n\rangle = 2n|n-1\rangle", color=YELLOW, font_size=22),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("3.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("単位の分解で作用素を展開:", color=WHITE, font_size=22),
                    MathTex(r"\mathcal{L} = \sum_{n,m} \alpha_m |m\rangle \langle m|\mathcal{L}|n\rangle \alpha_n \langle n|", color=GREEN, font_size=20),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("4.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("行列要素が系統的に求まる:", color=WHITE, font_size=22),
                    MathTex(r"L_{mn} = 2n \, \delta_{m,n-1}", color=RED, font_size=22),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        summary.scale(0.9)
        summary.shift(UP * 0.2)

        for point in summary:
            self.play(Write(point), run_time=0.7)
            self.wait(0.4)

        self.wait(1.5)

        all_final = VGroup(summary, subtitle_end, title)
        self.play(FadeOut(all_final), run_time=1.0)
        self.wait(0.5)
