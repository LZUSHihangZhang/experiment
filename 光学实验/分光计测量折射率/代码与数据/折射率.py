import numpy as np

varphi1 = np.array([(38+41/60),(38+44/60),(38+45/60)])
A = np.pi/3
n = np.sin((np.mean(varphi1/180*np.pi)+A)/2)/np.sin(A/2)
print(np.sin((np.mean(varphi1/180*np.pi)+A)/2)/np.sin(A/2))
varphi0 = np.mean(varphi1)
print(varphi0)
print(varphi1-varphi0)
a = np.sqrt(np.sum( (varphi1-varphi0)**2 )/(3*2))
b = 1/60/np.sqrt(3)
print(a)
print(b)
print(np.sqrt(a**2+b**2)/180*np.pi)
U_delta = np.cos((np.mean(varphi1/180*np.pi)+A)/2)/np.sin(A/2)*0.5*np.sqrt(a**2+b**2)
print(U_delta)
r = (2+15.0/60)/180*np.pi
print(np.sin(A)*np.sqrt(n**2-np.sin(r)**2) + np.cos(A)*np.sin(r))
print(U_delta*np.sin(A)*n/np.sqrt(n**2-np.sin(r)**2)/180*np.pi)
print((np.sin(A)*n/np.sqrt(n**2-np.sin(r)**2)*(-np.sin(r)*np.cos(r))+np.cos(A)*np.cos(r))*b/180*np.pi)
print(np.sqrt((U_delta*np.sin(A)*n/np.sqrt(n**2-np.sin(r)**2))**2+((np.sin(A)*n/np.sqrt(n**2-np.sin(r)**2)*(-np.sin(r)*np.cos(r))+np.cos(A)*np.cos(r))*b)**2)/180*np.pi)
print((A-np.arcsin(np.sin(35/180*np.pi)/1.6))/np.pi*180)
print(np.arcsin(1/1.6)/np.pi*180)