import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 显式指定 openpyxl 引擎，避免调用 xlrd
df = pd.read_excel('1.xlsx', engine='openpyxl')

# 打印第一列的前几行数据（按位置访问）
print(df.iloc[:, 0].head())