from manim import *
import numpy as np

class OperatorIntroduction(Scene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"

        # タイトル
        title = Text("作用素: 関数を関数に変える操作", font_size=34, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)

        # === Part 1: ベクトル vs 関数の変換 ===
        subtitle1 = Text("これまで: ベクトル → ベクトル", font_size=32, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.5)

        # ベクトルの線形写像の図
        vector_label = Text("線形写像 (ベクトル空間)", color=BLUE, font_size=26, weight=BOLD)
        vector_label.shift(UP * 1.8 + LEFT * 1.5)
        self.play(Write(vector_label), run_time=0.5)
        self.wait(0.3)

        # 入力ベクトルの数式
        input_vec_text = MathTex(
            r"\mathbf{v} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}",
            color=BLUE, font_size=26
        )
        input_vec_text.shift(UP * 0.9 + LEFT * 3.7)

        # 変換行列
        transform_vec = MathTex(
            r"A = \begin{pmatrix} 2 & 0 \\ 0 & 1.5 \end{pmatrix}",
            color=YELLOW, font_size=24
        )
        transform_vec.shift(UP * 0.9 + LEFT * 1.3)

        # 出力ベクトルの数式
        output_vec_text = MathTex(
            r"\mathbf{w} = \begin{pmatrix} 2 \\ 3 \end{pmatrix}",
            color=GREEN, font_size=26
        )
        output_vec_text.shift(UP * 0.9 + RIGHT * 1.0)

        # 矢印
        arrow_to_transform = Arrow(
            LEFT * 2.7 + UP * 0.9,
            LEFT * 2.0 + UP * 0.9,
            color=YELLOW, buff=0.1, stroke_width=3
        )
        arrow_to_output = Arrow(
            LEFT * 0.5 + UP * 0.9,
            RIGHT * 0.0 + UP * 0.9,
            color=YELLOW, buff=0.1, stroke_width=3
        )

        self.play(Write(input_vec_text), run_time=0.5)
        self.play(GrowArrow(arrow_to_transform), Write(transform_vec), run_time=0.6)
        self.play(GrowArrow(arrow_to_output), Write(output_vec_text), run_time=0.5)
        self.wait(0.5)

        # グラフで可視化
        vec_graph_note = Text("グラフで見ると:", color=ORANGE, font_size=24, weight=BOLD)
        vec_graph_note.shift(DOWN * 0.3 + LEFT * 3.5)
        self.play(Write(vec_graph_note), run_time=0.5)
        self.wait(0.3)

        # 入力側の座標平面
        axes_vec_in = Axes(
            x_range=[0, 3.5, 1],
            y_range=[0, 3.5, 1],
            x_length=2.5,
            y_length=2.5,
            tips=False,
            axis_config={"include_numbers": False, "stroke_width": 2}
        ).shift(DOWN * 1.8 + LEFT * 3.0)

        # 入力ベクトル (1, 2)
        input_vector = Arrow(
            axes_vec_in.c2p(0, 0),
            axes_vec_in.c2p(1, 2),
            color=BLUE, buff=0, stroke_width=5
        )
        input_vec_label = MathTex(r"\mathbf{v}", color=BLUE, font_size=20)
        input_vec_label.next_to(axes_vec_in, DOWN, buff=0.1)

        # 出力側の座標平面
        axes_vec_out = Axes(
            x_range=[0, 3.5, 1],
            y_range=[0, 3.5, 1],
            x_length=2.5,
            y_length=2.5,
            tips=False,
            axis_config={"include_numbers": False, "stroke_width": 2}
        ).shift(DOWN * 1.8 + RIGHT * 1.0)

        # 出力ベクトル (2, 3)
        output_vector = Arrow(
            axes_vec_out.c2p(0, 0),
            axes_vec_out.c2p(2, 3),
            color=GREEN, buff=0, stroke_width=5
        )
        output_vec_label = MathTex(r"\mathbf{w}", color=GREEN, font_size=20)
        output_vec_label.next_to(axes_vec_out, DOWN, buff=0.1)

        # 間の矢印
        arrow_vec_graph = Arrow(
            LEFT * 1.3 + DOWN * 1.8,
            LEFT * 0.3 + DOWN * 1.8,
            color=YELLOW, buff=0.1, stroke_width=4
        )

        self.play(
            Create(axes_vec_in), GrowArrow(input_vector),
            Write(input_vec_label),
            run_time=0.7
        )
        self.play(GrowArrow(arrow_vec_graph), run_time=0.4)
        self.play(
            Create(axes_vec_out), GrowArrow(output_vector),
            Write(output_vec_label),
            run_time=0.7
        )
        self.wait(0.8)

        vec_group = VGroup(
            input_vec_text, transform_vec, output_vec_text,
            arrow_to_transform, arrow_to_output,
            vec_graph_note, axes_vec_in, input_vector, input_vec_label,
            arrow_vec_graph, axes_vec_out, output_vector, output_vec_label
        )

        self.play(FadeOut(vec_group), FadeOut(vector_label), FadeOut(subtitle1))
        self.wait(0.3)

        # === Part 2: 関数を関数に写す ===
        subtitle2 = Text("今回: 関数 → 関数", font_size=32, color=GREEN)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)

        function_label = Text("作用素 (関数空間)", color=GREEN, font_size=26, weight=BOLD)
        function_label.shift(UP * 1.8 + LEFT * 1.5)
        self.play(Write(function_label), run_time=0.5)
        self.wait(0.3)

        # 入力関数
        input_func = MathTex(
            r"f(x)",
            color=BLUE, font_size=28
        )
        input_func.shift(UP * 0.8 + LEFT * 3.5)

        # 矢印
        arrow_func = Arrow(
            LEFT * 2.3 + UP * 0.8,
            LEFT * 0.7 + UP * 0.8,
            color=YELLOW, buff=0.1
        )

        # 作用素
        operator_label = MathTex(
            r"\mathcal{L}",
            color=YELLOW, font_size=28
        )
        operator_label.next_to(arrow_func, UP, buff=0.2)

        # operator_text = Text("(微分)", color=YELLOW, font_size=20)
        # operator_text.next_to(operator_label, DOWN, buff=0.1)

        # 出力関数
        output_func = MathTex(
            r"g(x)",
            color=GREEN, font_size=28
        )
        output_func.shift(UP * 0.8 + RIGHT * 1.0)

        self.play(Write(input_func), run_time=0.5)
        self.play(
            GrowArrow(arrow_func),
            Write(operator_label),
            # Write(operator_text),
            run_time=0.7
        )
        self.play(Write(output_func), run_time=0.5)
        self.wait(0.8)

        # グラフで可視化
        graph_note = Text("グラフで見ると:", color=ORANGE, font_size=24, weight=BOLD)
        graph_note.shift(DOWN * 0.5 + LEFT * 3.5)
        self.play(Write(graph_note), run_time=0.5)
        self.wait(0.3)

        # 簡単なグラフ
        axes_input = Axes(
            x_range=[-1.5, 1.5, 1],
            y_range=[-0.5, 2.5, 1],
            x_length=2.5,
            y_length=2,
            tips=False,
            axis_config={"include_numbers": False, "stroke_width": 2}
        ).shift(DOWN * 1.8 + LEFT * 3.0)

        graph_input = axes_input.plot(lambda x: x**2, color=BLUE, x_range=[-1.2, 1.2])
        # input_graph_label = MathTex(r"f(x)=x^2", color=BLUE, font_size=20)
        # input_graph_label.next_to(axes_input, DOWN, buff=0.1)

        axes_output = Axes(
            x_range=[-1.5, 1.5, 1],
            y_range=[-2.5, 2.5, 1],
            x_length=2.5,
            y_length=2,
            tips=False,
            axis_config={"include_numbers": False, "stroke_width": 2}
        ).shift(DOWN * 1.8 + RIGHT * 1.0)

        graph_output = axes_output.plot(lambda x: 2*x, color=GREEN, x_range=[-1.2, 1.2])
        # output_graph_label = MathTex(r"g(x)=2x", color=GREEN, font_size=20)
        # output_graph_label.next_to(axes_output, DOWN, buff=0.1)

        arrow_graph = Arrow(
            LEFT * 1.3 + DOWN * 1.8,
            LEFT * 0.3 + DOWN * 1.8,
            color=YELLOW, buff=0.1, stroke_width=4
        )

        self.play(
            Create(axes_input), Create(graph_input),
            # Write(input_graph_label),
            run_time=0.7
        )
        self.play(GrowArrow(arrow_graph), run_time=0.4)
        self.play(
            Create(axes_output), Create(graph_output),
            # Write(output_graph_label),
            run_time=0.7
        )
        self.wait(1.0)

        self.play(
            FadeOut(input_func), FadeOut(arrow_func),
            FadeOut(operator_label), # FadeOut(operator_text),
            FadeOut(output_func), FadeOut(graph_note),
            FadeOut(axes_input), FadeOut(graph_input),# FadeOut(input_graph_label),
            FadeOut(arrow_graph),
            FadeOut(axes_output), FadeOut(graph_output), #FadeOut(output_graph_label),
            FadeOut(function_label), FadeOut(subtitle2)
        )
        self.wait(0.3)

        # === Part 3: 線形写像と行列 ===
        subtitle3 = Text("線形性を満たす操作", font_size=32, color=PURPLE)
        subtitle3.next_to(title, DOWN)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.5)

        # 線形写像の復習
        recall_label = Text("思い出そう: 線形写像は行列で書ける", color=YELLOW, font_size=26, weight=BOLD)
        recall_label.shift(UP * 1.6)
        self.play(Write(recall_label), run_time=0.6)
        self.wait(0.4)

        # ベクトル空間の線形写像
        linear_map_vec = MathTex(
            r"T: \mathbb{R}^n \to \mathbb{R}^m, \quad T(\mathbf{v}) = A\mathbf{v}",
            color=WHITE, font_size=28
        )
        linear_map_vec.shift(UP * 0.8)
        self.play(Write(linear_map_vec), run_time=0.7)
        self.wait(0.5)

        # 線形性の条件
        linearity_cond = VGroup(
            MathTex(r"T(\alpha \mathbf{v} + \beta \mathbf{w}) = \alpha T(\mathbf{v}) + \beta T(\mathbf{w})", 
                    color=BLUE, font_size=26),
        )
        linearity_cond.shift(UP * 0.1)
        linearity_box = SurroundingRectangle(linearity_cond, color=BLUE, buff=0.2)
        self.play(Write(linearity_cond), Create(linearity_box), run_time=0.7)
        self.wait(0.6)

        # 同様に...
        similarly_note = Text("同様に、関数空間でも:", color=ORANGE, font_size=24, weight=BOLD)
        similarly_note.shift(DOWN * 0.9)
        self.play(Write(similarly_note), run_time=0.5)
        self.wait(0.3)

        # 関数空間の線形作用素
        linear_op_func = MathTex(
            r"\mathcal{L}(\alpha f + \beta g) = \alpha \mathcal{L}(f) + \beta \mathcal{L}(g)",
            color=GREEN, font_size=26
        )
        linear_op_func.shift(DOWN * 1.6)
        linear_op_box = SurroundingRectangle(linear_op_func, color=GREEN, buff=0.2)
        self.play(Write(linear_op_func), Create(linear_op_box), run_time=0.8)
        self.wait(0.5)

        # 注釈
        detail_note = Text("詳細は後で取り扱う", color=GRAY, font_size=20, slant=ITALIC)
        detail_note.shift(DOWN * 2.6)
        self.play(Write(detail_note), run_time=0.4)
        self.wait(0.8)

        self.play(
            FadeOut(recall_label), FadeOut(linear_map_vec),
            FadeOut(linearity_cond), FadeOut(linearity_box),
            FadeOut(similarly_note), FadeOut(linear_op_func),
            FadeOut(linear_op_box), FadeOut(detail_note),
            FadeOut(subtitle3)
        )
        self.wait(0.3)

        # === Part 4: 微分作用素 ===
        subtitle4 = Text("例: 微分作用素", font_size=32, color=TEAL)
        subtitle4.next_to(title, DOWN)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.5)

        # 微分は線形性を持つ
        diff_intro = Text("微分は線形性を持つ操作の代表例", color=YELLOW, font_size=26, weight=BOLD)
        diff_intro.shift(UP * 1.8)
        self.play(Write(diff_intro), run_time=0.6)
        self.wait(0.4)

        # 微分の線形性
        diff_linearity = MathTex(
            r"\frac{d}{dx}\bigl(\alpha f(x) + \beta g(x)\bigr) = "
            r"\alpha \frac{df}{dx} + \beta \frac{dg}{dx}",
            color=WHITE, font_size=28
        )
        diff_linearity.shift(UP * 1.0)
        self.play(Write(diff_linearity), run_time=0.8)
        self.wait(0.6)

        # 記号の準備
        symbol_label = Text("記号の準備:", color=ORANGE, font_size=26, weight=BOLD)
        symbol_label.shift(UP * 0.1)
        self.play(Write(symbol_label), run_time=0.5)
        self.wait(0.3)

        # 作用素の記号
        operator_symbol = VGroup(
            MathTex(r"\mathcal{L}", color=WHITE, font_size=28),
            Text("で作用素を表す", color=WHITE, font_size=24),
        ).arrange(RIGHT, buff=0.3)
        operator_symbol.shift(DOWN * 0.5)
        self.play(Write(operator_symbol), run_time=0.6)
        self.wait(0.4)

        # 微分作用素の表記
        diff_operator = VGroup(
            Text("微分の場合:", color=GREEN, font_size=24),
            MathTex(r"\mathcal{L} = \frac{d}{dx}", color=GREEN, font_size=28),
        ).arrange(RIGHT, buff=0.3)
        diff_operator.shift(DOWN * 1.2)
        diff_op_box = SurroundingRectangle(diff_operator, color=GREEN, buff=0.2)
        self.play(Write(diff_operator), Create(diff_op_box), run_time=0.7)
        self.wait(0.6)

        # 使用例
        usage_example = MathTex(
            r"\mathcal{L}(x^2) = \frac{d}{dx}(x^2) = 2x",
            color=BLUE, font_size=26
        )
        usage_example.shift(DOWN * 2.2)
        self.play(Write(usage_example), run_time=0.6)
        self.wait(0.8)

        self.play(
            FadeOut(diff_intro), FadeOut(diff_linearity),
            FadeOut(symbol_label), FadeOut(operator_symbol),
            FadeOut(diff_operator), FadeOut(diff_op_box),
            FadeOut(usage_example), FadeOut(subtitle4)
        )
        self.wait(0.3)

        # === Part 5: 非可換な作用素 ===
        subtitle5 = Text("注意: 非可換な作用素", font_size=32, color=RED)
        subtitle5.next_to(title, DOWN)
        self.play(Write(subtitle5), run_time=0.6)
        self.wait(0.5)

        # 重要な注意
        warning_label = Text("作用する対象を起点に計算が始まる！", 
                           color=RED, font_size=28, weight=BOLD)
        warning_label.shift(UP * 1.8)
        warning_box = SurroundingRectangle(warning_label, color=RED, buff=0.2)
        self.play(Write(warning_label), Create(warning_box), run_time=0.7)
        self.wait(0.6)

        # 例: 複合作用素
        composite_label = Text("例: 「xを掛けてxで微分する」作用素", 
                              color=ORANGE, font_size=24, weight=BOLD)
        composite_label.shift(UP * 0.9)
        self.play(Write(composite_label), run_time=0.6)
        self.wait(0.4)

        # 作用素の定義
        composite_def = MathTex(
            r"\tilde{\mathcal{L}} = \frac{d}{dx}(x \cdot \;)",
            color=YELLOW, font_size=30
        )
        composite_def.shift(UP * 0.2)
        composite_def_box = SurroundingRectangle(composite_def, color=YELLOW, buff=0.15)
        self.play(Write(composite_def), Create(composite_def_box), run_time=0.7)
        self.wait(0.5)

        # 正しい適用
        correct_label = VGroup(
            Text("✓ 正しい:", color=GREEN, font_size=24, weight=BOLD),
            Text("h₁(x) に作用させると", color=WHITE, font_size=22),
        ).arrange(RIGHT, buff=0.3)
        correct_label.shift(DOWN * 0.7 + LEFT * 3)
        self.play(Write(correct_label), run_time=0.5)
        self.wait(0.3)

        correct_calc = MathTex(
            r"\tilde{\mathcal{L}}(h_1) = \frac{d}{dx}(x \cdot h_1(x)) "
            r"= h_1(x) + x\frac{dh_1}{dx}",
            color=GREEN, font_size=26
        )
        correct_calc.shift(DOWN * 1.4)
        self.play(Write(correct_calc), run_time=0.8)
        self.wait(0.5)

        calc_note = Text("(積の微分公式)", color=GREEN, font_size=20, slant=ITALIC)
        calc_note.next_to(correct_calc, DOWN, buff=0.1)
        self.play(Write(calc_note), run_time=0.4)
        self.wait(0.6)

        # 間違った適用
        wrong_label = VGroup(
            Text("✗ 間違い:", color=RED, font_size=24, weight=BOLD),
            Text("順番を無視して", color=WHITE, font_size=22),
        ).arrange(RIGHT, buff=0.3)
        wrong_label.shift(DOWN * 2.3 + LEFT * 3.5)
        self.play(Write(wrong_label), run_time=0.5)
        self.wait(0.3)

        wrong_calc = MathTex(
            r"\frac{d}{dx}(x) \cdot h_1(x) = 1 \cdot h_1(x) = h_1(x)",
            color=RED, font_size=26
        )
        wrong_calc.shift(DOWN * 2.9)
        wrong_cross = Line(
            wrong_calc.get_corner(UL) + UP * 0.1 + LEFT * 0.2,
            wrong_calc.get_corner(DR) + DOWN * 0.1 + RIGHT * 0.2,
            color=RED, stroke_width=6
        )
        self.play(Write(wrong_calc), run_time=0.7)
        self.play(Create(wrong_cross), run_time=0.5)
        self.wait(1.0)

        # 強調メッセージ
        emphasis = Text(
            "作用素は作用する対象とセットで考える！",
            color=YELLOW, font_size=24, weight=BOLD, slant=ITALIC
        )
        emphasis.shift(DOWN * 3.6)
        self.play(Write(emphasis), run_time=0.7)
        self.wait(1.2)

        self.play(
            FadeOut(warning_label), FadeOut(warning_box),
            FadeOut(composite_label), FadeOut(composite_def), FadeOut(composite_def_box),
            FadeOut(correct_label), FadeOut(correct_calc), FadeOut(calc_note),
            FadeOut(wrong_label), FadeOut(wrong_calc), FadeOut(wrong_cross),
            FadeOut(emphasis), FadeOut(subtitle5)
        )
        self.wait(0.3)

        # === Part 6: 線形作用素の行列表現 ===
        subtitle6 = Text("線形作用素は必ず行列で書ける！", font_size=30, color=GOLD)
        subtitle6.next_to(title, DOWN)
        self.play(Write(subtitle6), run_time=0.6)
        self.wait(0.5)

        # 強調メッセージ
        key_msg = Text("線形性がある → 必ず行列表現が存在する", color=YELLOW, font_size=26, weight=BOLD)
        key_msg.shift(UP * 1.8)
        key_box = SurroundingRectangle(key_msg, color=YELLOW, buff=0.2)
        self.play(Write(key_msg), Create(key_box), run_time=0.7)
        self.wait(0.5)

        # 方法ラベル
        method_title = Text("方法:", color=ORANGE, font_size=24, weight=BOLD)
        method_title.shift(UP * 0.8 + LEFT * 5.5)
        self.play(Write(method_title), run_time=0.4)
        self.wait(0.2)

        # フロー図
        fx_label = MathTex(r"f(x)", color=BLUE, font_size=26)
        fx_label.shift(LEFT * 4.5)
        fx_box = SurroundingRectangle(fx_label, color=BLUE, buff=0.2)

        cvec_label = MathTex(r"\mathbf{c}", color=WHITE, font_size=26)
        cvec_label.shift(LEFT * 1.5)
        cvec_box = SurroundingRectangle(cvec_label, color=WHITE, buff=0.2)
        cvec_sub = Text("係数ベクトル", color=GRAY, font_size=14)
        cvec_sub.next_to(cvec_box, DOWN, buff=0.1)

        Lc_label = MathTex(r"L\mathbf{c}", color=YELLOW, font_size=26)
        Lc_label.shift(RIGHT * 1.5)
        Lc_box = SurroundingRectangle(Lc_label, color=YELLOW, buff=0.2)

        gx_label = MathTex(r"g(x)", color=GREEN, font_size=26)
        gx_label.shift(RIGHT * 4.5)
        gx_box = SurroundingRectangle(gx_label, color=GREEN, buff=0.2)

        arr_f_c = Arrow(fx_box.get_right(), cvec_box.get_left(), buff=0.1, color=GRAY)
        arr_f_c_lbl = Text("基底展開", color=GRAY, font_size=15)
        arr_f_c_lbl.next_to(arr_f_c, UP, buff=0.1)

        arr_c_Lc = Arrow(cvec_box.get_right(), Lc_box.get_left(), buff=0.1, color=GRAY)
        arr_c_Lc_lbl = Text("行列をかける", color=GRAY, font_size=15)
        arr_c_Lc_lbl.next_to(arr_c_Lc, UP, buff=0.1)

        arr_Lc_g = Arrow(Lc_box.get_right(), gx_box.get_left(), buff=0.1, color=GRAY)
        arr_Lc_g_lbl = Text("基底で合成", color=GRAY, font_size=15)
        arr_Lc_g_lbl.next_to(arr_Lc_g, UP, buff=0.1)

        self.play(FadeIn(fx_label), Create(fx_box), run_time=0.5)
        self.play(
            GrowArrow(arr_f_c), Write(arr_f_c_lbl),
            FadeIn(cvec_label), Create(cvec_box), Write(cvec_sub),
            run_time=0.6
        )
        self.play(
            GrowArrow(arr_c_Lc), Write(arr_c_Lc_lbl),
            FadeIn(Lc_label), Create(Lc_box),
            run_time=0.6
        )
        self.play(
            GrowArrow(arr_Lc_g), Write(arr_Lc_g_lbl),
            FadeIn(gx_label), Create(gx_box),
            run_time=0.6
        )
        self.wait(0.7)

        flow_comment = VGroup(
            Text("基底を決めると", color=WHITE, font_size=22),
            Text("→ 作用素が行列に化ける！", color=YELLOW, font_size=22, weight=BOLD),
        ).arrange(RIGHT, buff=0.2)
        flow_comment.shift(DOWN * 1.5)
        self.play(Write(flow_comment), run_time=0.6)
        self.wait(1.0)

        self.play(
            FadeOut(key_msg), FadeOut(key_box), FadeOut(method_title),
            FadeOut(fx_label), FadeOut(fx_box),
            FadeOut(cvec_label), FadeOut(cvec_box), FadeOut(cvec_sub),
            FadeOut(Lc_label), FadeOut(Lc_box),
            FadeOut(gx_label), FadeOut(gx_box),
            FadeOut(arr_f_c), FadeOut(arr_f_c_lbl),
            FadeOut(arr_c_Lc), FadeOut(arr_c_Lc_lbl),
            FadeOut(arr_Lc_g), FadeOut(arr_Lc_g_lbl),
            FadeOut(flow_comment), FadeOut(subtitle6)
        )
        self.wait(0.3)

        # === Part 7: 具体例 - 微分の表現行列 ===
        subtitle7 = Text("具体例: 微分の表現行列", font_size=30, color=TEAL)
        subtitle7.next_to(title, DOWN)
        self.play(Write(subtitle7), run_time=0.6)
        self.wait(0.5)

        # Phase 1: 基底 + h1 + 微分 + h2
        basis_row = VGroup(
            Text("基底:", color=ORANGE, font_size=24, weight=BOLD),
            MathTex(r"|1\rangle,\; |x\rangle,\; |x^2\rangle", color=ORANGE, font_size=26),
        ).arrange(RIGHT, buff=0.3)
        basis_row.shift(UP * 1.7)
        self.play(Write(basis_row), run_time=0.6)
        self.wait(0.3)

        h1_eq = MathTex(
            r"h_1(x) = c_{1,0}|1\rangle + c_{1,1}|x\rangle + c_{1,2}|x^2\rangle",
            color=BLUE, font_size=26
        )
        h1_eq.shift(UP * 1.0)
        self.play(Write(h1_eq), run_time=0.7)
        self.wait(0.3)

        diff_down = MathTex(
            r"\downarrow \;\; \mathcal{L} = \frac{d}{dx}",
            color=YELLOW, font_size=24
        )
        diff_down.shift(UP * 0.3 + LEFT * 3.5)
        self.play(Write(diff_down), run_time=0.4)

        h2_eq = MathTex(
            r"h_2(x) = \mathcal{L} h_1(x) = c_{1,1}|1\rangle + 2c_{1,2}|x\rangle + 0\cdot|x^2\rangle",
            color=GREEN, font_size=26
        )
        h2_eq.shift(DOWN * 0.4)
        self.play(Write(h2_eq), run_time=0.8)
        self.wait(0.8)

        # Phase 2: h1・diff_downを消し、係数変換と行列を表示
        self.play(FadeOut(h1_eq), FadeOut(diff_down))
        self.wait(0.2)

        coeff_note = Text("係数ベクトルで見ると:", color=YELLOW, font_size=22, weight=BOLD)
        coeff_note.shift(UP * 0.9 + LEFT * 3.5)
        self.play(Write(coeff_note), run_time=0.5)

        coeff_tf = MathTex(
            r"\begin{pmatrix} c_{1,0} \\ c_{1,1} \\ c_{1,2} \end{pmatrix}"
            r"\;\longrightarrow\;"
            r"\begin{pmatrix} c_{1,1} \\ 2c_{1,2} \\ 0 \end{pmatrix}",
            color=WHITE, font_size=26
        )
        coeff_tf.shift(UP * 0.1)
        self.play(Write(coeff_tf), run_time=0.8)
        self.wait(0.5)

        matrix_intro = Text("この変換は行列で書ける:", color=ORANGE, font_size=22, weight=BOLD)
        matrix_intro.shift(DOWN * 1.1 + LEFT * 3.5)
        self.play(Write(matrix_intro), run_time=0.5)

        matrix_L = MathTex(
            r"L = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix}",
            color=YELLOW, font_size=28
        )
        matrix_L.shift(DOWN * 2.3)
        matrix_L_box = SurroundingRectangle(matrix_L, color=YELLOW, buff=0.15)
        self.play(Write(matrix_L), Create(matrix_L_box), run_time=0.8)
        self.wait(0.7)

        # 表現行列の名称
        repr_label = VGroup(
            Text("この", color=WHITE, font_size=22),
            MathTex(r"L", color=YELLOW, font_size=24),
            Text("を作用素", color=WHITE, font_size=22),
            MathTex(r"\mathcal{L}", color=TEAL, font_size=24),
            Text("の", color=WHITE, font_size=22),
            Text("「表現行列」", color=GOLD, font_size=24, weight=BOLD),
            Text("と呼ぶ", color=WHITE, font_size=22),
        ).arrange(RIGHT, buff=0.12)
        repr_label.shift(DOWN * 3.4)
        repr_box = SurroundingRectangle(repr_label, color=GOLD, buff=0.15)
        self.play(Write(repr_label), Create(repr_box), run_time=0.9)
        self.wait(1.2)

        self.play(
            FadeOut(basis_row), FadeOut(h2_eq),
            FadeOut(coeff_note), FadeOut(coeff_tf),
            FadeOut(matrix_intro), FadeOut(matrix_L), FadeOut(matrix_L_box),
            FadeOut(repr_label), FadeOut(repr_box),
            FadeOut(subtitle7)
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
                    Text("作用素は「関数を関数に変える操作」", color=WHITE, font_size=24),
                    Text("線形性を持つものを線形作用素という", color=YELLOW, font_size=22, weight=BOLD),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("2.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("線形作用素は必ず行列で表現できる", color=WHITE, font_size=24),
                    Text("手順: 関数 → 係数ベクトル → 行列積 → 関数", color=GREEN, font_size=22, weight=BOLD),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("3.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("具体例: 微分の表現行列 (2次多項式基底)", color=WHITE, font_size=24),
                    MathTex(
                        r"L = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix}",
                        color=TEAL, font_size=20
                    ),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("4.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("この行列を「表現行列」と呼ぶ", color=WHITE, font_size=24),
                    Text("※ 基底が変わると表現行列も変わる", color=ORANGE, font_size=22, weight=BOLD),
                ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        summary.scale(0.9)
        summary.shift(UP * 0.3)

        for point in summary:
            self.play(Write(point), run_time=0.7)
            self.wait(0.4)

        self.wait(1.5)

        all_final = VGroup(summary, subtitle_end, title)
        self.play(FadeOut(all_final), run_time=1.0)
        self.wait(0.5)
