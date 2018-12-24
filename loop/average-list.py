#  find the average of numbers in a list in 

n = int(input("Enter the number of elements to be insterted: "))

a = []

for i in range(0,n):
    elem = int(input("Enter element: "))
    a.append(elem)
avg = sum(a)/n
print("Average of elements in the list", round(avg,2))
