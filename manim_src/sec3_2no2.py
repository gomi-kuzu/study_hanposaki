from manim import *

class InnerProductPerspectives(ThreeDScene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"
        
        # タイトル
        title = Text("内積の3つの視点", font_size=40, color=WHITE)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)
        
        # === イントロ: 同じものを違う角度から ===
        intro_subtitle = Text("同じ内積、異なる解釈", font_size=32, color=YELLOW)
        intro_subtitle.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(intro_subtitle)
        self.play(Write(intro_subtitle), run_time=0.6)
        self.wait(0.5)
        
        intro_text = VGroup(
            Text("内積の表記法が違うのは", color=WHITE, font_size=26),
            Text("単なる記法の違いではなく", color=WHITE, font_size=26),
            Text("見方・解釈の違いを反映している", color=YELLOW, font_size=26, weight=BOLD),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        intro_text.shift(DOWN * 0.5)
        self.add_fixed_in_frame_mobjects(intro_text)
        
        self.play(Write(intro_text), run_time=1.0)
        self.wait(1.2)
        
        self.play(FadeOut(intro_text), FadeOut(intro_subtitle))
        self.wait(0.3)
        
        # === パート1: 関数としての内積 ===
        subtitle1 = Text("視点1: 関数としての内積", font_size=32, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle1)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.5)
        
        # 表記
        notation1 = MathTex(
            r"(\mathbf{a}_1, \mathbf{a}_2)",
            color=BLUE, font_size=44
        )
        notation1.shift(UP * 1.5)
        self.add_fixed_in_frame_mobjects(notation1)
        self.play(Write(notation1), run_time=0.7)
        self.wait(0.5)
        
        # 説明
        function_view = VGroup(
            Text("2つのベクトルを受け取り", color=WHITE, font_size=26),
            Text("1つの数値を返す「関数」", color=YELLOW, font_size=26),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        function_view.shift(UP * 0.3)
        self.add_fixed_in_frame_mobjects(function_view)
        self.play(Write(function_view), run_time=0.8)
        self.wait(0.8)
        
        # 図式的表現
        function_diagram = VGroup(
            MathTex(r"\mathbf{a}_1", color=GREEN, font_size=32),
            Text("⟹", color=WHITE, font_size=32),
            MathTex(r"(\cdot, \mathbf{a}_2)", color=BLUE, font_size=28),
            Text("⟹", color=WHITE, font_size=32),
            Text("スカラ値", color=ORANGE, font_size=28),
        ).arrange(RIGHT, buff=0.3)
        function_diagram.shift(DOWN * 1.0)
        self.add_fixed_in_frame_mobjects(function_diagram)
        self.play(Write(function_diagram), run_time=1.0)
        self.wait(0.8)
        
        # ポイント
        function_point = Text(
            "関数解析や最適化でよく使われる視点",
            color=YELLOW, font_size=24, slant=ITALIC
        )
        function_point.shift(DOWN * 2.2)
        self.add_fixed_in_frame_mobjects(function_point)
        self.play(Write(function_point), run_time=0.7)
        self.wait(1.0)
        
        self.play(
            FadeOut(notation1), FadeOut(function_view),
            FadeOut(function_diagram), FadeOut(function_point),
            FadeOut(subtitle1)
        )
        self.wait(0.3)
        
        # === パート2: 掛け算としての内積 ===
        subtitle2 = Text("視点2: 掛け算としての内積", font_size=32, color=GREEN)
        subtitle2.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle2)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)
        
        # 表記
        notation2 = MathTex(
            r"\mathbf{a}_1^T \mathbf{a}_2",
            color=GREEN, font_size=44
        )
        notation2.shift(UP * 1.5)
        self.add_fixed_in_frame_mobjects(notation2)
        self.play(Write(notation2), run_time=0.7)
        self.wait(0.5)
        
        # 説明
        matrix_view = VGroup(
            Text("行ベクトル × 列ベクトル", color=WHITE, font_size=26),
            Text("の「行列の積」として捉える", color=YELLOW, font_size=26),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        matrix_view.shift(UP * 0.3)
        self.add_fixed_in_frame_mobjects(matrix_view)
        self.play(Write(matrix_view), run_time=0.8)
        self.wait(0.8)
        
        # 行列表現
        matrix_calc = MathTex(
            r"\begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \end{bmatrix}",
            r"\begin{bmatrix} a_{21} \\ a_{22} \\ \vdots \\ a_{2n} \end{bmatrix}",
            color=WHITE, font_size=24
        )
        scalar_result = Text("= スカラ", color=WHITE, font_size=24)
        matrix_calc_group = VGroup(matrix_calc, scalar_result).arrange(RIGHT, buff=0.2)
        matrix_calc_group.shift(DOWN * 0.8)
        self.add_fixed_in_frame_mobjects(matrix_calc_group)
        self.play(Write(matrix_calc_group), run_time=1.0)
        self.wait(0.8)
        
        # ポイント
        matrix_point = VGroup(
            Text("線形代数の計算で自然な表現", color=YELLOW, font_size=24, slant=ITALIC),
            Text("プログラミングでも直感的", color=YELLOW, font_size=24, slant=ITALIC),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        matrix_point.shift(DOWN * 2.0)
        self.add_fixed_in_frame_mobjects(matrix_point)
        self.play(Write(matrix_point), run_time=0.8)
        self.wait(1.0)
        
        self.play(
            FadeOut(notation2), FadeOut(matrix_view),
            FadeOut(matrix_calc_group), FadeOut(matrix_point),
            FadeOut(subtitle2)
        )
        self.wait(0.3)
        
        # === パート3: 状態の観測としての内積（ブラケット記法） ===
        subtitle3 = Text("視点3: 状態の観測としての内積", font_size=32, color=PURPLE)
        subtitle3.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle3)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.5)
        
        # 表記
        notation3 = MathTex(
            r"\langle \mathbf{a}_1 | \mathbf{a}_2 \rangle",
            color=PURPLE, font_size=44
        )
        notation3.shift(UP * 1.8)
        self.add_fixed_in_frame_mobjects(notation3)
        self.play(Write(notation3), run_time=0.7)
        self.wait(0.5)
        
        # ブラケット記法の説明
        bracket_intro = Text(
            "ブラケット記法（Dirac記法）",
            color=ORANGE, font_size=28, weight=BOLD
        )
        bracket_intro.shift(UP * 1.0)
        self.add_fixed_in_frame_mobjects(bracket_intro)
        self.play(Write(bracket_intro), run_time=0.6)
        self.wait(0.5)
        
        # 分解して説明
        decomposition = VGroup(
            MathTex(r"\langle \mathbf{a}_1 |", color=RED, font_size=36),
            Text("と", color=WHITE, font_size=24),
            MathTex(r"| \mathbf{a}_2 \rangle", color=BLUE, font_size=36),
            Text("に分解できる", color=WHITE, font_size=24),
        ).arrange(RIGHT, buff=0.3)
        decomposition.shift(UP * 0.2)
        self.add_fixed_in_frame_mobjects(decomposition)
        self.play(Write(decomposition), run_time=0.8)
        self.wait(0.8)
        
        self.play(FadeOut(decomposition))
        self.wait(0.3)
        
        # ケットとブラの説明
        ket_bra_explain = VGroup(
            VGroup(
                MathTex(r"| \mathbf{a}_2 \rangle", color=BLUE, font_size=32),
                Text("「ケット」", color=BLUE, font_size=24),
                Text("= 状態ベクトル", color=BLUE, font_size=22),
            ).arrange(DOWN, buff=0.2),
            VGroup(
                MathTex(r"\langle \mathbf{a}_1 |", color=RED, font_size=32),
                Text("「ブラ」", color=RED, font_size=24),
                Text("= 観測装置", color=RED, font_size=22),
            ).arrange(DOWN, buff=0.2),
        ).arrange(RIGHT, buff=1.5)
        ket_bra_explain.shift(UP * 0.0)
        self.add_fixed_in_frame_mobjects(ket_bra_explain)
        self.play(Write(ket_bra_explain), run_time=1.0)
        self.wait(1.2)
        
        # 物理的解釈
        physics_view = VGroup(
            Text("物理的解釈：", color=ORANGE, font_size=26, weight=BOLD),
            Text("「状態」を「観測装置」で測定", color=WHITE, font_size=24),
            Text("→ 観測値（スカラ）を得る", color=YELLOW, font_size=24),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        physics_view.shift(DOWN * 1.5)
        self.add_fixed_in_frame_mobjects(physics_view)
        self.play(Write(physics_view), run_time=1.0)
        self.wait(1.0)
        
        self.play(FadeOut(ket_bra_explain))
        self.wait(0.3)
        
        # === より詳しく：ケットとブラの役割 ===
        subtitle3b = Text("ケットとブラの役割", font_size=28, color=GOLD)
        subtitle3b.next_to(title, DOWN).shift(DOWN * 0.5)
        self.add_fixed_in_frame_mobjects(subtitle3b)
        self.play(
            Transform(subtitle3, subtitle3b),
            FadeOut(bracket_intro),
            FadeOut(notation3),
            FadeOut(physics_view)
        )
        self.wait(0.5)
        
        # ケットの説明
        ket_detail = VGroup(
            MathTex(r"| \mathbf{a}_2 \rangle", color=BLUE, font_size=38),
            Text("ケット（Ket）", color=BLUE, font_size=28, weight=BOLD),
            VGroup(
                Text("• システムの「状態」を表す", color=WHITE, font_size=22),
                Text("• 列ベクトルとして表現", color=WHITE, font_size=22),
                Text("• 例：粒子の位置、スピン状態", color=YELLOW, font_size=20),
            ).arrange(DOWN, buff=0.2, aligned_edge=LEFT),
        ).arrange(DOWN, buff=0.4)
        ket_detail.shift(UP * 0.8 + LEFT * 2.5)
        self.add_fixed_in_frame_mobjects(ket_detail)
        self.play(Write(ket_detail), run_time=1.0)
        self.wait(1.0)
        
        # ブラの説明
        bra_detail = VGroup(
            MathTex(r"\langle \mathbf{a}_1 |", color=RED, font_size=38),
            Text("ブラ（Bra）", color=RED, font_size=28, weight=BOLD),
            VGroup(
                Text("• 「観測装置」を表す", color=WHITE, font_size=22),
                Text("• 行ベクトルとして表現", color=WHITE, font_size=22),
                Text("• 状態に作用して測定値を得る", color=YELLOW, font_size=20),
            ).arrange(DOWN, buff=0.2, aligned_edge=LEFT),
        ).arrange(DOWN, buff=0.4)
        bra_detail.shift(UP * 0.8 + RIGHT * 2.5)
        self.add_fixed_in_frame_mobjects(bra_detail)
        self.play(Write(bra_detail), run_time=1.0)
        self.wait(1.2)
        
        # 測定のプロセス
        measurement_process = VGroup(
            Text("測定のプロセス：", color=ORANGE, font_size=26, weight=BOLD),
            VGroup(
                Text("1. 状態", color=BLUE, font_size=22),
                MathTex(r"| \mathbf{a}_2 \rangle", color=BLUE, font_size=24),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("2. 観測装置", color=RED, font_size=22),
                MathTex(r"\langle \mathbf{a}_1 |", color=RED, font_size=24),
                Text("で測定", color=WHITE, font_size=22),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("3. 結果", color=ORANGE, font_size=22),
                MathTex(r"\langle \mathbf{a}_1 | \mathbf{a}_2 \rangle", color=PURPLE, font_size=24),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        measurement_process.shift(DOWN * 2.2)
        self.add_fixed_in_frame_mobjects(measurement_process)
        self.play(Write(measurement_process), run_time=1.2)
        self.wait(1.5)
        
        self.play(
            FadeOut(ket_detail), FadeOut(bra_detail),
            FadeOut(measurement_process), FadeOut(subtitle3),
            FadeOut(subtitle3b)
        )
        self.wait(0.3)
        
        # # === パート4: 量子力学での応用 ===
        # subtitle4 = Text("量子力学での応用例", font_size=32, color=TEAL)
        # subtitle4.next_to(title, DOWN)
        # self.add_fixed_in_frame_mobjects(subtitle4)
        # self.play(Write(subtitle4), run_time=0.6)
        # self.wait(0.5)
        
        # quantum_intro = Text(
        #     "量子力学では標準的な記法",
        #     color=YELLOW, font_size=26, weight=BOLD
        # )
        # quantum_intro.shift(UP * 1.5)
        # self.add_fixed_in_frame_mobjects(quantum_intro)
        # self.play(Write(quantum_intro), run_time=0.6)
        # self.wait(0.5)
        
        # # 具体例
        # quantum_examples = VGroup(
        #     VGroup(
        #         Text("• 状態の重ね合わせ：", color=BLUE, font_size=24),
        #         MathTex(r"|\psi\rangle = \alpha|0\rangle + \beta|1\rangle", 
        #                color=BLUE, font_size=22),
        #     ).arrange(DOWN, buff=0.2, aligned_edge=LEFT),
        #     VGroup(
        #         Text("• 観測確率：", color=GREEN, font_size=24),
        #         MathTex(r"P = |\langle \phi | \psi \rangle|^2", 
        #                color=GREEN, font_size=22),
        #     ).arrange(DOWN, buff=0.2, aligned_edge=LEFT),
        #     VGroup(
        #         Text("• 期待値：", color=PURPLE, font_size=24),
        #         MathTex(r"\langle \hat{A} \rangle = \langle \psi | \hat{A} | \psi \rangle", 
        #                color=PURPLE, font_size=22),
        #     ).arrange(DOWN, buff=0.2, aligned_edge=LEFT),
        # ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        # quantum_examples.shift(UP * 0.0)
        # self.add_fixed_in_frame_mobjects(quantum_examples)
        
        # for example in quantum_examples:
        #     self.play(Write(example), run_time=0.7)
        #     self.wait(0.5)
        
        # quantum_note = Text(
        #     "ブラケット記法は量子状態の操作に最適",
        #     color=YELLOW, font_size=22, slant=ITALIC
        # )
        # quantum_note.shift(DOWN * 2.0)
        # self.add_fixed_in_frame_mobjects(quantum_note)
        # self.play(Write(quantum_note), run_time=0.7)
        # self.wait(1.2)
        
        # self.play(
        #     FadeOut(quantum_intro), FadeOut(quantum_examples),
        #     FadeOut(quantum_note), FadeOut(subtitle4)
        # )
        # self.wait(0.3)
        
        # === まとめ ===
        summary_subtitle = Text("まとめ", font_size=36, color=GOLD, weight=BOLD)
        summary_subtitle.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(summary_subtitle)
        self.play(Write(summary_subtitle), run_time=0.6)
        self.wait(0.5)
        
        # 3つの視点をまとめたグループ
        summary_perspectives = VGroup(
            VGroup(
                MathTex(r"(\mathbf{a}_1, \mathbf{a}_2)", color=BLUE, font_size=28),
                Text("→ 関数としての視点", color=BLUE, font_size=22),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                MathTex(r"\mathbf{a}_1^T \mathbf{a}_2", color=GREEN, font_size=28),
                Text("→ 行列の積としての視点", color=GREEN, font_size=22),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                MathTex(r"\langle \mathbf{a}_1 | \mathbf{a}_2 \rangle", color=PURPLE, font_size=28),
                Text("→ 観測としての視点", color=PURPLE, font_size=22),
            ).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        summary_perspectives.shift(UP * 0.5)
        self.add_fixed_in_frame_mobjects(summary_perspectives)
        
        for point in summary_perspectives:
            self.play(Write(point), run_time=0.6)
            self.wait(0.4)
        
        # 結論のグループ
        summary_conclusion = VGroup(
            Text("同じ内積、異なる世界観", color=WHITE, font_size=26, weight=BOLD),
            Text("文脈に応じて使い分ける", color=WHITE, font_size=24),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        summary_conclusion.shift(DOWN * 1.8)
        self.add_fixed_in_frame_mobjects(summary_conclusion)
        
        self.play(Write(summary_conclusion), run_time=0.8)
        self.wait(0.5)
        
        self.wait(2.0)
        
        # フェードアウト
        all_objects = VGroup(title, summary_subtitle, summary_perspectives, summary_conclusion)
        self.play(FadeOut(all_objects), run_time=1.0)
        self.wait(0.5)
