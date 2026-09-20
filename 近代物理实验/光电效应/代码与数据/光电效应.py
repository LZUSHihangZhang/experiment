import numpy as np
import matplotlib.pyplot as plt

L = np.array([400,425,450,475,500,525,550])*1e-9
c = 299792458
v = c/L
U = np.array([-1.898,-1.828,-1.588,-1.424,-1.268,-1.132,-1.0140])
U1 = np.array([-1.78,-1.56,-1.32,-1.222,-1.084,-0.972,-0.878])
x = v
y = U1


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
         label=f'U= {slope:.19f}  v  +  {intercept:.4f}\nR² = {r_squared:.4f}')

# 使用数学符号设置坐标轴标签
plt.xlabel(r'$\nu(Hz)$', fontsize=16)
plt.ylabel(f'$U(V)$', fontsize=16)
plt.title(r'$U$ = $\frac{h}{c}\nu-\frac{h}{c}\nu_0$', fontsize=18)

plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(fontsize=12, loc='best')
plt.tight_layout()
plt.savefig('.pdf',bbox_inches='tight', dpi=300)
plt.show()
