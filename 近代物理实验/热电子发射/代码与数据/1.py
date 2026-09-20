import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([14,14,14,14,15,15,15])
x2 = np.array([39,40,41,41,42,44,44])
x3 = np.array([100,102,103,105,107,111,113])
x4 = np.array([238,241,243,244,251,259,263])
x5 = np.array([514,521,535,544,550,584,592])
x6 = np.array([1069,1090,1105,1123,1132,1161,1178])
Ua = np.array([25,36,49,64,81,121,144])


If = np.array([0.58,0.62,0.66,0.70,0.74,0.78])
temperatures = np.array([1960,2030,2100,2170,2240,2310])

# 数据列表
x_data = [x1, x2, x3, x4, x5, x6]
colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown']

# 创建图形
plt.figure(figsize=(12, 8))
Intercept = []
# 对每组数据进行处理
for i in range(6):
    x = np.sqrt(Ua)
    y = np.log10(x_data[i])

    # 计算线性回归
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean) ** 2)
    slope = numerator / denominator
    intercept = y_mean - slope * x_mean
    Intercept.append(intercept)
    # 计算R²值
    y_pred = slope * x + intercept
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - y_mean) ** 2)
    r_squared = 1 - (ss_res / ss_tot)

    # 生成拟合线
    x_line = np.linspace(min(x) - 0.1, max(x) + 0.1, 100)
    y_line = slope * x_line + intercept

    # 绘制拟合线和数据点
    plt.plot(x_line, y_line, color=colors[i], linewidth=2,
             label=f'$lgI_a$= {slope:.4f}$\\sqrt{{U_a}}$+ {intercept:.4f}\n$R^2$= {r_squared:.4f}, T={temperatures[i]}K')
    plt.scatter(x, y, color=colors[i], alpha=0.6, s=50)

# 使用数学符号设置坐标轴标签
plt.xlabel(r'$\sqrt{U_a}$', fontsize=20)
plt.ylabel(r'$lgI_a$', fontsize=20)
plt.title(r'$lgI_a=lgI + \frac{0.439}{2.3T}\frac{\sqrt{U_a}}{\sqrt{r_1\ln{\frac{r_2}{r_1}}}}$', fontsize=18)
# 调整图例框大小
legend = plt.legend(fontsize=20, handlelength=1, handleheight=1)
frame = legend.get_frame()
frame.set_facecolor('white')  # 背景色
frame.set_alpha(0.8)  # 透明度
plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(fontsize=9, loc='best')
plt.tight_layout()
plt.show()


lgT2 = np.log10(1/temperatures**2)
a = Intercept-lgT2
x = 1/temperatures
y = a


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
plt.xlabel(r'$\frac{1}{T}$', fontsize=20)
plt.ylabel(r'$lg\frac{I}{T^2}$', fontsize=20)
plt.title(r'$lg\frac{I}{T^2} = lgAS - 5.03\times10^3\phi\frac{1}{T}$ ', fontsize=18)

plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(fontsize=12, loc='best')
plt.tight_layout()
plt.show()