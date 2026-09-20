import matplotlib.pyplot as plt
import numpy as np

y = np.array([3.9734,3.5258,3.0687,2.8640,1.7455])
x = np.array([7.4712,6.6906,5.8873,5.4636,3.3317])*1e7
delta = y/x
print(np.sqrt(np.sum((delta-np.mean(delta))**2)/(5*4)))
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
x_line = np.linspace(min(x-1), max(x+1), 100)
y_line = slope * x_line + intercept
plt.plot(x_line, y_line, color='blue', linewidth=2,
         label=f'$E$= {slope:.4f}' r'$T^4$' f'  {intercept:.4f}\nR² = {r_squared:.4f}')

# 使用数学符号设置坐标轴标签
plt.xlabel(r'$T^4(K)$', fontsize=16)
plt.ylabel(r'$E$', fontsize=16)
plt.title(r'$E$ = $\delta T^4$+bias ', fontsize=18)

plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(fontsize=12, loc='best')
plt.tight_layout()
plt.savefig('Wen.pdf', bbox_inches='tight', dpi=300)
plt.show()