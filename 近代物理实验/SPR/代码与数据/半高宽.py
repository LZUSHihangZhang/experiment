import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 读取数据
df = pd.read_excel('1.xlsx', header=0)

# 获取数据
x = df.iloc[:, 0].values
y1 = df.iloc[:, 1].values
y2 = df.iloc[:, 2].values
y3 = df.iloc[:, 3].values
y4 = df.iloc[:, 4].values
y5 = df.iloc[:, 5].values
y6 = df.iloc[:, 6].values
y7 = df.iloc[:, 7].values
y8 = df.iloc[:, 8].values
y9 = df.iloc[:, 9].values

# 数据切片
x = x[150:-100]
y1 = y1[150:-100]
y2 = y2[150:-100]
y3 = y3[150:-100]
y4 = y4[150:-100]
y5 = y5[150:-100]
y6 = y6[150:-100]
y7 = y7[150:-100]
y8 = y8[150:-100]
y9 = y9[150:-100]

# 定义曲线数据和属性
curves_data = [
    (y9, 'green', '0%'),
    (y8, 'black', '5%'),
    (y7, 'yellow', '10%'),
    (y6, 'blue', '15%'),
    (y5, 'brown', '20%'),
    (y4, 'red', '25%'),
    (y3, 'darkgray', 'Unknow 1'),
    (y2, 'purple', 'Unknow 2')
]


# 修正的半高宽计算函数
def calculate_fwhm_corrected(x_data, y_data, peak_idx):
    """
    修正的半高宽计算 - 对于SPR曲线，半高是指从基线到峰值深度的一半
    """
    # 找到基线（曲线的最大值，即反射率的最高点）
    baseline = np.max(y_data)
    min_value = y_data[peak_idx]  # 最小值（反射率最低点）

    # 计算半高位置：基线 - (基线 - 最小值) / 2
    half_max = baseline - (baseline - min_value) / 2

    print(f"调试: 基线={baseline:.3f}, 最小值={min_value:.3f}, 半高位置={half_max:.3f},半高={(baseline-min_value)/2}")

    # 在峰值左侧找到半高点
    left_half = None
    for i in range(peak_idx, 0, -1):
        if y_data[i] <= half_max and y_data[i - 1] >= half_max:
            # 线性插值
            x1, y1 = x_data[i], y_data[i]
            x2, y2 = x_data[i - 1], y_data[i - 1]
            left_half = x1 + (x2 - x1) * (half_max - y1) / (y2 - y1)
            break

    # 在峰值右侧找到半高点
    right_half = None
    for i in range(peak_idx, len(y_data) - 1):
        if y_data[i] <= half_max and y_data[i + 1] >= half_max:
            # 线性插值
            x1, y1 = x_data[i], y_data[i]
            x2, y2 = x_data[i + 1], y_data[i + 1]
            right_half = x1 + (x2 - x1) * (half_max - y1) / (y2 - y1)
            break

    if left_half is not None and right_half is not None:
        fwhm = right_half - left_half
        return fwhm, left_half, right_half, half_max, baseline
    else:
        return np.nan, np.nan, np.nan, np.nan, baseline


# 创建更大的图形
plt.figure(figsize=(14, 10))

# 存储最小值信息和半高宽信息
min_values = []
fwhm_values = []

# 绘制曲线并记录最小值和计算半高宽
for i, (y, color, label) in enumerate(curves_data):
    # 绘制曲线
    linewidth = 2 if i in [3, 4, 6, 7] else 1.5
    plt.plot(x, y, '-', color=color, linewidth=linewidth, label=f'{label}')

    # 找到最小值点
    min_idx = np.argmin(y)
    x_min = x[min_idx]
    y_min = y[min_idx]

    # 标记最小值点
    plt.scatter(x_min, y_min, color=color, s=100, zorder=5, marker='o', edgecolors='white', linewidth=1.5)

    # 计算半高宽
    print(f"\n计算曲线 {label}:")
    fwhm_result = calculate_fwhm_corrected(x, y, min_idx)

    if len(fwhm_result) == 5 and not np.isnan(fwhm_result[0]):
        fwhm, left_half, right_half, half_max, baseline = fwhm_result

        # 绘制半高宽线
        plt.hlines(half_max, left_half, right_half, color=color, linestyle='--', alpha=0.8, linewidth=1.5)
        plt.vlines(left_half, half_max, y_min, color=color, linestyle=':', alpha=0.6, linewidth=1)
        plt.vlines(right_half, half_max, y_min, color=color, linestyle=':', alpha=0.6, linewidth=1)

        # 标记半高宽点
        plt.scatter(left_half, half_max, color=color, s=80, zorder=5, marker='D', edgecolors='white')
        plt.scatter(right_half, half_max, color=color, s=80, zorder=5, marker='D', edgecolors='white')

        # 添加半高宽标注
        plt.annotate(f'FWHM={fwhm:.1f}nm',
                     xy=((left_half + right_half) / 2, half_max),
                     xytext=(0, 15),
                     textcoords='offset points',
                     fontsize=8,
                     color=color,
                     ha='center',
                     bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))

        fwhm_values.append((color, label, fwhm, left_half, right_half, half_max, baseline))
        print(f"成功: {label}: FWHM = {fwhm:.2f} nm")
    else:
        baseline = fwhm_result[4]
        fwhm_values.append((color, label, np.nan, np.nan, np.nan, np.nan, baseline))
        print(f"失败: {label}: 无法计算半高宽")

    # 在最小值点上添加坐标标注
    plt.annotate(f'({x_min:.1f}, {y_min:.3f})',
                 xy=(x_min, y_min),
                 xytext=(10, 10),
                 textcoords='offset points',
                 fontsize=9,
                 color=color,
                 alpha=0.9,
                 bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))

    # 保存最小值信息
    min_values.append((color, label, x_min, y_min))

