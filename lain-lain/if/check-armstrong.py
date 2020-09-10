# Check if a Number is an Armstrong Number

n = int(input("Enter any number: "))
a = list(map(int,str(n)))
b = list(map(lambda x:x**3,a))

if (sum(b) == n):
    print("The number is an Armstrong number!")
else:
    print("The number isn't an Armstrong number!")
