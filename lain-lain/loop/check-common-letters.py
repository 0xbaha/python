# Check Common Letters in Two Input Strings

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print()
a = list(set(s1)&set(s2))

print("The common letters are:")
for i in a:
    print(i)
print()
a.sort()
print("The common letters are (sorted):")
for i in a:
    print(i)

# OUTPUT #
# D:\Git\learn-py\examples>python check-common-letters.py
# Enter first string: New York
# Enter second string: Singapore
#
# The common letters are:
# o
# r
# e
#
# The common letters are (sorted):
# e
# o
# r
#
# D:\Git\learn-py\examples>
