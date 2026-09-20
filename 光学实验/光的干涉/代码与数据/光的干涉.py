import numpy as np
import matplotlib.pyplot as plt

x = np.array([1.5,11.5,21.5,31.5,41.5])
y = np.array([114.5,134.0,155.5,175.5,195.1])

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
x_line = np.linspace(min(x-0.0001), max(x+0.0001), 100)
y_line = slope * x_line + intercept
plt.plot(x_line, y_line, color='blue', linewidth=2,
         label=f'$y$= {slope:.4f}x+  {intercept:.4f}\nR² = {r_squared:.4f}')
# 调整图例框大小
legend = plt.legend(fontsize=20, handlelength=1, handleheight=1)
frame = legend.get_frame()
frame.set_facecolor('white')  # 背景色
frame.set_alpha(0.8)  # 透明度
# 使用数学符号设置坐标轴标签
plt.xlabel(r'$\theta_{\frac{\lambda}{2}}$', fontsize=20)
plt.ylabel(r'$\varphi_{P}$', fontsize=20)
plt.title(fr'$\varphi_P = {slope}\times\theta_{{\frac{{\lambda}}{{2}}}}+{intercept}$', fontsize=18)
plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(fontsize=12, loc='best')
plt.tight_layout()
plt.show()