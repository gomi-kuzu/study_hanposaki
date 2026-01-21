from manim import *

class ProjectionAndOrthogonalization(ThreeDScene):
    def construct(self):
        # 背景色を設定
        self.camera.background_color = "#012817"
        
        # タイトル
        title = Text("射影と観測装置で理解する直交化", font_size=40, color=WHITE)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)
        
        # === イントロ: 前回の復習 ===
        # intro_subtitle = Text("前回の復習: 正規化ベクトルとの内積", font_size=32, color=YELLOW)
        # intro_subtitle.next_to(title, DOWN)
        # self.add_fixed_in_frame_mobjects(intro_subtitle)
        # self.play(Write(intro_subtitle), run_time=0.6)
        # self.wait(0.5)
        
        intro_text = VGroup(
            Text("再掲：正規化ベクトルとの内積 → 影の長さ", color=WHITE, font_size=32, weight=BOLD),
            MathTex(r"\langle \mathbf{u}_1 | \mathbf{x} \rangle = \|\mathbf{x}\| \cos\theta", 
                   color=YELLOW, font_size=32),
            Text("||u₁|| = 1 のとき、内積 = u₁方向への射影", color=GREEN, font_size=24),
        ).arrange(DOWN, buff=0.4)
        intro_text.shift(DOWN * 0.5)
        self.add_fixed_in_frame_mobjects(intro_text)
        
        self.play(Write(intro_text), run_time=1.2)
        self.wait(1.5)
        
        self.play(FadeOut(intro_text))
        self.wait(0.3)
        
        # === パート1: 3次元空間の設定 ===
        # subtitle1 = Text("3次元空間でのベクトル分解", font_size=32, color=BLUE)
        # subtitle1.next_to(title, DOWN)
        # self.add_fixed_in_frame_mobjects(subtitle1)
        # self.play(Write(subtitle1), run_time=0.6)
        # self.wait(0.5)
        
        # 3D空間の設定
        self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)
        
        # 座標軸
        axes = ThreeDAxes(
            x_range=[-1, 3, 1],
            y_range=[-1, 3, 1],
            z_range=[-1, 3, 1],
            x_length=6,
            y_length=6,
            z_length=5,
            axis_config={"color": GREY, "stroke_width": 2}
        )
        axes.shift(UP+RIGHT*2)  # 座標軸を少し下げる
        
        axis_labels = axes.get_axis_labels(
            MathTex("x", font_size=24),
            MathTex("y", font_size=24),
            MathTex("z", font_size=24)
        )
        
        self.play(Create(axes), Write(axis_labels), run_time=1.0)
        self.wait(0.5)
        
        # 直交する正規化ベクトル u1, u2を設定
        # u1 = (1, 0, 0) / sqrt(1) = (1, 0, 0)
        u1_end = np.array([1, 0, 0])
        u1_vector = Arrow3D(
            start=axes.c2p(0, 0, 0),
            end=axes.c2p(*u1_end),
            color=RED,
            thickness=0.025,
            height=0.25,
            base_radius=0.1
        )
        u1_label = MathTex(r"|\mathbf{u}_1\rangle", color=RED, font_size=30)
        u1_label.next_to(axes.c2p(*u1_end), DOWN+RIGHT, buff=0.2)
        self.add_fixed_orientation_mobjects(u1_label)
        
        self.play(Create(u1_vector), Write(u1_label), run_time=0.8)
        self.wait(0.5)
        
        # u2 = (0, 1, 0) / sqrt(1) = (0, 1, 0)
        u2_end = np.array([0, 1, 0])
        u2_vector = Arrow3D(
            start=axes.c2p(0, 0, 0),
            end=axes.c2p(*u2_end),
            color=GREEN,
            thickness=0.025,
            height=0.25,
            base_radius=0.1
        )
        u2_label = MathTex(r"|\mathbf{u}_2\rangle", color=GREEN, font_size=30)
        u2_label.next_to(axes.c2p(*u2_end), LEFT, buff=0.2)
        self.add_fixed_orientation_mobjects(u2_label)
        
        self.play(Create(u2_vector), Write(u2_label), run_time=0.8)
        self.wait(0.5)
        
        # 正規化の説明
        norm_text = VGroup(
            MathTex(r"\|\mathbf{u}_1\| = 1", color=RED, font_size=24),
            MathTex(r"\|\mathbf{u}_2\| = 1", color=GREEN, font_size=24),
            MathTex(r"\langle \mathbf{u}_1 | \mathbf{u}_2 \rangle = 0", color=YELLOW, font_size=24),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        norm_text.to_corner(UL).shift(DOWN * 2.5 + RIGHT * 0.3)
        self.add_fixed_in_frame_mobjects(norm_text)
        self.play(Write(norm_text), run_time=0.8)
        self.wait(0.8)
        
        # 任意のベクトル a3
        a3_end = np.array([1.5, 1.2, 1.8])
        a3_vector = Arrow3D(
            start=axes.c2p(0, 0, 0),
            end=axes.c2p(*a3_end),
            color=BLUE,
            thickness=0.025,
            height=0.25,
            base_radius=0.1
        )
        a3_label = MathTex(r"|a_3\rangle", color=BLUE, font_size=32)
        a3_label.next_to(axes.c2p(*a3_end), UP, buff=0.2)
        self.add_fixed_orientation_mobjects(a3_label)
        
        self.play(Create(a3_vector), Write(a3_label), run_time=0.8)
        self.wait(1.0)
        
        # self.play(FadeOut(subtitle1))
        self.wait(0.3)
        
        # === パート2: ベクトルの分解式 ===
        subtitle2 = Text("観点１：ベクトルを直交成分に分解", font_size=32, color=ORANGE)
        subtitle2.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle2)
        self.play(Write(subtitle2), run_time=0.6)
        self.wait(0.5)
        
        # 分解式の表示
        decomposition_eq = MathTex(
            r"|a_3\rangle = \langle \mathbf{u}_1 | a_3 \rangle |\mathbf{u}_1\rangle + "
            r"\langle \mathbf{u}_2 | a_3 \rangle |\mathbf{u}_2\rangle + |\tilde{\mathbf{u}}_3\rangle",
            color=WHITE, font_size=30
        )
        decomposition_eq.shift(DOWN*2)
        self.add_fixed_in_frame_mobjects(decomposition_eq)
        self.play(Write(decomposition_eq), run_time=1.2)
        self.wait(1.0)
        
        # 各項の説明
        term_explanation = VGroup(
            MathTex(r"\langle \mathbf{u}_1 | a_3 \rangle |\mathbf{u}_1\rangle", 
                   color=RED, font_size=24),
            Text(": u₁方向の成分", color=WHITE, font_size=22),
        ).arrange(RIGHT, buff=0.2)
        term_explanation.to_corner(DR).shift(UP * 3.5 + LEFT * 0.5)
        self.add_fixed_in_frame_mobjects(term_explanation)
        self.play(Write(term_explanation), run_time=0.7)
        self.wait(0.6)
        
        # u1方向への射影を描画
        proj_u1_length = np.dot(a3_end, u1_end)  # 内積
        proj_u1_end = proj_u1_length * u1_end
        proj_u1_vector = Arrow3D(
            start=axes.c2p(0, 0, 0),
            end=axes.c2p(*proj_u1_end),
            color=RED,
            thickness=0.02,
            height=0.2,
            base_radius=0.08,
            resolution=8
        )
        proj_u1_label = MathTex(
            r"\langle \mathbf{u}_1 | a_3 \rangle |\mathbf{u}_1\rangle",
            color=RED, font_size=24
        )
        proj_u1_label.next_to(axes.c2p(*proj_u1_end), DOWN, buff=0.3)
        self.add_fixed_orientation_mobjects(proj_u1_label)
        
        self.play(Create(proj_u1_vector), Write(proj_u1_label), FadeOut((u1_label)), run_time=0.9)
        self.wait(0.8)
        
        # 垂線（u1成分を引いた後の残り）
        # perp_u1_start = proj_u1_end
        # perp_u1_end = a3_end
        # perp_u1_line = DashedLine(
        #     axes.c2p(*perp_u1_start),
        #     axes.c2p(*perp_u1_end),
        #     color=ORANGE,
        #     stroke_width=3,
        #     dash_length=0.1
        # )
        
        # self.play(Create(perp_u1_line), run_time=0.7)
        # self.wait(0.8)
        
        self.play(FadeOut(term_explanation))
        
        # u2方向の成分の説明
        term_explanation2 = VGroup(
            MathTex(r"\langle \mathbf{u}_2 | a_3 \rangle |\mathbf{u}_2\rangle", 
                   color=GREEN, font_size=24),
            Text(": u₂方向の成分", color=WHITE, font_size=22),
        ).arrange(RIGHT, buff=0.2)
        term_explanation2.to_corner(DR).shift(UP * 3.5 + LEFT * 0.5)
        self.add_fixed_in_frame_mobjects(term_explanation2)
        self.play(Write(term_explanation2), run_time=0.7)
        self.wait(0.6)
        
        # u2方向への射影を描画
        proj_u2_length = np.dot(a3_end, u2_end)
        proj_u2_end = proj_u2_length * u2_end
        proj_u2_vector = Arrow3D(
            start=axes.c2p(0, 0, 0),
            end=axes.c2p(*proj_u2_end),
            color=GREEN,
            thickness=0.02,
            height=0.2,
            base_radius=0.08,
            resolution=8
        )
        proj_u2_label = MathTex(
            r"\langle \mathbf{u}_2 | a_3 \rangle |\mathbf{u}_2\rangle",
            color=GREEN, font_size=24
        )
        proj_u2_label.next_to(axes.c2p(*proj_u2_end), LEFT, buff=0.3)
        self.add_fixed_orientation_mobjects(proj_u2_label)
        
        self.play(Create(proj_u2_vector), Write(proj_u2_label), FadeOut((u2_label)), run_time=0.9)
        self.wait(0.8)
        
        self.play(FadeOut(term_explanation2))
        
        # u3成分（残りの成分）の説明
        term_explanation3 = VGroup(
            MathTex(r"|\tilde{\mathbf{u}}_3\rangle", color=PURPLE, font_size=24),
            Text(": u₁, u₂と直交する成分", color=WHITE, font_size=22),
        ).arrange(RIGHT, buff=0.2)
        term_explanation3.to_corner(DR).shift(UP * 3.5 + LEFT * 0.5)
        self.add_fixed_in_frame_mobjects(term_explanation3)
        self.play(Write(term_explanation3), run_time=0.7)
        self.wait(0.6)
        
        # u3成分を計算して描画
        u3_tilde_end = a3_end - proj_u1_end - proj_u2_end
        u3_tilde_vector = Arrow3D(
            start=axes.c2p(0, 0, 0),
            end=axes.c2p(*u3_tilde_end),
            color=PURPLE,
            thickness=0.025,
            height=0.25,
            base_radius=0.1
        )
        u3_tilde_label = MathTex(r"|\tilde{\mathbf{u}}_3\rangle", color=PURPLE, font_size=30)
        u3_tilde_label.next_to(axes.c2p(*u3_tilde_end), RIGHT, buff=0.2)
        self.add_fixed_orientation_mobjects(u3_tilde_label)
        
        self.play(Create(u3_tilde_vector), Write(u3_tilde_label), run_time=0.9)
        self.wait(1.2)
        
        self.play(FadeOut(term_explanation3))
        self.wait(0.3)
        
        # === ベクトルの合成を視覚化 ===
        composition_text = Text("これら3つの成分を繋ぐと...", color=YELLOW, font_size=26, weight=BOLD)
        composition_text.to_corner(DR).shift(UP * 3.5 + LEFT * 0.5)
        self.add_fixed_in_frame_mobjects(composition_text)
        self.play(Write(composition_text), run_time=0.8)
        self.wait(0.5)
        
        # proj_u2_vectorを複製してproj_u1_vectorの先端から開始するように移動
        proj_u2_shifted_vector = Arrow3D(
            start=axes.c2p(*proj_u1_end),
            end=axes.c2p(*(proj_u1_end + proj_u2_end)),
            color=GREEN,
            thickness=0.02,
            height=0.2,
            base_radius=0.08,
            resolution=8
        )
        
        # u3_tilde_vectorを複製してproj_u1 + proj_u2の先端から開始するように移動
        combined_u1_u2_end = proj_u1_end + proj_u2_end
        u3_tilde_shifted_vector = Arrow3D(
            start=axes.c2p(*combined_u1_u2_end),
            end=axes.c2p(*(combined_u1_u2_end + u3_tilde_end)),
            color=PURPLE,
            thickness=0.025,
            height=0.25,
            base_radius=0.1
        )
        
        # 元のproj_u2とu3_tildeをフェードアウトし、シフトしたものをフェードイン
        self.play(
            FadeOut(proj_u2_vector),
            FadeOut(u3_tilde_vector),
            run_time=0.5
        )
        self.play(
            Create(proj_u2_shifted_vector),
            run_time=0.8
        )
        self.wait(0.5)
        
        self.play(
            Create(u3_tilde_shifted_vector),
            run_time=0.8
        )
        self.wait(1.0)
        
        
        # カメラを回転させて3次元構造を強調
        self.move_camera(phi=70 * DEGREES, theta=75 * DEGREES, run_time=2.0)
        self.wait(0.8)
        
        self.play(FadeOut(u1_vector), FadeOut(u2_vector))
        self.wait(0.3)
        
        # 3つのベクトルが繋がってa3になることを強調
        result_text = Text("元のベクトル|a₃〉になる!", color=YELLOW, font_size=28, weight=BOLD)
        result_text.to_corner(DR).shift(UP * 3.5 + LEFT * 0.5)
        self.add_fixed_in_frame_mobjects(result_text)
        self.play(
            FadeOut(composition_text),
            Write(result_text),
            a3_vector.animate.set_color(YELLOW).set_opacity(1),
            run_time=1.0
        )
        self.wait(1.5)
        
        # a3_vectorを元の色に戻す
        self.play(
            a3_vector.animate.set_color(BLUE),
            FadeOut(result_text),
            run_time=0.6
        )
        self.wait(0.5)
        
        # シフトしたベクトルをフェードアウト
        self.play(
            FadeOut(proj_u2_shifted_vector),
            FadeOut(u3_tilde_shifted_vector),
            run_time=0.6
        )
        self.wait(0.3)
        
        self.play(FadeOut(subtitle2), FadeOut(decomposition_eq),
                  FadeIn(proj_u2_vector), FadeIn(u3_tilde_vector),
        )
        self.wait(0.3)
        
        # === パート3: 式変形とシュミットの直交化 ===
        subtitle3 = Text("観点２：観測装置で成分を測定", font_size=32, color=TEAL)
        subtitle3.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle3)
        self.play(Write(subtitle3), run_time=0.6)
        self.wait(0.5)
        
        # 元の式
        original_eq = MathTex(
            r"|a_3\rangle = (\langle \mathbf{u}_1 | a_3 \rangle ) |\mathbf{u}_1\rangle + "
            r"(\langle \mathbf{u}_2 | a_3 \rangle ) |\mathbf{u}_2\rangle + |\tilde{\mathbf{u}}_3\rangle",
            color=WHITE, font_size=24
        )
        original_eq.to_corner(UR).shift(DOWN * 1.5 + LEFT * 0.3)
        self.add_fixed_in_frame_mobjects(original_eq)
        self.play(Write(original_eq), run_time=0.8)
        self.wait(0.6)
        
        # 式変形の矢印
        arrow = MathTex(r"\Downarrow", color=YELLOW, font_size=28)
        arrow.next_to(original_eq, DOWN, buff=0.2)
        rearrange_text = Text("式を変形", color=YELLOW, font_size=20)
        rearrange_text.next_to(arrow, RIGHT, buff=0.2).shift(LEFT*2)
        self.add_fixed_in_frame_mobjects(arrow, rearrange_text)
        self.play(Write(arrow), Write(rearrange_text), run_time=0.6)
        self.wait(0.5)
        
        # 変形後の式（シュミットの直交化の形）
        schmidt_eq = MathTex(
            r"|\tilde{\mathbf{u}}_3\rangle = |a_3\rangle - "
            r"\langle \mathbf{u}_1 | a_3 \rangle |\mathbf{u}_1\rangle - "
            r"\langle \mathbf{u}_2 | a_3 \rangle |\mathbf{u}_2\rangle",
            color=ORANGE, font_size=26
        )
        schmidt_eq.next_to(arrow, DOWN, buff=0.3, aligned_edge=LEFT*2.5).shift(LEFT*1.7)
        schmidt_box = SurroundingRectangle(schmidt_eq, color=ORANGE, buff=0.15)
        self.add_fixed_in_frame_mobjects(schmidt_eq, schmidt_box)
        self.play(Write(schmidt_eq), Create(schmidt_box), run_time=1.0)
        self.wait(1.2)
        
        # 解釈の説明
        interpretation = VGroup(
            Text("これはシュミットの直交化法!", color=YELLOW, font_size=24, weight=BOLD),
            VGroup(
                Text("① ", color=WHITE, font_size=22),
                Text("元のベクトル |a₃〉から", color=WHITE, font_size=22),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("② ", color=WHITE, font_size=22),
                Text("観測装置〈u₁|で測定した成分を引き", color=RED, font_size=22),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("③ ", color=WHITE, font_size=22),
                Text("観測装置〈u₂|で測定した成分を引く", color=GREEN, font_size=22),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        interpretation.shift(DOWN * 1.8 + RIGHT *3.6)
        self.add_fixed_in_frame_mobjects(interpretation)
        self.play(Write(interpretation), run_time=2)
        self.wait(2.5)
        
        self.play(
            FadeOut(original_eq), FadeOut(arrow), FadeOut(rearrange_text),
            FadeOut(schmidt_eq), FadeOut(schmidt_box),
            FadeOut(interpretation), FadeOut(subtitle3)
        )
        self.wait(0.3)
        
        # === パート4: 直交性の確認 ===
        # subtitle4 = Text("直交性の確認", font_size=32, color=GOLD)
        # subtitle4.next_to(title, DOWN)
        # self.add_fixed_in_frame_mobjects(subtitle4)
        # self.play(Write(subtitle4), run_time=0.6)
        # self.wait(0.5)
        
        # # u3はu1, u2と直交していることを確認
        # orthogonal_check = VGroup(
        #     MathTex(r"\langle \mathbf{u}_1 | \tilde{\mathbf{u}}_3 \rangle = 0", 
        #            color=RED, font_size=26),
        #     MathTex(r"\langle \mathbf{u}_2 | \tilde{\mathbf{u}}_3 \rangle = 0", 
        #            color=GREEN, font_size=26),
        # ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        # orthogonal_check.shift(UP * 0.5)
        # self.add_fixed_in_frame_mobjects(orthogonal_check)
        
        # for check in orthogonal_check:
        #     self.play(Write(check), run_time=0.7)
        #     self.wait(0.5)
        
        # self.wait(0.8)
        
        # # 直交基底の完成
        # complete_text = Text(
        #     "u₁, u₂, ũ₃ は互いに直交する!",
        #     color=YELLOW, font_size=28, weight=BOLD
        # )
        # complete_text.shift(DOWN * 1.2)
        # complete_box = SurroundingRectangle(complete_text, color=YELLOW, buff=0.2)
        # self.add_fixed_in_frame_mobjects(complete_text, complete_box)
        # self.play(Write(complete_text), Create(complete_box), run_time=0.8)
        # self.wait(1.2)
        
        # self.play(
        #     FadeOut(orthogonal_check),
        #     FadeOut(complete_text), FadeOut(complete_box),
        #     FadeOut(subtitle4)
        # )
        # self.wait(0.3)
        
        # カメラをさらに回転
        self.move_camera(phi=60 * DEGREES, theta=30 * DEGREES, run_time=2.0)
        self.wait(0.5)
        
        # 3Dオブジェクトをフェードアウト
        self.play(
            FadeOut(axes), FadeOut(axis_labels),
            # FadeOut(u1_vector),
            # FadeOut(u2_vector), 
            FadeOut(a3_vector), FadeOut(a3_label),
            FadeOut(proj_u1_vector), FadeOut(proj_u1_label),
            FadeOut(proj_u2_vector), FadeOut(proj_u2_label),
            FadeOut(u3_tilde_vector), FadeOut(u3_tilde_label),
            # FadeOut(perp_u1_line),
            FadeOut(norm_text),
            run_time=0.8
        )
        self.wait(0.3)
        
        # === まとめ ===
        summary_subtitle = Text("まとめ", font_size=32, color=GOLD, weight=BOLD)
        summary_subtitle.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(summary_subtitle)
        self.play(Write(summary_subtitle), run_time=0.6)
        self.wait(0.5)
        
        # まとめのポイント
        summary_points = VGroup(
            VGroup(
                Text("1.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("射影と観測装置の概念で", color=WHITE, font_size=24),
                    Text("直交化が直感的に理解できる", color=YELLOW, font_size=24, weight=BOLD),
                ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            
            VGroup(
                Text("2.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("正規化ベクトルは「観測装置」として機能し、", color=WHITE, font_size=24),
                    # MathTex(r"\langle \mathbf{u}_i | a \rangle", color=GREEN, font_size=24),
                    Text("その方向の成分を測定できる", color=WHITE, font_size=24),
                ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            
            VGroup(
                Text("3.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("シュミットの直交化は", color=WHITE, font_size=24),
                    Text("「測定した成分を引く」操作の繰り返し", color=ORANGE, font_size=24, weight=BOLD),
                ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
            
            VGroup(
                Text("4.", color=WHITE, font_size=26, weight=BOLD),
                VGroup(
                    Text("内積計算だけで影の長さを求められる", color=WHITE, font_size=24),
                    Text("→ 計算が簡単で便利!", color=GREEN, font_size=24, weight=BOLD),
                ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
            ).arrange(RIGHT, buff=0.3, aligned_edge=UP),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        summary_points.shift(DOWN * 0.2)
        self.add_fixed_in_frame_mobjects(summary_points)
        
        for point in summary_points:
            self.play(Write(point), run_time=0.9)
            self.wait(0.6)
        
        self.wait(1.5)
        
        # 最終メッセージ
        # final_message = Text(
        #     "射影 = 観測 = 直交化の核心!",
        #     color=YELLOW, font_size=32, weight=BOLD, slant=ITALIC
        # )
        # final_message.shift(DOWN * 2.8)
        # final_box = SurroundingRectangle(final_message, color=YELLOW, buff=0.25)
        # self.add_fixed_in_frame_mobjects(final_message, final_box)
        # self.play(Write(final_message), Create(final_box), run_time=1.0)
        # self.wait(2.0)
        
        # フェードアウト
        all_objects = VGroup(
            title, summary_subtitle, summary_points, 
            # final_message, final_box
        )
        self.play(FadeOut(all_objects), run_time=1.0)
        self.wait(0.5)
