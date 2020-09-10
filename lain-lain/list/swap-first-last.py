# Swap the First and Last Value of a List

a = []

n = int(input("Enter the number of elements in list: "))

for x in range(0,n):
    element = int(input("Enter element " + str(x+1) + ": "))
    a.append(element)
print()
print("Old list is:")
print(a)
print()
temp = a[0]
a[0] = a[n-1]
a[n-1] = temp
print("New list is:")
print(a)

# OUTPUT #
# Enter the number of elements in list: 10
# Enter element 1: 2
# Enter element 2: 3
# Enter element 3: 4
# Enter element 4: 5
# Enter element 5: 6
# Enter element 6: 7
# Enter element 7: 8
# Enter element 8: 9
# Enter element 9: 11
# Enter element 10: 12
#
# Old list is:
# [2, 3, 4, 5, 6, 7, 8, 9, 11, 12]
#
# New list is:
# [12, 3, 4, 5, 6, 7, 8, 9, 11, 2]
