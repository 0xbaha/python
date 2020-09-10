
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline,interp1d

fpr = np.array([0,0.17818919,1])
tpr = np.array([0,0.99878673,1])

n = 4
x_interp = np.linspace(0,1,n)
y_interp = spline(fpr, tpr, x_interp, order=0)

m = 50
x_new = np.linspace(0,1,m)
# y_interp3 = spline(fpr, tpr, x_interp3, order=0)
y_new = interp1d(x_interp,y_interp,kind='cubic')

print('tpr:\n',tpr)
print('fpr:\n',fpr)
print('x_interp:\n',x_interp)
print('y_interp:\n',y_interp)

fig0 = plt.plot(fpr,tpr,label='fig0')
fig1 = plt.plot(x_interp,y_interp,label='fig1')
fig2 = plt.plot(x_new,y_new(x_new),label='fig2')

plt.legend(loc='best')
plt.show(fig0)
plt.show(fig1)
plt.show(fig2)
