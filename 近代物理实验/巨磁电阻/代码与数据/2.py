import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
I = np.arange(0.05,1.05,0.05)
'''I = np.arange(0,1.25,0.05)'''
R = 0.1
N = 200
B = 8*4*np.pi*10**(-7)*N*I/(5**(3/2)*R)
'''V = np.array(
    [0,0.0042,0.0142,0.0266,0.0391,0.0513,0.0643,
     0.0769,0.0898,0.1020,0.1138,0.1258,0.1386,0.1507,
     0.1623,0.1741,0.1853,0.1965,0.2076,0.2188,
     0.2290,0.2386,0.2484,0.2576,0.2658]
)'''
V = np.array(
    [0.0042,0.0142,0.0266,0.0391,0.0513,0.0643,
     0.0769,0.0898,0.1020,0.1138,0.1258,0.1386,0.1507,
     0.1623,0.1741,0.1853,0.1965,0.2076,0.2188,
     0.2290]
)
# Linear regression
x = B
y = V
x_mean = np.mean(x)
y_mean = np.mean(y)

numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean)**2)

slope = numerator / denominator
intercept = y_mean - slope * x_mean

y_pred = slope * x + intercept
ss_res = np.sum((y - y_pred)**2)
ss_tot = np.sum((y - y_mean)**2)
r_squared = 1 - (ss_res / ss_tot)
print(slope,intercept)
plt.figure(figsize=(6, 4))
plt.plot(B, V, 'o', markersize=4, label='Data')
plt.plot(B, y_pred, '-', linewidth=1.5, label=f'Linear fit (R²={r_squared:.4f})')
plt.xlabel('B (T)')
plt.ylabel(r'$V_{\text{output}}$ (V)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('B-V_output_2.pdf')

print(133.76/0.0022*4*1e-7/2)