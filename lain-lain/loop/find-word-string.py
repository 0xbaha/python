# Python string, find specific word, then copy the word after it
# https://stackoverflow.com/questions/18005701/python-string-find-specific-word-then-copy-the-word-after-it

teststring = "This is a test of number, number: 525, number: 585, number2: 559"
teststring = teststring.split()
found = False

templist = []
for word in teststring:
    if found:
        templist.append(word)
        found = False
    if word == "number:":
        found = True

print('isi dari teststring')
for i in teststring:
    print(i)
print()
print('isi dari templist')
for i in templist:
    print(i)

# OUTPUT #
# D:\Git\learn-py\examples>python find-word-string.py
# isi dari teststring
# This
# is
# a
# test
# of
# number,
# number:
# 525,
# number:
# 585,
# number2:
# 559
#
# isi dari templist
# 525,
# 585,
#
# D:\Git\learn-py\examples>
