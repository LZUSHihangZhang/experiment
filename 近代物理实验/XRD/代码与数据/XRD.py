import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_excel('XRD.xlsx')

theta = df.iloc[:, 0]
amplitude = np.array(df.iloc[:, 1])
plt.plot(theta, amplitude,'b-', label='absorption X-ray spectrum')
plt.xlabel(r'$\theta$')
plt.ylabel(r'$A$')
plt.grid(True)
plt.legend(loc='best', fontsize=10)

# 调整布局
plt.tight_layout()

# 保存图形（在show之后）
plt.savefig('XRD.pdf', format='pdf', dpi=150, bbox_inches='tight')
plt.show()