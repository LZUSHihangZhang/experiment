import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import find_peaks

# 读取数据
df = pd.read_excel('XRD.xlsx')
theta = df.iloc[:, 0]
amplitude = np.array(df.iloc[:, 1])

# 找峰：可以调整height和distance参数来控制峰的敏感度
peaks, properties = find_peaks(amplitude, height=30, distance=20)  # 根据数据调整height和distance

# 获取峰的位置和高度
peak_theta = np.array(theta.iloc[peaks])
peak_amplitude = np.array(amplitude[peaks])

# 绘图
plt.plot(theta, amplitude, 'b-', label='absorption X-ray spectrum')
plt.plot(peak_theta, peak_amplitude, 'ro', label='Detected peaks')  # 标记峰
plt.xlabel(r'$2\theta$')
plt.ylabel(r'$A$')
plt.grid(True)
plt.legend(loc='best', fontsize=10)

# 可选：在图上标注每个峰的坐标
for x, y in zip(peak_theta, peak_amplitude):
    plt.text(x, y, f'({x:.1f}, {y:.0f})', fontsize=8, verticalalignment='bottom')

# 调整布局
plt.tight_layout()

# 保存图形
plt.savefig('XRD_with_peaks.pdf', format='pdf', dpi=150, bbox_inches='tight')
plt.show()



# 您的实验数据
two_theta_exp = peak_theta

intensity_exp = peak_amplitude

hkl_theory = ['100', '002', '101', '102', '110', '103', '200',
              '112', '201', '004', '202', '104', '203', '210',
              '211', '114', '105', '212', '300', '213', '205']

two_theta_theory = np.array([31.77, 34.42, 36.25, 47.54, 56.60, 62.86, 66.38,
                             67.96, 69.10, 72.56, 76.95, 81.37, 89.60, 92.80,
                             95.20, 98.60, 103.00, 104.10, 107.50, 110.40, 116.20])

print("=" * 80)
print("                     ZnO XRD谱图中吸收峰检查")
print("=" * 80)

# 检查每个峰的匹配情况
print("\n详细峰位匹配分析:")
print("序号 | 2θ实验(°) | 2θ理论(°) | Δ2θ(°) | hkl  | 强度  | 误差")
print("-" * 85)

unmatched_peaks = []
tolerance = 0.25  # 允许偏差范围（度）

for i, exp_2theta in enumerate(two_theta_exp):
    # 寻找最接近的理论峰
    min_diff = float('inf')
    closest_idx = -1

    for j, theo_2theta in enumerate(two_theta_theory):
        diff = abs(exp_2theta - theo_2theta)
        if diff < min_diff:
            min_diff = diff
            closest_idx = j

    if min_diff <= tolerance:
        status = "✓ 匹配"
        hkl = hkl_theory[closest_idx]
    else:
        status = "⚠ 未匹配"
        hkl = "???"
        unmatched_peaks.append((i, exp_2theta, intensity_exp[i]))

    print(f"{i + 1:3d} | {exp_2theta:8.2f} | {two_theta_theory[closest_idx] if closest_idx >= 0 else 'N/A':8.2f} | "
          f"{exp_2theta - two_theta_theory[closest_idx] if closest_idx >= 0 else 'N/A':7.2f} | {hkl:4s} | "
          f"{intensity_exp[i]:6.0f}|{((two_theta_exp[i])-(two_theta_theory[i])):6f}")


print(((two_theta_exp)-(two_theta_theory)))