import numpy as np
import matplotlib.pyplot as plt

type = float
d1 = np.array([0,9.54,9.44,9.36,9.50,9.46],dtype=type)
d2 = np.array([0,1.68,1.78,1.86,1.62,1.76],dtype=type)
d3 = np.array([0,2.48,2.455,2.495,2.495,2.495],dtype=type)
D1 = np.array([0],dtype=type)
D2 = np.array([0],dtype=type)
D3 = np.array([0],dtype=type)

for i in range(1,6):
    D1 = np.append(D1,D1[i-1]+d1[i])
    D2 = np.append(D2,D2[i-1]+d2[i])
    D3 = np.append(D3,D3[i-1]+d3[i])


n1 = np.array([167,127,116,105,86,78],dtype=type)
n2 = np.array([167,145,117,101,94,65],dtype=type)
n3 = np.array([167,131,119,110,96,80],dtype=type)

x = D1
y = np.log(n1/100)

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
         label=f'$lnI$= {slope:.4f}d+  {intercept:.4f}\nR² = {r_squared:.4f}')

# 使用数学符号设置坐标轴标签
plt.xlabel(r'$d/mm$', fontsize=16)
plt.ylabel(r'$lnI$', fontsize=16)
plt.title(r'$lnI$ = $lnI_0-\mu_md$ (Al)', fontsize=18)

plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(fontsize=12, loc='best')
plt.tight_layout()
plt.show()

print(np.log(n3/100))