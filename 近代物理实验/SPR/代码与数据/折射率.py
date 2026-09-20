import numpy as np
import matplotlib.pyplot as plt

x = np.array([1.3336,1.3401,1.3476,1.3564,1.3646,1.3721])
y = np.array([0,5,10,15,20,25])

# 计算线性回归
x_mean = np.mean(x)
y_mean = np.mean(y)

numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean)**2)

slope = numerator / denominator
intercept = y_mean - slope * x_mean

# 计算R²值
y_pred = slope * x + intercept
ss_res = np.sum((y - y_pred)**2)
ss_tot = np.sum((y - y_mean)**2)
r_squared = 1 - (ss_res / ss_tot)

print("斜率:", slope)
print("截距:", intercept)
print("R²值:", r_squared)

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'ro')

# 生成更平滑的拟合线
x_line = np.linspace(min(x-0.01), max(x+0.01), 100)
y_line = slope * x_line + intercept
plt.plot(x_line, y_line, color='blue', linewidth=2,
         label=f'$C$= {slope:.4f}n  {intercept:.4f}\nR² = {r_squared:.4f}')

# 使用数学符号设置坐标轴标签
plt.xlabel(r'$n $', fontsize=16)
plt.ylabel(r'$C(concentration)$', fontsize=16)
plt.title(r'$C$ = $kn+b$ ', fontsize=18)

plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(fontsize=12, loc='best')
plt.tight_layout()
plt.savefig('4.pdf', bbox_inches='tight', dpi=300)
plt.show()
print(slope*1.3661+intercept)
print(slope)
print(intercept)