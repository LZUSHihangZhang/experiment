import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
I = np.arange(0,1.25,0.05)
'''I = np.arange(0.05,1.05,0.05)'''
R = 0.1
N = 200
B = 8*4*np.pi*10**(-7)*N*I/(5**(3/2)*R)
V = np.array([
    1.5875,1.5894,1.5934,1.5986,1.6045,1.6099,1.6153,1.6210,1.6264,
    1.6318,1.6370,1.6424,1.6478,1.6532,1.6584,1.6638,1.6688,1.6737,
    1.6787,1.6834,1.6880,1.6925,1.6965,1.7007,1.7043
])
'''V = np.array([
    1.5894,1.5934,1.5986,1.6045,1.6099,1.6153,1.6210,1.6264,
    1.6318,1.6370,1.6424,1.6478,1.6532,1.6584,1.6638,1.6688,1.6737,
    1.6787,1.6834,1.6880
])'''
V1 = 5
V0 = 1.5875
R = V0*(V1-V)/V/(V1-V0)
print(V)
print(R)
print(R-1)

# Linear least-squares fitting
x = B
y = R
x_mean = np.mean(x)
y_mean = np.mean(y)

slope = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean)**2)
intercept = y_mean - slope * x_mean

y_pred = slope * x + intercept
ss_res = np.sum((y - y_pred)**2)
ss_tot = np.sum((y - y_mean)**2)
r_squared = 1 - (ss_res / ss_tot)

print(f"Slope = {slope:.6f}")
print(f"Intercept = {intercept:.6f}")
print(f"R² = {r_squared:.6f}")

plt.figure(figsize=(6, 4))
plt.plot(B, R, 'o', markersize=4, label='Data')
plt.plot(B, y_pred, '-', linewidth=1.5, label=f'Linear fit (R²={r_squared:.4f})')
plt.xlabel('B')
plt.ylabel(r'$\dfrac{R_B}{R_0}$')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('B-R.pdf')

