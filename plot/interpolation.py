
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline,interp1d

tpr =[0,0.3,0.4,0.5,1]
fpr =[0,0.1,0.4,0.9,1]

n = 20
x_interp = np.linspace(0,1,n+1)
y_interp = spline(fpr, tpr, x_interp, order=0)

m = 100
x_interp2 = np.linspace(0,1,m+1)
y_interp2 = spline(fpr, tpr, x_interp2, order=0)

m = 200
x_interp3 = np.linspace(0,1,m+1)
# y_interp3 = spline(fpr, tpr, x_interp3, order=0)
y_interp3 = interp1d(fpr,tpr,kind='cubic')

print('tpr:\n',tpr)
print('fpr:\n',fpr)
print('x_interp:\n',x_interp)
print('y_interp:\n',y_interp)

fig1 = plt.plot(tpr,fpr,label='fig1')
fig2 = plt.plot(x_interp,y_interp,label='fig2')
fig3 = plt.plot(x_interp2,y_interp2,label='fig3')
fig4 = plt.plot(x_interp3,y_interp3(x_interp3),label='fig4')

plt.legend(loc='best')
plt.show(fig1)
plt.show(fig2)
plt.show(fig3)
plt.show(fig4)
