import numpy as np
import matplotlib.pyplot as plt
# Data: W = optical power, N = average count rate
# Temperatures: 10°C, 0°C, -10°C
W_10C = np.array([0.85, 0.9, 0.95, 1.00, 1.05])*1e-6
W_0C = np.array([0.85, 0.9, 0.95, 1.01, 1.05, 1.10])*1e-6
W_n10C = np.array([0.85, 0.9, 0.95, 1.00, 1.05])*1e-6

N_10C = np.array([47318, 50385, 53181, 56407, 59602])
N_0C = np.array([46989, 50070, 53474, 56912, 59812, 62478])
N_n10C = np.array([47303, 50533, 54397, 56600, 59484])

# Subtract background (dark counts - these are already low)
# The small subtraction (10-11) suggests dark counts are negligible
n_10C = N_10C - 11
n_0C = N_0C - 10
n_n10C = N_n10C - 10

print('*********************************************')
print('利用滤波器得到的功率')
F = 0.88
P0_1 = W_10C*0.019*0.019*0.018*(1-0.019)*2*F
P0_0 = W_0C*0.019*0.019*0.018*(1-0.019)*2*F
P0_n1 = W_n10C*0.019*0.019*0.018*(1-0.019)*2*F

print('10C',P0_1)
print('0C',P0_0)
print('-10C',P0_n1)

A = 6.63*1e-34*3*1e8/(500*1e-9)
P1_1 = n_10C*A/0.15
P1_0 = n_0C*A/0.15
P1_n1 = n_n10C*A/0.15
print('*********************************************')
print('利用光子计数得到的功率')
print('10C',P1_1)
print('0C',P1_0)
print('-10C',P1_n1)
print('*********************************************')

fig, ax = plt.subplots(figsize=(10, 6))
plt.plot(P1_1,P0_1,'ro',label='T = 283.15K')
plt.plot(P1_0,P0_0,'bo',label = 'T = 273.15K')
plt.plot(P1_n1,P0_n1,'go',label='T = 263.15K')
plt.plot(P1_1,P0_1,'r-',label='T = 283.15K')
plt.plot(P1_0,P0_0,'b-',label = 'T = 273.15K')
plt.plot(P1_n1,P0_n1,'g-',label='T = 263.15K')

# Format plot
ax.set_xlabel('Filter Power /W', fontsize=12)
ax.set_ylabel('Optical Power /W', fontsize=12)
ax.set_title('Filter Power vs Optical Power at Different Temperatures', fontsize=14)
ax.legend(loc='upper left', fontsize=10)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('/media/E/实验/近代物理实验/单光子计数/a.pdf', bbox_inches='tight', dpi=300)
plt.show()
