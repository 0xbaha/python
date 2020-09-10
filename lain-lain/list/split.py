# Mendefinisikan nilai list0
list0 = [
    [9, 'ee', 11],
    [7, 'bb', 22],
    [6, 'dd', 33],
    [3, 'bb', 44],
    [3, 'cc', 44],
    [3, 'bb', 55],
    [1, 'aa', 77]
]
# Menampilkan isi dari list0
print('isi dari list0')
for i in list0:
    print(i)
print()

# Mendefinisikan nilai awal list1, list2, dan list3
list1 = []
list2 = []
list3 = []

# Split isi dari list0 ke list1, list2, dan list3
for i in range(len(list0)):
    for j in range(1):
        list1.append(list0[i][0])
        list2.append(list0[i][1])
        list3.append(list0[i][2])

# Menampilkan isi dari list1
print('isi dari list1:',list1)
# Menampilkan isi dari list2
print('isi dari list2:',list2)
# Menampilkan isi dari list3
print('isi dari list3:',list3)
