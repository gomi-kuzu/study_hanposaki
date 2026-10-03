import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Ellipse, FancyArrowPatch

# Set Japanese font
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK JP', 'Noto Sans JP', 'IPAGothic', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 1. Simulate Van der Pol oscillator
epsilon = 1.0

def van_der_pol(t, y):
    x1, x2 = y
    return [x2, epsilon * x2 * (1 - x1**2) - x1]

t_span = (0, 3.0)
t_eval = np.arange(0, 3.0, 0.1) # dt_obs = 0.1, 30 points
sol = solve_ivp(van_der_pol, t_span, [0.2, 0.9], t_eval=t_eval, rtol=1e-9, atol=1e-9)

t_pts = sol.t
x1_pts = sol.y[0]
x2_pts = sol.y[1]

# High-resolution trajectory for smooth curve
t_fine = np.linspace(0, 2.9, 300)
sol_dense = solve_ivp(van_der_pol, (0, 2.9), [0.2, 0.9], t_eval=t_fine, rtol=1e-9, atol=1e-9)
x1_fine = sol_dense.y[0]
x2_fine = sol_dense.y[1]

# Color palette matching original diagram
x1_color = '#1f77b4' # Blue
x2_color = '#d9531e' # Orange-Red
green_color = '#2e7d32' # Dark Green

fig = plt.figure(figsize=(11, 5.2), dpi=150, facecolor='white')

# Subplot placement
ax1 = fig.add_axes([0.08, 0.18, 0.38, 0.62])
ax2 = fig.add_axes([0.58, 0.18, 0.38, 0.62])

# --- Panel 1: Time Series ---
ax1.plot(t_fine, x1_fine, color=x1_color, linewidth=1.5, zorder=2)
ax1.plot(t_fine, x2_fine, color=x2_color, linewidth=1.5, zorder=2)

ax1.scatter(t_pts, x1_pts, color=x1_color, s=22, zorder=3)
ax1.scatter(t_pts, x2_pts, color=x2_color, s=22, zorder=3)

# Curve labels
ax1.text(2.0, 1.0, r'$x_1$', color='#555555', fontsize=12, style='italic')
ax1.text(0.8, 0.5, r'$x_2$', color='#555555', fontsize=12, style='italic')

# Axis limits and ticks
ax1.set_xlim(-0.1, 3.1)
ax1.set_ylim(-1.8, 1.4)
ax1.set_xticks([0, 1, 2, 3])
ax1.set_yticks([-1.5, -1.0, -0.5, 0.0, 0.5, 1.0])
ax1.set_xlabel('$t$', fontsize=11)

# Vertical dotted line at t=0
ax1.plot([0, 0], [-0.5, 0.9], color='gray', linestyle=':', linewidth=1.2)

# Green dotted vertical lines at t=2.5 and t=2.6
idx_25 = 25 # t=2.5
idx_26 = 26 # t=2.6
ax1.plot([t_pts[idx_25], t_pts[idx_25]], [x2_pts[idx_25], x1_pts[idx_25]], color=green_color, linestyle=':', linewidth=1.5)
ax1.plot([t_pts[idx_26], t_pts[idx_26]], [x2_pts[idx_26], x1_pts[idx_26]], color=green_color, linestyle=':', linewidth=1.5)

# Text annotation for discrete data collection
ax1.text(0.15, -1.25, '連続的な時間発展から\n離散的にデータを取得', fontsize=9.5, color='#333333', va='top')

# Badge [1]
badge1 = FancyBboxPatch((0.11, 0.83), 0.32, 0.07, transform=fig.transFigure,
                        boxstyle="round,pad=0.02,rounding_size=0.03",
                        facecolor='#d5e8d4', edgecolor='none', zorder=10)
fig.patches.append(badge1)
fig.text(0.27, 0.865, '〔1〕　時間経過をプロット', transform=fig.transFigure,
         ha='center', va='center', fontsize=11, fontweight='bold', color='#274e13', zorder=11)


# --- Panel 2: Phase Space ---
ax2.plot(x1_fine, x2_fine, color='black', linewidth=1.2, zorder=2)
ax2.scatter(x1_pts, x2_pts, color='black', s=20, zorder=3)

# Initial point (red)
ax2.scatter([x1_pts[0]], [x2_pts[0]], color='red', s=40, zorder=5)

