import numpy as np
import matplotlib.pyplot as plt

CH = np.array([330,214,54,15])#全能峰,康普顿边缘,反散射峰,X射线峰
E = np.array([0.662,0.478,0.184,0.032])

x = CH
y = E

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
x_line = np.linspace(min(x-40), max(x+40), 100)
y_line = slope * x_line + intercept
plt.plot(x_line, y_line, color='blue', linewidth=2,
         label=f'$CH$= {slope:.4f}E  +{intercept:.4f}\nR² = {r_squared:.4f}')

# 使用数学符号设置坐标轴标签
plt.xlabel(r'$CH$', fontsize=16)
plt.ylabel(r'$E$', fontsize=16)
plt.title(r'$E$ = $kE+b$ ', fontsize=18)

plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(fontsize=12, loc='best')
plt.tight_layout()
plt.savefig('2.pdf', bbox_inches='tight', dpi=300)
plt.show()
