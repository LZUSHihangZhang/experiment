import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('basic_line.xlsx')
L = df.iloc[:, 0]
E1 = np.array(df.iloc[:, 1])
plt.plot(L,E1)
plt.show()
