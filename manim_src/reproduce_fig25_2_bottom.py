import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from mpl_toolkits.mplot3d import Axes3D
import shutil

# 日本語フォント設定
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK JP', 'Noto Sans JP', 'IPAGothic', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# ファン・デル・ポル方程式 (\epsilon = 1.0)
epsilon = 1.0
def van_der_pol(t, y):
    x1, x2 = y
    return [x2, epsilon * x2 * (1 - x1**2) - x1]

# --- 1. シミュレーションデータ生成 ---
t_span = (0, 3.0)
t_eval = np.arange(0, 3.0, 0.1) # 離散スナップショット点
sol = solve_ivp(van_der_pol, t_span, [0.2, 0.9], t_eval=t_eval, rtol=1e-9, atol=1e-9)

x1_pts, x2_pts = sol.y[0], sol.y[1]

# --- 2. 3D曲面データの生成 ---
grid_x1 = np.linspace(-2, 2, 40)
grid_x2 = np.linspace(-2, 2, 40)
X1, X2 = np.meshgrid(grid_x1, grid_x2)

# (a) 超平面: \phi(x) = x_1
Z_flat = X1.copy()

# (b) 曲面: \phi(x, t = \Delta t_obs) (概念図として非線形性を明瞭に見せるため \Delta t = 0.8)
dt_eval = 0.8
Z_evolved = np.zeros_like(X1)

for i in range(X1.shape[0]):
    for j in range(X1.shape[1]):
        x1_0 = X1[i, j]
        x2_0 = X2[i, j]
        res = solve_ivp(van_der_pol, (0, dt_eval), [x1_0, x2_0], rtol=1e-6, atol=1e-6)
        Z_evolved[i, j] = res.y[0, -1]

# 軌跡点に対応する z 値
z_pts_flat = x1_pts.copy()
z_pts_evolved = np.zeros_like(x1_pts)
for k in range(len(x1_pts)):
    res_pt = solve_ivp(van_der_pol, (0, dt_eval), [x1_pts[k], x2_pts[k]], rtol=1e-6, atol=1e-6)
    z_pts_evolved[k] = res_pt.y[0, -1]

# --- 3. 描画設定 ---
fig = plt.figure(figsize=(13, 6.5), dpi=150, facecolor='white')

# 視角設定 (平面が潰れず、曲面の歪み・写像構造が見やすい角度)
ELEV = 28
AZIM = -35
Z_BOTTOM = -2.0 # 底面の z 位置

# --- 左側 3D プロット: \phi(x) = x_1 (超平面) ---
ax1 = fig.add_subplot(121, projection='3d')
surf1 = ax1.plot_surface(X1, X2, Z_flat, cmap='coolwarm', alpha=0.45, 
                         linewidth=0.3, edgecolor='gray', rstride=2, cstride=2)

ax1.set_title('$x_1$ を観測する関数\n$\\phi(\\boldsymbol{x}) = x_1$', fontsize=12, pad=12, fontweight='bold')
ax1.set_xlabel('$x_1$', fontsize=11)
ax1.set_ylabel('$x_2$', fontsize=11)
ax1.set_zlabel('$\\phi$', fontsize=11)
ax1.set_xlim(-2, 2)
ax1.set_ylim(-2, 2)
ax1.set_zlim(-2, 2)
ax1.view_init(elev=ELEV, azim=AZIM)

# (1) 底面上の状態軌跡 (x1-x2 平面)
ax1.plot(x1_pts, x2_pts, np.full_like(x1_pts, Z_BOTTOM), color='black', linestyle='-', linewidth=1.5, zorder=3)
ax1.scatter(x1_pts, x2_pts, np.full_like(x1_pts, Z_BOTTOM), color='black', s=15, zorder=4)

# (2) 補助線: 底面 -> 超平面 (垂直線) -> 奥壁 (水平折れ線)
for k in range(0, len(x1_pts), 3): # 見やすさのため間引き表示
    x1_val, x2_val = x1_pts[k], x2_pts[k]
    z_val = z_pts_flat[k]
    
    # 垂直上昇線
    ax1.plot([x1_val, x1_val], [x2_val, x2_val], [Z_BOTTOM, z_val], 
             color='green', linestyle='--', linewidth=1.2, zorder=5)
    # 超平面上の点
    ax1.scatter([x1_val], [x2_val], [z_val], color='darkgreen', s=18, zorder=6)
    # 水平奥送り線
    ax1.plot([x1_val, x1_val], [x2_val, 2.0], [z_val, z_val], 
             color='#2e7d32', linestyle=':', linewidth=1.0, zorder=5)

# 観測断面を示すハイライト線 (x2=0 での x1 軸方向直線)
x1_line = np.linspace(-2, 2, 50)
x2_zero = np.zeros_like(x1_line)
ax1.plot(x1_line, x2_zero, x1_line, color='red', linewidth=2.0, zorder=7)


# --- 右側 3D プロット: \phi(x, t = \Delta t_obs) (曲面) ---
ax2 = fig.add_subplot(122, projection='3d')
surf2 = ax2.plot_surface(X1, X2, Z_evolved, cmap='coolwarm', alpha=0.45, 
                         linewidth=0.3, edgecolor='gray', rstride=2, cstride=2)

ax2.set_title('時間発展後の観測関数\n$\\phi(\\boldsymbol{x}, t = \\Delta t_{\\mathrm{obs}})$', fontsize=12, pad=12, fontweight='bold')
ax2.set_xlabel('$x_1$', fontsize=11)
ax2.set_ylabel('$x_2$', fontsize=11)
ax2.set_zlabel('$\\phi$', fontsize=11)
ax2.set_xlim(-2, 2)
ax2.set_ylim(-2, 2)
ax2.set_zlim(-2, 2)
ax2.view_init(elev=ELEV, azim=AZIM)

# (1) 底面上の状態軌跡 (x1-x2 平面)
ax2.plot(x1_pts, x2_pts, np.full_like(x1_pts, Z_BOTTOM), color='black', linestyle='-', linewidth=1.5, zorder=3)
ax2.scatter(x1_pts, x2_pts, np.full_like(x1_pts, Z_BOTTOM), color='black', s=15, zorder=4)

# (2) 補助線: 底面 -> 曲面 (垂直線) -> 奥壁 (水平折れ線)
for k in range(0, len(x1_pts), 3):
    x1_val, x2_val = x1_pts[k], x2_pts[k]
    z_val = z_pts_evolved[k]
    
    # 垂直上昇線
    ax2.plot([x1_val, x1_val], [x2_val, x2_val], [Z_BOTTOM, z_val], 
             color='green', linestyle='--', linewidth=1.2, zorder=5)
    # 曲面上の点
    ax2.scatter([x1_val], [x2_val], [z_val], color='darkgreen', s=18, zorder=6)
    # 水平奥送り線
    ax2.plot([x1_val, x1_val], [x2_val, 2.0], [z_val, z_val], 
             color='#2e7d32', linestyle=':', linewidth=1.0, zorder=5)

plt.tight_layout()
plt.savefig('./media/images/fig25_2_bottom_only.png', dpi=150, bbox_inches='tight')
plt.close()

print("Successfully generated ./media/images/fig25_2_bottom_only.png and reproduce_fig25_2_bottom.py")
