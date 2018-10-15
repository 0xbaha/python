# referensi:
# https://solarianprogrammer.com/2017/02/25/install-numpy-scipy-matplotlib-python-3-windows/

import scipy as sp
import matplotlib.pylab as plt

t = sp.linspace(0,1,100)

plt.plot(t,t**2)
plt.show()
