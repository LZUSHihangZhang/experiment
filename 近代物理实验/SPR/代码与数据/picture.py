import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 读取数据
df = pd.read_excel('1.xlsx', header=0)

# 获取数据 - 修正列索引方式
x = df.iloc[:, 0].values  # 使用 iloc 而不是直接索引
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

# 创建图形
plt.figure(figsize=(10, 6))

# 绘制曲线 - 修正颜色和标记问题
plt.plot(x, y9, '-', color='green', linewidth=1.5, label='0%')
plt.plot(x, y8, '-', color='black', linewidth=1.5, label='5%')
plt.plot(x, y7, '-', color='yellow', linewidth=1.5, label='10%')
plt.plot(x, y6, '-', color='blue', linewidth=2, label='15%')  # 增加线宽而不是标记大小
plt.plot(x, y5, '-', color='brown', linewidth=1.5, label='20%')
plt.plot(x, y4, '-', color='red', linewidth=2, label='25%')   # 增加线宽而不是标记大小
plt.plot(x, y3, '-', color='darkgray', linewidth=2, label='Unknow 1')  # 改为深灰色
plt.plot(x, y2, '-', color='purple', linewidth=2, label='Unknow 2')


# 标签和网格
plt.xlabel(r'$\lambda$', fontsize=12)  # 修正 LaTeX 格式
plt.ylabel('Intensity', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=10)

# 保存为 PDF 格式
plt.savefig('figure.pdf', bbox_inches='tight', dpi=300)
plt.show()