# Check if a Number is a Prime Number

a = int(input("Enter number: "))

k = 0
for i in range(2,a//2+1): # a//2 -> a div 2
    if(a % i == 0): # a mod i
        k = k + 1
    print(k)
if(k <= 0):
    print("Number is prime!")
else:
    print("Number isn't prime!")
