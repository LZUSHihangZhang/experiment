import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

# 设置图片清晰度
plt.rcParams['figure.dpi'] = 300

# 设置 matplotlib 支持中文
plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']
plt.rcParams['axes.unicode_minus'] = False

# 读取 Excel 文件
excel_file = pd.ExcelFile('Default Dataset.xlsx')

# 获取指定工作表中的数据
df = excel_file.parse('Default Dataset')

# 创建两个数组分别存储两列数据
array1 = df.iloc[:, 0].tolist()
array2 = df.iloc[:, 1].tolist()

a = np.array(array1)
b = np.array(array2)

a = a - 461.2367
b = b - 574.0282685512368

a = a / 1236.6783 * 1.122
b = b / 698.9045935 * 1.01

a = a
b = b

# 去除 a 中的重复值及其对应的 b 中的值
unique_indices = np.unique(a, return_index=True)[1]
a = a[unique_indices]
b = b[unique_indices]

# 使用 interp1d 进行插值，kind='cubic' 表示使用三次样条插值
f = interp1d(a, b, kind='cubic')

# 生成更密集的 x 值用于绘制光滑曲线
x_smooth = np.linspace(min(a), max(a), 1000)
y_smooth = f(x_smooth)



# 绘制光滑连接后的曲线
plt.plot(x_smooth, y_smooth, color='blue')

plt.xlabel('t/ms')
plt.ylabel('U/V')
plt.grid(True)
plt.legend()
plt.show()