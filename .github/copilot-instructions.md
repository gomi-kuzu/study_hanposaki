# Manim線形代数可視化プロジェクト - Copilot指示書

このドキュメントは、本プロジェクトでManimアニメーションを作成する際の統一規則とベストプラクティスをまとめたものです。

## プロジェクト概要

線形代数の概念（ベクトル、行列、内積、基底、直交化など）をManimライブラリで可視化する教育用アニメーションプロジェクト。すべてのアニメーションは日本語で説明され、数学的概念を直感的に理解できるよう設計されています。

## 必須設定

### 1. 基本構造

すべてのアニメーションは以下の基本構造に従います：

```python
from manim import *

class ClassName(ThreeDScene):  # または Scene
    def construct(self):
        # 背景色を設定（必須）
        self.camera.background_color = "#012817"
        
        # タイトル
        title = Text("タイトル名", font_size=40, color=WHITE)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)  # ThreeDSceneの場合
        self.play(Write(title), run_time=0.8)
        self.wait(0.8)
        
        # 以降、パート構成で展開
```

### 2. ThreeDScene vs Scene

- **3D要素が必要な場合**: `ThreeDScene`を継承
- **2D平面のみの場合**: `Scene`を継承

**ThreeDScene使用時の注意点**:
- すべてのテキスト・UI要素は`self.add_fixed_in_frame_mobjects()`で固定する
- 3D空間内のラベル（ベクトルの先端など）は`self.add_fixed_orientation_mobjects()`を使用
- カメラの向きを設定: `self.set_camera_orientation(phi=70*DEGREES, theta=45*DEGREES)`
- 正面ビューに戻す: `self.set_camera_orientation(phi=0, theta=-90*DEGREES)`
- 2Dビュー（真正面）: `self.set_camera_orientation(phi=0, theta=-90*DEGREES)`
- カメラ角度を切り替えることで、2Dと3Dの表現を切り替え可能

## スタイルガイド

### 色使いの規則

| 用途 | 色 | 用途例 |
|------|------|--------|
| タイトル・基本テキスト | `WHITE` | メインテキスト |
| サブタイトル・強調 | `YELLOW` | セクション見出し、重要な概念 |
| 定義・説明 | `BLUE` | 第1のベクトル、基底 |
| 対比・第2要素 | `RED` | 第2のベクトル、異なる基底 |
| 結果・成功 | `GREEN` | 正解、完成形 |
| 警告・注意 | `ORANGE` | 補足説明 |
| 座標軸 | `GRAY` | グリッド、補助線 |

### フォントサイズの規則

- **メインタイトル**: `font_size=40` または `font_size=44`
- **サブタイトル**: `font_size=32`
- **セクション見出し**: `font_size=28`
- **説明テキスト**: `font_size=24` または `font_size=26`
- **補足テキスト**: `font_size=22`
- **数式ラベル**: `font_size=24` - `font_size=32`

### タイミング規則

```python
# アニメーション時間
run_time=0.8    # 標準的な書き込み・作成
run_time=0.6    # 短いアニメーション
run_time=1.0    # 複雑なアニメーション

# 待機時間
self.wait(0.3)  # 短い間
self.wait(0.5)  # 標準的な間
self.wait(0.8)  # 長めの間
self.wait(1.0)  # 重要な内容の後
self.wait(1.2)  # セクション終了時
```

## アニメーション構成パターン

### パート分け構造

各アニメーションは複数のパートで構成：

```python
# === パート1: 導入 ===
subtitle1 = Text("パート1のタイトル", font_size=32, color=YELLOW)
subtitle1.next_to(title, DOWN)
self.add_fixed_in_frame_mobjects(subtitle1)
self.play(Write(subtitle1), run_time=0.6)
self.wait(0.5)

# パート1の内容
# ...

# クリーンアップ
self.play(FadeOut(subtitle1), FadeOut(other_objects))
self.wait(0.3)

# === パート2: 次の展開 ===
subtitle2 = Text("パート2のタイトル", font_size=32, color=BLUE)
# ...
```

