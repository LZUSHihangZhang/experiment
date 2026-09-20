import numpy as np
import numpy as np
import matplotlib.pyplot as plt

L = np.array([0.310,0.375,0.447,0.492,0.554,0.609])
U = np.array([0.25,0.54,0.96,1.23,1.65,2.07])

x = L
y = U


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
x_line = np.linspace(min(x-0.001), max(x+0.001), 100)
y_line = slope * x_line + intercept
plt.plot(x_line, y_line, color='blue', linewidth=2,
         label=f'U= {slope:.5f}L  {intercept:.4f}\nR² = {r_squared:.4f}')
# 使用数学符号设置坐标轴标签
plt.xlabel(r'$L(mm)$', fontsize=16)
plt.ylabel(f'$U(V)$', fontsize=16)
plt.title(r'$U(V)$ = $kL(mm)+b$', fontsize=18)

plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(fontsize=12, loc='best')
plt.tight_layout()
plt.savefig('3.pdf',bbox_inches='tight', dpi=300)
plt.show()
