from manim import *

class VectorAngleFromNorm(ThreeDScene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"
        
        # タイトル
        title = Text("ベクトルの成す角とノルム", font_size=40, color=WHITE)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)
        
        # === イントロ: 2次元から高次元へ ===
        intro_subtitle = Text("2次元の直感から高次元への拡張", font_size=32, color=YELLOW)
        intro_subtitle.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(intro_subtitle)
        self.play(Write(intro_subtitle), run_time=0.6)
        self.wait(0.5)
        
        intro_text = VGroup(
            Text("2次元では角度が直感的にわかる", color=WHITE, font_size=26),
            Text("しかし4次元以上は?", color=WHITE, font_size=26),
            Text("ノルムの定義から角度の式を導こう", color=YELLOW, font_size=26, weight=BOLD),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        intro_text.shift(DOWN * 0.5)
        self.add_fixed_in_frame_mobjects(intro_text)
        
        self.play(Write(intro_text), run_time=1.0)
        self.wait(1.2)
        
        self.play(FadeOut(intro_text), FadeOut(intro_subtitle))
        self.wait(0.3)
        
        # === パート1: 2次元ベクトルの成す角 ===
        subtitle1 = Text("2次元ベクトルの成す角", font_size=32, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle1)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.5)
        
        # 2次元平面の設定
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)
        
        # 座標軸
        axes = Axes(
            x_range=[-1, 4, 1],
            y_range=[-1, 4, 1],
            x_length=5,
            y_length=5,
            axis_config={"color": GREY, "include_tip": True}
        )
        axes.shift(LEFT * 2)
        self.play(Create(axes), run_time=0.8)
        self.wait(0.3)
        
        # ベクトルa1とa2
        vector_a1 = Arrow(
            axes.c2p(0, 0), axes.c2p(3, 1),
            buff=0, color=RED, stroke_width=6
        )
        vector_a2 = Arrow(
            axes.c2p(0, 0), axes.c2p(1, 2),
            buff=0, color=BLUE, stroke_width=6
        )
        
        label_a1 = MathTex(r"\mathbf{a}_1", color=RED, font_size=32)
        label_a1.next_to(vector_a1.get_end(), RIGHT, buff=0.1)
        
        label_a2 = MathTex(r"\mathbf{a}_2", color=BLUE, font_size=32)
        label_a2.next_to(vector_a2.get_end(), UP, buff=0.1)
        
        self.play(
            Create(vector_a1), Write(label_a1),
            Create(vector_a2), Write(label_a2),
            run_time=1.0
        )
        self.wait(0.5)
        
        # 角度θの弧
        angle_arc = Arc(
            radius=0.6,
            start_angle=vector_a1.get_angle(),
            angle=vector_a2.get_angle() - vector_a1.get_angle(),
            color=YELLOW,
            arc_center=axes.c2p(0, 0)
        )
        angle_label = MathTex(r"\theta", color=YELLOW, font_size=28)
        angle_label.move_to(axes.c2p(0.8, 0.5))
        
        self.play(Create(angle_arc), Write(angle_label), run_time=0.7)
        self.wait(0.8)
        
        # 説明テキスト（右側）
        explanation_2d = VGroup(
            Text("2次元なら角度θが", color=WHITE, font_size=24),
            Text("直接見える", color=YELLOW, font_size=24, weight=BOLD),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        explanation_2d.to_edge(RIGHT).shift(UP * 1.5)
        self.add_fixed_in_frame_mobjects(explanation_2d)
        self.play(Write(explanation_2d), run_time=0.8)
        self.wait(1.0)
        
        # === パート2: ノルムの定義を使った式変形 ===
        self.play(
            FadeOut(axes), FadeOut(vector_a1), FadeOut(vector_a2),
            FadeOut(label_a1), FadeOut(label_a2),
            FadeOut(angle_arc), FadeOut(angle_label),
            FadeOut(explanation_2d), FadeOut(subtitle1)
        )
        self.wait(0.3)
        
        # カメラを正面に戻す
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)
        
        subtitle2 = Text("ノルムの定義から角度の式を導く", font_size=32, color=GREEN)
        subtitle2.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle2)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)
        
        # ステップ1: ベクトルの差のノルム
        step1_title = Text("Step 1: ベクトルの差のノルム", color=ORANGE, font_size=28, weight=BOLD)
        step1_title.shift(UP * 1.5)
        self.add_fixed_in_frame_mobjects(step1_title)
        self.play(Write(step1_title), run_time=0.6)
        self.wait(0.4)
        
        norm_def = MathTex(
            r"\|\mathbf{a}_1 - \mathbf{a}_2\|^2",
            color=WHITE, font_size=36
        )
        norm_def.shift(UP * 1)
        self.add_fixed_in_frame_mobjects(norm_def)
        self.play(Write(norm_def), run_time=0.7)
        self.wait(0.5)
        
        # ステップ2: 内積の定義を使って展開
        step2_eq = MathTex(
            r"=", r"(\mathbf{a}_1 - \mathbf{a}_2, \mathbf{a}_1 - \mathbf{a}_2)",
            color=WHITE, font_size=32
        )
        step2_eq.next_to(norm_def, DOWN* 1.5, buff=0.4)
        self.add_fixed_in_frame_mobjects(step2_eq)
        self.play(Write(step2_eq), run_time=0.7)
        self.wait(0.5)
        
        # ステップ3: 内積を展開
        step3_eq = MathTex(
            r"=", r"(\mathbf{a}_1, \mathbf{a}_1)", r"-", r"2(\mathbf{a}_1, \mathbf{a}_2)", 
            r"+", r"(\mathbf{a}_2, \mathbf{a}_2)",
            color=WHITE, font_size=32
        )
        step3_eq.next_to(step2_eq, DOWN*1.5, buff=0.4)
        self.add_fixed_in_frame_mobjects(step3_eq)
        self.play(Write(step3_eq), run_time=0.8)
        self.wait(0.8)
        
        # ステップ4: ノルムの記法で書き直す
        step4_eq = MathTex(
            r"=", r"\|\mathbf{a}_1\|^2", r"-", r"2(\mathbf{a}_1, \mathbf{a}_2)", 
            r"+", r"\|\mathbf{a}_2\|^2",
            color=WHITE, font_size=32
        )
        step4_eq.next_to(step3_eq, DOWN, buff=0.4)
        self.add_fixed_in_frame_mobjects(step4_eq)
        self.play(Write(step4_eq), run_time=0.8)
        self.wait(0.8)
        
        # ハイライト: 内積の項
        highlight_box = SurroundingRectangle(step4_eq[3], color=YELLOW, buff=0.1)
        self.add_fixed_in_frame_mobjects(highlight_box)
        self.play(Create(highlight_box), run_time=0.5)
        self.wait(0.5)
        
        inner_product_note = Text(
            "この内積の項を取り出したい",
            color=YELLOW, font_size=24, slant=ITALIC
        )
        inner_product_note.next_to(step4_eq, DOWN, buff=0.8)
        self.add_fixed_in_frame_mobjects(inner_product_note)
        self.play(Write(inner_product_note), run_time=0.6)
        self.wait(0.8)
        
        self.play(
            FadeOut(step1_title), FadeOut(norm_def), FadeOut(step2_eq),
            FadeOut(step3_eq), FadeOut(step4_eq), 
            FadeOut(highlight_box), FadeOut(inner_product_note)
        )
        self.wait(0.3)
        
        # === パート3: 余弦定理との対応 ===
        subtitle2b = Text("余弦定理との対応", font_size=28, color=GOLD)
        subtitle2b.next_to(title, DOWN).shift(DOWN * 0)
        self.add_fixed_in_frame_mobjects(subtitle2b)
        self.play(Transform(subtitle2, subtitle2b))
        self.wait(0.5)
        
        # 余弦定理
        cosine_law_title = Text("余弦定理:", color=ORANGE, font_size=26, weight=BOLD)
        cosine_law_title.shift(UP * 2.1)
        self.add_fixed_in_frame_mobjects(cosine_law_title)
        self.play(Write(cosine_law_title), run_time=0.5)
        self.wait(0.3)
        
        cosine_law = MathTex(
            r"\|\mathbf{a}_1 - \mathbf{a}_2\|^2 = \|\mathbf{a}_1\|^2 + \|\mathbf{a}_2\|^2 - 2\|\mathbf{a}_1\|\|\mathbf{a}_2\|\cos\theta",
            color=WHITE, font_size=28
        )
        cosine_law.shift(UP * 1.5)
        self.add_fixed_in_frame_mobjects(cosine_law)
        self.play(Write(cosine_law), run_time=1.0)
        self.wait(0.8)
        
        # 前のステップの式を再表示
        previous_eq = MathTex(
            r"\|\mathbf{a}_1 - \mathbf{a}_2\|^2 = \|\mathbf{a}_1\|^2 - 2(\mathbf{a}_1, \mathbf{a}_2) + \|\mathbf{a}_2\|^2",
            color=WHITE, font_size=28
        )
        previous_eq.shift(UP * 0.5)
        self.add_fixed_in_frame_mobjects(previous_eq)
        self.play(Write(previous_eq), run_time=1.0)
        self.wait(0.8)
        
        # 比較の矢印
        comparison_arrow = Text("⇕", color=YELLOW, font_size=40)
        comparison_arrow.shift(UP * 1.0)
        self.add_fixed_in_frame_mobjects(comparison_arrow)
        self.play(Write(comparison_arrow), run_time=0.5)
        self.wait(0.5)
        
        # 対応関係
        correspondence = MathTex(
            r"2(\mathbf{a}_1, \mathbf{a}_2) = 2\|\mathbf{a}_1\|\|\mathbf{a}_2\|\cos\theta",
            color=YELLOW, font_size=32
        )
        correspondence.shift(DOWN * 0.8)
        self.add_fixed_in_frame_mobjects(correspondence)
        self.play(Write(correspondence), run_time=0.8)
        self.wait(0.8)
        
        # 結論の式
        conclusion_box = Rectangle(
            width=8, height=1.2,
            color=GREEN, stroke_width=3
        )
        conclusion_box.shift(DOWN * 2.0)
        
        conclusion_formula = MathTex(
            r"\cos\theta = \frac{(\mathbf{a}_1, \mathbf{a}_2)}{\|\mathbf{a}_1\|\|\mathbf{a}_2\|}",
            color=GREEN, font_size=40
        )
        conclusion_formula.shift(DOWN * 2.0)
        
        self.add_fixed_in_frame_mobjects(conclusion_box)
        self.add_fixed_in_frame_mobjects(conclusion_formula)
        self.play(
            Create(conclusion_box),
            Write(conclusion_formula),
            run_time=1.0
        )
        self.wait(1.2)
        
        self.play(
            FadeOut(cosine_law_title), FadeOut(cosine_law),
            FadeOut(previous_eq), FadeOut(comparison_arrow),
            FadeOut(correspondence), FadeOut(subtitle2), FadeOut(subtitle2b)
        )
        self.wait(0.3)
        
        # 式を中央に移動
        self.play(
            conclusion_box.animate.move_to(UP * 1.5),
            conclusion_formula.animate.move_to(UP * 1.5),
            run_time=0.8
        )
        self.wait(0.5)
        
        # === パート4: 高次元への拡張 ===
        subtitle3 = Text("高次元への拡張", font_size=32, color=PURPLE)
        subtitle3.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle3)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.5)
        
        key_insight = VGroup(
            Text("重要な洞察:この式は次元に依存しない!", color=ORANGE, font_size=28, weight=BOLD),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        key_insight.shift(UP * 0.3)
        self.add_fixed_in_frame_mobjects(key_insight)
        self.play(Write(key_insight), run_time=0.8)
        self.wait(0.8)
        
        # 次元の比較
        dimension_comparison = VGroup(
            VGroup(
                Text("2次元:角度が直接見える", color=BLUE, font_size=24, weight=BOLD),
            ).arrange(DOWN*1.8, buff=0.2, aligned_edge=LEFT),
            VGroup(
                Text("3次元:まだ想像できる", color=GREEN, font_size=24, weight=BOLD),
            ).arrange(DOWN*1.8, buff=0.2, aligned_edge=LEFT),
            VGroup(
                Text("4次元以上:人間には想像できない", color=RED, font_size=24, weight=BOLD),
            ).arrange(DOWN*1.8, buff=0.2, aligned_edge=LEFT),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        dimension_comparison.shift(DOWN * 1.2)
        self.add_fixed_in_frame_mobjects(dimension_comparison)
        
        for dim in dimension_comparison:
            self.play(Write(dim), run_time=0.6)
            self.wait(0.4)
        
        self.wait(0.8)
        
        # しかし...
        but_text = Text("だけど...", color=YELLOW, font_size=28, slant=ITALIC)
        but_text.shift(DOWN * 3)
        self.add_fixed_in_frame_mobjects(but_text)
        self.play(Write(but_text), run_time=0.5)
        self.wait(0.5)
        
        self.play(FadeOut(key_insight), FadeOut(dimension_comparison),
                  FadeOut(but_text), FadeOut(conclusion_formula),
                  FadeOut(conclusion_box))
        self.wait(0.3)
        
        # === パート5: 高次元でも同じ式 ===
        subtitle3b = Text("高次元でも同じ式で角度を定義してしまえば…", font_size=28, color=TEAL)
        subtitle3b.next_to(title, DOWN).shift(DOWN * 0.5)
        self.add_fixed_in_frame_mobjects(subtitle3b)
        self.play(Transform(subtitle3, subtitle3b))
        self.wait(0.5)
        
        # 高次元の例
        high_dim_title = Text("例: 4次元ベクトル", color=ORANGE, font_size=26, weight=BOLD)
        high_dim_title.shift(UP * 1)
        self.add_fixed_in_frame_mobjects(high_dim_title)
        self.play(Write(high_dim_title), run_time=0.6)
        self.wait(0.4)
        
        vector_example = VGroup(
            MathTex(
                r"\mathbf{a}_1 = \begin{bmatrix} 1 \\ 0 \\ 0 \\ 1 \end{bmatrix}, \quad"
                r"\mathbf{a}_2 = \begin{bmatrix} 0 \\ 1 \\ 1 \\ 0 \end{bmatrix}",
                color=WHITE, font_size=28
            ),
        )
        vector_example.shift(DOWN * 0.2)
        self.add_fixed_in_frame_mobjects(vector_example)
        self.play(Write(vector_example), run_time=0.8)
        self.wait(0.6)
        
        # 計算
        calculation_text = Text("同じ式を使って計算:", color=YELLOW, font_size=24)
        calculation_text.shift(DOWN * 1.2)
        self.add_fixed_in_frame_mobjects(calculation_text)
        self.play(Write(calculation_text), run_time=0.6)
        self.wait(0.4)
        
        calculation = MathTex(
            r"\cos\theta = \frac{0}{\sqrt{2} \cdot \sqrt{2}} = 0",
            color=WHITE, font_size=28
        )
        calculation.shift(DOWN * 1.8)
        self.add_fixed_in_frame_mobjects(calculation)
        self.play(Write(calculation), run_time=0.8)
        self.wait(0.6)
        
        result = MathTex(
            r"\therefore \theta = 90°",
            color=GREEN, font_size=32
        )
        result.shift(DOWN * 2.5)
        self.add_fixed_in_frame_mobjects(result)
        self.play(Write(result), run_time=0.7)
        self.wait(1.0)
        
        self.play(
            FadeOut(high_dim_title), FadeOut(vector_example),
            FadeOut(calculation_text), FadeOut(calculation),
            FadeOut(result), FadeOut(subtitle3), FadeOut(subtitle3b)
        )
        self.wait(0.3)
        
        # === まとめ ===
        summary_subtitle = Text("まとめ", font_size=36, color=GOLD, weight=BOLD)
        summary_subtitle.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(summary_subtitle)
        self.play(Write(summary_subtitle), run_time=0.6)
        self.wait(0.5)
        
        # まとめのポイント
        summary_points = VGroup(
            VGroup(
                Text("1.", color=WHITE, font_size=26, weight=BOLD),
                Text("ノルムの定義から角度の式を導出", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("2.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    MathTex(r"\cos\theta = \frac{(\mathbf{a}_1, \mathbf{a}_2)}{\|\mathbf{a}_1\|\|\mathbf{a}_2\|}", 
                           color=GREEN, font_size=26),
                ),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("3.", color=WHITE, font_size=26, weight=BOLD),
                Text("この式は任意の次元で成立", color=YELLOW, font_size=24),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("4.", color=WHITE, font_size=26, weight=BOLD),
                Text("つまり高次元でも「角度」を定義できる？", color=BLUE, font_size=24),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        summary_points.shift(DOWN * 0.3)
        self.add_fixed_in_frame_mobjects(summary_points)
        
        for point in summary_points:
            self.play(Write(point), run_time=0.6)
            self.wait(0.4)
        
        self.wait(0.5)
        
        # 最終メッセージ
        final_message = Text(
            "幾何学的直感を代数に翻訳する力",
            color=YELLOW, font_size=28, weight=BOLD, slant=ITALIC
        )
        final_message.shift(DOWN * 2.5)
        self.add_fixed_in_frame_mobjects(final_message)
        self.play(Write(final_message), run_time=0.8)
        self.wait(1.5)
        
        self.wait(2.0)
        
        # フェードアウト
        all_objects = VGroup(
            title, summary_subtitle, summary_points, 
            final_message
        )
        self.play(FadeOut(all_objects), run_time=1.0)
        self.wait(0.5)
