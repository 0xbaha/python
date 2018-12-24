# reverse a number

n = int(input("Enter number: "))
rev = 0
while (n>0):
    dig = n % 10            # dig = n mod 10
    rev = rev * 10 + dig
    n = n // 10             # n = n div 10
print("Reverse of the number:", rev)