### 座標軸とグリッドの標準設定

```python
# 2D座標軸
axes = Axes(
    x_range=[-1, 4, 1],
    y_range=[-1, 4, 1],
    x_length=5,
    y_length=5,
    axis_config={"color": GRAY}
)
axes.shift(LEFT * 3.5)  # 左側に配置して右側を説明用に空ける

# グリッド（背景方眼）
grid = NumberPlane(
    x_range=[-1, 4, 1],
    y_range=[-1, 4, 1],
    x_length=5,
    y_length=5,
    background_line_style={
        "stroke_color": BLUE_E,
        "stroke_width": 1,
        "stroke_opacity": 0.3
    },
    axis_config={"stroke_opacity": 0}
)
grid.shift(LEFT * 3.5)

# 座標軸ラベル
x_label = Text("X", color=RED, font_size=22)
y_label = Text("Y", color=GREEN, font_size=22)
x_label.next_to(axes.get_x_axis().get_end(), DOWN)
y_label.next_to(axes.get_y_axis().get_end(), LEFT)
```

### ベクトルの標準表示

**2Dベクトル:**
```python
# ベクトルの作成
vector = Vector(
    axes.c2p(x, y) - axes.c2p(0, 0),
    color=BLUE,
    stroke_width=6
).shift(axes.c2p(0, 0))

# ラベル
vector_label = MathTex(r"\mathbf{v}", color=BLUE, font_size=28)
vector_label.next_to(vector.get_end(), RIGHT, buff=0.2)

# 表示
self.play(Create(vector), Write(vector_label), run_time=0.7)
self.wait(0.5)
```

**3Dベクトル（Arrow3D）:**
```python
# 3Dベクトルの作成
vector_3d = Arrow3D(
    start=axes.c2p(0, 0, 0),
    end=axes.c2p(1, 2, 1),
    color=BLUE,
    thickness=0.02,      # 矢印の太さ
    height=0.2,          # 矢印の頭の高さ
    base_radius=0.08     # 矢印の頭の底面半径
)

# 3D空間内のラベル
label_3d = MathTex(r"\mathbf{v}", color=BLUE, font_size=28)
label_3d.next_to(axes.c2p(1, 2, 1), RIGHT, buff=0.1)
self.add_fixed_orientation_mobjects(label_3d)  # 3D空間内に配置

self.play(Create(vector_3d), Write(label_3d), run_time=0.7)
self.wait(0.5)
```

### 説明テキストの配置

**基本配置:**
```python
# 右側に説明を配置（左側は図）
explanation = VGroup(
    Text("説明行1", color=WHITE, font_size=26),
    Text("説明行2", color=YELLOW, font_size=26),
).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
explanation.to_edge(RIGHT).shift(LEFT * 1.5 + UP * 1.5)
```

**コーナー配置:**
```python
# 右下に配置
note = Text("補足説明", color=YELLOW, font_size=24, slant=ITALIC)
note.to_corner(DR).shift(UP * 0.5)  # 右下から少し上に

# その他のコーナー
# UL: 左上, UR: 右上, DL: 左下, DR: 右下
```

**位置の明示的指定:**
```python
# 特定の座標に配置
text = Text("テキスト", font_size=26)
text.shift(UP * 2.2)  # または
text.shift(DOWN * 1.5 + LEFT * 3.5)
```

## 数式の記述規則

### ベクトルの表記

```python
# 列ベクトル
MathTex(r"\mathbf{v} = \begin{bmatrix} x \\ y \\ z \end{bmatrix}")

# 行ベクトル（転置）
MathTex(r"\mathbf{v}^T = \begin{bmatrix} x & y & z \end{bmatrix}")

# ブラケット記法（量子力学風）
MathTex(r"|v\rangle = \begin{bmatrix} x \\ y \\ z \end{bmatrix}")
```

