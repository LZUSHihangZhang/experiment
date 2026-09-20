import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Data
I = np.arange(1.8, 2.21, 0.01)
P = np.array([0.212, 0.212, 0.212, 0.211, 0.211, 0.211, 0.210, 0.210, 0.210, 0.209, 0.209, 0.208,
              0.206, 0.201, 0.198, 0.190, 0.173, 0.148, 0.144, 0.148, 0.175, 0.194,
              0.200, 0.204, 0.206, 0.208, 0.209, 0.210, 0.211, 0.211, 0.213, 0.213, 0.213,
              0.214, 0.214, 0.214, 0.216, 0.216, 0.216, 0.215, 0.215]) / 0.218 * 100
B = 0.1898 * I + 0.0079

# Smooth curve
B_smooth = np.linspace(B.min(), B.max(), 300)
spl = make_interp_spline(B, P, k=3)
P_smooth = spl(B_smooth)

# ------------------ FWHM calculation (peak/valley) ------------------
def calculate_fwhm(x, y, mode='valley'):
    """
    Calculate Full Width at Half Maximum.
    mode: 'peak' or 'valley'
    """
    if mode == 'peak':
        y_max = np.max(y)
        y_min = np.min(y)
        half = y_min + (y_max - y_min) / 2
        above_half = y >= half
    elif mode == 'valley':
        y_min = np.min(y)
        y_max = np.max(y)
        half = y_min + (y_max - y_min) / 2
        above_half = y <= half
    else:
        raise ValueError("mode must be 'peak' or 'valley'")

    crossings = []
    for i in range(len(x) - 1):
        if above_half[i] != above_half[i + 1]:
            x1, x2 = x[i], x[i + 1]
            y1, y2 = y[i], y[i + 1]
            x_cross = x1 + (half - y1) * (x2 - x1) / (y2 - y1)
            crossings.append(x_cross)

    if len(crossings) < 2:
        return None
    left, right = crossings[0], crossings[-1]
    fwhm = right - left
    return fwhm, left, right, half

# Valley-mode FWHM
fwhm, left, right, half = calculate_fwhm(B_smooth, P_smooth, mode='valley')
print(f"FWHM = {fwhm:.5f}")
print(f"Left B = {left:.5f}, Right B = {right:.5f}")
print(f"Half value = {half:.2f}")

# Plot
plt.figure(figsize=(8, 5))
plt.plot(B, P, 'o', label='Raw data')
plt.plot(B_smooth, P_smooth, '-', label='Smooth fit')
plt.axhline(y=half, color='r', linestyle='--', label=f'Half = {half:.2f}')
plt.axvline(x=left, color='g', linestyle=':', label='Left boundary')
plt.axvline(x=right, color='g', linestyle=':', label='Right boundary')
plt.hlines(y=half, xmin=left, xmax=right, colors='orange', linewidth=3, label=f'FWHM = {fwhm:.4f}')
plt.xlabel('B')
plt.ylabel('P')
plt.title('FWHM calculation (valley mode)')
plt.legend()
plt.show()