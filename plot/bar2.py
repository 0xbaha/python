import matplotlib.pyplot as plt
import operator
from functools import reduce

nama = ['ee','bb','dd','hh','aa']
nilai = [44,77,33,88,55]

# menentukan warna pada nama tertentu
nama_terpilih = 'hh'
for i,j in enumerate(nama):
    if j == nama_terpilih:
        kolom_terpilih = i

barlist = plt.bar(nama,nilai)
barlist[kolom_terpilih].set_color('r')
plt.show()