### 行列の表記

```python
# 基本的な行列
MathTex(r"A = \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix}")

# 省略記法を使った大きな行列
MathTex(r"A = \begin{bmatrix} a_{11} & \cdots & a_{1n} \\" 
        r"\vdots & \ddots & \vdots \\" 
        r"a_{m1} & \cdots & a_{mn} \end{bmatrix}")
```

### 内積の表記

```python
# 関数記法
MathTex(r"(\mathbf{a}, \mathbf{b})")

# 転置記法
MathTex(r"\mathbf{a}^T \mathbf{b}")

# ドット記法
MathTex(r"\mathbf{a} \cdot \mathbf{b}")

# ブラケット記法
MathTex(r"\langle a | b \rangle")
```

## よくある実装パターン

### パターン1: 複数要素の順次表示

```python
elements = [elem1, elem2, elem3]
labels = [label1, label2, label3]

for element, label in zip(elements, labels):
    self.play(Create(element), Write(label), run_time=0.7)
    self.wait(0.3)
```

### パターン2: 強調表示

```python
# 色を変えて強調
self.play(
    vector.animate.set_color(YELLOW),
    label.animate.set_color(YELLOW),
    run_time=0.4
)
self.wait(0.3)

# ボックスで囲んで強調
important_text = Text("重要なポイント", color=YELLOW, font_size=26, weight=BOLD)
important_box = SurroundingRectangle(important_text, color=YELLOW, buff=0.2)
self.play(Write(important_text), Create(important_box), run_time=0.9)
self.wait(1.2)
```

### パターン3: 計算過程の表示

```python
# 式を段階的に表示
eq1 = MathTex(r"\mathbf{v} = 2\mathbf{a} + 3\mathbf{b}", font_size=32)
eq1.to_edge(RIGHT).shift(UP * 2)
self.play(Write(eq1), run_time=0.6)
self.wait(0.4)

# 計算結果
calc1 = MathTex(
    r"= 2\begin{bmatrix} 1 \\ 0 \end{bmatrix} + 3\begin{bmatrix} 0 \\ 1 \end{bmatrix}",
    font_size=28
)
calc1.next_to(eq1, DOWN, buff=0.3, aligned_edge=RIGHT)
self.play(Write(calc1), run_time=0.6)
self.wait(0.4)

# 最終結果
result = MathTex(r"= \begin{bmatrix} 2 \\ 3 \end{bmatrix}", font_size=28)
result.next_to(calc1, DOWN, buff=0.3, aligned_edge=RIGHT)
self.play(Write(result), run_time=0.6)
self.wait(0.5)
```

### パターン4: Transformアニメーション

**基本的なTransform:**
```python
# オブジェクトを別のオブジェクトに変換
original = Arrow(ORIGIN, [2, 1, 0], color=GREEN)
target = Arrow(ORIGIN, [1, 2, 0], color=BLUE)

# コピーを作成して変換（元のオブジェクトは保持）
transform_copy = original.copy()
self.add(transform_copy)
self.play(Transform(transform_copy, target), run_time=1.0)
self.wait(0.5)

# 後でtransform_copyも削除することを忘れずに
self.play(FadeOut(transform_copy))
```

**TransformFromCopy:**
```python
# 元のオブジェクトから新しいオブジェクトへのコピー変換
matrix_A = MathTex(r"A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}")
a_row = MathTex(r"[1, 2]")

self.play(TransformFromCopy(matrix_A, a_row), run_time=0.8)
self.wait(0.5)
```

## ThreeDSceneでの3D可視化

### 基本的な3D設定

```python
# カメラアングル設定
self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)

# 3D座標軸
axes_3d = ThreeDAxes(
    x_range=[-2, 3, 1],
    y_range=[-2, 3, 1],
    z_range=[-2, 2, 1],
    x_length=6,
    y_length=6,
    z_length=4,
    axis_config={"color": GREY}
)

# 3Dベクトル
vector_3d = Arrow3D(
    start=axes_3d.c2p(0, 0, 0),
    end=axes_3d.c2p(1, 2, 1),
    color=BLUE,
    thickness=0.02,
    height=0.2,
    base_radius=0.08
)
```