# 创建图例
legend_handles = []
legend_labels = []

for i, (color, label, x_min, y_min) in enumerate(min_values):
    handle = plt.Line2D([0], [0], color=color, linewidth=3, marker='o',
                        markersize=8, markeredgecolor='white')
    legend_handles.append(handle)

    # 添加半高宽信息到图例
    if i < len(fwhm_values) and not np.isnan(fwhm_values[i][2]):
        fwhm_info = f'FWHM={fwhm_values[i][2]:.1f}nm'
    else:
        fwhm_info = 'FWHM=N/A'

    legend_labels.append(f'{label}\nλ={x_min:.1f}nm\n{fwhm_info}')

plt.legend(legend_handles, legend_labels, fontsize=9, loc='best', framealpha=0.9)

# 标签和网格
plt.xlabel(r'Wavelength $\lambda$ (nm)', fontsize=14)
plt.ylabel('Reflectivity Intensity', fontsize=14)
plt.title('SPR Curves with FWHM Analysis', fontsize=16)
plt.grid(True, alpha=0.3)

# 调整布局并保存
plt.tight_layout()
plt.savefig('SPR_curves_with_FWHM.pdf', bbox_inches='tight', dpi=300)
plt.show()

# 打印详细的半高宽结果表格
print("\n" + "=" * 80)
print("半高宽详细计算结果:")
print("=" * 80)
print(
    f"{'曲线':<12} {'共振波长(nm)':<12} {'基线强度':<10} {'半高位置':<10} {'FWHM(nm)':<10} {'左边界(nm)':<12} {'右边界(nm)':<12}")
print("-" * 80)
for color, label, fwhm, left, right, half_max, baseline in fwhm_values:
    x_min = next((x_min for c, l, x_min, y_min in min_values if l == label), np.nan)
    if not np.isnan(fwhm):
        print(
            f"{label:<12} {x_min:<12.1f} {baseline:<10.3f} {half_max:<10.3f} {fwhm:<10.2f} {left:<12.1f} {right:<12.1f}")
    else:
        print(f"{label:<12} {x_min:<12.1f} {baseline:<10.3f} {'N/A':<10} {'N/A':<10} {'N/A':<12} {'N/A':<12}")

# 保存结果到CSV文件
results_df = pd.DataFrame({
    'Curve': [label for _, label, _, _, _, _, _ in fwhm_values],
    'Resonance_Wavelength_nm': [x_min for _, _, x_min, _ in min_values],
    'Baseline_Intensity': [baseline for _, _, _, _, _, _, baseline in fwhm_values],
    'HalfMax_Intensity': [half_max for _, _, _, _, _, half_max, _ in fwhm_values],
    'FWHM_nm': [fwhm for _, _, fwhm, _, _, _, _ in fwhm_values],
    'Left_Bound_nm': [left for _, _, _, left, _, _, _ in fwhm_values],
    'Right_Bound_nm': [right for _, _, _, _, right, _, _ in fwhm_values]
})
results_df.to_csv('SPR_FWHM_results.csv', index=False)
print(f"\n结果已保存到 'SPR_FWHM_results.csv'")


a = np.array([109.2,120.9,119.9,122.4,167.1,155.7,143.4,154.3])
S = np.array([2111.6406])
print(S/a)
print(np.mean(S/a))