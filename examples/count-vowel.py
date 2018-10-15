# Count the Number of Vowels in a String

string = input("Enter string: ")
vowels = 0

for i in string:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
print("Number of vowels are:", vowels)

# OUTPUT #
# D:\Git\learn-py\examples>python count-vowel.py
# Enter string: New York
# Number of vowels are: 2
#
# D:\Git\learn-py\examples>python count-vowel.py
# Enter string: Washington
# Number of vowels are: 3
#
# D:\Git\learn-py\examples>python count-vowel.py
# Enter string: Singapore
# Number of vowels are: 4
