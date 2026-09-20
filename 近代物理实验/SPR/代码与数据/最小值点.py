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
y = [y9,y8,y7,y6,y5,y4,y3,y2,y1]
# 创建更大的图形
plt.figure(figsize=(14, 8))

# 定义曲线数据和属性
curves = [
    (y9, 'green', '0%'),
    (y8, 'black', '5%'),
    (y7, 'yellow', '10%'),
    (y6, 'blue', '15%'),
    (y5, 'brown', '20%'),
    (y4, 'red', '25%'),
    (y3, 'darkgray', 'Unknow 1'),
    (y2, 'purple', 'Unknow 2')
]

# 存储最小值信息
min_values = []

# 绘制曲线并记录最小值
for i, (y, color, label) in enumerate(curves):
    # 绘制曲线
    linewidth = 2 if i in [3, 4, 6, 7] else 1.5
    plt.plot(x, y, '-', color=color, linewidth=linewidth)

    # 找到最小值点
    min_idx = np.argmin(y)
    x_min = x[min_idx]
    y_min = y[min_idx]

    # 标记最小值点
    plt.scatter(x_min, y_min, color=color, s=100, zorder=5, marker='o', edgecolors='white', linewidth=1.5)

    # 在点上添加坐标标注
    plt.annotate(f'({x_min:.1f}, {y_min:.3f})',
                 xy=(x_min, y_min),
                 xytext=(8, 8),
                 textcoords='offset points',
                 fontsize=9,
                 color=color,
                 alpha=0.8,
                 bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.7))

    # 保存最小值信息用于图例
    min_values.append((color, label, x_min, y_min))

# 创建图例，包含完整的坐标信息
legend_handles = []
legend_labels = []

for color, label, x_min, y_min in min_values:
    handle = plt.Line2D([0], [0], color=color, linewidth=3, marker='o',
                        markersize=8, markeredgecolor='white')
    legend_handles.append(handle)
    # 图例中显示完整坐标
    legend_labels.append(f'{label}\nλ={x_min:.1f}, I={y_min:.3f}')

plt.legend(legend_handles, legend_labels, fontsize=10, loc='best', framealpha=0.9)

# 标签和网格
plt.xlabel(r'$\lambda$', fontsize=14)
plt.ylabel('Intensity', fontsize=14)
plt.grid(True, alpha=0.3)

# 调整布局并保存
plt.tight_layout()
plt.savefig('figure.pdf', bbox_inches='tight', dpi=300)
plt.show()
