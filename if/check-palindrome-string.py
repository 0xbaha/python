# Check if a String is a Palindrome or Not

string = input("Enter string: ")

if (string == string[::-1]):
    print("The string is a palindrome!")
else:
    print("The string isn't a palindrome!")

# OUTPUT #
# D:\Git\learn-py\examples>python check-palindrome-string.py
# Enter string: baju
# The string isn't a palindrome!
#
# D:\Git\learn-py\examples>python check-palindrome-string.py
# Enter string: kodok
# The string is a palindrome!
#
# D:\Git\learn-py\examples>python check-palindrome-string.py
# Enter string: katak
# The string is a palindrome!