### 2Dと3Dの切り替え

```python
# 3Dビューで開始
self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)
# ... 3D表示 ...

# 2Dビュー（正面）に切り替え
self.set_camera_orientation(phi=0, theta=-90*DEGREES)
# ... 2D表示 ...

# 再び3Dビューに戻す
self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)
```

### 3D空間でのラベル配置

```python
# UIテキスト（常にカメラに正対）
title = Text("タイトル", font_size=32)
self.add_fixed_in_frame_mobjects(title)  # カメラに固定

# 3D空間内のラベル（空間内の特定位置に配置）
label_3d = MathTex(r"\mathbf{v}", color=BLUE, font_size=28)
label_3d.next_to(axes.c2p(1, 2, 1), RIGHT, buff=0.1)
self.add_fixed_orientation_mobjects(label_3d)  # 向きは固定、位置は3D空間内
```

## コメント記法

### コメント省略記法

長いコード内で繰り返し部分を省略する場合：

```python
for i, (coord, name, pos) in enumerate(zip(a_coords, a_names, a_positions)):
    /* Lines 61-72 omitted */
```

この記法は添付ファイルで使用されており、繰り返しパターンを示す際に有効です。

## エラー処理とデバッグ

### よくあるエラーと対処法

1. **ThreeDSceneでテキストが回転する**
   - 解決: `self.add_fixed_in_frame_mobjects(text)`を使用

2. **座標がずれる**
   - 解決: `axes.c2p(x, y)`で座標変換を正しく使用

3. **日本語が表示されない**
   - 解決: システムに日本語フォントがインストールされていることを確認

4. **MathTexで日本語を使うとLaTeXエラーが発生する（超重要）**
   - 問題: `MathTex(r"\text{影}")`のように日本語をLaTeX内で使用するとコンパイルエラー
   - 解決: 日本語テキストは必ず`Text()`を使用する
   ```python
   # ❌ エラーになる
   label = MathTex(r"\text{影}", color=GREEN)
   label = MathTex(r"\text{影の長さ}", color=GREEN)
   
   # ✅ 正しい書き方
   label = Text("影", color=GREEN, font_size=28)
   label = Text("影の長さ", color=GREEN, font_size=28)
   ```
   - 数式に日本語を混在させたい場合は、`Text()`と`MathTex()`を`VGroup`で組み合わせる：
   ```python
   # ✅ 推奨パターン
   combined = VGroup(
       Text("影の長さ = ", color=WHITE, font_size=24),
       MathTex(r"\|\mathbf{x}\| \cos\theta", color=GREEN, font_size=24),
   ).arrange(RIGHT, buff=0.2)
   ```

5. **アニメーションが速すぎる/遅すぎる**
   - 解決: `run_time`と`wait()`の値を本ガイドの推奨値に調整

## ファイル命名規則

プロジェクトのファイル命名パターン：

- `sec{章番号}_{節番号}.py`: 基本パターン
- `sec{章番号}_{節番号}_no{番号}.py`: 複数ファイルに分割する場合
- `sec{章番号}_{節番号}_no{番号}no{番号}.py`: さらに細分化する場合

例:
- `sec1_1.py`: 第1章第1節
- `sec2_1_no1.py`: 第2章第1節の1番目のファイル
- `sec2_1_no1no2.py`: 第2章第1節の1番目のサブトピックの2番目のファイル

## レンダリングコマンド

```bash
# プレビュー品質（低解像度・高速）
manim -pql filename.py ClassName

# 高品質
manim -pqh filename.py ClassName

# 4K品質
manim -pqk filename.py ClassName

# 静止画のみ
manim -sqh filename.py ClassName
```

