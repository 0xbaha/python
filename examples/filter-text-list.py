# Check if a Python list item contains a string inside another string
# https://stackoverflow.com/questions/4843158/check-if-a-python-list-item-contains-a-string-inside-another-string#4843172

some_list = ['abc-123', 'def-456', 'ghi-789', 'abc-456']
if any("abc" in s for s in some_list):
    print('FOUND abc!')
if any("def" in s for s in some_list):
    print('FOUND def!')
print('------------------------------------------------')
# -------------------------------------------------------
for i,j in enumerate(some_list):
    print('i =',i,'| j =',j)
    if any("ghi" in s for s in some_list):
        print('index dari ghi=', i)
print('------------------------------------------------')
# -------------------------------------------------------
for i,j in enumerate(some_list):
    print('i =',i,'| j =',j)
    if any("ghi" in j for s in some_list):
        print('index dari ghi=', i)
print('------------------------------------------------')
# -------------------------------------------------------
for i,j in enumerate(some_list):
    print('i =',i,'| j =',j)
    if any("ghi" in j for j in some_list):
        print('index dari ghi=', i)

# OUTPUT #
# D:\Git\learn-py\examples>python filter-text-list.py
# FOUND abc!
# FOUND def!
# ------------------------------------------------
# i = 0 | j = abc-123
# index dari ghi= 0
# i = 1 | j = def-456
# index dari ghi= 1
# i = 2 | j = ghi-789
# index dari ghi= 2
# i = 3 | j = abc-456
# index dari ghi= 3
# ------------------------------------------------
# i = 0 | j = abc-123
# i = 1 | j = def-456
# i = 2 | j = ghi-789
# index dari ghi= 2
# i = 3 | j = abc-456
# ------------------------------------------------
# i = 0 | j = abc-123
# index dari ghi= 0
# i = 1 | j = def-456
# index dari ghi= 1
# i = 2 | j = ghi-789
# index dari ghi= 2
# i = 3 | j = abc-456
# index dari ghi= 3
#
# D:\Git\learn-py\examples>
