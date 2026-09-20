import numpy as np
import matplotlib.pyplot as plt

# 设置高清输出参数
plt.rcParams['figure.dpi'] = 300  # 设置分辨率
plt.rcParams['savefig.dpi'] = 300  # 保存图片的分辨率

# 设置中文字体和数学符号
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.rcParams['mathtext.fontset'] = 'stix'  # 设置数学字体

# 数据
x1 = np.array([32.731,32.390,32.021,31.622,31.179,30.698,30.149,29.609])
x2 = np.array([20.750,21.085,21.480,21.856,22.288,22.765,23.285,23.931])
y1 = x1 - x2
y2 = y1**2
k = np.array([45,40,35,30,25,20,15,10])

x = k
y = y2

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
         label=f'$r^2$= {slope:.4f}k  {intercept:.4f}\nR² = {r_squared:.4f}')

# 使用数学符号设置坐标轴标签
plt.xlabel(r'$kR\lambda$', fontsize=16)
plt.ylabel(r'$r^2$', fontsize=16)
plt.title(r'$r^2$ = $kR\lambda-2R\delta_0$ ', fontsize=18)

plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(fontsize=12, loc='best')
plt.tight_layout()
plt.show()

# 输出详细信息
print(f"\n回归方程: r² = {slope:.4f} × (kRλ)  {intercept:.4f}")
print( np.round(y1[::-1], 2))
print( np.round(y2[::-1], 2))

p = 0
for i in range(4):
    q = (y2[i+4]-y2[i])/(589.3*1e-9)/80*1e-6
    print(q)
    p = p + q

print(p/4)
print(slope/(4*589.3*1e-3))

print(sum(y2))

print((5.7735e-6)*(np.sqrt(np.sum(y2)))*1e-3/160/(589.3*1e-9))