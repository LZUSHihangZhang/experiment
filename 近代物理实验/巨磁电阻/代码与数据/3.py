import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

I = np.arange(0, 5.5, 0.5)
V = np.array([0, 0, 0.0007, 0.0016, 0.0022, 0.0034, 0.0046, 0.0055, 0.0075, 0.0094, 0.0105])

'''# Linear least-squares fitting
x = I
y = V
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
print(f"V = {slope:.6f} * I + ({intercept:.6f})")
print(f"R² = {r_squared:.6f}")

plt.figure(figsize=(6, 4))
plt.plot(I, V, 'o', markersize=4, label='Data')
plt.plot(I, y_pred, '-', linewidth=1.5, label=f'Linear fit (R²={r_squared:.4f})')
plt.xlabel('I (A)')
plt.ylabel(r'$V_{\text{output}}$ (V)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('I-V_input.pdf')'''
B = (V+0.0077)/133.76
print(B)
print(4*1e-7*I/2/B*1e3)