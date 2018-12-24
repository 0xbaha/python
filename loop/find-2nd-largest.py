# Find the Second Largest Number in a List

a = []
n = int(input("Enter number of elements: "))

for i in range(1,n+1):
    b = int(input("Enter elemen: "))
    a.append(b)
    a.sort()
print(a)
print("Second largest element is:",a[n-2]) # n-2 because index of list started from 0

# OUTPUT #
# Enter number of elements: 10
# Enter elemen: 2
# Enter elemen: 4
# Enter elemen: 6
# Enter elemen: 8
# Enter elemen: 10
# Enter elemen: 13
# Enter elemen: 1
# Enter elemen: 7
# Enter elemen: 5
# Enter elemen: 4
# [1, 2, 4, 4, 5, 6, 7, 8, 10, 13]
# Second largest element is: 10
