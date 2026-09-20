import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dtype = np.float64

file_path = '/media/E/Python3.12/Python代码/实验/磁光克尔效应/1.192.xlsx'
df = pd.read_excel(file_path)
H = (np.array(df.iloc[:, 1])*1e-3*1250-1273.5)
M = (np.array(df.iloc[:, 2])*1e-3*0.00988015+1.50226)
H = H - H.mean()
M = M - M.mean()
H = np.append(H,H[0])
M = np.append(M,M[0])
plt.plot(H,M,'b-')
plt.plot(H,M,'ro')
plt.xlabel(r'$B(mT)$')
plt.ylabel(r'$\theta$')
plt.title(r'$B$ = $f(\theta)$ ', fontsize=18)

plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(fontsize=12, loc='best')
plt.tight_layout()
plt.savefig('磁滞回线.pdf', bbox_inches='tight', dpi=300)
plt.show()
print(H.mean())
print(M.mean())
print(max(M)-min(M))