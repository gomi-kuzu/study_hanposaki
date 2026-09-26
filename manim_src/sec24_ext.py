from manim import *
import numpy as np


class SDEDiffusionModelRelation(Scene):
    def construct(self):
        self.camera.background_color = "#012817"

        title = Text("確率微分方程式と拡散モデルの関係", font_size=36, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title), run_time=0.8)
        self.wait(0.5)

        # ============================================================
        # Part 1: 導入 — 拡散モデルの本質
        # ============================================================
        subtitle1 = Text("導入：拡散モデルとは何か", font_size=28, color=BLUE)
        subtitle1.next_to(title, DOWN)
        self.play(Write(subtitle1), run_time=0.5)
        self.wait(0.3)

        intro1 = Text(
            "拡散モデル（Diffusion Model）は生成AIの中核をなす技術",
            color=WHITE, font_size=26,
        )
        intro1.shift(UP * 1.8)
        self.play(Write(intro1), run_time=0.8)
        self.wait(0.3)

        intro2 = Text(
            "その正体は、24話で学んだ確率微分方程式（SDE）そのもの",
            color=GOLD, font_size=28, weight=BOLD,
        )
        intro2.shift(UP * 0.8)
        self.play(Write(intro2), run_time=0.8)
        self.wait(0.3)

        intro3 = Text(
            "ノイズ化のSDEを「逆再生」し、そこに「スコア」の補正を加えて生成する",
            color=WHITE, font_size=26,
        )
        intro3.shift(DOWN * 0.2)
        self.play(Write(intro3), run_time=0.8)
        self.wait(0.3)

        intro4 = Text(
            "ここでは、その仕組みを SDE の視点から順に解きほぐしていく",
            color=TEAL, font_size=26,
        )
        intro4.shift(DOWN * 1.2)
        self.play(Write(intro4), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(intro1), FadeOut(intro2), FadeOut(intro3), FadeOut(intro4),
        )
        self.wait(0.3)

        # ============================================================
        # Part 2: 順過程（ノイズ化）— インクの拡散
        # ============================================================
        subtitle2 = Text("順過程：データにノイズを加えていく", font_size=28, color=GOLD)
        subtitle2.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle2), run_time=0.5)
        self.wait(0.3)

        fwd_intro = Text(
            "きれいなデータにノイズを加えていく過程は SDE で記述される",
            color=WHITE, font_size=26,
        )
        fwd_intro.shift(UP * 2.0)
        self.play(Write(fwd_intro), run_time=0.7)
        self.wait(0.3)

        fwd_eq = MathTex(
            r"d\mathbf{x} = \mathbf{f}(\mathbf{x}, t)\,dt "
            r"+ g(t)\,d\mathbf{W}",
            font_size=44,
        )
        fwd_eq[0][0:4].set_color(WHITE)
        fwd_eq.shift(UP * 1.0)
        fwd_box = SurroundingRectangle(fwd_eq, color=YELLOW, buff=0.25)
        self.play(Write(fwd_eq), Create(fwd_box), run_time=1.0)
        self.wait(0.4)

        # インク拡散のポンチ絵
        drift_label = Text("ドリフト項 𝐟(𝐱,t)dt", color=BLUE, font_size=22)
        drift_desc = Text("水全体の流れ（インクを寄せる力）", color=WHITE, font_size=20)
        drift_group = VGroup(drift_label, drift_desc).arrange(DOWN, buff=0.1)
        drift_group.shift(LEFT * 3.3 + DOWN * 0.6)

        diff_label = Text("拡散項 g(t)d𝐖", color=RED, font_size=22)
        diff_desc = Text("インク粒子のブラウン運動", color=WHITE, font_size=20)
        diff_group = VGroup(diff_label, diff_desc).arrange(DOWN, buff=0.1)
        diff_group.shift(RIGHT * 3.3 + DOWN * 0.6)

        self.play(Write(drift_group), Write(diff_group), run_time=0.9)
        self.wait(0.3)

        # 左：ドリフトの矢印（中心へ集める）
        drift_center = LEFT * 3.3 + DOWN * 2.0
        drift_arrows = VGroup()
        for angle in np.linspace(0, TAU, 8, endpoint=False):
            start = drift_center + 0.9 * np.array([np.cos(angle), np.sin(angle), 0])
            end = drift_center + 0.25 * np.array([np.cos(angle), np.sin(angle), 0])
            drift_arrows.add(Arrow(start, end, color=BLUE, buff=0, stroke_width=3,
                                   max_tip_length_to_length_ratio=0.3))
        drift_dot = Dot(drift_center, color=BLUE, radius=0.1)

        # 右：ブラウン運動的な散らばり
        diff_center = RIGHT * 3.3 + DOWN * 2.0
        rng_p = np.random.default_rng(7)
        diff_dots = VGroup()
        for _ in range(18):
            offset = rng_p.normal(0, 0.35, size=2)
            d = Dot(diff_center + np.array([offset[0], offset[1], 0]),
                    color=RED, radius=0.06)
            diff_dots.add(d)

        self.play(Create(drift_arrows), Create(drift_dot),
                  Create(diff_dots), run_time=1.0)
        self.wait(1.5)

        self.play(
            FadeOut(fwd_intro), FadeOut(fwd_eq), FadeOut(fwd_box),
            FadeOut(drift_group), FadeOut(diff_group),
            FadeOut(drift_arrows), FadeOut(drift_dot), FadeOut(diff_dots),
        )
        self.wait(0.3)

        # ============================================================
        # Part 3: 順過程の結果 — サンプルパスがガウスノイズへ
        # ============================================================
        subtitle3 = Text("順過程の結果：データはガウスノイズへ", font_size=28, color=GOLD)
        subtitle3.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle3), run_time=0.5)
        self.wait(0.3)

        res1 = Text(
            "t=0：きれいなデータ  →  t=T：無秩序なガウスノイズ",
            color=WHITE, font_size=26,
        )
        res1.shift(UP * 2.1)
        self.play(Write(res1), run_time=0.7)
        self.wait(0.2)

        axes_f = Axes(
            x_range=[0, 5, 1],
            y_range=[-2.2, 2.2, 1],
            x_length=8.5,
            y_length=3.5,
            axis_config={"color": WHITE, "include_tip": False, "stroke_width": 2},
        )
        axes_f.shift(DOWN * 0.5)
        t_lab_f = MathTex("t", color=WHITE, font_size=26).next_to(
            axes_f.x_axis.get_end(), RIGHT, buff=0.1)
        x_lab_f = MathTex(r"x(t)", color=WHITE, font_size=26).next_to(
            axes_f.y_axis.get_end(), UP, buff=0.1)

        t0_lab = MathTex(r"t{=}0", color=BLUE, font_size=24).next_to(
            axes_f.c2p(0, 0), DOWN, buff=0.3)
        tT_lab = MathTex(r"t{=}T", color=RED, font_size=24).next_to(
            axes_f.c2p(5, 0), DOWN, buff=0.3)

        self.play(Create(axes_f), Write(t_lab_f), Write(x_lab_f),
                  Write(t0_lab), Write(tT_lab), run_time=0.7)

        # 複数サンプルパスを描画
        rng_f = np.random.default_rng(1)
        n_paths = 6
        n_steps_f = 120
        ts_f = np.linspace(0, 5, n_steps_f + 1)
        dt_f = ts_f[1] - ts_f[0]
        starts = np.linspace(-0.4, 0.4, n_paths)
        colors = [BLUE, TEAL, GREEN, YELLOW, ORANGE, RED]
        paths_f = VGroup()
        for i in range(n_paths):
            xs_f = np.zeros(n_steps_f + 1)
            xs_f[0] = starts[i]
            for k in range(n_steps_f):
                # 拡散が徐々に強くなる： g(t) を増加
                g = 0.35 + 0.15 * ts_f[k]
                xs_f[k + 1] = xs_f[k] + g * np.sqrt(dt_f) * rng_f.standard_normal()
            pts_f = [axes_f.c2p(ts_f[k], xs_f[k]) for k in range(n_steps_f + 1)]
            p = VMobject(color=colors[i], stroke_width=2.0)
            p.set_points_as_corners(pts_f)
            paths_f.add(p)

        self.play(Create(paths_f), run_time=2.0)
        self.wait(0.4)

        arrow_time = Arrow(
            axes_f.c2p(0, -1.9), axes_f.c2p(5, -1.9),
            color=GOLD, buff=0, stroke_width=4,
        )
        arrow_lab = Text("時間の流れ（ノイズが増す）", color=GOLD, font_size=22)
        arrow_lab.next_to(arrow_time, DOWN, buff=0.15)
        self.play(GrowArrow(arrow_time), Write(arrow_lab), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(res1), FadeOut(axes_f), FadeOut(t_lab_f), FadeOut(x_lab_f),
            FadeOut(t0_lab), FadeOut(tT_lab), FadeOut(paths_f),
            FadeOut(arrow_time), FadeOut(arrow_lab),
        )
        self.wait(0.3)

        # ============================================================
        # Part 4: 逆過程 — 生成とは時間の逆再生
        # ============================================================
        subtitle4 = Text("逆過程：時間を遡ってデータを生成する", font_size=28, color=ORANGE)
        subtitle4.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle4), run_time=0.5)
        self.wait(0.3)

        rev1 = Text(
            "データ生成とは、時間の針を逆回し（t=T → 0）にすること",
            color=WHITE, font_size=26,
        )
        rev1.shift(UP * 2.0)
        self.play(Write(rev1), run_time=0.7)
        self.wait(0.3)

        rev2 = Text(
            "完全なノイズから、きれいな画像を復元するプロセス",
            color=GOLD, font_size=26,
        )
        rev2.shift(UP * 1.2)
        self.play(Write(rev2), run_time=0.7)
        self.wait(0.3)

        need_title = Text("逆再生に必要な2つの要素：", color=TEAL, font_size=26, weight=BOLD)
        need_title.shift(UP * 0.2)
        self.play(Write(need_title), run_time=0.6)

        need1 = Text(
            "① 流れの逆再生（dt < 0）：時間を遡ればドリフトは自動的に逆向き",
            color=WHITE, font_size=24,
        )
        need2 = Text(
            "② ノイズの回収力（スコア）：散らばった粒子を密度の高い方向へ引き戻す",
            color=WHITE, font_size=24,
        )
        needs = VGroup(need1, need2).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        needs.shift(DOWN * 1.1)
        for n in needs:
            self.play(Write(n), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(rev1), FadeOut(rev2), FadeOut(need_title), FadeOut(needs),
        )
        self.wait(0.3)

        # ============================================================
        # Part 5: スコアとは何か（ポンチ絵）
        # ============================================================
        subtitle5 = Text("スコアとは：データへ引き戻す回収ベクトル", font_size=28, color=PURPLE)
        subtitle5.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle5), run_time=0.5)
        self.wait(0.3)

        score_lbl = Text("スコア　＝", color=YELLOW, font_size=30)
        score_math = MathTex(
            r"\nabla_{\mathbf{x}}\log p_t(\mathbf{x})",
            color=YELLOW, font_size=40,
        )
        score_def = VGroup(score_lbl, score_math).arrange(RIGHT, buff=0.25)
        score_def.shift(UP * 2)
        self.play(Write(score_def), run_time=0.8)
        self.wait(0.3)

        score_desc = Text(
            "「密度 p_t(𝐱) が高い方向」＝「データがありそうな方向」を指すベクトル場",
            color=WHITE, font_size=24,
        )
        score_desc.next_to(score_def, DOWN, buff=0.3)
        self.play(Write(score_desc), run_time=0.8)
        self.wait(0.3)

        # 2次元のスコア場ポンチ絵：中心にデータ、外側から中心へのベクトル
        field_center = DOWN * 0.7
        # 等高線風の円
        circles = VGroup(
            Circle(radius=0.5, color=GOLD, stroke_width=2),
            Circle(radius=1.0, color=GOLD, stroke_width=1.5),
            Circle(radius=1.5, color=GOLD, stroke_width=1),
        )
        for c in circles:
            c.move_to(field_center)
        data_dot = Dot(field_center, color=WHITE, radius=0.09)
        data_lab = Text("高密度領域", color=GOLD, font_size=20)
        data_lab.next_to(circles[0], UP, buff=0.15)

        # スコア矢印（外周から中心方向）
        score_arrows = VGroup()
        for r in [1.3, 1.8]:
            n_ar = 8 if r < 1.6 else 10
            for angle in np.linspace(0, TAU, n_ar, endpoint=False):
                direction = np.array([np.cos(angle), np.sin(angle), 0])
                start = field_center + r * direction
                end = field_center + (r - 0.5) * direction
                score_arrows.add(Arrow(start, end, color=RED, buff=0,
                                       stroke_width=3,
                                       max_tip_length_to_length_ratio=0.35))

        self.play(Create(circles), Create(data_dot), Write(data_lab),
                  run_time=0.7)
        self.play(Create(score_arrows), run_time=1.2)

        score_arrow_lab = Text("スコア（回収力）", color=RED, font_size=24)
        score_arrow_lab.to_edge(RIGHT, buff=0.8).shift(DOWN * 0.5)
        self.play(Write(score_arrow_lab), run_time=0.5)
        self.wait(1.8)

        self.play(
            FadeOut(score_def), FadeOut(score_desc),
            FadeOut(circles), FadeOut(data_dot), FadeOut(data_lab),
            FadeOut(score_arrows), FadeOut(score_arrow_lab),
        )
        self.wait(0.3)

        # ============================================================
        # Part 6: 逆時間SDE
        # ============================================================
        subtitle6 = Text("逆時間SDE：ノイズから画像を生成する式", font_size=28, color=YELLOW)
        subtitle6.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle6), run_time=0.5)
        self.wait(0.3)

        rev_sde_intro = Text(
            "ドリフトの逆再生 + スコアの回収力 を組み合わせると：",
            color=WHITE, font_size=26,
        )
        rev_sde_intro.shift(UP * 1.8)
        self.play(Write(rev_sde_intro), run_time=0.7)
        self.wait(0.3)

        rev_sde = MathTex(
            r"d\mathbf{x} = \bigl[\,",
            r"\mathbf{f}(\mathbf{x}, t)",
            r"\;-\;",
            r"g(t)^2 \,\nabla_{\mathbf{x}}\log p_t(\mathbf{x})",
            r"\,\bigr]\,dt \;+\; g(t)\,d\bar{\mathbf{W}}",
            font_size=40,
        )
        rev_sde.set_color(WHITE)
        rev_sde[1].set_color(BLUE)
        rev_sde[3].set_color(RED)
        rev_sde.shift(UP * 0.7)
        rev_box = SurroundingRectangle(rev_sde, color=YELLOW, buff=0.25)
        self.play(Write(rev_sde), Create(rev_box), run_time=1.2)
        self.wait(0.4)

        annot1 = Text("元のドリフト", color=BLUE, font_size=26)
        annot1.next_to(rev_sde[1], DOWN, buff=0.9).shift(LEFT * 1.5)
        annot1_arrow = Arrow(annot1.get_top(), rev_sde[1].get_bottom(),
                             color=BLUE, buff=0.05, stroke_width=3,
                             max_tip_length_to_length_ratio=0.2)

        annot2 = Text("スコアによる回収項", color=RED, font_size=26)
        annot2.next_to(rev_sde[3], DOWN, buff=0.9).shift(RIGHT * 0.8)
        annot2_arrow = Arrow(annot2.get_top(), rev_sde[3].get_bottom(),
                             color=RED, buff=0.05, stroke_width=3,
                             max_tip_length_to_length_ratio=0.2)

        self.play(Write(annot1), GrowArrow(annot1_arrow),
                  Write(annot2), GrowArrow(annot2_arrow), run_time=1.0)
        self.wait(0.4)

        note = Text(
            "dt は t=T→0 の向き（負）なので、ドリフトの符号反転は自動で起きる",
            color=TEAL, font_size=24,
        )
        note.shift(DOWN * 2.4)
        self.play(Write(note), run_time=0.8)
        self.wait(1.8)

        self.play(
            FadeOut(rev_sde_intro), FadeOut(rev_sde), FadeOut(rev_box),
            FadeOut(annot1), FadeOut(annot1_arrow),
            FadeOut(annot2), FadeOut(annot2_arrow), FadeOut(note),
        )
        self.wait(0.3)

        # ============================================================
        # Part 7: サンプリングの流れ（オイラー・丸山）
        # ============================================================
        subtitle7 = Text("サンプリング：時間を遡る(オイラー・丸山法)", font_size=28, color=TEAL)
        subtitle7.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle7), run_time=0.5)
        self.wait(0.3)

        step_intro = Text(
            "学習済みネットワークが計算するスコアを組み込んで、離散化して解く",
            color=WHITE, font_size=25,
        )
        step_intro.shift(UP * 2.1)
        self.play(Write(step_intro), run_time=0.7)
        self.wait(0.3)

        step1 = Text(
            "① 完全なガウスノイズ 𝐱_T ～ 𝒩(0, 𝐈) を用意する",
            color=WHITE, font_size=24,
        )
        step2 = Text(
            "② 逆時間SDE を 1ステップずつ差分近似で解き進める（t=T → 0）",
            color=WHITE, font_size=24,
        )
        step3 = Text(
            "③ 目的地 t=0 に到達したとき、1枚のきれいな画像 𝐱_0 が得られる",
            color=WHITE, font_size=24,
        )
        steps = VGroup(step1, step2, step3).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        steps.shift(UP * 0.9)
        for s in steps:
            self.play(Write(s), run_time=0.6)
        self.wait(0.3)

        # 逆再生のポンチ絵：多数の粒子が「拡散→整列」していくアニメ
        # 2D の絵にして、Part 2 のインク拡散のアナロジーと直接つなげる
        panel = Rectangle(width=8.5, height=3.0, color=WHITE, stroke_width=1.5)
        panel.shift(DOWN * 2.0)

        rng_r = np.random.default_rng(11)
        n_particles = 40

        # 目標位置：データ多様体を「横方向の細い帯」で表現
        target_xs = np.linspace(-3.5, 3.5, n_particles)
        target_ys = 0.05 * rng_r.standard_normal(n_particles)
        # 順序をシャッフルして「粒子 i がどこに行くか」に必然性を持たせない
        perm = rng_r.permutation(n_particles)
        target_xs = target_xs[perm]

        panel_center = panel.get_center()
        # 初期位置：パネル内に広く散らばったガウスノイズ
        init_pos = rng_r.normal(0, 0.9, size=(n_particles, 2))
        # y方向もある程度散らす
        init_pos[:, 1] *= 0.9

        particles = VGroup()
        for i in range(n_particles):
            p = Dot(
                panel_center + np.array([init_pos[i, 0], init_pos[i, 1], 0]),
                color=RED, radius=0.06,
            )
            particles.add(p)

        # 時間進行を示すバー（t=T → t=0）
        bar_len = 6.5
        bar_left = panel.get_top() + LEFT * bar_len / 2 + UP * 0.35
        bar_right = panel.get_top() + RIGHT * bar_len / 2 + UP * 0.35
        bar_line = Line(bar_left, bar_right, color=WHITE, stroke_width=2)
        t_T_lab = MathTex("t{=}T", color=RED, font_size=22).next_to(bar_left, LEFT, buff=0.2)
        t_0_lab = MathTex("t{=}0", color=GREEN, font_size=22).next_to(bar_right, RIGHT, buff=0.2)
        marker = Dot(bar_left, color=YELLOW, radius=0.09)

        noise_lab = Text("ノイズ（拡散した粒子）", color=RED, font_size=22)
        noise_lab.next_to(panel, DOWN, buff=0.15)

        self.play(Create(panel), Create(bar_line),
                  Write(t_T_lab), Write(t_0_lab), Create(marker),
                  run_time=0.6)
        self.play(FadeIn(particles), Write(noise_lab), run_time=0.7)
        self.wait(0.6)

        # 段階的に粒子を目標位置へ整列させる（複数中間ステップで“凝集”を表現）
        n_stages = 4
        for s in range(1, n_stages + 1):
            alpha = s / n_stages
            # 各粒子の中間目標＝初期位置と目標位置の内挿 + 残ノイズ（減衰）
            resid_scale = (1 - alpha) * 0.35
            anims = []
            for i, p in enumerate(particles):
                interp_x = (1 - alpha) * init_pos[i, 0] + alpha * target_xs[i]
                interp_y = (1 - alpha) * init_pos[i, 1] + alpha * target_ys[i]
                # 残ノイズを足す
                interp_x += resid_scale * rng_r.standard_normal()
                interp_y += resid_scale * rng_r.standard_normal()
                new_pos = panel_center + np.array([interp_x, interp_y, 0])
                anims.append(p.animate.move_to(new_pos))
            # 進行マーカーも動かす
            marker_target = bar_left + (bar_right - bar_left) * alpha
            anims.append(marker.animate.move_to(marker_target))
            self.play(*anims, run_time=0.9)
            self.wait(0.15)

        # 最終ラベルへ差し替え
        image_lab = Text("整列した粒子＝生成された画像", color=GREEN, font_size=22)
        image_lab.next_to(panel, DOWN, buff=0.15)
        self.play(Transform(noise_lab, image_lab),
                  particles.animate.set_color(GREEN),
                  run_time=0.6)
        self.wait(1.5)

        self.play(
            FadeOut(step_intro), FadeOut(steps),
            FadeOut(panel), FadeOut(particles),
            FadeOut(bar_line), FadeOut(t_T_lab), FadeOut(t_0_lab),
            FadeOut(marker), FadeOut(noise_lab),
        )
        self.wait(0.3)

        # ============================================================
        # Part 8: ニューラルネットワークの入出力
        # ============================================================
        subtitle8 = Text("ニューラルネットワークの入出力", font_size=28, color=GREEN)
        subtitle8.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle8), run_time=0.5)
        self.wait(0.3)

        nn_intro = Text(
            "スコアや加えたノイズは、ニューラルネットワークで近似する",
            color=WHITE, font_size=26,
        )
        nn_intro.shift(UP * 2.1)
        self.play(Write(nn_intro), run_time=0.7)
        self.wait(0.3)

        # NNのポンチ絵
        nn_box = Rectangle(width=2.6, height=1.8, color=YELLOW, stroke_width=3)
        nn_box.shift(DOWN * 0.2)
        nn_label = Text("NN\n(θ)", color=YELLOW, font_size=28)
        nn_label.move_to(nn_box.get_center())

        in1 = MathTex(r"\mathbf{x}", color=WHITE, font_size=36)
        in1.next_to(nn_box, LEFT, buff=1.5).shift(UP * 0.5)
        in2 = MathTex(r"t", color=WHITE, font_size=36)
        in2.next_to(nn_box, LEFT, buff=1.5).shift(DOWN * 0.5)

        out_math1 = MathTex(r"\mathbf{s}_\theta(\mathbf{x}, t)",
                            color=WHITE, font_size=30)
        out_or = Text("または", color=WHITE, font_size=24)
        out_math2 = MathTex(r"\boldsymbol{\epsilon}_\theta(\mathbf{x}, t)",
                            color=WHITE, font_size=30)
        out = VGroup(out_math1, out_or, out_math2).arrange(RIGHT, buff=0.2)
        out.next_to(nn_box, RIGHT, buff=1.2)

        arr_in1 = Arrow(in1.get_right(), nn_box.get_left() + UP * 0.5,
                        color=WHITE, buff=0.15, stroke_width=3)
        arr_in2 = Arrow(in2.get_right(), nn_box.get_left() + DOWN * 0.5,
                        color=WHITE, buff=0.15, stroke_width=3)
        arr_out = Arrow(nn_box.get_right(), out.get_left(),
                        color=WHITE, buff=0.15, stroke_width=3)

        in_lab = Text("入力", color=BLUE, font_size=22).next_to(in1, UP, buff=0.8)
        out_lab = Text("出力：𝐱と同次元のベクトル", color=RED, font_size=22)
        out_lab.next_to(out, DOWN, buff=0.4)

        self.play(Create(nn_box), Write(nn_label), run_time=0.5)
        self.play(Write(in1), Write(in2), GrowArrow(arr_in1), GrowArrow(arr_in2),
                  Write(in_lab), run_time=0.8)
        self.play(GrowArrow(arr_out), Write(out), Write(out_lab), run_time=0.8)
        self.wait(0.4)

        in_desc = Text(
            "𝐱：時刻 t のノイズ混じりの状態    t：現在のノイズ強度",
            color=WHITE, font_size=22,
        )
        in_desc.shift(DOWN * 2.5)
        self.play(Write(in_desc), run_time=0.7)
        self.wait(1.8)

        self.play(
            FadeOut(nn_intro), FadeOut(nn_box), FadeOut(nn_label),
            FadeOut(in1), FadeOut(in2), FadeOut(out),
            FadeOut(arr_in1), FadeOut(arr_in2), FadeOut(arr_out),
            FadeOut(in_lab), FadeOut(out_lab), FadeOut(in_desc),
        )
        self.wait(0.3)

        # ============================================================
        # Part 9: パラメータ化の2つのアプローチ
        # ============================================================
        subtitle9 = Text("何を予測させるか：スコア型 vs ノイズ型", font_size=28, color=BLUE)
        subtitle9.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle9), run_time=0.5)
        self.wait(0.3)

        para1_title = Text("① スコア予測型", color=GOLD, font_size=26, weight=BOLD)
        para1_eq = MathTex(
            r"\mathbf{s}_\theta(\mathbf{x}, t) \;\approx\; "
            r"\nabla_{\mathbf{x}}\log p_t(\mathbf{x})",
            color=YELLOW, font_size=38,
        )
        para1_group = VGroup(para1_title, para1_eq).arrange(DOWN, buff=0.25)
        para1_group.shift(UP * 1.5)
        self.play(Write(para1_title), Write(para1_eq), run_time=0.9)
        self.wait(0.3)

        para2_title = Text("② ノイズ予測型（こちらの方が実装例は多い）",
                           color=GOLD, font_size=26, weight=BOLD)
        para2_desc = Text(
            "順過程で加えられた標準ガウスノイズ 𝜀 ～ 𝒩(0, 𝐈) を予測",
            color=WHITE, font_size=22,
        )
        para2_eq = MathTex(
            r"\nabla_{\mathbf{x}}\log p_t(\mathbf{x}) \;=\; "
            r"-\frac{\boldsymbol{\epsilon}_\theta(\mathbf{x}, t)}{\sigma_t}",
            color=YELLOW, font_size=38,
        )
        para2_group = VGroup(para2_title, para2_desc, para2_eq).arrange(DOWN, buff=0.2)
        para2_group.shift(DOWN * 1.1)
        self.play(Write(para2_title), Write(para2_desc), Write(para2_eq), run_time=1.1)
        self.wait(0.4)

        conv_note = Text("σ_t は時刻 t におけるノイズの標準偏差", color=TEAL, font_size=22)
        conv_note.shift(DOWN * 2.7)
        self.play(Write(conv_note), run_time=0.6)
        self.wait(1.8)

        self.play(
            FadeOut(para1_title), FadeOut(para1_eq),
            FadeOut(para2_title), FadeOut(para2_desc), FadeOut(para2_eq),
            FadeOut(conv_note),
        )
        self.wait(0.3)

        # ============================================================
        # Part 10: 逆時間SDEへの組み込み
        # ============================================================
        subtitle10 = Text("逆時間SDEへの組み込み", font_size=28, color=ORANGE)
        subtitle10.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle10), run_time=0.5)
        self.wait(0.3)

        emb_intro = Text(
            "学習済みNNの出力を、真のスコアの位置に代入する",
            color=WHITE, font_size=26,
        )
        emb_intro.shift(UP * 2)
        self.play(Write(emb_intro), run_time=0.7)
        self.wait(0.3)

        emb1_title = Text("① スコア予測型を組み込む", color=GOLD, font_size=24)
        emb1_eq = MathTex(
            r"d\mathbf{x} = \bigl[\mathbf{f}(\mathbf{x}, t) "
            r"- g(t)^2 \mathbf{s}_\theta(\mathbf{x}, t)\bigr]dt "
            r"+ g(t)\,d\bar{\mathbf{W}}",
            color=YELLOW, font_size=38,
        )
        emb1_group = VGroup(emb1_title, emb1_eq).arrange(DOWN, buff=0.2)
        emb1_group.shift(UP * 0.7)
        self.play(Write(emb1_title), Write(emb1_eq), run_time=1.0)
        self.wait(0.3)

        emb2_title = Text("② ノイズ予測型を組み込む", color=GOLD, font_size=24)
        emb2_eq = MathTex(
            r"d\mathbf{x} = \Bigl[\mathbf{f}(\mathbf{x}, t) "
            r"+ \frac{g(t)^2}{\sigma_t} \boldsymbol{\epsilon}_\theta(\mathbf{x}, t)\Bigr]dt "
            r"+ g(t)\,d\bar{\mathbf{W}}",
            color=YELLOW, font_size=38,
        )
        emb2_group = VGroup(emb2_title, emb2_eq).arrange(DOWN, buff=0.2)
        emb2_group.shift(DOWN * 0.9)
        self.play(Write(emb2_title), Write(emb2_eq), run_time=1.0)
        self.wait(0.4)

        sign_note = Text(
            "※ 符号が「−」から「+」に反転するのは、スコアとノイズの関係式にある − と打ち消し合うため",
            color=TEAL, font_size=22,
        )
        sign_note.shift(DOWN * 2.4)
        self.play(Write(sign_note), run_time=0.9)
        self.wait(2.0)

        self.play(
            FadeOut(emb_intro),
            FadeOut(emb1_title), FadeOut(emb1_eq),
            FadeOut(emb2_title), FadeOut(emb2_eq),
            FadeOut(sign_note),
        )
        self.wait(0.3)

        # ============================================================
        # Part 11: 学習の損失関数
        # ============================================================
        subtitle11 = Text("学習：シンプルな2乗誤差", font_size=28, color=GREEN)
        subtitle11.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle11), run_time=0.5)
        self.wait(0.3)

        loss_intro = Text(
            "ノイズ予測型 𝜀_θ の学習は、次の MSE Loss で行う",
            color=WHITE, font_size=26,
        )
        loss_intro.shift(UP * 2)
        self.play(Write(loss_intro), run_time=0.7)
        self.wait(0.3)

        loss_eq = MathTex(
            r"\mathcal{L}(\theta) = "
            r"\mathbb{E}_{t,\, \mathbf{x}_0,\, \boldsymbol{\epsilon}} "
            r"\Bigl[\, \bigl\|\boldsymbol{\epsilon} "
            r"- \boldsymbol{\epsilon}_\theta(\mathbf{x}_t, t)\bigr\|^2 \,\Bigr]",
            color=YELLOW, font_size=42,
        )
        loss_eq.shift(UP * 0.6)
        loss_box = SurroundingRectangle(loss_eq, color=YELLOW, buff=0.25)
        self.play(Write(loss_eq), Create(loss_box), run_time=1.0)
        self.wait(0.3)

        proc1 = Text(
            "① 元データ 𝐱_0 にノイズ 𝜀 を加え、時刻 t の状態 𝐱_t を作る",
            color=WHITE, font_size=24,
        )
        proc2 = Text(
            "② ネットワークに (𝐱_t, t) を渡し、加えたノイズを予測させる",
            color=WHITE, font_size=24,
        )
        proc3 = Text(
            "③ 正解ノイズ 𝜀 との差が小さくなるよう、勾配降下法で θ を更新",
            color=WHITE, font_size=24,
        )
        procs = VGroup(proc1, proc2, proc3).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        procs.shift(DOWN * 1.6)
        for p in procs:
            self.play(Write(p), run_time=0.6)
        self.wait(1.8)

        self.play(
            FadeOut(loss_intro), FadeOut(loss_eq), FadeOut(loss_box),
            FadeOut(procs),
        )
        self.wait(0.3)

        # ============================================================
        # Part 12: まとめ
        # ============================================================
        subtitle12 = Text("まとめ", font_size=36, color=TEAL)
        subtitle12.next_to(title, DOWN)
        self.play(Transform(subtitle1, subtitle12), run_time=0.6)
        self.wait(0.3)

        summary = VGroup(
            Text("• 順過程：d𝐱 = 𝐟(𝐱,t)dt + g(t)d𝐖  でデータがガウスノイズへ変化する様子をモデリング",
                 color=WHITE, font_size=24),
            Text("• 拡散項は水中でインクが散らばるブラウン運動のアナロジー",
                 color=WHITE, font_size=24),
            Text("• 逆過程には「時間逆再生」＋「スコア（密度が高い方向）による回収力」が必要",
                 color=WHITE, font_size=24),
            Text("• 逆時間SDE：d𝐱 = [𝐟 − g(t)² ∇log p_t] dt + g(t)d𝐖̄",
                 color=WHITE, font_size=24),
            Text("• スコアや加えたノイズをNNで近似（スコア型 / ノイズ型の2大アプローチ）",
                 color=WHITE, font_size=24),
            Text("• 学習はシンプルなMSE：正解ノイズと予測ノイズの2乗誤差最小化",
                 color=WHITE, font_size=24),
            Text("• 生成はガウスノイズから出発し、オイラー・丸山近似で t=T→0 に軌道を辿る",
                 color=WHITE, font_size=24),
            Text("• 拡散モデル ＝「ノイズ化SDEの逆再生 ＋ スコアによる補正」",
                 color=GOLD, font_size=24, weight=BOLD),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        summary.shift(DOWN * 0.2)

        for row in summary:
            self.play(Write(row), run_time=0.5)
            self.wait(0.15)
        self.wait(2.0)

        self.play(
            FadeOut(VGroup(title, subtitle1, summary)),
            run_time=1.0,
        )
        self.wait(0.5)
