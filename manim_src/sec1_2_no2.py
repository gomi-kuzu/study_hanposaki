from manim import *

class VectorDecomposition(Scene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"
        
        # 座標平面を作成
        plane = NumberPlane(
            x_range=[-1, 6],
            y_range=[-1, 5],
            x_length=10,
            y_length=8,
            axis_config={"color": GRAY},
            background_line_style={
                "stroke_color": GRAY,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        )
        plane.add_coordinates()
        self.add(plane)
        
        # タイトル
        title = Text("ベクトルの1次結合による「分解する」という視点", font_size=32, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # === パート1: 正しい基底での分解 ===
        subtitle1 = Text("任意のベクトルは、特定のベクトルに分解できる", font_size=28, color=YELLOW)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1))
        self.wait(1)
        
        # 目標ベクトル
        target_vec = Vector([3, 2], color=YELLOW)
        target_vec.put_start_and_end_on(plane.c2p(0, 0), plane.c2p(3, 2))
        target_label = MathTex(r"\boldsymbol{v} = \begin{bmatrix} 3 \\ 2 \end{bmatrix}", color=YELLOW)
        target_label.next_to(target_vec.get_center(), UP, buff=0.3)
        
        self.play(Create(target_vec), Write(target_label))
        self.wait(1)
        
        # 説明テキスト
        question = Text("このベクトルを分解できるか？", font_size=24, color=WHITE)
        question.to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(question))
        self.wait(1)
        
        # 基底ベクトル
        basis1 = Vector([1, 0], color=BLUE)
        basis1.put_start_and_end_on(plane.c2p(0, 0), plane.c2p(1, 0))
        basis1_label = MathTex(r"\boldsymbol{e}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}", color=BLUE)
        basis1_label.next_to(basis1.get_end(), DOWN, buff=0.2)
        
        basis2 = Vector([0, 1], color=GREEN)
        basis2.put_start_and_end_on(plane.c2p(0, 0), plane.c2p(0, 1))
        basis2_label = MathTex(r"\boldsymbol{e}_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}", color=GREEN)
        basis2_label.next_to(basis2.get_end(), LEFT, buff=0.2)
        
        self.play(
            FadeOut(question),
            Create(basis1), Write(basis1_label),
            Create(basis2), Write(basis2_label)
        )
        self.wait(1)
        
        # 分解の式
        decomp_formula = MathTex(
            r"\boldsymbol{v} = 3\boldsymbol{e}_1 + 2\boldsymbol{e}_2",
            color=WHITE,
            font_size=36
        )
        decomp_formula.to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(decomp_formula))
        self.wait(1)
        
        # 3e1 を継ぎ足しで表示
        # 1つ目のe1
        basis1_copy1 = basis1.copy()
        self.play(Indicate(basis1))
        self.wait(0.3)
        
        # 2つ目のe1を継ぎ足し
        basis1_2 = Vector([1, 0], color=BLUE)
        basis1_2.put_start_and_end_on(plane.c2p(1, 0), plane.c2p(2, 0))
        self.play(Create(basis1_2))
        self.wait(0.3)
        
        # 3つ目のe1を継ぎ足し
        basis1_3 = Vector([1, 0], color=BLUE)
        basis1_3.put_start_and_end_on(plane.c2p(2, 0), plane.c2p(3, 0))
        self.play(Create(basis1_3))
        self.wait(0.5)
        
        # ラベルを更新
        basis1_scaled_label = MathTex(r"3\boldsymbol{e}_1", color=BLUE)
        basis1_scaled_label.next_to(plane.c2p(1.5, 0), DOWN, buff=0.2)
        self.play(
            FadeOut(basis1_label),
            Write(basis1_scaled_label)
        )
        self.wait(1)
        
        # 2e2 を継ぎ足しで表示
        # 1つ目のe2
        self.play(Indicate(basis2))
        self.wait(0.3)
        
        # 2つ目のe2を継ぎ足し
        basis2_2 = Vector([0, 1], color=GREEN)
        basis2_2.put_start_and_end_on(plane.c2p(0, 1), plane.c2p(0, 2))
        self.play(Create(basis2_2))
        self.wait(0.5)
        
        # ラベルを更新
        basis2_scaled_label = MathTex(r"2\boldsymbol{e}_2", color=GREEN)
        basis2_scaled_label.next_to(plane.c2p(0, 1), LEFT, buff=0.2)
        self.play(
            FadeOut(basis2_label),
            Write(basis2_scaled_label)
        )
        self.wait(1)
        
        # 2e2 を 3e1 の先端に移動（全体を移動）
        basis2_group = VGroup(basis2, basis2_2)
        basis2_shifted_1 = Vector([0, 1], color=GREEN)
        basis2_shifted_1.put_start_and_end_on(plane.c2p(3, 0), plane.c2p(3, 1))
        basis2_shifted_2 = Vector([0, 1], color=GREEN)
        basis2_shifted_2.put_start_and_end_on(plane.c2p(3, 1), plane.c2p(3, 2))
        
        basis2_label_shifted = basis2_scaled_label.copy()
        basis2_label_shifted.next_to(plane.c2p(3, 1), RIGHT, buff=0.2)
        
        self.play(
            Transform(basis2, basis2_shifted_1),
            Transform(basis2_2, basis2_shifted_2),
            Transform(basis2_scaled_label, basis2_label_shifted)
        )
        self.wait(1)
        
        # 大きなベクトルを消す演出
        self.play(
            FadeOut(target_vec),
            FadeOut(target_label),
            run_time=1
        )
        self.wait(1)
        
        # 成功メッセージ
        success_msg = Text("分解成功！", font_size=32, color=GREEN)
        success_msg.next_to(decomp_formula, DOWN, buff=0.3)
        self.play(
            Write(success_msg),
            run_time=1
        )
        self.wait(1)
                
        # クリア
        self.play(
            FadeOut(basis1), FadeOut(basis1_2), FadeOut(basis1_3), FadeOut(basis1_scaled_label),
            FadeOut(basis2), FadeOut(basis2_2), FadeOut(basis2_scaled_label),
            FadeOut(decomp_formula), FadeOut(success_msg),
            FadeOut(subtitle1)
        )
        self.wait(1)
        
        # === パート1.5: 直交していない基底でも分解可能 ===
        subtitle1_5 = Text("ちなみに…直行していないベクトルにも分解は可能", font_size=28, color=YELLOW)
        subtitle1_5.next_to(title, DOWN)
        self.play(Write(subtitle1_5))
        self.wait(1)
        
        # 目標ベクトル
        target_vec1_5 = Vector([3, 2], color=YELLOW)
        target_vec1_5.put_start_and_end_on(plane.c2p(0, 0), plane.c2p(3, 2))
        target_label1_5 = MathTex(r"\boldsymbol{v} = \begin{bmatrix} 3 \\ 2 \end{bmatrix}", color=YELLOW)
        target_label1_5.next_to(target_vec1_5.get_center(), UP, buff=0.3)
        
        self.play(Create(target_vec1_5), Write(target_label1_5))
        self.wait(1)
        
        # 直交していない基底（でも線形独立）
        non_ortho_basis1 = Vector([1, 0], color=BLUE)
        non_ortho_basis1.put_start_and_end_on(plane.c2p(0, 0), plane.c2p(1, 0))
        non_ortho_basis1_label = MathTex(r"\boldsymbol{f}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}", color=BLUE)
        non_ortho_basis1_label.next_to(non_ortho_basis1.get_end(), DOWN, buff=0.2)
        
        non_ortho_basis2 = Vector([1, 1], color=GREEN)
        non_ortho_basis2.put_start_and_end_on(plane.c2p(0, 0), plane.c2p(1, 1))
        non_ortho_basis2_label = MathTex(r"\boldsymbol{f}_2 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}", color=GREEN)
        non_ortho_basis2_label.next_to(non_ortho_basis2.get_end(), UP + LEFT, buff=0.2)
        
        self.play(
            Create(non_ortho_basis1), Write(non_ortho_basis1_label),
            Create(non_ortho_basis2), Write(non_ortho_basis2_label)
        )
        self.wait(1)
        
        # 説明テキスト
        non_ortho_text = Text("この2つは直交していない…", font_size=24, color=WHITE)
        non_ortho_text.to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(non_ortho_text))
        self.wait(1)
        
        # でも分解できる
        decomp_formula1_5 = MathTex(
            r"\boldsymbol{v} = 1\boldsymbol{f}_1 + 2\boldsymbol{f}_2",
            color=WHITE,
            font_size=36
        )
        decomp_formula1_5.next_to(non_ortho_text, DOWN, buff=0.3)
        self.play(Write(decomp_formula1_5))
        self.wait(1)
        
        # 1f1 を表示（そのまま）
        self.play(Indicate(non_ortho_basis1))
        self.wait(0.5)
        
        f1_scaled_label = MathTex(r"1\boldsymbol{f}_1", color=BLUE)
        f1_scaled_label.next_to(non_ortho_basis1.get_end(), DOWN, buff=0.2)
        self.play(
            FadeOut(non_ortho_basis1_label),
            Write(f1_scaled_label)
        )
        self.wait(1)
        
        # 2f2 を継ぎ足しで表示
        self.play(Indicate(non_ortho_basis2))
        self.wait(0.3)
        
        # 2つ目のf2を継ぎ足し
        non_ortho_basis2_2 = Vector([1, 1], color=GREEN)
        non_ortho_basis2_2.put_start_and_end_on(plane.c2p(1, 1), plane.c2p(2, 2))
        self.play(Create(non_ortho_basis2_2))
        self.wait(0.5)
        
        # ラベルを更新
        f2_scaled_label = MathTex(r"2\boldsymbol{f}_2", color=GREEN)
        f2_scaled_label.next_to(plane.c2p(0.5, 0.5), LEFT, buff=0.2)
        self.play(
            FadeOut(non_ortho_basis2_label),
            Write(f2_scaled_label)
        )
        self.wait(1)
        
        # 2f2 を 1f1 の先端に移動
        basis2_group_1_5 = VGroup(non_ortho_basis2, non_ortho_basis2_2)
        f2_shifted_1 = Vector([1, 1], color=GREEN)
        f2_shifted_1.put_start_and_end_on(plane.c2p(1, 0), plane.c2p(2, 1))
        f2_shifted_2 = Vector([1, 1], color=GREEN)
        f2_shifted_2.put_start_and_end_on(plane.c2p(2, 1), plane.c2p(3, 2))
        
        f2_label_shifted = f2_scaled_label.copy()
        f2_label_shifted.next_to(plane.c2p(2, 1), RIGHT, buff=0.2)
        
        self.play(
            Transform(non_ortho_basis2, f2_shifted_1),
            Transform(non_ortho_basis2_2, f2_shifted_2),
            Transform(f2_scaled_label, f2_label_shifted)
        )
        self.wait(1)
        
        # 大きなベクトルを消す演出
        self.play(
            FadeOut(target_vec1_5),
            FadeOut(target_label1_5),
            run_time=1
        )
        self.wait(1)
        
        # 成功メッセージ
        success_msg1_5 = Text("分解成功！", 
                             font_size=28, color=GREEN, line_spacing=1.2)
        success_msg1_5.to_corner(DOWN + RIGHT, buff=0.5)
        self.play(
            Write(success_msg1_5),
            run_time=1
        )
        self.wait(1)
                
        # クリア
        self.play(
            FadeOut(non_ortho_basis1), FadeOut(f1_scaled_label),
            FadeOut(non_ortho_basis2), FadeOut(non_ortho_basis2_2), FadeOut(f2_scaled_label),
            FadeOut(decomp_formula1_5), FadeOut(success_msg1_5),
            FadeOut(non_ortho_text), FadeOut(subtitle1_5)
        )
        self.wait(1)
        
        # === パート2: 不適切な基底での失敗 ===
        subtitle2 = Text("ただし、分解パーツを間違えると分解できない…", font_size=28, color=YELLOW)
        subtitle2.next_to(title, DOWN)
        self.play(Write(subtitle2))
        self.wait(1)
        
        # 同じ目標ベクトル
        target_vec2 = Vector([3, 2], color=YELLOW)
        target_vec2.put_start_and_end_on(plane.c2p(0, 0), plane.c2p(3, 2))
        target_label2 = MathTex(r"\boldsymbol{v} = \begin{bmatrix} 3 \\ 2 \end{bmatrix}", color=YELLOW)
        target_label2.next_to(target_vec2.get_center(), UP, buff=0.3)
        
        self.play(Create(target_vec2), Write(target_label2))
        self.wait(1)
        
        # 不適切な基底（線形従属）
        bad_basis1 = Vector([1, 1], color=BLUE)
        bad_basis1.put_start_and_end_on(plane.c2p(0, 0), plane.c2p(1, 1))
        bad_basis1_label = MathTex(r"\boldsymbol{b}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}", color=BLUE)
        bad_basis1_label.next_to(bad_basis1.get_end(), UP + LEFT, buff=0.2)
        
        bad_basis2 = Vector([2, 2], color=GREEN)
        bad_basis2.put_start_and_end_on(plane.c2p(0, 0), plane.c2p(2, 2))
        bad_basis2_label = MathTex(r"\boldsymbol{b}_2 = \begin{bmatrix} 2 \\ 2 \end{bmatrix}", color=GREEN)
        bad_basis2_label.next_to(bad_basis2.get_end(), UP + LEFT, buff=0.2)
        
        self.play(
            Create(bad_basis1), Write(bad_basis1_label),
            Create(bad_basis2), Write(bad_basis2_label)
        )
        self.wait(1)
        
        # 問題点の説明
        problem_text = Text("この2つのベクトルは同じ方向！", font_size=24, color=RED)
        problem_text.to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(problem_text))
        self.wait(1)
        
        # 線形従属の説明
        linearly_dependent = MathTex(
            r"\boldsymbol{b}_2 = 2\boldsymbol{b}_1",
            color=RED,
            font_size=36
        )
        linearly_dependent.next_to(problem_text, DOWN, buff=0.3)
        self.play(Write(linearly_dependent))
        self.wait(1)
        
        # 分解不可能を視覚化
        # どんなスカラ倍をしても目標ベクトルに到達できない
        attempt_text = Text("このベクトルをどんな組み合わせにしても...", font_size=20, color=YELLOW)
        attempt_text.move_to([3.5, 1.8, 0])
        self.play(Write(attempt_text))
        
        # いくつかの試行を表示
        test_vec1 = Vector([1.5, 1.5], color=PURPLE)
        test_vec1.put_start_and_end_on(plane.c2p(0, 0), plane.c2p(1.5, 1.5))
        self.play(Create(test_vec1))
        self.wait(0.5)
        
        test_vec2 = Vector([2.5, 2.5], color=PURPLE)
        test_vec2.put_start_and_end_on(plane.c2p(0, 0), plane.c2p(2.5, 2.5))
        self.play(Transform(test_vec1, test_vec2))
        self.wait(0.5)
        
        test_vec3 = Vector([3.5, 3.5], color=PURPLE)
        test_vec3.put_start_and_end_on(plane.c2p(0, 0), plane.c2p(3.5, 3.5))
        self.play(Transform(test_vec1, test_vec3))
        self.wait(0.5)
        
        # 失敗のクロスマーク
        cross1 = Line(
            plane.c2p(2.5, 1.5), plane.c2p(3.5, 2.5),
            color=RED, stroke_width=8
        )
        cross2 = Line(
            plane.c2p(3.5, 1.5), plane.c2p(2.5, 2.5),
            color=RED, stroke_width=8
        )
        
        self.play(
            FadeOut(test_vec1),
            Create(cross1), Create(cross2)
        )
        self.wait(1)
        
        # 失敗メッセージ
        fail_msg = Text("分解不可能！", font_size=32, color=RED)
        fail_msg.to_corner(DOWN + RIGHT, buff=0.5)
        self.play(Write(fail_msg))
        self.wait(2)
        
        # クリア
        self.play(
            FadeOut(target_vec2), FadeOut(target_label2),
            FadeOut(bad_basis1), FadeOut(bad_basis1_label),
            FadeOut(bad_basis2), FadeOut(bad_basis2_label),
            FadeOut(problem_text), FadeOut(linearly_dependent),
            FadeOut(attempt_text), FadeOut(cross1), FadeOut(cross2),
            FadeOut(fail_msg), FadeOut(subtitle2)
        )
        self.wait(1)
        
        # === パート3: 正しい基底の条件 ===

        # subtitle3 = Text("線形独立な基底が必要", font_size=28, color=YELLOW)
        # subtitle3.next_to(title, DOWN)
        # self.play(Write(subtitle3))
        # self.wait(1)
        
        # # 同じ目標ベクトル
        # target_vec3 = Vector([3, 2], color=YELLOW)
        # target_vec3.put_start_and_end_on(plane.c2p(0, 0), plane.c2p(3, 2))
        # target_label3 = MathTex(r"\boldsymbol{v} = \begin{bmatrix} 3 \\ 2 \end{bmatrix}", color=YELLOW)
        # target_label3.next_to(target_vec3.get_center(), UP, buff=0.3)
        
        # self.play(Create(target_vec3), Write(target_label3))
        # self.wait(1)
        
        # # 異なる方向の基底
        # good_basis1 = Vector([1, 0], color=BLUE)
        # good_basis1.put_start_and_end_on(plane.c2p(0, 0), plane.c2p(1, 0))
        # good_basis1_label = MathTex(r"\boldsymbol{u}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}", color=BLUE)
        # good_basis1_label.next_to(good_basis1.get_end(), DOWN, buff=0.2)
        
        # good_basis2 = Vector([0, 1], color=GREEN)
        # good_basis2.put_start_and_end_on(plane.c2p(0, 0), plane.c2p(0, 1))
        # good_basis2_label = MathTex(r"\boldsymbol{u}_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}", color=GREEN)
        # good_basis2_label.next_to(good_basis2.get_end(), LEFT, buff=0.2)
        
        # self.play(
        #     Create(good_basis1), Write(good_basis1_label),
        #     Create(good_basis2), Write(good_basis2_label)
        # )
        # self.wait(1)
        
        # # 線形独立の条件
        # condition_text = Text("この2つは線形独立（異なる方向）", font_size=24, color=GREEN)
        # condition_text.to_edge(DOWN).shift(UP * 0.5)
        # self.play(Write(condition_text))
        # self.wait(1)
        
        # # 分解の式
        # final_formula = MathTex(
        #     r"\boldsymbol{v} = 3\boldsymbol{u}_1 + 2\boldsymbol{u}_2",
        #     color=WHITE,
        #     font_size=36
        # )
        # final_formula.next_to(condition_text, DOWN, buff=0.3)
        # self.play(Write(final_formula))
        # self.wait(1)
        
        # # 分解の可視化（継ぎ足し表現）
        # # 3u1を継ぎ足し
        # self.play(Indicate(good_basis1))
        # self.wait(0.3)
        
        # comp1_2 = Vector([1, 0], color=BLUE)
        # comp1_2.put_start_and_end_on(plane.c2p(1, 0), plane.c2p(2, 0))
        # self.play(Create(comp1_2))
        # self.wait(0.3)
        
        # comp1_3 = Vector([1, 0], color=BLUE)
        # comp1_3.put_start_and_end_on(plane.c2p(2, 0), plane.c2p(3, 0))
        # self.play(Create(comp1_3))
        # self.wait(0.5)
        
        # # 2u2を継ぎ足し
        # self.play(
        #     FadeOut(good_basis1_label),
        #     FadeOut(good_basis2_label)
        # )
        
        # comp2_1 = Vector([0, 1], color=GREEN)
        # comp2_1.put_start_and_end_on(plane.c2p(3, 0), plane.c2p(3, 1))
        # self.play(
        #     Transform(good_basis2, comp2_1)
        # )
        # self.wait(0.3)
        
        # comp2_2 = Vector([0, 1], color=GREEN)
        # comp2_2.put_start_and_end_on(plane.c2p(3, 1), plane.c2p(3, 2))
        # self.play(Create(comp2_2))
        # self.wait(1)
        
        # # 最終メッセージ
        # final_message = Text("基底が線形独立なら\nどんなベクトルも分解できる！", 
        #                     font_size=28, color=GREEN, line_spacing=1.2)
        # final_message.to_corner(DOWN + LEFT, buff=0.5)
        
        # self.play(
        #     Indicate(target_vec3),
        #     Indicate(final_formula),
        #     run_time=2
        # )
        # self.play(Write(final_message))
        # self.wait(3)
