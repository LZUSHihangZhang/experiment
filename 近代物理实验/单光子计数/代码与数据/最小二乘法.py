import numpy as np
import matplotlib.pyplot as plt

# Data: W = optical power, N = average count rate
# Temperatures: 10°C, 0°C, -10°C
W_10C = np.array([0.85, 0.9, 0.95, 1.00, 1.05])
W_0C = np.array([0.85, 0.9, 0.95, 1.01, 1.05, 1.10])
W_n10C = np.array([0.85, 0.9, 0.95, 1.00, 1.05])

N_10C = np.array([47318, 50385, 53181, 56407, 59602])
N_0C = np.array([46989, 50070, 53474, 56912, 59812, 62478])
N_n10C = np.array([47303, 50533, 54397, 56600, 59484])

# Subtract background (dark counts - these are already low)
# The small subtraction (10-11) suggests dark counts are negligible
n_10C = N_10C - 11
n_0C = N_0C - 10
n_n10C = N_n10C - 10

W = [W_10C,W_0C,W_n10C]
N = [n_10C,n_0C,n_n10C]

for i in range(3):
    x = W[i]
    y = N[i]

    # 计算线性回归
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean) ** 2)

    slope = numerator / denominator
    intercept = y_mean - slope * x_mean

    # 计算R²值
    y_pred = slope * x + intercept
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - y_mean) ** 2)
    r_squared = 1 - (ss_res / ss_tot)

    print("斜率:", slope)
    print("截距:", intercept)
    print("R²值:", r_squared)
    print(intercept/slope)
    # 绘图
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'ro')

    # 生成更平滑的拟合线
    x_line = np.linspace(min(x - 0.02), max(x + 0.02), 100)
    y_line = slope * x_line + intercept
    plt.plot(x_line, y_line, color='blue', linewidth=2,
             label=f'$N$= {slope:.4f}P  {intercept:.4f}\nP = {r_squared:.4f}')

    # 使用数学符号设置坐标轴标签
    plt.xlabel(r'$P/(\mu\mathrm{W})$', fontsize=16)
    plt.ylabel(r'$n$', fontsize=16)
    plt.title(r'$n$ = $kP+b$ ', fontsize=18)

    plt.grid(True, alpha=0.3, linestyle='--')
    plt.legend(fontsize=12, loc='best')
    plt.tight_layout()
    plt.savefig(f'{i+6}.pdf', bbox_inches='tight', dpi=300)
    plt.show()