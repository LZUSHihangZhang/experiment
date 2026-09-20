import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Data: W = optical power, N = average count rate
# Temperatures: 10°C, 0°C, -10°C
W_10C = np.array([0.85, 0.9, 0.95, 1.00, 1.05])
W_0C = np.array([0.85, 0.9, 0.95, 1.01, 1.05, 1.10])
W_n10C = np.array([0.85, 0.9, 0.95, 1.00, 1.05])

N_10C = np.array([47318, 50385, 53181, 56407, 59602])
N_0C = np.array([46989, 50070, 53474, 56912, 59812, 62478])
N_n10C = np.array([47303, 50533, 54397, 56600, 59484])

# Subtract background (dark counts - these are already low)
# The small subtraction (10-11) suggests dark counts are negligible
n_10C = N_10C - 11
n_0C = N_0C - 10
n_n10C = N_n10C - 10




# ========== 3. Create main figure ==========
fig, ax = plt.subplots(figsize=(10, 6))
plt.plot(W_10C,n_10C,'ro')
plt.plot(W_0C,n_0C,'bo')
plt.plot(W_n10C,n_n10C,'go')
plt.plot(W_10C,n_10C,'r-')
plt.plot(W_0C,n_0C,'b-')
plt.plot(W_n10C,n_n10C,'g-')
# Format plot
ax.set_xlabel('Optical Power (arb. units)', fontsize=12)
ax.set_ylabel('Count Rate (s⁻¹)', fontsize=12)
ax.set_title('Count Rate vs Optical Power at Different Temperatures', fontsize=14)
ax.legend(loc='upper left', fontsize=10)
ax.grid(True, alpha=0.3)
plt.savefig('1.pdf',bbox_inches='tight', dpi=300)
plt.tight_layout()
plt.show()

