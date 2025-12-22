from manim import *

class GramSchmidtOrthogonalization(ThreeDScene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"
        
        # タイトル
        title = Text("グラム-シュミットの直交化法", font_size=40, color=WHITE)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)
        
        # === イントロ: 問題設定 ===
        intro_subtitle = Text("3つのベクトルから直交基底を作る", font_size=32, color=YELLOW)
        intro_subtitle.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(intro_subtitle)
        self.play(Write(intro_subtitle), run_time=0.6)
        self.wait(0.5)
        
        intro_text = VGroup(
            Text("与えられた3つのベクトル:", color=WHITE, font_size=26),
            MathTex(r"|a_1\rangle = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}, \quad"
                   r"|a_2\rangle = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}, \quad"
                   r"|a_3\rangle = \begin{bmatrix} 1 \\ 2 \\ -1 \end{bmatrix}",
                   color=WHITE, font_size=24),
            Text("↓", color=YELLOW, font_size=30),
            Text("直交基底を作りたい!", color=YELLOW, font_size=26, weight=BOLD),
        ).arrange(DOWN, buff=0.3)
        intro_text.shift(DOWN * 0.5)
        self.add_fixed_in_frame_mobjects(intro_text)
        
        self.play(Write(intro_text), run_time=1.2)
        self.wait(1.5)
        
        self.play(FadeOut(intro_text), FadeOut(intro_subtitle))
        self.wait(0.3)
        
        # === パート1: グラム-シュミット法の概要 ===
        subtitle1 = Text("グラム-シュミット法の手順", font_size=32, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle1)
        self.play(Write(subtitle1), run_time=0.6)
        self.wait(0.5)
        
        # 手順の説明
        procedure = VGroup(
            VGroup(
                Text("Step 1:", color=GREEN, font_size=26, weight=BOLD),
                Text("最初のベクトルをそのまま使う", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("Step 2:", color=GREEN, font_size=26, weight=BOLD),
                Text("2番目のベクトルから1番目の成分を引く", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("Step 3:", color=GREEN, font_size=26, weight=BOLD),
                Text("3番目から1番目と2番目の成分を引く", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        procedure.shift(UP * 0.5)
        self.add_fixed_in_frame_mobjects(procedure)
        
        for step in procedure:
            self.play(Write(step), run_time=0.7)
            self.wait(0.5)
        
        self.wait(0.8)
        
        key_idea = Text(
            "キーアイデア: 射影を引いて直交成分を取り出す",
            color=YELLOW, font_size=26, weight=BOLD, slant=ITALIC
        )
        key_idea.shift(DOWN * 1.8)
        self.add_fixed_in_frame_mobjects(key_idea)
        self.play(Write(key_idea), run_time=0.8)
        self.wait(1.2)
        
        self.play(FadeOut(procedure), FadeOut(key_idea), FadeOut(subtitle1))
        self.wait(0.3)
        
        # === パート2: Step 1 - 最初のベクトル ===
        subtitle2 = Text("Step 1: 最初のベクトル", font_size=32, color=GREEN)
        subtitle2.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle2)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)
        
        step1_explanation = Text(
            "最初のベクトルはそのまま使う",
            color=WHITE, font_size=26
        )
        step1_explanation.shift(UP * 1.8)
        self.add_fixed_in_frame_mobjects(step1_explanation)
        self.play(Write(step1_explanation), run_time=0.6)
        self.wait(0.5)
        
        # 3D空間の設定
        self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)
        
        # 座標軸
        axes = ThreeDAxes(
            x_range=[-2, 3, 1],
            y_range=[-2, 3, 1],
            z_range=[-2, 2, 1],
            x_length=6,
            y_length=6,
            z_length=4,
            axis_config={"color": GREY}
        )
        self.play(Create(axes), run_time=0.8)
        self.wait(0.3)
        
        # v1ベクトル
        v1_vector = Arrow3D(
            start=axes.c2p(0, 0, 0),
            end=axes.c2p(1, 1, 0),
            color=RED,
            thickness=0.02,
            height=0.2,
            base_radius=0.08
        )
        v1_label = MathTex(r"|a_1\rangle = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}", 
                          color=RED, font_size=28)
        v1_label.to_corner(UL).shift(DOWN * 2)
        self.add_fixed_orientation_mobjects(v1_label)
        
        self.play(Create(v1_vector), Write(v1_label), run_time=1.0)
        self.wait(0.8)
        
        # u1 = v1
        u1_formula = MathTex(
            r"\mathbf{u}_1 = |a_1\rangle = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}",
            color=RED, font_size=32
        )
        u1_formula.shift(DOWN * 2)
        self.add_fixed_in_frame_mobjects(u1_formula)
        self.play(Write(u1_formula), run_time=0.8)
        self.wait(1.0)
        
        self.play(FadeOut(step1_explanation), FadeOut(u1_formula), FadeOut(v1_label))
        self.wait(0.3)
        
        # === パート3: Step 2 - 2番目のベクトル ===
        self.play(FadeOut(subtitle2))
        subtitle3 = Text("Step 2: 2番目のベクトルを直交化", font_size=32, color=BLUE)
        subtitle3.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle3)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.5)
        
        # v2ベクトルを追加
        v2_vector = Arrow3D(
            start=axes.c2p(0, 0, 0),
            end=axes.c2p(1, 0, 1),
            color=BLUE,
            thickness=0.02,
            height=0.2,
            base_radius=0.08
        )
        v2_label = MathTex(r"|a_2\rangle = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}", 
                          color=BLUE, font_size=28)
        v2_label.to_corner(UL).shift(DOWN * 2.5 + LEFT * (-9))
        self.add_fixed_orientation_mobjects(v2_label)
        
        self.play(Create(v2_vector), Write(v2_label), run_time=1.0)
        self.wait(0.8)
        
        # 射影の公式を表示
        projection_formula = MathTex(
            r"\text{proj}_{\mathbf{u}_1} |a_2\rangle = "
            r"\frac{\langle a_2 | \mathbf{u}_1 \rangle}{\langle \mathbf{u}_1 | \mathbf{u}_1 \rangle} \mathbf{u}_1",
            color=YELLOW, font_size=28
        )
        projection_formula.to_corner(UR).shift(DOWN * 1.5)
        self.add_fixed_in_frame_mobjects(projection_formula)
        self.play(Write(projection_formula), run_time=0.8)
        self.wait(0.8)
        
        # 内積の計算
        inner_product_calc = VGroup(
            MathTex(r"\langle a_2 | \mathbf{u}_1 \rangle = 1 \cdot 1 + 0 \cdot 1 + 1 \cdot 0 = 1", 
                   color=WHITE, font_size=24),
            MathTex(r"\langle \mathbf{u}_1 | \mathbf{u}_1 \rangle = 1^2 + 1^2 + 0^2 = 2", 
                   color=WHITE, font_size=24),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        inner_product_calc.to_corner(UR).shift(DOWN * 2.5)
        self.add_fixed_in_frame_mobjects(inner_product_calc)
        self.play(Write(inner_product_calc), run_time=1.0)
        self.wait(0.8)
        
        # 射影ベクトルを描画
        proj_v2_u1 = Arrow3D(
            start=axes.c2p(0, 0, 0),
            end=axes.c2p(0.5, 0.5, 0),
            color=YELLOW,
            thickness=0.015,
            height=0.15,
            base_radius=0.06
        )
        proj_label = MathTex(r"\text{proj}_{\mathbf{u}_1} |a_2\rangle", 
                            color=YELLOW, font_size=24)
        proj_label.next_to(axes.c2p(0.5, 0.5, 0), DOWN, buff=0.1).shift(UP*0.5 + LEFT*1.2)
        self.add_fixed_orientation_mobjects(proj_label)
        
        self.play(Create(proj_v2_u1), Write(proj_label), run_time=0.8)
        self.wait(0.8)
        
        # u2の計算
        u2_calc = MathTex(
            r"\mathbf{u}_2 = |a_2\rangle - \text{proj}_{\mathbf{u}_1} |a_2\rangle",
            color=GREEN, font_size=28
        )
        u2_calc.shift(DOWN * 2.2)
        self.add_fixed_in_frame_mobjects(u2_calc)
        self.play(Write(u2_calc), run_time=0.8)
        self.wait(0.6)
        
        u2_result = MathTex(
            r"= \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix} - \frac{1}{2}\begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}"
            r"= \begin{bmatrix} 1/2 \\ -1/2 \\ 1 \end{bmatrix}",
            color=GREEN, font_size=26
        )
        u2_result.next_to(u2_calc, DOWN, buff=0.3)
        self.add_fixed_in_frame_mobjects(u2_result)
        self.play(Write(u2_result), run_time=1.0)
        self.wait(0.8)
        
        # u2ベクトルを描画
        u2_vector = Arrow3D(
            start=axes.c2p(0, 0, 0),
            end=axes.c2p(0.5, -0.5, 1),
            color=GREEN,
            thickness=0.02,
            height=0.2,
            base_radius=0.08
        )
        u2_label_3d = MathTex(r"\mathbf{u}_2", color=GREEN, font_size=28)
        u2_label_3d.next_to(axes.c2p(0.5, -0.5, 1), RIGHT, buff=0.1)
        self.add_fixed_orientation_mobjects(u2_label_3d)
        
        self.play(Create(u2_vector), Write(u2_label_3d), run_time=0.8)
        self.wait(1.0)
        
        # 直交性の確認
        orthogonal_check = MathTex(
            r"\langle \mathbf{u}_1 | \mathbf{u}_2 \rangle = 1 \cdot \frac{1}{2} + 1 \cdot (-\frac{1}{2}) + 0 \cdot 1 = 0 \,\checkmark",
            color=YELLOW, font_size=24
        )
        orthogonal_check.to_corner(DR).shift(UP * 0.5)
        self.add_fixed_in_frame_mobjects(orthogonal_check)
        self.play(Write(orthogonal_check), run_time=0.8)
        self.wait(1.2)
        
        self.play(
            FadeOut(projection_formula), FadeOut(inner_product_calc),
            FadeOut(proj_v2_u1), FadeOut(proj_label),
            FadeOut(u2_calc), FadeOut(u2_result),
            FadeOut(orthogonal_check), FadeOut(v2_label), FadeOut(u2_label_3d)
        )
        self.wait(0.3)
        
        # === パート4: Step 3 - 3番目のベクトル ===
        self.play(FadeOut(subtitle3), FadeOut(v2_vector))
        subtitle4 = Text("Step 3: 3番目のベクトルを直交化", font_size=32, color=PURPLE)
        subtitle4.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle4)
        self.play(Write(subtitle4), run_time=0.6)
        self.wait(0.5)
        
        # v3ベクトルを追加
        v3_vector = Arrow3D(
            start=axes.c2p(0, 0, 0),
            end=axes.c2p(1, 2, -1),
            color=ORANGE,
            thickness=0.02,
            height=0.2,
            base_radius=0.08
        )
        v3_label = MathTex(r"|a_3\rangle = \begin{bmatrix} 1 \\ 2 \\ -1 \end{bmatrix}", 
                          color=ORANGE, font_size=28)
        v3_label.to_corner(UR).shift(DOWN * 7 + LEFT * 3)
        self.add_fixed_orientation_mobjects(v3_label)
        
        self.play(Create(v3_vector), Write(v3_label), run_time=1.0)
        self.wait(0.8)
        
        # u3の公式
        u3_formula = MathTex(
            r"\mathbf{u}_3 = |a_3\rangle - \text{proj}_{\mathbf{u}_1} |a_3\rangle - \text{proj}_{\mathbf{u}_2} |a_3\rangle",
            color=PURPLE, font_size=26
        )
        u3_formula.shift(UP * 1.8)
        self.add_fixed_in_frame_mobjects(u3_formula)
        self.play(Write(u3_formula), run_time=0.8)
        self.wait(0.8)
        
        # 射影の計算
        proj_calc_title = Text("射影の計算:", color=ORANGE, font_size=24, weight=BOLD)
        proj_calc_title.to_corner(UR).shift(DOWN * 1.5 )
        self.add_fixed_in_frame_mobjects(proj_calc_title)
        self.play(Write(proj_calc_title), run_time=0.5)
        self.wait(0.3)
        
        proj_calculations = VGroup(
            MathTex(r"\langle a_3 | \mathbf{u}_1 \rangle = 1 + 2 + 0 = 3", color=WHITE, font_size=22),
            MathTex(r"\text{proj}_{\mathbf{u}_1} |a_3\rangle = \frac{3}{2}\begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}", 
                   color=WHITE, font_size=22),
            MathTex(r"\langle a_3 | \mathbf{u}_2 \rangle = \frac{1}{2} - 1 - 1 = -\frac{3}{2}", 
                   color=WHITE, font_size=22),
            MathTex(r"\langle \mathbf{u}_2 | \mathbf{u}_2 \rangle = \frac{1}{4} + \frac{1}{4} + 1 = \frac{3}{2}", 
                   color=WHITE, font_size=22),
            MathTex(r"\text{proj}_{\mathbf{u}_2} |a_3\rangle = -1 \cdot \begin{bmatrix} 1/2 \\ -1/2 \\ 1 \end{bmatrix}", 
                   color=WHITE, font_size=22),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        proj_calculations.to_corner(UR).shift(DOWN * 2)
        self.add_fixed_in_frame_mobjects(proj_calculations)
        self.play(Write(proj_calculations), run_time=1.5)
        self.wait(1.0)
        
        # u3の結果
        u3_calc = MathTex(
            r"\mathbf{u}_3 = \begin{bmatrix} 1 \\ 2 \\ -1 \end{bmatrix} - "
            r"\begin{bmatrix} 3/2 \\ 3/2 \\ 0 \end{bmatrix} - "
            r"\begin{bmatrix} -1/2 \\ 1/2 \\ -1 \end{bmatrix}",
            color=PURPLE, font_size=24
        )
        u3_calc.shift(DOWN * 2.2 + RIGHT * 1.5)
        self.add_fixed_in_frame_mobjects(u3_calc)
        self.play(Write(u3_calc), run_time=1.0)
        self.wait(0.6)
        
        u3_result = MathTex(
            r"= \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}",
            color=RED, font_size=28
        )
        u3_result.next_to(u3_calc, DOWN, buff=0.3)
        self.add_fixed_in_frame_mobjects(u3_result)
        self.play(Write(u3_result), run_time=0.8)
        self.wait(1.0)
        
        # 重要な結論
        conclusion_text = VGroup(
            Text("重要な発見!", color=RED, font_size=26, weight=BOLD),
            Text("|a₃⟩は |a₁⟩ と |a₂⟩ の線形結合で表せる", color=YELLOW, font_size=24),
            Text("→ 3つのベクトルは独立ではない", color=YELLOW, font_size=24),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        conclusion_text.to_corner(DL).shift(UP * 0.5)
        self.add_fixed_in_frame_mobjects(conclusion_text)
        self.play(Write(conclusion_text), run_time=1.0)
        self.wait(1.5)
        
        self.play(
            FadeOut(v3_vector), FadeOut(v3_label),
            FadeOut(u3_formula), FadeOut(proj_calc_title),
            FadeOut(proj_calculations), FadeOut(u3_calc),
            FadeOut(u3_result), FadeOut(conclusion_text),
            FadeOut(subtitle4)
        )
        self.wait(0.3)
        
        # === パート5: 結果の確認 ===
        subtitle5 = Text("得られた直交基底", font_size=32, color=GOLD)
        subtitle5.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle5)
        self.play(Write(subtitle5), run_time=0.6)
        self.wait(0.5)
        
        # カメラを回転させて見やすくする
        self.move_camera(phi=60 * DEGREES, theta=30 * DEGREES, run_time=1.5)
        self.wait(0.5)
        
        # 結果のまとめ
        result_summary = VGroup(
            Text("直交基底:", color=GOLD, font_size=26, weight=BOLD),
            MathTex(
                r"\mathbf{u}_1 = \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}",
                color=RED, font_size=24
            ),
            MathTex(
                r"\mathbf{u}_2 = \begin{bmatrix} 1/2 \\ -1/2 \\ 1 \end{bmatrix}",
                color=GREEN, font_size=24
            ),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        result_summary.to_corner(UL).shift(DOWN * 1.5 + RIGHT * 0.5)
        self.add_fixed_in_frame_mobjects(result_summary)
        self.play(Write(result_summary), run_time=1.0)
        self.wait(0.8)
        
        # 直交性の確認
        orthogonality = VGroup(
            Text("直交性の確認:", color=YELLOW, font_size=24, weight=BOLD),
            MathTex(r"\langle \mathbf{u}_1 | \mathbf{u}_2 \rangle = 0 \,\checkmark", color=GREEN, font_size=22),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        orthogonality.to_corner(DR).shift(UP * 1)
        self.add_fixed_in_frame_mobjects(orthogonality)
        self.play(Write(orthogonality), run_time=0.8)
        self.wait(1.0)
        
        # u1とu2が張る平面を可視化
        # 平面をパラメトリック表現: s*u1 + t*u2
        u1_coords = np.array([1, 1, 0])
        u2_coords = np.array([0.5, -0.5, 1])
        
        plane_surface = Surface(
            lambda u, v: axes.c2p(*(u * u1_coords + v * u2_coords)),
            u_range=[-1.5, 1.5],
            v_range=[-1.5, 1.5],
            resolution=(10, 10),
            fill_color=TEAL,
            fill_opacity=0.3,
            stroke_color=TEAL,
            stroke_opacity=0.5
        )
        
        plane_note = Text(
            "u₁とu₂が張る平面",
            color=TEAL, font_size=24, slant=ITALIC
        )
        plane_note.to_corner(DL).shift(UP * 0.5)
        self.add_fixed_in_frame_mobjects(plane_note)
        
        self.play(Create(plane_surface), run_time=1.0)
        self.play(Write(plane_note), run_time=0.6)
        self.wait(1.2)
        
        self.play(FadeOut(plane_surface), run_time=0.5)
        
        self.play(
            FadeOut(result_summary), FadeOut(orthogonality),
            FadeOut(plane_note), FadeOut(subtitle5)
        )
        self.wait(0.3)
        
        # === まとめ ===
        # カメラを正面に戻す
        self.play(
            FadeOut(axes), FadeOut(v1_vector), FadeOut(u2_vector),
            run_time=1.0
        )
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, run_time=1.0)
        self.wait(0.3)
        
        summary_subtitle = Text("まとめ", font_size=36, color=GOLD, weight=BOLD)
        summary_subtitle.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(summary_subtitle)
        self.play(Write(summary_subtitle), run_time=0.6)
        self.wait(0.5)
        
        # まとめのポイント
        summary_points = VGroup(
            VGroup(
                Text("1.", color=WHITE, font_size=26, weight=BOLD),
                Text("グラム-シュミット法で直交基底を構成", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("2.", color=WHITE, font_size=26, weight=BOLD),
                Text("各ベクトルから既存の成分を射影で引く", color=WHITE, font_size=24),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("3.", color=WHITE, font_size=26, weight=BOLD),
                Text("結果: 2つの直交ベクトルを得た", color=YELLOW, font_size=24),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            VGroup(
                Text("※それぞれ正規化すると教科書のように正規直交基底に", color=GREEN, font_size=24),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        summary_points.shift(UP * 0.3)
        self.add_fixed_in_frame_mobjects(summary_points)
        
        for point in summary_points:
            self.play(Write(point), run_time=0.6)
            self.wait(0.4)
        
        self.wait(0.5)
        
        # 最終メッセージ
        final_message = Text(
            "内積と射影で直交性を作り出す",
            color=YELLOW, font_size=28, weight=BOLD, slant=ITALIC
        )
        final_message.shift(DOWN * 2.5)
        self.add_fixed_in_frame_mobjects(final_message)
        self.play(Write(final_message), run_time=0.8)
        self.wait(1.5)
        
        self.wait(2.0)
        
        # フェードアウト
        all_objects = VGroup(
            title, summary_subtitle, summary_points, final_message
        )
        self.play(FadeOut(all_objects), run_time=1.0)
        self.wait(0.5)
