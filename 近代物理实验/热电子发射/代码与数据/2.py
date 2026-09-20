import numpy as np
import matplotlib.pyplot as plt

s = np.array([0.003,0.025,0.036,0.044,0.051,0.057,0.062,0.067,0.072,0.076,0.081,0.085,0.088,0.092,0.095,0.099,0.102,0.105,0.108,0.111,0.114])
a = np.array([42,40,38,36,34,32,29,25,22,19,14,11,8,5,4,2,2,1,1,1,0.001])
p = 42.2612
a = a/p
a = a
s2 = s**2
lna = np.log(1/a -1)

x = lna
y = s2


# 计算线性回归
x_mean = np.mean(x)
y_mean = np.mean(y)

numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean)**2)

slope = numerator / denominator
intercept = y_mean - slope * x_mean

# 计算R²值
y_pred = slope * x + intercept
ss_res = np.sum((y - y_pred)**2)
ss_tot = np.sum((y - y_mean)**2)
r_squared = 1 - (ss_res / ss_tot)

print("斜率:", slope)
print("截距:", intercept)
print("R²值:", r_squared)

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'ro')

# 生成更平滑的拟合线
x_line = np.linspace(min(x-1), max(x+1), 100)
y_line = slope * x_line + intercept
label_line1 = fr'$r^2 = {slope:.4f} \ln\left(\frac{{I_{{a_0}}}}{{I_a}}-1\right) + {intercept:.4f}$'
label_line2 = f'$R^2 = {r_squared:.4f}$'
label_line3 = fr'$I_{{a_0}} = {p}$'
label_line4 = fr'$\epsilon_F = \frac{{1}}{{k_BT}}\frac{{b}}{{k}}={intercept/slope*1.38*1e-4*2.36*1e3/1.6}eV$'
plt.plot(x_line, y_line, color='blue', linewidth=2,
         label=f'{label_line1}\n{label_line2}\n{label_line3}\n{label_line4}')# 使用数学符号设置坐标轴标签
plt.xlabel(r'$ln(\frac{I_{a_0}}{I_a}-1)$', fontsize=16)
plt.ylabel(r'$I_s^2$', fontsize=16)
plt.title(r'$I_s^2 = kln(\frac{I_{a_0}}{I_a}-1) + b$ ', fontsize=18)

plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(fontsize=12, loc='best')
plt.tight_layout()
plt.show()

print(intercept/slope*1.38*1e-4*2.36*1e3/1.6)
o = intercept/slope*1.38*1e-4*2.36*1e3/1.6
z = 1.38*1e-23*2.36*1e3/(1.6*1e-19)/slope
w = o/intercept
print(z)
print(w)
print((2*np.sqrt(w*1.6)/2.95*1e2)**(2/3))
s2 = np.linspace(0,0.015,1000)
m = 1/(np.exp((s2*w- 0.9699215207244691)*1.6*1e-19/(1.38*1e-23*2.36*1e3))+1)
plt.plot(s2,m,'r')
plt.grid(True, alpha=0.3, linestyle='--')
plt.xlabel(r'$I_{s}^2$', fontsize=40)
plt.ylabel(r'$\frac{1}{exp[\frac{KI_s^2-\epsilon_F}{kT}]+1}$', fontsize=40)
plt.title(r'$I_{s}^2-\frac{1}{exp[\frac{KI_s^2-\epsilon_F}{kT}]+1}$ ', fontsize=36)
plt.show()


n = np.exp((o*s2/intercept- 0.9699215207244691)*1.6*1e-19/(1.38*1e-23*2.36*1e3))/(np.exp((o*s2/intercept- 0.9699215207244691)*1.6*1e-19/(1.38*1e-23*2.36*1e3))+1)**2/(1.38*1e-23*2.36*1e3)*1.6*1e-19
plt.plot(s2,n,'r')
plt.grid(True, alpha=0.3, linestyle='--')
plt.xlabel(r'$I_{s}^2$', fontsize=40)
plt.ylabel(r'$\frac{exp[\frac{KI_s^2-\epsilon_F}{kT}]}{kT(exp[\frac{KI_s^2-\epsilon_F}{kT}]+1)^2}$', fontsize=40)
plt.title(r'$I_{s}^2-\frac{exp[\frac{KI_s^2-\epsilon_F}{kT}]}{kT(exp[\frac{KI_s^2-\epsilon_F}{kT}]+1)^2}$ ', fontsize=36)
plt.show()