import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

# 设置中文字体为 WenQuanYi Zen Hei（你的系统中存在）
plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

I = np.arange(1.8, 2.21, 0.01)
P1 = np.array([0.212,0.212,0.212,0.211,0.211,0.211,0.210,0.210,0.210,0.209,0.209,0.208,
              0.206,0.201,0.198,0.190,0.173,0.148,0.144,0.148,0.175,0.194,
              0.200,0.204,0.206,0.208,0.209,0.210,0.211,0.211,0.213,0.213,0.213,
              0.214,0.214,0.214,0.216,0.216,0.216,0.215,0.215]) / 0.218 * 100

P2 = np.array([0.214,0.213,0.213,0.212,0.211,0.211,0.209,0.209,0.208,
               0.207,0.203,0.200,0.193,0.180,0.156,0.144,0.144,
               0.164,0.184,0.196,0.201,0.203,0.205,0.206,0.206,0.208,
               0.209,0.209,0.210,0.211,0.211,0.211,0.211,0.212,0.212,
               0.212,0.212,0.213,0.214,0.214,0.214])/0.218*100
P3 = np.array([0.210,0.210,0.210,0.210,0.210,0.209,0.209,0.209,0.208,0.208,
               0.207,0.205,0.202,0.198,0.191,0.175,0.150,0.142,0.141,0.163,
               0.181,0.191,0.196,0.199,0.201,0.202,0.203,0.204,0.205,0.205,0.207,
               0.207,0.208,0.208,0.208,0.209,0.210,0.210,0.209,0.209,0.208])/0.218*100

P = P3
B = 0.1898 * I + 0.0079

B_dense = np.linspace(B.min(), B.max(), 300)

# 平滑样条拟合（保持您选择的 best_s = 2.5）
best_s =1.8
spline = UnivariateSpline(B, P, s=best_s, k=3)
P_smooth = spline(B_dense)

# 固定高度
fixed_height1 = 0.1715 / 0.218 * 100
fixed_height2 = 0.1722 / 0.218 * 100
fixed_height3 = 0.1687 / 0.218 * 100
fixed_height    = fixed_height3
print(f"Fixed height = {fixed_height:.3f}")

def find_intersections(x, y, y0):
    intersections = []
    for i in range(len(x)-1):
        if (y[i] - y0) * (y[i+1] - y0) <= 0:
            x1, x2 = x[i], x[i+1]
            y1, y2 = y[i], y[i+1]
            if y2 != y1:
                x_cross = x1 + (y0 - y1) * (x2 - x1) / (y2 - y1)
                intersections.append(x_cross)
    return intersections

crossings = find_intersections(B_dense, P_smooth, fixed_height)

if len(crossings) >= 2:
    left = crossings[0]
    right = crossings[-1]
    width = right - left
    print(f"Left B = {left:.5f}")
    print(f"Right B = {right:.5f}")
    print(f"Width (ΔB) = {width:.5f}")
else:
    print("Not enough intersections found.")
    left, right, width = None, None, None

# 绘图
plt.figure(figsize=(8,5))
plt.plot(B, P, 'o', label='Raw data')
plt.plot(B_dense, P_smooth, '-', label=f'Smoothing spline (s={best_s})')
plt.axhline(y=fixed_height, color='r', linestyle='--', label=f'Fixed height = {fixed_height:.2f}')
if left is not None and right is not None:
    plt.axvline(x=left, color='g', linestyle=':', label='Left intersection')
    plt.axvline(x=right, color='g', linestyle=':', label='Right intersection')
    plt.hlines(y=fixed_height, xmin=left, xmax=right, colors='orange', linewidth=3, label=f'Width = {width:.4f}')
plt.xlabel('B/T')
plt.ylabel('P/%')
plt.title('磁共振吸收曲线3')   # 中文标题，现在会正常显示
plt.legend()
plt.savefig('3.pdf')
plt.show()