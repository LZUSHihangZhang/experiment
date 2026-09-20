import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 设置图形大小
plt.figure(figsize=(10, 6))

# 读取数据
df1 = pd.read_excel('2940.xlsx')
df2 = pd.read_excel('2860.xlsx')
df3 = pd.read_excel('2770.xlsx')
df4 = pd.read_excel('2720.xlsx')
df5 = pd.read_excel('2400.xlsx')
ldf1 = pd.read_excel('ll2940.xlsx')
ldf2 = pd.read_excel('ll2860.xlsx')
ldf3 = pd.read_excel('ll2770.xlsx')
ldf4 = pd.read_excel('ll2720.xlsx')
ldf5 = pd.read_excel('ll2400.xlsx')

# 提取数据
L = df1.iloc[:, 0]
E1 = np.array(df1.iloc[:, 1])
E2 = np.array(df2.iloc[:, 1])
E3 = np.array(df3.iloc[:, 1])
E4 = np.array(df4.iloc[:, 1])
E5 = np.array(df5.iloc[:, 1])

lE1 = np.array(ldf1.iloc[:,1])
lE2 = np.array(ldf2.iloc[:,1])
lE3 = np.array(ldf3.iloc[:,1])
lE4 = np.array(ldf4.iloc[:,1])
lE5 = np.array(ldf5.iloc[:,1])



"""对T=2940的修正"""
indices1 = np.where(L == 830)[0]
indices2 = np.where(L == 1024)[0]
indices3 = np.where(L == 1286)[0]
indices4 = np.where(L == 1490)[0]
indices5 = np.where(L == 1598)[0]
indices6 = np.where(L == 1802)[0]
N1 = (2759.7/E1[indices1]+2806.7/E1[indices2]+1776.6/E1[indices4]+1560.1/E2[indices5]+1184.4/E1[indices6])/5
print(2759.7/E1[indices1],2806.7/E1[indices2],2279.9/E1[indices3],1776.6/E1[indices4],1560.1/E2[indices5],1184.4/E1[indices6])
E1 = E1*N1


"""对T=2860的修正"""
indices1 = np.where(L == 850)[0]
indices2 = np.where(L == 970)[0]
indices3 = np.where(L == 1076)[0]
indices4 = np.where(L == 1184)[0]
indices5 = np.where(L == 1252)[0]
indices6 = np.where(L == 1466)[0]
N2 = (2366/E2[indices1]+2476.1/E2[indices2]+2395.7/E2[indices3]+2214.5/E2[indices4]+2070.5/E2[indices5]+1643.1/E2[indices6])/6
print(2366/E2[indices1],2476.1/E2[indices2],2395.7/E2[indices3],2214.5/E2[indices4],2070.5/E2[indices5],1643.1/E2[indices6])
E2 = E2*N2


"""对T=2770的修正"""
indices1 = np.where(L == 842)[0]
indices2 = np.where(L == 926)[0]
indices3 = np.where(L == 998)[0]
indices4 = np.where(L == 1254)[0]
indices5 = np.where(L == 1486)[0]
indices6 = np.where(L == 1682)[0]
N3 = (1924.3/E3[indices1]+2069.3/E3[indices2]+2102/E3[indices3]+1473.4/E3[indices5]+1116/E3[indices6])/5
print(1924.3/E3[indices1],2069.3/E3[indices2],2102/E3[indices3],1800.5/E3[indices4],1473.4/E3[indices5],1116/E3[indices6])
E3 = E3*N3

"""对T=2720的修正"""
indices1 = np.where(L == 864)[0]
indices2 = np.where(L == 952)[0]
indices3 = np.where(L == 1050)[0]
indices4 = np.where(L == 1146)[0]
indices5 = np.where(L == 1384)[0]
indices6 = np.where(L == 1640)[0]
N4 = (1753.9/E4[indices1]+1881.6/E4[indices2]+1917.8/E4[indices3]+1836.4/E4[indices4]+1491.1/E4[indices5]+1128/E4[indices6])/6
print(1753.9/E4[indices1],1881.6/E4[indices2],1917.8/E4[indices3],1836.4/E4[indices4],1491.1/E4[indices5],1128/E4[indices6])
E4 = E4*N4

"""对T=2400的修正"""
indices1 = np.where(L == 882)[0]
indices2 = np.where(L == 948)[0]
indices3 = np.where(L == 1096)[0]
indices4 = np.where(L == 1260)[0]
indices5 = np.where(L == 1468)[0]
indices6 = np.where(L == 1678)[0]
N5 = (734.5/E5[indices1]+846/E5[indices2]+1003.1/E5[indices3]+1011.3/E5[indices4]+891.6/E5[indices5]+730.3/E5[indices6])/6
print(734.5/E5[indices1],846/E5[indices2],1003.1/E5[indices3],1011.3/E5[indices4],891.6/E5[indices5],730.3/E5[indices6])
E5 = E5*N5



# 绘制曲线（为不同曲线添加标签以便区分）
plt.plot(L, E1, 'r-', label='2940K')  # 改为虚线以区分
plt.plot(L, E2, 'b-', label='2860K')
plt.plot(L, E3, 'g-', label='2770K')
plt.plot(L, E4, 'y-', label='2720K')
plt.plot(L, E5, '-', color='black', label='2400K')

plt.plot(L, lE1, 'r--', label='Theory2940K')  # 改为虚线以区分
plt.plot(L, lE2, 'b--', label='Theory2860K')
plt.plot(L, lE3, 'g--', label='Theory2770K')
plt.plot(L, lE4, 'y--', label='Theory2720K')
plt.plot(L, lE5, '--', color='black', label='Theory2400K')

# 设置坐标轴标签
plt.xlabel(r'$\lambda/mm$', fontsize=14)
plt.ylabel('E', fontsize=14)

# 添加网格和图例
plt.grid(True, alpha=0.3)
plt.legend(loc='best', fontsize=10)

# 调整布局
plt.tight_layout()

# 保存图形（在show之后）
plt.savefig('result.pdf', format='pdf', dpi=150, bbox_inches='tight')
# 先显示再保存
plt.show()
