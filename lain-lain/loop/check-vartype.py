# https://stackoverflow.com/questions/4843173/how-to-check-if-type-of-a-variable-is-string

# periksa tipe dari nilai suatu Variabel

lst1 = [1,2,3,4,5]

for i,j in enumerate(lst1):
    abc = i+1
    if isinstance(abc,int):     # periksa apakan abc bertipe integer
        print('integer: True')
    abc = str(abc)              # konversi nilai abc dari integer menjadi string
    if isinstance(abc,str):     # periksa apakan abc bertipe string
        print('string : True')
    print()
