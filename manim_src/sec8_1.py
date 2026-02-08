from manim import *

class PolynomialBasisChoice(Scene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"
        
        # タイトル
        title = Text("多項式空間における基底のとり方", font_size=40, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)
        
        # === イントロ ===
        intro_text = VGroup(
            Text("ベクトル空間には様々な基底のとり方がある", color=WHITE, font_size=32, weight=BOLD),
            Text("多項式でも同様に基底を選べる!", color=YELLOW, font_size=26),
        ).arrange(DOWN, buff=0.4)
        intro_text.shift(DOWN * 0.5)
        
        self.play(Write(intro_text), run_time=1.2)
        self.wait(1.5)
        
        self.play(FadeOut(intro_text))
        self.wait(0.3)
        
        # === パート1: 具体例の多項式 ===
        subtitle1 = Text("具体例: 2次多項式", font_size=32, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.5)
        
        # 例の多項式
        example_poly = MathTex(
            r"f(x) = 7 + 4x + 6x^2",
            color=YELLOW, font_size=44
        )
        example_poly.shift(UP * 1.5)
        example_box = SurroundingRectangle(example_poly, color=YELLOW, buff=0.25)
        
        self.play(Write(example_poly), Create(example_box), run_time=1.0)
        self.wait(1.0)
        
        # この多項式を様々な基底で表現してみる
        question_text = Text(
            "この多項式を異なる基底で表現してみよう",
            color=WHITE, font_size=28, slant=ITALIC
        )
        question_text.next_to(example_box, DOWN, buff=0.6)
        self.play(Write(question_text), run_time=0.8)
        self.wait(1.0)
        
        self.play(FadeOut(question_text))
        self.wait(0.3)
        
        # === パート2: 標準的な基底 ===
        subtitle2 = Text("方法1: 標準的な基底", font_size=32, color=GREEN)
        subtitle2.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle2), run_time=0.6)
        self.wait(0.5)
        
        # 標準基底の説明
        basis1_label = Text("基底:", color=WHITE, font_size=28, weight=BOLD)
        basis1_label.shift(UP * 0.2 + LEFT * 4)
        self.play(Write(basis1_label), run_time=0.5)
        self.wait(0.3)
        
        # 基底ベクトル（ケット記法で）
        basis1_vectors = MathTex(
            r"|1\rangle, \quad |x\rangle, \quad |x^2\rangle",
            color=GREEN, font_size=36
        )
        basis1_vectors.next_to(basis1_label, RIGHT, buff=0.5)
        self.play(Write(basis1_vectors), run_time=0.9)
        self.wait(0.8)
        
        # 多項式の表現
        repr1_text = Text("多項式の表現:", color=WHITE, font_size=26, weight=BOLD)
        repr1_text.shift(DOWN * 0.5 + LEFT * 4)
        self.play(Write(repr1_text), run_time=0.5)
        self.wait(0.3)
        
        repr1_formula = MathTex(
            r"f(x) = 7|1\rangle + 4|x\rangle + 6|x^2\rangle",
            color=GREEN, font_size=32
        )
        repr1_formula.next_to(repr1_text, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(repr1_formula), run_time=1.0)
        self.wait(0.8)
        
        # 係数ベクトル
        coeff1_label = Text("係数ベクトル:", color=WHITE, font_size=26, weight=BOLD)
        coeff1_label.shift(DOWN * 1.8 + LEFT * 4)
        self.play(Write(coeff1_label), run_time=0.5)
        self.wait(0.3)
        
        coeff1_vector = MathTex(
            r"\begin{bmatrix} 7 \\ 4 \\ 6 \end{bmatrix}",
            color=GREEN, font_size=36
        )
        coeff1_vector.next_to(coeff1_label, RIGHT, buff=0.5).shift(DOWN * 0.7)
        self.play(Write(coeff1_vector), run_time=0.7)
        self.wait(1.0)
        
        # シンプルであることを強調
        simple_note = Text(
            "✓ 最もシンプルで直感的!",
            color=YELLOW, font_size=24, weight=BOLD
        )
        simple_note.shift(DOWN * 2.8 + RIGHT * 1.5)
        self.play(Write(simple_note), run_time=0.7)
        self.wait(1.2)
        
        self.play(
            FadeOut(basis1_label), FadeOut(basis1_vectors),
            FadeOut(repr1_text), FadeOut(repr1_formula),
            FadeOut(coeff1_label), FadeOut(coeff1_vector),
            FadeOut(simple_note)
        )
        self.wait(0.3)
        
        # === パート3: 別の基底 ===
        subtitle3 = Text("方法2: 別の基底を選ぶ", font_size=32, color=PURPLE)
        subtitle3.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle3), run_time=0.6)
        self.wait(0.5)
        
        # 別の基底
        basis2_label = Text("基底:", color=WHITE, font_size=28, weight=BOLD)
        basis2_label.shift(UP * 0.2 + LEFT * 4)
        self.play(Write(basis2_label), run_time=0.5)
        self.wait(0.3)
        
        basis2_vectors = MathTex(
            r"|1\rangle, \quad |3+x\rangle, \quad |3+x+x^2\rangle",
            color=PURPLE, font_size=32
        )
        basis2_vectors.next_to(basis2_label, RIGHT, buff=0.5)
        self.play(Write(basis2_vectors), run_time=0.9)
        self.wait(0.8)
        
        # この基底でも表現可能
        repr2_text = Text("この基底でも表現可能!", color=WHITE, font_size=26, weight=BOLD)
        repr2_text.shift(DOWN * 0.5 + LEFT * 4)
        self.play(Write(repr2_text), run_time=0.5)
        self.wait(0.3)
        
        # 計算過程を示す
        calc_label = Text("計算してみよう:", color=YELLOW, font_size=24, slant=ITALIC)
        calc_label.shift(DOWN * 1.0 + LEFT * 4)
        self.play(Write(calc_label), run_time=0.5)
        self.wait(0.3)
        
        # a|1> + b|3+x> + c|3+x+x^2> = 7 + 4x + 6x^2
        calc_eq = MathTex(
            r"a|1\rangle + b|3+x\rangle + c|3+x+x^2\rangle",
            color=WHITE, font_size=28
        )
        calc_eq.shift(DOWN)
        self.play(Write(calc_eq), run_time=0.8)
        self.wait(0.5)
        
        # 展開
        calc_expand = MathTex(
            r"= a + b(3+x) + c(3+x+x^2)",
            color=WHITE, font_size=28
        )
        calc_expand.next_to(calc_eq, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(calc_expand), run_time=0.8)
        self.wait(0.5)
        
        calc_expand2 = MathTex(
            r"= (a+3b+3c) + (b+c)x + cx^2",
            color=WHITE, font_size=28
        )
        calc_expand2.next_to(calc_expand, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(calc_expand2), run_time=0.8)
        self.wait(0.8)
        
        # 係数比較
        compare_text = Text("係数を比較:", color=YELLOW, font_size=24, weight=BOLD)
        compare_text.shift(DOWN * 2.8 + LEFT * 4.5)
        self.play(Write(compare_text), run_time=0.5)
        self.wait(0.3)
        
        system_eqs = MathTex(
            r"a + 3b + 3c &= 7 \\",
            r"b + c &= 4 \\",
            r"c &= 6",
            color=ORANGE, font_size=26
        )
        system_eqs.shift(DOWN * 3.0 + RIGHT * 0.5)
        self.play(Write(system_eqs), run_time=1.0)
        self.wait(0.8)
        
        # 解
        solution_arrow = Arrow(
            system_eqs.get_right() + RIGHT * 0.2,
            system_eqs.get_right() + RIGHT * 1.5,
            color=YELLOW, buff=0.05, stroke_width=4
        )
        solution_text = MathTex(
            r"c=6, b=-2, a=1",
            color=GREEN, font_size=26
        )
        solution_text.next_to(solution_arrow, RIGHT, buff=0.1)
        
        self.play(Create(solution_arrow), Write(solution_text), run_time=0.8)
        self.wait(1.0)
        
        self.play(
            FadeOut(basis2_label), FadeOut(basis2_vectors),
            FadeOut(repr2_text), FadeOut(calc_label),
            FadeOut(calc_eq), FadeOut(calc_expand), FadeOut(calc_expand2),
            FadeOut(compare_text), FadeOut(system_eqs),
            FadeOut(solution_arrow), FadeOut(solution_text)
        )
        self.wait(0.3)
        
        # 結果を表示
        result2_label = Text("結果:", color=WHITE, font_size=28, weight=BOLD)
        result2_label.shift(UP * 0.5 + LEFT * 4)
        self.play(Write(result2_label), run_time=0.5)
        self.wait(0.3)
        
        repr2_formula = MathTex(
            r"f(x) = 1|1\rangle - 2|3+x\rangle + 6|3+x+x^2\rangle",
            color=PURPLE, font_size=32
        )
        repr2_formula.next_to(result2_label, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(repr2_formula), run_time=1.0)
        self.wait(0.8)
        
        coeff2_label = Text("係数ベクトル:", color=WHITE, font_size=26, weight=BOLD)
        coeff2_label.shift(DOWN * 1.5 + LEFT * 4)
        self.play(Write(coeff2_label), run_time=0.5)
        self.wait(0.3)
        
        coeff2_vector = MathTex(
            r"\begin{bmatrix} 1 \\ -2 \\ 6 \end{bmatrix}",
            color=PURPLE, font_size=36
        )
        coeff2_vector.next_to(coeff2_label, RIGHT, buff=0.5)
        self.play(Write(coeff2_vector), run_time=0.7)
        self.wait(1.0)
        
        # 基底が異なると係数も変わる
        different_note = Text(
            "✓【復習】基底が異なれば係数も変わる!",
            color=YELLOW, font_size=24, weight=BOLD
        )
        different_note.shift(DOWN * 2.0 + RIGHT * 1.8)
        self.play(Write(different_note), run_time=0.7)
        self.wait(1.2)
        
        self.play(
            FadeOut(result2_label), FadeOut(repr2_formula),
            FadeOut(coeff2_label), FadeOut(coeff2_vector),
            FadeOut(different_note)
        )
        self.wait(0.3)
        
        # === パート4: 冗長な基底（1次従属） ===
        subtitle4 = Text("方法3: 冗長な生成元の集合", font_size=32, color=RED)
        subtitle4.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle4), run_time=0.6)
        self.wait(0.5)
        
        # 冗長な基底セット
        basis3_label = Text("生成元:", color=WHITE, font_size=28, weight=BOLD)
        basis3_label.shift(UP * 0.8 + LEFT * 4)
        self.play(Write(basis3_label), run_time=0.5)
        self.wait(0.3)
        
        basis3_vectors = MathTex(
            r"|1\rangle, \quad |3+x\rangle, \quad |3+x\rangle, |3+x+x^2\rangle, \quad |x^2\rangle",
            color=RED, font_size=28
        )
        basis3_vectors.next_to(basis3_label, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(basis3_vectors), run_time=1.0)
        self.wait(0.8)
        
        # 5つある（多すぎる）
        count_note = Text(
            "5つの生成元がある（2次多項式なのに！）",
            color=ORANGE, font_size=24, slant=ITALIC
        )
        count_note.next_to(basis3_vectors, DOWN, buff=0.4)
        self.play(Write(count_note), run_time=0.8)
        self.wait(0.8)
        
        # 冗長性の指摘
        redundancy_label = Text("冗長性:", color=YELLOW, font_size=26, weight=BOLD)
        redundancy_label.shift(DOWN + LEFT * 4)
        self.play(Write(redundancy_label), run_time=0.5)
        self.wait(0.3)
        
        # |3+x>が2回登場
        redundancy1_math = MathTex(
            r"|3+x\rangle",
            color=ORANGE, font_size=26
        )
        redundancy1_text = Text(" が2回登場", color=ORANGE, font_size=26)
        redundancy1 = VGroup(redundancy1_math, redundancy1_text).arrange(RIGHT, buff=0.1)
        redundancy1.shift(DOWN *1.1 + LEFT * 1)
        self.play(Write(redundancy1), run_time=0.7)
        self.wait(0.5)
        
        # |3+x+x^2>は|3+x>と|x^2>で作れる
        redundancy2 = MathTex(
            r"|3+x+x^2\rangle = |3+x\rangle + |x^2\rangle",
            color=ORANGE, font_size=26
        )
        redundancy2.next_to(redundancy1, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(redundancy2), run_time=0.8)
        self.wait(0.8)
        
        # 無駄がある
        waste_note = Text(
            "→ 無駄がある（1次従属）",
            color=RED, font_size=26, weight=BOLD
        )
        waste_note.next_to(redundancy2, DOWN, buff=0.4)
        self.play(Write(waste_note), run_time=0.7)
        self.wait(1.0)
        
        # この集合でも表現は可能だが...
        can_represent = Text(
            "この生成元でも f(x) は表現できるが、効率が悪い",
            color=WHITE, font_size=24, slant=ITALIC
        )
        can_represent.shift(DOWN * 3.2)
        self.play(Write(can_represent), run_time=0.8)
        self.wait(1.2)
        
        self.play(
            FadeOut(basis3_label), FadeOut(basis3_vectors), FadeOut(count_note),
            FadeOut(redundancy_label), FadeOut(redundancy1), FadeOut(redundancy2),
            FadeOut(waste_note), FadeOut(can_represent), 
            FadeOut(example_poly), FadeOut(example_box)
        )
        self.wait(0.3)
        
        # === パート5: 1次独立と1次従属 ===
        subtitle5 = Text("1次独立と1次従属(復習)", font_size=32, color=TEAL)
        subtitle5.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle5), run_time=0.6)
        self.wait(0.5)
        
        # 定義
        indep_def_label = Text("1次独立:", color=GREEN, font_size=28, weight=BOLD)
        indep_def_label.shift(UP * 1.5 + LEFT * 4)
        self.play(Write(indep_def_label), run_time=0.5)
        self.wait(0.3)
        
        indep_def = Text(
            "どのベクトルも他のベクトルの線形結合で表せない",
            color=WHITE, font_size=24
        )
        indep_def.next_to(indep_def_label, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(indep_def), run_time=0.9)
        self.wait(0.8)
        
        dep_def_label = Text("1次従属:", color=RED, font_size=28, weight=BOLD)
        dep_def_label.shift(UP * 0.2 + LEFT * 4)
        self.play(Write(dep_def_label), run_time=0.5)
        self.wait(0.3)
        
        dep_def = Text(
            "少なくとも1つのベクトルが他のベクトルで表せる",
            color=WHITE, font_size=24
        )
        dep_def.next_to(dep_def_label, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(Write(dep_def), run_time=0.9)
        self.wait(0.8)
        
        # 具体例
        example_label = Text("例:", color=YELLOW, font_size=26, weight=BOLD)
        example_label.shift(DOWN * 1.2 + LEFT * 4)
        self.play(Write(example_label), run_time=0.5)
        self.wait(0.3)
        
        # 1次独立の例
        indep_example_math = MathTex(
            r"|1\rangle, |x\rangle, |x^2\rangle",
            color=GREEN, font_size=26
        )
        indep_example_text = Text(" は1次独立", color=GREEN, font_size=26)
        indep_example = VGroup(indep_example_math, indep_example_text).arrange(RIGHT, buff=0.2)
        indep_example.shift(DOWN * 1.1 + LEFT * 0.5)
        self.play(Write(indep_example), run_time=0.8)
        self.wait(0.6)
        
        # もう一つの1次独立の例
        indep_example2_math = MathTex(
            r"|1\rangle, |3+x\rangle, |3+x+x^2\rangle",
            color=GREEN, font_size=26
        )
        indep_example2_text = Text(" も1次独立", color=GREEN, font_size=26)
        indep_example2 = VGroup(indep_example2_math, indep_example2_text).arrange(RIGHT, buff=0.2)
        indep_example2.next_to(indep_example, DOWN, buff=0.25, aligned_edge=LEFT)
        self.play(Write(indep_example2), run_time=0.8)
        self.wait(0.6)
        
        # 注意書き
        note_independent = Text(
            "（|3+x+x^2>と|3+x>は互いに表現不可→独立!）",
            color=YELLOW, font_size=20, slant=ITALIC
        )
        note_independent.next_to(indep_example2, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(note_independent), run_time=0.8)
        self.wait(0.8)
        
        # 1次従属の例
        dep_example = MathTex(
            r"|1\rangle, |3+x\rangle, |3+x\rangle, |3+x+x^2\rangle, |x^2\rangle",
            color=RED, font_size=22
        )
        dep_example.shift(DOWN * 3.2 + LEFT * 0.2)
        dep_label = Text("は1次従属", color=RED, font_size=22)
        dep_label.next_to(dep_example, RIGHT, buff=0.2)
        
        self.play(Write(dep_example), Write(dep_label), run_time=0.9)
        self.wait(1.0)
        
        self.play(
            FadeOut(indep_def_label), FadeOut(indep_def),
            FadeOut(dep_def_label), FadeOut(dep_def),
            FadeOut(example_label), FadeOut(indep_example), FadeOut(indep_example2),
            FadeOut(note_independent), FadeOut(dep_example), FadeOut(dep_label)
        )
        self.wait(0.3)
        
        # === パート6: 次元と基底の関係 ===
        subtitle6 = Text("次元と基底の関係", font_size=32, color=ORANGE)
        subtitle6.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle6), run_time=0.6)
        self.wait(0.5)
        
        # 次数と次元の関係
        dim_relation_label = Text("重要な関係:", color=YELLOW, font_size=28, weight=BOLD)
        dim_relation_label.shift(UP * 1.5)
        self.play(Write(dim_relation_label), run_time=0.5)
        self.wait(0.3)
        
        dim_formula_text1 = Text("N次多項式の空間", color=ORANGE, font_size=32)
        dim_formula_arrow = MathTex(r"\Rightarrow", color=ORANGE, font_size=36)
        dim_formula_text2 = Text("次元", color=ORANGE, font_size=32)
        dim_formula_eq = MathTex(r"= N+1", color=ORANGE, font_size=36)
        dim_formula = VGroup(
            dim_formula_text1, dim_formula_arrow, dim_formula_text2, dim_formula_eq
        ).arrange(RIGHT, buff=0.3)
        dim_formula.shift(UP * 0.7)
        dim_box = SurroundingRectangle(dim_formula, color=ORANGE, buff=0.25)
        
        self.play(Write(dim_formula), Create(dim_box), run_time=1.0)
        self.wait(1.0)
        
        # 基底の数
        basis_count_label = Text("基底の数:", color=WHITE, font_size=28, weight=BOLD)
        basis_count_label.shift(DOWN * 0.2)
        self.play(Write(basis_count_label), run_time=0.5)
        self.wait(0.3)
        
        basis_count_text1 = Text("次元", color=GREEN, font_size=28)
        basis_count_eq1 = MathTex(r"=", color=GREEN, font_size=32)
        basis_count_text2 = Text("基底の個数", color=GREEN, font_size=28)
        basis_count_eq2 = MathTex(r"= N+1", color=GREEN, font_size=32)
        basis_count_text = VGroup(
            basis_count_text1, basis_count_eq1, basis_count_text2, basis_count_eq2
        ).arrange(RIGHT, buff=0.3)
        basis_count_text.next_to(basis_count_label, DOWN, buff=0.4)
        basis_count_box = SurroundingRectangle(basis_count_text, color=GREEN, buff=0.25)
        
        self.play(Write(basis_count_text), Create(basis_count_box), run_time=1.0)
        self.wait(1.0)
        
        # 具体例
        concrete_label = Text("2次多項式の例:", color=YELLOW, font_size=26, weight=BOLD)
        concrete_label.shift(DOWN * 1.7)
        self.play(Write(concrete_label), run_time=0.5)
        self.wait(0.3)
        
        concrete_text = VGroup(
            Text("次数 N = 2", color=WHITE, font_size=24),
            Text("→ 次元 = 3", color=BLUE, font_size=24),
            Text("→ 基底は3個必要", color=GREEN, font_size=24),
        ).arrange(RIGHT, buff=0.5)
        concrete_text.next_to(concrete_label, DOWN, buff=0.4)
        
        self.play(Write(concrete_text), run_time=1.0)
        self.wait(1.2)
        
        # 確認
        # check_text = Text(
        #     "✓ |1>, |x>, |x^2> → 3個（OK!）",
        #     color=GREEN, font_size=24, weight=BOLD
        # )
        # check_text.shift(DOWN * 2.8 + LEFT * 2)
        # self.play(Write(check_text), run_time=0.7)
        # self.wait(0.5)
        
        # check_text2 = Text(
        #     "✓ |1>, |3+x>, |3+x+x^2> → 3個（OK!）",
        #     color=GREEN, font_size=24, weight=BOLD
        # )
        # check_text2.next_to(check_text, DOWN, buff=0.2, aligned_edge=LEFT)
        # self.play(Write(check_text2), run_time=0.7)
        # self.wait(0.5)
        
        # check_text3 = Text(
        #     "✗ |1>, |3+x>, |3+x>, |3+x+x^2>, |x^2> → 5個（多すぎる!）",
        #     color=RED, font_size=24, weight=BOLD
        # )
        # check_text3.next_to(check_text2, DOWN, buff=0.2, aligned_edge=LEFT)
        # self.play(Write(check_text3), run_time=0.7)
        # self.wait(1.2)
        
        self.play(
            FadeOut(dim_relation_label), FadeOut(dim_formula), FadeOut(dim_box),
            FadeOut(basis_count_label), FadeOut(basis_count_text), FadeOut(basis_count_box),
            FadeOut(concrete_label), FadeOut(concrete_text),
            # FadeOut(check_text), FadeOut(check_text2), FadeOut(check_text3),
            FadeOut(subtitle1)
        )
        self.wait(0.3)
        
        # === まとめ ===
        summary_subtitle = Text("まとめ", font_size=32, color=GOLD, weight=BOLD)
        summary_subtitle.next_to(title, DOWN)
        self.play(Write(summary_subtitle), run_time=0.6)
        self.wait(0.5)
        
        # まとめのポイント
        summary_points = VGroup(
            VGroup(
                Text("1.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("同じ多項式でも異なる基底で", color=WHITE, font_size=24),
                    Text("様々に表現できる", color=YELLOW, font_size=24, weight=BOLD),
                ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            
            VGroup(
                Text("2.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("1次独立: 互いに表現できない", color=WHITE, font_size=24),
                    Text("1次従属: 冗長性がある", color=RED, font_size=24, weight=BOLD),
                ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            
            VGroup(
                Text("3.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("見た目が似ていても、互いに表現不可なら", color=WHITE, font_size=24),
                    Text("1次独立（|3+x+x^2>と|3+x>など）", color=GREEN, font_size=24, weight=BOLD),
                ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            
            VGroup(
                Text("4.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("N次多項式の空間の次元 = N+1", color=WHITE, font_size=24),
                    Text("→ 基底は必ずN+1個", color=ORANGE, font_size=24, weight=BOLD),
                ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        summary_points.scale(0.92)
        summary_points.shift(UP * 0.1)
        
        for point in summary_points:
            self.play(Write(point), run_time=0.9)
            self.wait(0.6)
        
        self.wait(1.5)
        
        # 最終メッセージ
        final_message = Text(
            "基底の選び方は自由だが、次元で個数が決まる!",
            color=YELLOW, font_size=28, weight=BOLD, slant=ITALIC
        )
        final_message.shift(DOWN * 2.5)
        final_box = SurroundingRectangle(final_message, color=YELLOW, buff=0.25)
        self.play(Write(final_message), Create(final_box), run_time=1.0)
        self.wait(2.0)
        
        # フェードアウト
        all_objects = VGroup(
            title, summary_subtitle, summary_points,
            final_message, final_box
        )
        self.play(FadeOut(all_objects), run_time=1.0)
        self.wait(0.5)