## ベストプラクティス

### 1. 段階的な表示

一度に多くの要素を表示せず、段階的に構築する：

```python
# ❌ 避けるべき
self.add(elem1, elem2, elem3, elem4, elem5)

# ✅ 推奨
self.play(Create(elem1), run_time=0.7)
self.wait(0.3)
self.play(Create(elem2), run_time=0.7)
self.wait(0.3)
```

### 1.5. Transformアニメーション使用時の注意

Transformを使う場合は、コピーを作成して変換し、元のオブジェクトは保持する：

```python
# ✅ 正しいパターン
original = Arrow(ORIGIN, [2, 1, 0], color=GREEN)
self.play(Create(original), run_time=0.7)

# 変換用のコピーを作成
transform_copy = original.copy()
self.add(transform_copy)

target = Arrow(ORIGIN, [1, 2, 0], color=BLUE)
self.play(Transform(transform_copy, target), run_time=1.0)

# 最後にコピーも削除
self.play(FadeOut(original), FadeOut(transform_copy))
```

### 2. 視覚的な整理

- 図は左側、説明は右側
- タイトルは常に上部に固定
- 関連する要素は`VGroup`でグループ化

### 3. 適切なwait時間

- 新しい概念の導入後: `wait(1.0)` 以上
- 計算ステップの間: `wait(0.5)`
- アニメーション間: `wait(0.3)`

### 4. クリーンアップ

各パートの終わりに不要な要素を削除：

```python
self.play(FadeOut(elem1), FadeOut(elem2), FadeOut(subtitle))
self.wait(0.3)
```

### 5. 一貫性の維持

- 同じ概念には同じ色を使用
- ベクトル記号は太字 (`\mathbf`)
- 数式のフォントサイズは統一

### 6. テキスト装飾の活用

重要度や役割に応じてテキスト属性を使い分ける：

```python
# 通常のテキスト
normal_text = Text("説明文", font_size=26, color=WHITE)

# 強調（太字）
important_text = Text("重要", font_size=26, color=YELLOW, weight=BOLD)

# イタリック体（補足・注釈）
note_text = Text("補足説明", font_size=24, color=ORANGE, slant=ITALIC)

# 太字＋イタリック（最重要）
key_point = Text("キーポイント", font_size=28, color=GREEN, 
                 weight=BOLD, slant=ITALIC)
```

## プロジェクト固有の数学概念

### 扱うトピック

1. **ベクトルの基本** (sec1_*): ベクトルの表現、線形結合
2. **線形独立と基底** (sec2_*): 1次独立、1次従属、基底の概念、基底変換
3. **内積** (sec3_*): 内積の定義、ノルム、距離、内積の3つの視点
4. **角度と直交性** (sec4_*): ベクトルの成す角、直交基底の便利さ、グラム-シュミット直交化法
5. **行列** (sec5_*): 行列の積の直感的理解（経路の総和）、線型変換の性質、非可換性

### 表記の統一

- ベクトル: `\mathbf{v}`, `\mathbf{a}`, `\mathbf{x}`
- 基底: `\mathbf{e}_1, \mathbf{e}_2, ...`
- 行列: `A, B, C` (大文字、太字なし)
- スカラー: `c, \alpha, \lambda` (小文字、イタリック)
- ノルム: `\|\mathbf{v}\|`
- 内積: `(\mathbf{a}, \mathbf{b})` または `\mathbf{a}^T\mathbf{b}`

## まとめ

このガイドに従うことで、プロジェクト全体で一貫性のある、視覚的に美しく、教育的に効果的なManimアニメーションを作成できます。新しいファイルを作成する際は、既存のファイル（特に`sec2_1_no1no2.py`, `sec3_1.py`, `sec4_2.py`など）を参考にしてください。

---

**最終更新**: 2026年1月10日
**対象Manimバージョン**: Community Edition (CE) v0.18.0+
