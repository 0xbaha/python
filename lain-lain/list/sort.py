
# Mendefinisikan isi list
list1 = [3, 7, 9, 1, 6, 3, 3]
list2 = ['cc', 'bb', 'ee', 'aa', 'dd', 'bb', 'bb']
list3 = [44, 22, 11, 77, 33, 55, 44]

# Menampilkan isi dari list1,list2,dan list3
print('Isi dari list1:',list1)
print('Isi dari list2:',list2)
print('Isi dari list3:',list3)
print()
# Menggabungkan list1,list2,dan list3
list_x = []
for i in range(len(list1)):
    list_x_col = []
    for j in range(1):
        list_x_col.append(list1[i])
        list_x_col.append(list2[i])
        list_x_col.append(list3[i])
    list_x.append(list_x_col)
# Menampilkan isi dari list_x
print('Isi dari list_x')
for i in list_x:
    print(i)
print()

# Mengurutkan list berdasarkan kolom ke-0
def selected_key(elem):
    return elem[0]
list_x.sort(key=selected_key)
# Menampilkan isi dari list_x
print('Hasil sort berdasarkan kolom ke-0')
for i in list_x:
    print(i)
print()

# Mengurutkan list berdasarkan kolom ke-0 dan ke-1
def selected_key(elem):
    return elem[0],elem[1]
list_x.sort(key=selected_key)
# Menampilkan isi dari list_x
print('Hasil sort berdasarkan kolom ke-0 dan ke-1')
for i in list_x:
    print(i)
print()

# Mengurutkan list berdasarkan kolom ke-0, ke-1, dan ke-2
def selected_key(elem):
    return elem[0],elem[1],elem[2]
list_x.sort(key=selected_key)
# Menampilkan isi dari list_x
print('Hasil sort berdasarkan kolom ke-0, ke-1, dan ke-2')
for i in list_x:
    print(i)
print()

# Mengurutkan list berdasarkan kolom ke-1
def selected_key(elem):
    return elem[1]
list_x.sort(key=selected_key)
# Menampilkan isi dari list_x
print('Hasil sort berdasarkan kolom ke-1')
for i in list_x:
    print(i)
print()

# Mengurutkan list berdasarkan kolom ke-2
def selected_key(elem):
    return elem[2]
list_x.sort(key=selected_key)
# Menampilkan isi dari list_x
print('Hasil sort berdasarkan kolom ke-2')
for i in list_x:
    print(i)
print()

# Mengurutkan list berdasarkan kolom ke-2 (reverse=True)
def selected_key(elem):
    return elem[2]
list_x.sort(key=selected_key,reverse=True)
# Menampilkan isi dari list_x
print('Hasil sort berdasarkan kolom ke-2 (reverse=True)')
for i in list_x:
    print(i)
print()

## OUTPUT ##
# Isi dari list1: [3, 7, 9, 1, 6, 3, 3]
# Isi dari list2: ['cc', 'bb', 'ee', 'aa', 'dd', 'bb', 'bb']
# Isi dari list3: [44, 22, 11, 77, 33, 55, 44]
#
# Isi dari list_x
# [3, 'cc', 44]
# [7, 'bb', 22]
# [9, 'ee', 11]
# [1, 'aa', 77]
# [6, 'dd', 33]
# [3, 'bb', 55]
# [3, 'bb', 44]
#
# Hasil sort berdasarkan kolom ke-0
# [1, 'aa', 77]
# [3, 'cc', 44]
# [3, 'bb', 55]
# [3, 'bb', 44]
# [6, 'dd', 33]
# [7, 'bb', 22]
# [9, 'ee', 11]
#
# Hasil sort berdasarkan kolom ke-0 dan ke-1
# [1, 'aa', 77]
# [3, 'bb', 55]
# [3, 'bb', 44]
# [3, 'cc', 44]
# [6, 'dd', 33]
# [7, 'bb', 22]
# [9, 'ee', 11]
#
# Hasil sort berdasarkan kolom ke-0, ke-1, dan ke-2
# [1, 'aa', 77]
# [3, 'bb', 44]
# [3, 'bb', 55]
# [3, 'cc', 44]
# [6, 'dd', 33]
# [7, 'bb', 22]
# [9, 'ee', 11]
#
# Hasil sort berdasarkan kolom ke-1
# [1, 'aa', 77]
# [3, 'bb', 44]
# [3, 'bb', 55]
# [7, 'bb', 22]
# [3, 'cc', 44]
# [6, 'dd', 33]
# [9, 'ee', 11]
#
# Hasil sort berdasarkan kolom ke-2
# [9, 'ee', 11]
# [7, 'bb', 22]
# [6, 'dd', 33]
# [3, 'bb', 44]
# [3, 'cc', 44]
# [3, 'bb', 55]
# [1, 'aa', 77]
