import matplotlib.pyplot as plt
import numpy as np

# ==================== LaTeX 标准样式设置 ====================
plt.rcParams.update({
    "text.usetex": True,                     # 使用 LaTeX 渲染文本
    "font.family": "serif",
    "font.serif": ["Times New Roman"],       # Times New Roman 字体
    "font.size": 12,
    "axes.labelsize": 12,
    "axes.linewidth": 0.8,
    "xtick.direction": "out",                # 刻度线向外
    "ytick.direction": "out",
    "xtick.major.size": 6,
    "ytick.major.size": 6,
    "savefig.dpi": 300,
    "savefig.format": "pdf"
})
# ========================================================

# 调制信号频率（设为 1 kHz，便于观察波形）
f_mod = 1000                     # Hz
omega = 2 * np.pi * f_mod        # 角频率 (rad/s)

A = 0.01                         # 调制幅度（相对半波电压的比例）
B = -0.5                          # 直流偏压（此处为 0，即工作点在最小输出点）

t = np.linspace(0, 5e-3, 10000)  # 5 ms，共 5 个调制周期
# 电光调制输出光强公式：I = 0.5 * [1 - cos(π*(B + A*sin(ωt)))]
I = 0.5 * (1 - np.cos(np.pi * (B + A * np.sin(omega * t))))

# 绘图
plt.figure(figsize=(6, 4))
plt.plot(t * 1000, I,color = 'orange')            # t 转换为毫秒，横轴更直观
plt.xlabel(r"$t$ (ms)")
plt.ylabel(r"$I/I_0$ ")
plt.title(r"$\frac{V_m}{V_\pi}=0.01,\ \frac{V_{DC}}{V_\pi}=-0.5$")
plt.grid(True, linestyle=":", alpha=0.6)
plt.tight_layout()

# 保存为 PDF 文件
plt.savefig("-0.5.pdf")
plt.show()
