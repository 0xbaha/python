# Check if a Number is a Perfect Number

n = int(input("Enter any number: "))

sum1 = 0

for i in range(1,n):
    if (n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("The number is a Perfect number!")
else:
    print("The number isn't a Perfect number!")