# Snapshot pair ellipse (green dotted)
pair_x1 = (x1_pts[idx_25] + x1_pts[idx_26]) / 2
pair_x2 = (x2_pts[idx_25] + x2_pts[idx_26]) / 2
ellipse = Ellipse((pair_x1, pair_x2), width=0.28, height=0.38, angle=-30,
                  edgecolor='#82b366', facecolor='#d5e8d4', alpha=0.5, linestyle='--', linewidth=1.5, zorder=3)
ax2.add_patch(ellipse)

# Highlight the two points inside ellipse
ax2.scatter([x1_pts[idx_25], x1_pts[idx_26]], [x2_pts[idx_25], x2_pts[idx_26]], color='#2e7d32', s=28, zorder=4)

# Axis limits and ticks
ax2.set_xlim(-0.1, 1.3)
ax2.set_ylim(-1.8, 1.4)
ax2.set_xticks([0.0, 0.4, 0.8, 1.2])
ax2.set_yticks([-1.5, -1.0, -0.5, 0.0, 0.5, 1.0])
ax2.set_xlabel('$x_1$', fontsize=11)
ax2.set_ylabel('$x_2$', fontsize=11, rotation=0, labelpad=10)

# Annotations in Panel 2
ax2.text(0.12, 0.55, '最初のデータ', fontsize=9.5, color='#333333')
ax2.text(-0.08, -0.25, '離散時間発展の前後の組が\nスナップショット・ペア', fontsize=9.5, color='#333333')

# Badge [2]
badge2 = FancyBboxPatch((0.61, 0.83), 0.32, 0.07, transform=fig.transFigure,
                        boxstyle="round,pad=0.02,rounding_size=0.03",
                        facecolor='#ffe6cc', edgecolor='none', zorder=10)
fig.patches.append(badge2)
fig.text(0.77, 0.865, '〔2〕　平面座標にプロット', transform=fig.transFigure,
         ha='center', va='center', fontsize=11, fontweight='bold', color='#b85450', zorder=11)


# --- Connection Arrows between Panel 1 and Panel 2 ---
trans_fig = fig.transFigure.inverted()

# Red arrow: (t=0, x2=0.9) in Panel 1 -> (x1(0), x2(0)) in Panel 2
p1_red = trans_fig.transform(ax1.transData.transform((0, 0.9)))
p2_red = trans_fig.transform(ax2.transData.transform((x1_pts[0], x2_pts[0])))

arrow_red = FancyArrowPatch(p1_red, p2_red, transform=fig.transFigure,
                            arrowstyle='->,head_width=4,head_length=6',
                            color='red', linestyle='--', linewidth=1.5, zorder=15)
fig.patches.append(arrow_red)

# Green arrow 1: Upper point (t=2.5, x1(2.5)) in Panel 1 -> Upper point in green pair
p1_green_top = trans_fig.transform(ax1.transData.transform((t_pts[idx_25], x1_pts[idx_25])))
p2_green_top = trans_fig.transform(ax2.transData.transform((x1_pts[idx_25] + 0.02, x2_pts[idx_25] + 0.05)))

arrow_green1 = FancyArrowPatch(p1_green_top, p2_green_top, transform=fig.transFigure,
                               arrowstyle='->,head_width=4,head_length=6',
                               color=green_color, linestyle='--', linewidth=1.2, zorder=15)

# Green arrow 2: Lower point (t=2.5, x2(2.5)) in Panel 1 -> Lower point in green pair
p1_green_bot = trans_fig.transform(ax1.transData.transform((t_pts[idx_25], x2_pts[idx_25])))
p2_green_bot = trans_fig.transform(ax2.transData.transform((x1_pts[idx_26] - 0.05, x2_pts[idx_26])))

arrow_green2 = FancyArrowPatch(p1_green_bot, p2_green_bot, transform=fig.transFigure,
                               arrowstyle='->,head_width=4,head_length=6',
                               color=green_color, linestyle='--', linewidth=1.2, zorder=15)

fig.patches.append(arrow_green1)
fig.patches.append(arrow_green2)

# Figure Title at bottom
fig.text(0.5, 0.03, '図 25.1　非線形な例題の軌跡をたどる', ha='center', va='center', fontsize=12, fontweight='bold')

plt.savefig('./media/images/fig25_1_reproduced.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved ./media/images/fig25_1_reproduced.png")
