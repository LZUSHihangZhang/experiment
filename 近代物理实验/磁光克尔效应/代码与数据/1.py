import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dtype = np.float64

file_path = '/media/E/Python3.12/Python代码/实验/磁光克尔效应/1.192.xlsx'
df = pd.read_excel(file_path)
H = np.array(df.iloc[:, 1])
M = np.array(df.iloc[:, 2])
H = np.append(H,H[0])
M = np.append(M,M[0])
plt.plot(H,M,'b-')
plt.plot(H,M,'ro')
plt.xlabel(r'$U_B$/mV')
plt.ylabel(r'N(S.E.V)/mV')
plt.title(r'$N$ = f$(U_B)$ ', fontsize=18)

plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(fontsize=12, loc='best')
plt.tight_layout()
plt.savefig('磁滞回线.pdf', bbox_inches='tight', dpi=300)
plt.show()