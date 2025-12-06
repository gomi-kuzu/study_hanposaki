from manim import *

class InnerProductIntro(ThreeDScene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"
        
        # タイトル
        title = Text("ベクトルの内積", font_size=44, color=WHITE)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)
        
        # === パート1: 内積の導入 ===
        subtitle1 = Text("ベクトル同士の関係を表す方法", font_size=32, color=YELLOW)
        subtitle1.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle1)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.5)
        
        # 2つのベクトルを視覚的に表示
        axes = Axes(
            x_range=[-1, 4, 1],
            y_range=[-1, 4, 1],
            x_length=4,
            y_length=4,
            axis_config={"color": GRAY}
        )
        axes.shift(LEFT * 3.5)
        self.add_fixed_in_frame_mobjects(axes)
        
        # 方眼を追加
        grid = NumberPlane(
            x_range=[-1, 4, 1],
            y_range=[-1, 4, 1],
            x_length=4,
            y_length=4,
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            },
            axis_config={"stroke_opacity": 0}
        )
        grid.shift(LEFT * 3.5)
        self.add_fixed_in_frame_mobjects(grid)
        
        self.play(Create(grid), Create(axes), run_time=0.7)
        self.wait(0.4)
        
        # ベクトルa1
        a1 = Vector(
            axes.c2p(3, 1) - axes.c2p(0, 0),
            color=BLUE,
            stroke_width=6
        ).shift(axes.c2p(0, 0))
        self.add_fixed_in_frame_mobjects(a1)
        
        a1_label = MathTex(r"\mathbf{a}_1", color=BLUE, font_size=28)
        a1_label.next_to(a1.get_end(), RIGHT, buff=0.2)
        self.add_fixed_in_frame_mobjects(a1_label)
        
        # ベクトルa2
        a2 = Vector(
            axes.c2p(1, 3) - axes.c2p(0, 0),
            color=RED,
            stroke_width=6
        ).shift(axes.c2p(0, 0))
        self.add_fixed_in_frame_mobjects(a2)
        
        a2_label = MathTex(r"\mathbf{a}_2", color=RED, font_size=28)
        a2_label.next_to(a2.get_end(), UP, buff=0.2)
        self.add_fixed_in_frame_mobjects(a2_label)
        
        self.play(Create(a1), Write(a1_label), run_time=0.7)
        self.wait(0.3)
        self.play(Create(a2), Write(a2_label), run_time=0.7)
        self.wait(0.5)
        
        # 説明テキスト
        explanation1 = VGroup(
            Text("2つのベクトルがあるとき", color=WHITE, font_size=26),
            Text("その関係を数値で表したい", color=YELLOW, font_size=26),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        explanation1.to_edge(RIGHT).shift(LEFT * 1.5 + UP * 1.5)
        self.add_fixed_in_frame_mobjects(explanation1)
        
        self.play(Write(explanation1), run_time=0.8)
        self.wait(0.5)
        
        # 内積の紹介
        inner_product_intro = Text("そこで登場するのが「内積」", 
                                   color=GREEN, font_size=28, weight=BOLD)
        inner_product_intro.to_edge(RIGHT).shift(LEFT * 1.5 + UP * 0.3)
        self.add_fixed_in_frame_mobjects(inner_product_intro)
        self.play(Write(inner_product_intro), run_time=0.7)
        self.wait(1.0)
        
        self.play(
            FadeOut(explanation1), 
            FadeOut(inner_product_intro), 
            FadeOut(subtitle1)
        )
        self.wait(0.3)
        
        # === パート2: 内積の定義 ===
        subtitle2 = Text("内積とは？", font_size=32, color=BLUE)
        subtitle2.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle2)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)
        
        # 内積の説明
        definition_text = VGroup(
            Text("内積は2つのベクトルを受け取り", color=WHITE, font_size=26),
            Text("スカラ値（数値）を返す関数", color=YELLOW, font_size=26),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        definition_text.to_edge(RIGHT).shift(LEFT * 1.5 + UP * 1.8)
        self.add_fixed_in_frame_mobjects(definition_text)
        
        self.play(Write(definition_text), run_time=0.8)
        self.wait(0.5)
        
        # 最も有名な定義を表示
        famous_def_title = Text("最も有名な定義:", color=ORANGE, font_size=28, weight=BOLD)
        famous_def_title.to_edge(RIGHT).shift(LEFT * 1.5 + UP * 0.8)
        self.add_fixed_in_frame_mobjects(famous_def_title)
        self.play(Write(famous_def_title), run_time=0.6)
        self.wait(0.4)
        
        # 具体例を示す
        vector_example = VGroup(
            MathTex(r"\mathbf{a}_1 = \begin{bmatrix} a_{11} \\ a_{12} \\ \vdots \\ a_{1n} \end{bmatrix}", 
                   color=BLUE, font_size=24),
            MathTex(r"\mathbf{a}_2 = \begin{bmatrix} a_{21} \\ a_{22} \\ \vdots \\ a_{2n} \end{bmatrix}", 
                   color=RED, font_size=24),
        ).arrange(RIGHT, buff=0.5)
        vector_example.to_edge(RIGHT).shift(LEFT * 1.5 + DOWN * 0.5)
        self.add_fixed_in_frame_mobjects(vector_example)
        self.play(Write(vector_example), run_time=0.8)
        self.wait(0.5)
        
        # 内積の式
        inner_product_text = Text("内積", color=GREEN, font_size=28)
        inner_product_eq = MathTex(r"=", color=GREEN, font_size=28)
        inner_product_math = MathTex(
            r"\sum_{i=1}^{n} a_{1i} \cdot a_{2i}",
            color=GREEN, font_size=28
        )
        inner_product_formula = VGroup(inner_product_text, inner_product_eq, inner_product_math).arrange(RIGHT, buff=0.2)
        inner_product_formula.to_edge(RIGHT).shift(LEFT * 1.5 + DOWN * 2)
        self.add_fixed_in_frame_mobjects(inner_product_formula)
        self.play(Write(inner_product_formula), run_time=0.8)
        self.wait(0.5)
        
        # 具体的な計算例
        calculation_text = Text("要素同士の積を全て足し合わせる", 
                               color=YELLOW, font_size=24)
        calculation_text.to_edge(RIGHT).shift(LEFT * 1.5 + DOWN * 3)
        self.add_fixed_in_frame_mobjects(calculation_text)
        self.play(Write(calculation_text), run_time=0.7)
        self.wait(1.0)
        
        # 実例を示す（左側のベクトルを使って）
        # concrete_example = MathTex(
        #     r"\mathbf{a}_1 = \begin{bmatrix} 3 \\ 1 \end{bmatrix}, \quad "
        #     r"\mathbf{a}_2 = \begin{bmatrix} 1 \\ 3 \end{bmatrix}",
        #     color=WHITE, font_size=24
        # )
        # concrete_example.to_edge(RIGHT).shift(LEFT * 1.5 + DOWN * 2.2)
        # self.add_fixed_in_frame_mobjects(concrete_example)
        # self.play(Write(concrete_example), run_time=0.7)
        # self.wait(0.3)
        
        # concrete_result_text = Text("内積", color=GREEN, font_size=26)
        # concrete_result_eq = MathTex(r"=", color=GREEN, font_size=26)
        # concrete_result_math = MathTex(
        #     r"3 \times 1 + 1 \times 3 = 6",
        #     color=GREEN, font_size=26
        # )
        # concrete_result = VGroup(concrete_result_text, concrete_result_eq, concrete_result_math).arrange(RIGHT, buff=0.2)
        # concrete_result.to_edge(RIGHT).shift(LEFT * 1.5 + DOWN * 2.8)
        # self.add_fixed_in_frame_mobjects(concrete_result)
        # self.play(Write(concrete_result), run_time=0.8)
        # self.wait(1.2)
        
        self.play(
            FadeOut(definition_text), FadeOut(famous_def_title),
            FadeOut(vector_example), FadeOut(inner_product_formula),
            FadeOut(calculation_text), FadeOut(subtitle2)
        )
        self.wait(0.3)
        
        # === パート3: 内積の表記法 ===
        subtitle3 = Text("内積の様々な書き方", font_size=32, color=PURPLE)
        subtitle3.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle3)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.5)
        
        # notation_intro = Text("内積には多様な表記法がある", 
        #                      color=WHITE, font_size=26)
        # notation_intro.to_edge(RIGHT).shift(LEFT * 1.5 + UP * 2.0)
        # self.add_fixed_in_frame_mobjects(notation_intro)
        # self.play(Write(notation_intro), run_time=0.6)
        # self.wait(0.5)
        
        # 各種表記法を順に表示
        notations = VGroup(
            VGroup(
                Text("1. ドット表記", color=BLUE, font_size=24),
                MathTex(r"\mathbf{a}_1 \cdot \mathbf{a}_2", color=BLUE, font_size=28)
            ).arrange(DOWN, buff=0.2),
            VGroup(
                Text("2. 関数表記", color=GREEN, font_size=24),
                MathTex(r"(\mathbf{a}_1, \mathbf{a}_2)", color=GREEN, font_size=28)
            ).arrange(DOWN, buff=0.2),
            VGroup(
                Text("3. 行列表記", color=ORANGE, font_size=24),
                MathTex(r"\mathbf{a}_1^T \mathbf{a}_2", color=ORANGE, font_size=28)
            ).arrange(DOWN, buff=0.2),
            VGroup(
                Text("4. ブラケット表記", color=RED, font_size=24),
                MathTex(r"\langle \mathbf{a}_1 | \mathbf{a}_2 \rangle", color=RED, font_size=28)
            ).arrange(DOWN, buff=0.2),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        
        notations.to_edge(RIGHT).shift(LEFT * 1.5 + UP * 0.5)
        self.add_fixed_in_frame_mobjects(notations)
        
        # 各表記法をまとめて表示（テンポよく）
        for i, notation in enumerate(notations):
            self.play(Write(notation), run_time=0.5)
            self.wait(0.2)
        
        # すべて同じことを表している強調
        all_same_text = Text("これらは全て同じ内積を表す！", 
                            color=YELLOW, font_size=26, weight=BOLD)
        all_same_text.to_edge(RIGHT).shift(LEFT * 1.5 + DOWN * 2.0)
        self.add_fixed_in_frame_mobjects(all_same_text)
        self.play(Write(all_same_text), run_time=0.7)
        self.wait(0.8)
        
        self.play(
            # FadeOut(notation_intro),
            FadeOut(notations),
            FadeOut(all_same_text), FadeOut(subtitle3)
        )
        self.wait(0.3)
        
        # === パート4: 定義は一つではない ===
        subtitle4 = Text("実は定義も一つではない", font_size=32, color=RED)
        subtitle4.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle4)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.5)
        
        # 説明
        multiple_def_text = VGroup(
            Text("内積の定義は空間の性質に応じて", color=WHITE, font_size=26),
            Text("様々な形をとる", color=WHITE, font_size=26),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        multiple_def_text.to_edge(RIGHT).shift(LEFT * 1.5 + UP * 1.8)
        self.add_fixed_in_frame_mobjects(multiple_def_text)
        
        self.play(Write(multiple_def_text), run_time=0.8)
        self.wait(0.5)
        
        # 例を挙げる
        # examples_title = Text("例：", color=ORANGE, font_size=28, weight=BOLD)
        # examples_title.to_edge(RIGHT).shift(LEFT * 1.5 + UP * 0.8)
        # self.add_fixed_in_frame_mobjects(examples_title)
        # self.play(Write(examples_title), run_time=0.5)
        # self.wait(0.3)
        
        definition_examples = VGroup(
            # VGroup(
            #     Text("• ユークリッド空間", color=BLUE, font_size=24),
            #     MathTex(r"\sum_{i=1}^{n} a_{1i} \cdot a_{2i}", color=BLUE, font_size=22)
            # ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
            VGroup(
                Text("• 重み付き空間", color=GREEN, font_size=24),
                MathTex(r"\sum_{i=1}^{n} w_i \cdot a_{1i} \cdot a_{2i}", color=GREEN, font_size=22)
            ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
            VGroup(
                Text("• 関数空間", color=PURPLE, font_size=24),
                MathTex(r"\int f(x) \cdot g(x) \, dx", color=PURPLE, font_size=22)
            ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        
        definition_examples.to_edge(RIGHT).shift(LEFT * 1.5 + UP * 0.0)
        self.add_fixed_in_frame_mobjects(definition_examples)
        
        for example in definition_examples:
            self.play(Write(example), run_time=0.5)
            self.wait(0.2)
        
        # 重要なポイント
        important_note = VGroup(
            Text("重要：", color=RED, font_size=26, weight=BOLD),
            Text("どの定義も「内積の公理」を", color=WHITE, font_size=24),
            Text("満たしている必要がある", color=WHITE, font_size=24),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        important_note.to_edge(RIGHT).shift(LEFT * 1.5 + DOWN * 1.8)
        self.add_fixed_in_frame_mobjects(important_note)
        
        self.play(Write(important_note), run_time=0.8)
        self.wait(0.8)
        
        self.play(
            FadeOut(multiple_def_text), FadeOut(definition_examples), FadeOut(important_note),
            FadeOut(subtitle4)
        )
        self.wait(0.3)
        
        # 左側のグラフをクリーンアップ
        self.play(
            FadeOut(a1), FadeOut(a1_label),
            FadeOut(a2), FadeOut(a2_label),
            FadeOut(axes), FadeOut(grid)
        )
        self.wait(0.5)
        
        # === パート5: まとめ ===
        subtitle5 = Text("まとめ", font_size=36, color=GREEN)
        subtitle5.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle5)
        self.play(Write(subtitle5), run_time=0.6)
        self.wait(0.5)
        
        summary = VGroup(
            Text("1. 内積はベクトル間の関係を表す", color=WHITE, font_size=28),
            Text("2. 2つのベクトル → スカラ値", color=WHITE, font_size=28),
            Text("3. 表記法は多様（ドット、カッコ、行列…）", color=WHITE, font_size=28),
            Text("4. 定義も空間に応じて様々", color=WHITE, font_size=28),
            Text("5. 共通するのは「内積の公理」", color=WHITE, font_size=28, weight=BOLD),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        summary.shift(DOWN * 0.3)
        self.add_fixed_in_frame_mobjects(summary)
        
        # まとめを一度に表示（テンポよく）
        for item in summary:
            self.play(Write(item), run_time=0.5)
            self.wait(0.3)
        
        self.wait(1.0)
        