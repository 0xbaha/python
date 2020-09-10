import matplotlib.pyplot as plt
import operator
from functools import reduce

nama = ['ee','bb','dd','hh','aa']
nilai = [44,77,33,88,55]

# gabung nama dan nilai
gabungan = []
for i in range(len(nama)):
    gabungan_col = []
    for j in range(1):
        gabungan_col.append(nama[i])
        gabungan_col.append(nilai[i])
    gabungan.append(gabungan_col)

# mengurutkan berdasarkan abjad nama
def selected_key(elem):
    return elem[1]
gabungan.sort(key=selected_key)

# menampilkan isi dari list gabungan
print(gabungan)

# split hasil gabungan yg telah diurukan berdasrkan abjad nama
nama = []
nilai = []
for i in range(len(gabungan)):
    for j in range(1):
        nama.append(gabungan[i][0])
        nilai.append(gabungan[i][1])

# menentukan warna pada nama tertentu
nama_terpilih = 'hh'
for i,j in enumerate(nama):
    if j == nama_terpilih:
        kolom_terpilih = i

barlist = plt.bar(nama,nilai)
barlist[kolom_terpilih].set_color('r')
plt.show()
