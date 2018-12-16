
import matplotlib.pyplot as plt

nama = ['ee','bb','dd','hh','aa']
nilai = [44,77,33,88,55]

barlist = plt.bar(nama,nilai)
barlist[1].set_color('r')
plt.show()
