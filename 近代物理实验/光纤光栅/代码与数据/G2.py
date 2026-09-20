import numpy as np
import matplotlib.pyplot as plt

# 数据
m = [0, 50, 100, 150, 200, 250]
lam1 = [1550.06, 1550.59, 1551.13, 1551.76, 1552.36, 1552.97]
lam2 = [1550.23, 1550.82, 1551.36, 1552.05, 1552.60, 1552.97]

x = np.array(m)
y1 = np.array(lam1)
y2 = np.array(lam2)

# 对第一组数据做线性回归
x_mean1 = np.mean(x)
y_mean1 = np.mean(y1)

numerator1 = np.sum((x - x_mean1) * (y1 - y_mean1))
denominator1 = np.sum((x - x_mean1)**2)

slope1 = numerator1 / denominator1
intercept1 = y_mean1 - slope1 * x_mean1

y_pred1 = slope1 * x + intercept1
ss_res1 = np.sum((y1 - y_pred1)**2)
ss_tot1 = np.sum((y1 - y_mean1)**2)
r_squared1 = 1 - (ss_res1 / ss_tot1)

# 对第二组数据做线性回归
x_mean2 = np.mean(x)
y_mean2 = np.mean(y2)

numerator2 = np.sum((x - x_mean2) * (y2 - y_mean2))
denominator2 = np.sum((x - x_mean2)**2)

slope2 = numerator2 / denominator2
intercept2 = y_mean2 - slope2 * x_mean2

y_pred2 = slope2 * x + intercept2
ss_res2 = np.sum((y2 - y_pred2)**2)
ss_tot2 = np.sum((y2 - y_mean2)**2)
r_squared2 = 1 - (ss_res2 / ss_tot2)

# 输出结果
print("第一组数据 (lam1):")
print(f"  斜率: {slope1:.6f} nm/g")
print(f"  截距: {intercept1:.4f} nm")
print(f"  R²值: {r_squared1:.6f}")
print(f"  拟合方程: λ₁ = {slope1:.6f}m + {intercept1:.4f}")
print()
print("第二组数据 (lam2):")
print(f"  斜率: {slope2:.6f} nm/g")
print(f"  截距: {intercept2:.4f} nm")
print(f"  R²值: {r_squared2:.6f}")
print(f"  拟合方程: λ₂ = {slope2:.6f}m + {intercept2:.4f}")

# 创建包含两个子图的图形
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# 第一个子图：lam1
ax1.plot(x, y1, 'ro', markersize=8)
x_line1 = np.linspace(min(x) - 10, max(x) + 10, 100)
y_line1 = slope1 * x_line1 + intercept1
ax1.plot(x_line1, y_line1, 'b-', linewidth=2,
         label=f'λ₁ = {slope1:.4f}m + {intercept1:.2f}\nR² = {r_squared1:.4f}')

ax1.set_xlabel(r'$m$ / g', fontsize=16)
ax1.set_ylabel(r'$\lambda$ / nm', fontsize=16)
ax1.grid(True, alpha=0.3, linestyle='--')
ax1.legend(fontsize=12, loc='best')

# 第二个子图：lam2
ax2.plot(x, y2, 'rs', markersize=8)
x_line2 = np.linspace(min(x) - 10, max(x) + 10, 100)
y_line2 = slope2 * x_line2 + intercept2
ax2.plot(x_line2, y_line2, 'g-', linewidth=2,
         label=f'λ₂ = {slope2:.4f}m + {intercept2:.2f}\nR² = {r_squared2:.4f}')

ax2.set_xlabel(r'$m$ / g', fontsize=16)
ax2.set_ylabel(r'$\lambda$ / nm', fontsize=16)

ax2.grid(True, alpha=0.3, linestyle='--')
ax2.legend(fontsize=12, loc='best')

# 调整布局并保存
plt.tight_layout()
plt.savefig('combined_fit.pdf', bbox_inches='tight', dpi=300)
plt.show()

# 也可以选择将两组数据画在同一张图上对比
fig2, ax = plt.subplots(figsize=(10, 6))

# 第一组数据
ax.plot(x, y1, 'ro', markersize=8)
ax.plot(x_line1, y_line1, 'r-', linewidth=2, alpha=0.7,
        label=f'λ₁ = {slope1:.4f}m + {intercept1:.2f} (R²={r_squared1:.4f})')

# 第二组数据
ax.plot(x, y2, 'bs', markersize=8)
ax.plot(x_line2, y_line2, 'b-', linewidth=2, alpha=0.7,
        label=f'λ₂ = {slope2:.4f}m + {intercept2:.2f} (R²={r_squared2:.4f})')

ax.set_xlabel(r'$m$ / g', fontsize=16)
ax.set_ylabel(r'$\lambda$ / nm', fontsize=16)
ax.grid(True, alpha=0.3, linestyle='--')
ax.legend(fontsize=12, loc='best')
plt.tight_layout()
plt.savefig('overlay_fit.pdf', bbox_inches='tight', dpi=300)
plt.show()