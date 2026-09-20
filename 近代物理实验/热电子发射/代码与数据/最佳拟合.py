import numpy as np
import matplotlib.pyplot as plt
import torch

device = torch.device('cuda')
type = torch.float64

s = torch.tensor([0.003,0.025,0.036,0.044,0.051,0.057,0.062,0.067,0.072,0.076,0.081,0.085,0.088,0.092,0.095,0.099,0.102,0.105,0.108,0.111,0.114],device=device,dtype=type)
a = torch.tensor([42,40,38,36,34,32,29,25,22,19,14,11,8,5,4,2,2,1,1,1,0.001],dtype=type,device=device)
p = torch.tensor([45],device=device,dtype=type)
p.requires_grad_(True)
optimizer = torch.optim.Adam([p], lr=0.01)
num_epochs = 10000
for epoch in range(num_epochs):
    optimizer.zero_grad()
    k = a / p
    s2 = s ** 2
    lna = torch.log(1 / k - 1)

    x = lna
    y = s2

    # 计算线性回归
    x_mean = torch.mean(x)
    y_mean = torch.mean(y)

    numerator = torch.sum((x - x_mean) * (y - y_mean))
    denominator = torch.sum((x - x_mean) ** 2)

    slope = numerator / denominator
    intercept = y_mean - slope * x_mean

    # 计算R²值
    y_pred = slope * x + intercept
    ss_res = torch.sum((y - y_pred) ** 2)
    ss_tot = torch.sum((y - y_mean) ** 2)
    r_squared = 1 - (ss_res / ss_tot)

    Loss = -r_squared
    Loss.backward()
    optimizer.step()

    if epoch % 100 == 0:
       print(f"Epoch {epoch}, $R^2$: {Loss.item():.6f}, p:{p} ")









