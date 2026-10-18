import matplotlib
import matplotlib.patches as patches
import matplotlib.pyplot as plt

# 日本語フォント設定（環境に合わせて 'Japan' / 'Gothic' 系フォントを指定）
plt.rcParams['font.sans-serif'] = [
    'Noto Sans CJK JP',
    'Noto Sans JP',
    'Hiragino Sans',
    'Yu Gothic',
    'sans-serif',
]
plt.rcParams['axes.unicode_minus'] = False

# キャンバスの作成（アスペクト比と解像度の設定）
fig, ax = plt.subplots(figsize=(10, 6.5), dpi=200)
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis('off')

# 配色設定（資料のトーンを模したナチュラルカラー）
green_bg = '#708E50'  # 前の時刻での状態（緑）
orange_bg = '#D76C51'  # 次の時刻での状態（テラコッタ）
blue_arrow = '#3B75B4'  # 時間発展矢印（青）
red_accent = '#D9381E'  # クープマン作用素（赤）
gray_dashed = '#666666'  # 観測の点線（グレー）

# --- 1. 上段：状態 x_n と y_n ---

# 左上：前の時刻での状態ボックス & x_n
rect_left = patches.FancyBboxPatch(
    (0.5, 5.4),
    2.8,
    0.55,
    boxstyle='round,pad=0.08,rounding_size=0.15',
    facecolor=green_bg,
    edgecolor='none',
)
ax.add_patch(rect_left)
ax.text(
    1.9,
    5.675,
    '前の時刻での状態',
    color='white',
    fontsize=11,
    fontweight='bold',
    ha='center',
    va='center',
)
ax.text(
    3.5,
    5.675,
    r'$\boldsymbol{x}_n$',
    color='#222222',
    fontsize=15,
    fontweight='bold',
    ha='center',
    va='center',
)

# 右上：次の時刻での状態ボックス & y_n
rect_right = patches.FancyBboxPatch(
    (6.0, 5.4),
    2.8,
    0.55,
    boxstyle='round,pad=0.08,rounding_size=0.15',
    facecolor=orange_bg,
    edgecolor='none',
)
ax.add_patch(rect_right)
ax.text(
    7.4,
    5.675,
    '次の時刻での状態',
    color='white',
    fontsize=11,
    fontweight='bold',
    ha='center',
    va='center',
)
ax.text(
    9.0,
    5.675,
    r'$\boldsymbol{y}_n$',
    color='#222222',
    fontsize=15,
    fontweight='bold',
    ha='center',
    va='center',
)

# 上段矢印：Δt_obs の時間発展
ax.annotate(
    '',
    xy=(8.8, 6.15),
    xytext=(3.6, 6.15),
    arrowprops=dict(
        arrowstyle='-|>', color=blue_arrow, lw=2, mutation_scale=15
    ),
)
ax.text(
    6.2,
    6.35,
    r'$\Delta t_{\mathrm{obs}}$ の時間発展',
    color='#222222',
    fontsize=11,
    ha='center',
    va='bottom',
)


# --- 2. 縦の矢印：観測 ---

# 左下への観測矢印
ax.annotate(
    '',
    xy=(3.5, 4.2),
    xytext=(3.5, 5.3),
    arrowprops=dict(
        arrowstyle='-|>',
        color=gray_dashed,
        lw=1.5,
        ls='--',
        mutation_scale=12,
    ),
)
ax.text(
    3.3, 4.75, '観測', color='#444444', fontsize=10, ha='right', va='center'
)

# 右下への観測矢印
ax.annotate(
    '',
    xy=(9.0, 4.2),
    xytext=(9.0, 5.3),
    arrowprops=dict(
        arrowstyle='-|>',
        color=gray_dashed,
        lw=1.5,
        ls='--',
        mutation_scale=12,
    ),
)
ax.text(
    8.8, 4.75, '観測', color='#444444', fontsize=10, ha='right', va='center'
)


# --- 3. 下段：観測量 φ(x_n) と φ(y_n) ---

# 左下観測量
ax.text(
    0.5,
    3.8,
    'とある観測量の値',
    color='#333333',
    fontsize=11,
    ha='left',
    va='center',
)
ax.text(
    3.5,
    3.8,
    r'$\phi(\boldsymbol{x}_n)$',
    color='#222222',
    fontsize=14,
    fontweight='bold',
    ha='center',
    va='center',
)
ax.text(
    0.5,
    3.2,
    r'※ $\phi(\boldsymbol{x}) = x_1$ ならば一つ目の座標を観測',
    color='#666666',
    fontsize=9.5,
    ha='left',
    va='center',
)

# 右下観測量
ax.text(
    6.1,
    3.8,
    '時間発展後の観測量の値',
    color='#333333',
    fontsize=11,
    ha='left',
    va='center',
)
ax.text(
    9.0,
    3.8,
    r'$\phi(\boldsymbol{y}_n)$',
    color='#222222',
    fontsize=14,
    fontweight='bold',
    ha='center',
    va='center',
)


# --- 4. クープマン作用素（赤色のマッピングと説明） ---

# [目的] (K φ)(x_n) のラベル
ax.text(
    4.4,
    4.9,
    '[目的]',
    color=red_accent,
    fontsize=11,
    fontweight='bold',
    ha='right',
    va='center',
)
ax.text(
    4.5,
    4.9,
    r'$(\mathcal{K}\phi)(\boldsymbol{x}_n)$',
    color=red_accent,
    fontsize=13,
    fontweight='bold',
    ha='left',
    va='center',
)

# 赤色曲線矢印（x_n から φ(y_n) へ）
ax.annotate(
    '',
    xy=(8.7, 3.5),
    xytext=(3.7, 5.4),
    arrowprops=dict(
        arrowstyle='-|>',
        color=red_accent,
        lw=1.8,
        ls=':',
        connectionstyle='arc3,rad=-0.25',
        mutation_scale=15,
    ),
)

# 赤色注釈テキストと指示矢印
ax.annotate(
    '前の状態を入力すると「これ」を出力する関数',
    xy=(8.2, 3.65),
    xytext=(4.2, 2.3),
    color=red_accent,
    fontsize=10.5,
    fontweight='bold',
    arrowprops=dict(arrowstyle='->', color=red_accent, lw=1.5, ls=':'),
    ha='left',
    va='center',
)


# --- 5. キャプション（図タイトル） ---

ax.text(
    5.0,
    1.0,
    '図 26.1　問題設定のおさらい',
    color='#111111',
    fontsize=13,
    fontweight='bold',
    ha='center',
    va='center',
)

plt.tight_layout()
plt.savefig('diagram_26_1.png', bbox_inches='tight', dpi=200)
plt.show()