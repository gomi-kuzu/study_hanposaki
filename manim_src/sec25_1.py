from manim import *
import numpy as np


class FuturePredictionProblemSetup(ThreeDScene):
    def vdp_step(self, x1, x2, dt, epsilon=1.0):
        dx1 = x2
        dx2 = epsilon * x2 * (1 - x1**2) - x1
        return x1 + dt * dx1, x2 + dt * dx2

    def vdp_rollout(self, x1_0, x2_0, dt_total=3.0, dt=0.01, epsilon=1.0):
        n = int(dt_total / dt)
        xs = np.zeros((n + 1, 2))
        ts = np.linspace(0.0, dt_total, n + 1)
        xs[0] = np.array([x1_0, x2_0])
        x1, x2 = x1_0, x2_0
        for k in range(n):
            x1, x2 = self.vdp_step(x1, x2, dt, epsilon=epsilon)
            xs[k + 1] = np.array([x1, x2])
        return ts, xs

    def forward_observation(self, x1, x2, delta_t_obs=0.8, n_substeps=40):
        dt = delta_t_obs / n_substeps
        z1, z2 = x1, x2
        for _ in range(n_substeps):
            z1, z2 = self.vdp_step(z1, z2, dt, epsilon=1.0)
        return z1

    def construct(self):
        self.camera.background_color = "#012817"

        title = Text("少し先の未来を予測する問題を考える", font_size=36, color=WHITE)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)

        # ============================================================
        # Part 1: 導入
        # ============================================================
        subtitle = Text("導入：4部の状態方程式をデータサイエンス視点で拡張", font_size=27, color=BLUE)
        subtitle.next_to(title, DOWN)
        self.add_fixed_in_frame_mobjects(subtitle)
        self.play(Write(subtitle), run_time=0.6)
        self.wait(0.3)

        intro1 = Text("第4部では、ベクトルや関数の時間発展を線型代数で学んだ", color=WHITE, font_size=25)
        intro2 = Text("第5部では、観測を介したより現実的な問題設定を考える", color=WHITE, font_size=25)
        intro3 = Text("（第3部・13話で触れた『観測』の考え方を再接続）", color=TEAL, font_size=24)
        intro = VGroup(intro1, intro2, intro3).arrange(DOWN, buff=0.35)
        intro.shift(UP * 0.9)

        for line in intro:
            self.play(Write(line), run_time=0.75)
            self.wait(0.2)

        self.wait(0.8)
        self.play(FadeOut(intro3), run_time=0.5)

        # 観測のイメージ図
        state_box = RoundedRectangle(width=3.0, height=1.2, corner_radius=0.18, color=BLUE)
        state_box.shift(LEFT * 4.2 + DOWN * 0.4)
        state_txt = Text("内部状態", color=BLUE, font_size=26).move_to(state_box.get_center())

        obs_box = RoundedRectangle(width=3.0, height=1.2, corner_radius=0.18, color=YELLOW)
        obs_box.shift(RIGHT * 4.2 + DOWN * 0.4)
        obs_txt = Text("観測値", color=YELLOW, font_size=26).move_to(obs_box.get_center())

        sensor = Circle(radius=0.35, color=WHITE)
        sensor.move_to(DOWN * 0.4)
        sensor_txt = Text("観測", color=WHITE, font_size=20).move_to(sensor.get_center())

        arr1 = Arrow(state_box.get_right(), sensor.get_left(), color=WHITE, buff=0.15, stroke_width=3)
        arr2 = Arrow(sensor.get_right(), obs_box.get_left(), color=WHITE, buff=0.15, stroke_width=3)

        cap_hidden = Text("状態は直接見えないことが多い", color=RED, font_size=23)
        cap_hidden.next_to(state_box, DOWN, buff=0.45)
        cap_data = Text("手に入るのは観測データ", color=GREEN, font_size=23)
        cap_data.next_to(obs_box, DOWN, buff=0.45)

        self.play(
            Create(state_box), Write(state_txt),
            Create(sensor), Write(sensor_txt),
            Create(obs_box), Write(obs_txt),
            GrowArrow(arr1), GrowArrow(arr2),
            run_time=1.0,
        )
        self.play(Write(cap_hidden), Write(cap_data), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(state_box), FadeOut(state_txt),
            FadeOut(sensor), FadeOut(sensor_txt),
            FadeOut(obs_box), FadeOut(obs_txt),
            FadeOut(arr1), FadeOut(arr2),
            FadeOut(cap_hidden), FadeOut(cap_data),
            FadeOut(intro1), FadeOut(intro2),
            run_time=0.6,
        )

        # ============================================================
        # Part 2: 図1 スナップショットペア
        # ============================================================
        subtitle2 = Text("状態の時間発展軌跡とスナップショットペア", font_size=28, color=GOLD)
        subtitle2.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle2), run_time=0.5)
        self.wait(0.3)

        # --- 導入ナレーション：問題設定を言葉と式で丁寧に ---
        lead1 = Text("更にここでは、少し先の未来の観測値を予測することを考える", color=WHITE, font_size=25)
        lead2 = Text("まず、2変数の状態ベクトルの時間発展軌跡があったとする", color=WHITE, font_size=25)
        lead_vec = MathTex(
            r"\mathbf{x}(t) = \begin{pmatrix} x_1(t) \\ x_2(t) \end{pmatrix}",
            color=TEAL, font_size=40,
        )
        lead = VGroup(lead1, lead2, lead_vec).arrange(DOWN, buff=0.4)
        lead.shift(UP * 0.2)
        self.add_fixed_in_frame_mobjects(lead)

        self.play(Write(lead1), run_time=0.8)
        self.wait(0.2)
        self.play(Write(lead2), run_time=0.8)
        self.wait(0.2)
        self.play(Write(lead_vec), run_time=0.8)
        self.wait(1.2)
        self.play(FadeOut(lead), run_time=0.5)

        t_vals, xs = self.vdp_rollout(0.2, 0.9, dt_total=3.0, dt=0.01)
        x1_vals = xs[:, 0]
        x2_vals = xs[:, 1]

        obs_times = np.arange(0.0, 3.0, 0.1)
        obs_idx = [int(t / 0.01) for t in obs_times]
        x1_obs = x1_vals[obs_idx]
        x2_obs = x2_vals[obs_idx]

        axes_t = Axes(
            x_range=[0, 3.0, 1.0],
            y_range=[-1.8, 1.4, 0.5],
            x_length=5.2,
            y_length=3.4,
            axis_config={"color": WHITE, "include_tip": False, "stroke_width": 2},
        )
        axes_t.shift(LEFT * 3.35)

        axes_t_xlabel = MathTex(r"t", color=WHITE, font_size=32)
        axes_t_xlabel.next_to(axes_t.x_axis.get_end(), RIGHT, buff=0.15)
        # axes_t_title = Text("時間 t", color=WHITE, font_size=22)
        # axes_t_title.next_to(axes_t, DOWN, buff=0.2)

        x1_curve = axes_t.plot_line_graph(
            x_values=t_vals,
            y_values=x1_vals,
            line_color=BLUE,
            add_vertex_dots=False,
            stroke_width=3,
        )
        x2_curve = axes_t.plot_line_graph(
            x_values=t_vals,
            y_values=x2_vals,
            line_color=ORANGE,
            add_vertex_dots=False,
            stroke_width=3,
        )

        obs_dots_1 = VGroup(*[
            Dot(axes_t.c2p(obs_times[k], x1_obs[k]), color=BLUE, radius=0.03)
            for k in range(len(obs_times))
        ])
        obs_dots_2 = VGroup(*[
            Dot(axes_t.c2p(obs_times[k], x2_obs[k]), color=ORANGE, radius=0.03)
            for k in range(len(obs_times))
        ])

        idx_k = 25
        idx_k1 = 26
        t_k = obs_times[idx_k]
        t_k1 = obs_times[idx_k1]

        vline_k = DashedLine(
            axes_t.c2p(t_k, x2_obs[idx_k]),
            axes_t.c2p(t_k, x1_obs[idx_k]),
            color=GREEN,
            dash_length=0.05,
            stroke_width=3,
        )
        vline_k1 = DashedLine(
            axes_t.c2p(t_k1, x2_obs[idx_k1]),
            axes_t.c2p(t_k1, x1_obs[idx_k1]),
            color=GREEN,
            dash_length=0.05,
            stroke_width=3,
        )

        x1_tag = MathTex(r"x_1", color=BLUE, font_size=34).next_to(axes_t.c2p(0.9, 1.3), UP, buff=0.1)
        x2_tag = MathTex(r"x_2", color=ORANGE, font_size=34).next_to(axes_t.c2p(0.9, 0.3), RIGHT, buff=0.1)

        axes_p = Axes(
            x_range=[-0.1, 1.3, 0.4],
            y_range=[-1.8, 1.4, 0.5],
            x_length=4.8,
            y_length=3.4,
            axis_config={"color": WHITE, "include_tip": False, "stroke_width": 2},
        )
        axes_p.shift(RIGHT * 3.25)

        axes_p_xlabel = MathTex(r"x_1", color=WHITE, font_size=32)
        axes_p_xlabel.next_to(axes_p.x_axis.get_end(), RIGHT, buff=0.15)
        axes_p_ylabel = MathTex(r"x_2", color=WHITE, font_size=32)
        axes_p_ylabel.next_to(axes_p.y_axis.get_end(), LEFT, buff=0.15)

        phase_pts = [axes_p.c2p(x1_vals[k], x2_vals[k]) for k in range(len(t_vals))]
        phase_path = VMobject(color=WHITE, stroke_width=2.5)
        phase_path.set_points_as_corners(phase_pts)

        phase_dots = VGroup(*[
            Dot(axes_p.c2p(x1_obs[k], x2_obs[k]), color=WHITE, radius=0.024)
            for k in range(len(obs_times))
        ])

        p_k = Dot(axes_p.c2p(x1_obs[idx_k], x2_obs[idx_k]), color=GREEN, radius=0.06)
        p_k1 = Dot(axes_p.c2p(x1_obs[idx_k1], x2_obs[idx_k1]), color=GREEN, radius=0.06)

        pair_ellipse = Ellipse(width=0.9, height=0.55, color=GREEN, stroke_width=2)
        pair_ellipse.rotate(-30 * DEGREES)
        pair_ellipse.move_to((p_k.get_center() + p_k1.get_center()) / 2)

        pair_arrow = Arrow(p_k.get_center(), p_k1.get_center(), color=YELLOW, buff=0.08, stroke_width=5)

        # 位相面の2点ラベル：現在 x(t) と Δt_obs 後の y(t)
        xt_label = MathTex(r"\mathbf{x}(t)", color=GREEN, font_size=36)
        xt_label.next_to(p_k, UP, buff=0.12)
        yt_label = MathTex(r"\mathbf{y}(t)", color=GREEN, font_size=36)
        yt_label.next_to(p_k1, DOWN, buff=0.12)
        dt_label = MathTex(r"\Delta t_{\mathrm{obs}}", color=YELLOW, font_size=26)
        dt_label.next_to(pair_arrow, DOWN*0.4+ RIGHT*0.1, buff=0.12)

        # 画面下部：スナップショットペアの定義（言葉＋式）
        pair_word = Text("任意の固定時間を挟んだ状態量のペアをスナップショットペアと呼ぶ", color=YELLOW, font_size=24)
        pair_math = MathTex(
            r"\bigl(\mathbf{x}(t),\ \mathbf{y}(t)\bigr),\quad"
            r"\mathbf{y}(t)=\mathbf{x}(t+\Delta t_{\mathrm{obs}})",
            color=YELLOW, font_size=32,
        )
        pair_def = VGroup(pair_word, pair_math).arrange(DOWN, buff=0.1).shift(DOWN * 2.4)
        # pair_def.to_edge(DOWN, buff=0.3)
        # if pair_def.width > config.frame_width - 1.0:
        #     pair_def.scale_to_fit_width(config.frame_width - 1.0)
        # self.add_fixed_in_frame_mobjects(pair_def)

        self.play(Create(axes_t), Create(axes_p), run_time=0.6)
        self.play(
            Write(axes_t_xlabel),
            Write(axes_p_xlabel), Write(axes_p_ylabel),
            run_time=0.6,
        )
        self.play(Create(x1_curve), Create(x2_curve), run_time=1.1)
        self.play(FadeIn(obs_dots_1), FadeIn(obs_dots_2), run_time=0.6)
        self.play(Write(x1_tag), Write(x2_tag), run_time=0.4)

        self.play(Create(phase_path), FadeIn(phase_dots), run_time=1.1)
        self.play(Create(vline_k), Create(vline_k1), run_time=0.6)
        self.play(FadeIn(p_k), FadeIn(p_k1), Create(pair_ellipse), GrowArrow(pair_arrow), run_time=0.7)
        self.play(Write(xt_label), Write(yt_label), Write(dt_label), run_time=0.7)
        self.play(Write(pair_def), run_time=0.9)
        self.wait(1.8)

        self.play(
            FadeOut(axes_t), FadeOut(axes_p),
            FadeOut(axes_t_xlabel), #FadeOut(axes_t_title),
            FadeOut(axes_p_xlabel), FadeOut(axes_p_ylabel),
            FadeOut(x1_curve), FadeOut(x2_curve),
            FadeOut(obs_dots_1), FadeOut(obs_dots_2),
            FadeOut(phase_path), FadeOut(phase_dots),
            FadeOut(vline_k), FadeOut(vline_k1),
            FadeOut(p_k), FadeOut(p_k1),
            FadeOut(pair_ellipse), FadeOut(pair_arrow),
            FadeOut(xt_label), FadeOut(yt_label), FadeOut(dt_label),
            FadeOut(pair_def),
            FadeOut(x1_tag), FadeOut(x2_tag),
            run_time=0.7,
        )

        # ============================================================
        # Part 3: 観測関数と予測対象
        # ============================================================
        subtitle3 = Text("スナップショットのペアの観測値を予測する", font_size=28, color=TEAL)
        subtitle3.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle3), run_time=0.5)
        self.wait(0.3)

        obs_def = VGroup(
            Text("観測関数の定義:", color=WHITE, font_size=30),
            MathTex(
            r"\phi(\mathbf{x}) = x_1",
            color=WHITE,
            font_size=46,
        )).arrange(RIGHT, buff=0.2)
        obs_def.shift(UP * 1.3)

        pred_in = VGroup(
            Text("入力:", color=BLUE, font_size=30),
            MathTex(r"\mathbf{x}(t)", color=BLUE, font_size=42),
        ).arrange(RIGHT, buff=0.2)

        pred_out = VGroup(
            Text("ペアの予測観測値:", color=GOLD, font_size=30),
            MathTex(
                r"\phi(\mathbf{y}(t)) = \phi(\mathbf{x}(t+\Delta t_{\mathrm{obs}}))",
                color=GOLD,
                font_size=40,
            ),
        ).arrange(RIGHT, buff=0.2)

        pred_def = VGroup(pred_in, pred_out).arrange(DOWN, buff=0.25)
        pred_def.shift(UP * 0.2)

        target_alias = VGroup(
            Text("→観測予測の別表記:", color=YELLOW, font_size=30),
            MathTex(
            r"\phi(\mathbf{x}, t=\Delta t_{\mathrm{obs}})",
            color=YELLOW,
            font_size=48,
        )).arrange(RIGHT, buff=0.2)
        target_alias.shift(DOWN * 1.2)

        note_typo = Text("↑この関数出力値を予測するのがここでの目的になる！", color=WHITE, font_size=24)
        note_typo.shift(DOWN * 2.1)

        self.play(Write(obs_def), run_time=0.8)
        self.play(Write(pred_def), run_time=1.0)
        self.play(Write(target_alias), Write(note_typo), run_time=0.8)
        self.wait(1.8)

        self.play(
            FadeOut(obs_def), FadeOut(pred_def),
            FadeOut(target_alias), FadeOut(note_typo),
            run_time=0.6,
        )

        # ============================================================
        # Part 4: 図2 線形超平面
        # ============================================================
        subtitle4 = Text("\u03d5(x)=x_1 は線形の超平面", font_size=28, color=ORANGE)
        subtitle4.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle4), run_time=0.5)
        self.wait(0.3)

        self.set_camera_orientation(phi=63 * DEGREES, theta=-35 * DEGREES)

        axes3 = ThreeDAxes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            z_range=[-2, 2, 1],
            x_length=6,
            y_length=6,
            z_length=4.5,
            axis_config={"color": GRAY},
        )
        axes3.shift(LEFT * 1.2 + DOWN * 0.2)

        # x軸・y軸を床面(z=-2)の高さまで下げ、x1-x2平面と軸の矢印を一致させる。
        # x_axis と y_axis を同じベクトルだけ平行移動するので c2p は不変。
        z_floor_shift = axes3.c2p(0, 0, -2.0) - axes3.c2p(0, 0, 0.0)
        axes3.x_axis.shift(z_floor_shift)
        axes3.y_axis.shift(z_floor_shift)

        # 3D軸ラベル: x軸→x_1, y軸→x_2, z軸→φ
        axis3_xlabel = MathTex(r"x_1", color=WHITE, font_size=44)
        axis3_xlabel.next_to(axes3.x_axis.get_end(), RIGHT, buff=0.15)
        axis3_ylabel = MathTex(r"x_2", color=WHITE, font_size=44)
        axis3_ylabel.next_to(axes3.y_axis.get_end(), UP, buff=0.15)
        axis3_zlabel = MathTex(r"\phi", color=WHITE, font_size=44)
        axis3_zlabel.next_to(axes3.z_axis.get_end(), OUT, buff=0.2)
        axis3_zlabel.shift(RIGHT * 0.5 + IN * 0.5)  # z軸ラベルを少し右下にずらす
        # カメラ方向を向くように回転（3D空間内で見やすくする）
        for lbl in (axis3_xlabel, axis3_ylabel, axis3_zlabel):
            lbl.rotate(90 * DEGREES, axis=RIGHT)
        axes3_labels = VGroup(axis3_xlabel, axis3_ylabel, axis3_zlabel)

        base_plane = Surface(
            lambda u, v: axes3.c2p(u, v, -2.0),
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=(8, 8),
            fill_opacity=0.12,
            fill_color=WHITE,
            stroke_color=GRAY,
        )

        flat_surface = Surface(
            lambda u, v: axes3.c2p(u, v, u),
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=(18, 18),
            fill_opacity=0.38,
            fill_color=BLUE,
            stroke_color=GRAY,
            stroke_width=0.8,
        )

        obs_idx_sparse = [int(t / 0.01) for t in np.arange(0.0, 3.0, 0.1)]
        floor_path_pts = [axes3.c2p(x1_vals[k], x2_vals[k], -2.0) for k in obs_idx_sparse]
        floor_path = VMobject(color=WHITE, stroke_width=2.5)
        floor_path.set_points_as_corners(floor_path_pts)

        lifts_flat = VGroup()
        top_dots_flat = VGroup()
        for k in obs_idx_sparse[::3]:
            x1v = x1_vals[k]
            x2v = x2_vals[k]
            zf = x1v
            lifts_flat.add(DashedLine(axes3.c2p(x1v, x2v, -2.0), axes3.c2p(x1v, x2v, zf), color=GREEN, dash_length=0.08))
            top_dots_flat.add(Dot3D(axes3.c2p(x1v, x2v, zf), color=GREEN, radius=0.04))

        section_line = ParametricFunction(
            lambda s: axes3.c2p(s, 0.0, s),
            t_range=np.array([-2.0, 2.0]),
            color=RED,
            stroke_width=4,
        )

        flat_label = VGroup(Text("観測値（縦軸）へは、", color=BLUE, font_size=26),
                            Text("線形写像で表される", color=BLUE, font_size=26)).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        flat_label.to_edge(RIGHT).shift(LEFT * 0.5 + UP)
        self.add_fixed_in_frame_mobjects(flat_label)

        self.play(Create(axes3), Create(base_plane), run_time=0.9)
        self.play(Write(axes3_labels), run_time=0.6)
        self.play(Create(flat_surface), run_time=1.1)
        self.play(Create(floor_path), run_time=0.7)
        self.play(Create(lifts_flat), FadeIn(top_dots_flat), run_time=0.9)
        self.play(Create(section_line), Write(flat_label), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(flat_surface), FadeOut(lifts_flat), FadeOut(top_dots_flat),
            FadeOut(section_line), FadeOut(flat_label),
            run_time=0.7,
        )

        # ============================================================
        # Part 5: 図3 非線形曲面
        # ============================================================
        subtitle5 = Text("\u03d5(x,t=\u0394t_obs) は非線形曲面", font_size=28, color=YELLOW)
        subtitle5.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle5), run_time=0.5)
        self.wait(0.3)

        nonlinear_surface = Surface(
            lambda u, v: axes3.c2p(u, v, self.forward_observation(u, v, delta_t_obs=0.8, n_substeps=36)),
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=(18, 18),
            fill_opacity=0.40,
            fill_color=ORANGE,
            stroke_color=GRAY,
            stroke_width=0.8,
        )

        lifts_nl = VGroup()
        top_dots_nl = VGroup()
        for k in obs_idx_sparse[::3]:
            x1v = x1_vals[k]
            x2v = x2_vals[k]
            zn = self.forward_observation(x1v, x2v, delta_t_obs=0.8, n_substeps=36)
            lifts_nl.add(DashedLine(axes3.c2p(x1v, x2v, -2.0), axes3.c2p(x1v, x2v, zn), color=GREEN, dash_length=0.08))
            top_dots_nl.add(Dot3D(axes3.c2p(x1v, x2v, zn), color=GREEN, radius=0.04))

        nonlinear_label1 = Text("時間発展が挟まると", color=WHITE, font_size=26)
        nonlinear_label2 = Text("写像は曲面として現れる", color=YELLOW, font_size=26)
        nonlinear_label3 = Text("この曲面の獲得こそが", color=GREEN, font_size=26)
        nonlinear_label4 = Text("予測問題を解くことに相当する", color=GREEN, font_size=26)

        nonlinear_labels = VGroup(nonlinear_label1, nonlinear_label2).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        nonlinear_labels.to_edge(LEFT).shift(UP)
        self.add_fixed_in_frame_mobjects(nonlinear_labels)
        nonlinear_labels2 = VGroup(nonlinear_label3, nonlinear_label4).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        nonlinear_labels2.to_edge(RIGHT).shift(RIGHT*0/7 + UP * 0.2)
        self.add_fixed_in_frame_mobjects(nonlinear_labels2)

        self.play(Create(nonlinear_surface), Create(nonlinear_labels2), run_time=1.3)
        self.play(Create(lifts_nl), FadeIn(top_dots_nl), run_time=0.9)

        self.move_camera(phi=78 * DEGREES, theta=-20 * DEGREES, run_time=1.8)
        self.wait(0.4)
        self.move_camera(phi=60 * DEGREES, theta=-50 * DEGREES, run_time=1.8)

        for row in nonlinear_labels:
            self.play(Write(row), run_time=0.65)
            self.wait(0.2)
        for row in nonlinear_labels2:
            self.play(Write(row), run_time=0.65)
            self.wait(0.2)

        self.wait(1.6)

        self.play(
            FadeOut(nonlinear_surface), FadeOut(lifts_nl), FadeOut(top_dots_nl),
            FadeOut(floor_path), FadeOut(base_plane), FadeOut(axes3),
            FadeOut(axes3_labels),
            FadeOut(nonlinear_labels), FadeOut(nonlinear_labels2),
            run_time=0.9,
        )

        # ============================================================
        # Part 6: まとめと次回予告
        # ============================================================
        self.set_camera_orientation(phi=0 * DEGREES, theta=0 * DEGREES)

        subtitle6 = Text("まとめ", font_size=30, color=GREEN)
        subtitle6.next_to(title, DOWN)
        self.play(Transform(subtitle, subtitle6), run_time=0.5)
        self.wait(0.3)

        summary = VGroup(
            Text("・時間発展する状態量を観測する", color=WHITE, font_size=26),
            Text("・1ステップ先の観測値\u03d5(x,t=\u0394t_obs)を予測する問題を考える ", color=YELLOW, font_size=26),
            Text("・これは非線形曲面の獲得問題として見える", color=ORANGE, font_size=26),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        summary.shift(UP * 0.3)

        next_note = Text(
            "次の動画では、\u03d5(x,t=\u03d5(x,t=\u0394t_obs)) の期待値の計算を通して『随伴作用素』を学ぶ",
            color=TEAL,
            font_size=24,
            weight=BOLD,
        )
        next_note.shift(DOWN * 2.1)

        self.add_fixed_in_frame_mobjects(summary, next_note)

        for line in summary:
            self.play(Write(line), run_time=0.7)
            self.wait(0.25)

        self.play(Write(next_note), run_time=0.9)
        self.wait(2.0)

        self.play(FadeOut(summary), FadeOut(next_note), FadeOut(subtitle), FadeOut(title), run_time=0.8)
        self.wait(0.5)
