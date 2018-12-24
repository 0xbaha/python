#  find sum of the digits of a number

n = int(input("Enter a number: "))
tot = 0
while(n>0):
    dig = n%10      # dig = n mod 10
    tot = tot + dig
    n = n//10       # n = n div 10
print("The total of digits is:", tot)
