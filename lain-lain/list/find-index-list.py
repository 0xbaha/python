# Finding the index of an item given a list containing it in Python

# used for list_3
from functools import reduce
import operator

for i, j in enumerate(['foo', 'bar', 'baz']):
    if j == 'bar':
        print(i)
# -----------------------------------------------------------------------------
list_2 = ['foo2', 'bar2', 'baz2']
for i, j in enumerate(list_2):
    if j == 'bar2':
        print(i)
print()
# -----------------------------------------------------------------------------
list_3 = [['foo2'], ['bar2'], ['baz2']]
content_check = 'bar2'
print(content_check)
for i, j in enumerate(list_3):
    print('nilai i =', i, end = ' | ')
    print('nilai j =', j)
    for k, m in enumerate(list_3[i]):
        print('nilai k =', k, end = ' | ')
        print('nilai m =', m)
        zetzet = reduce(operator.getitem, [i,k], list_3)
        print('i =',i,'k =',k, '->', zetzet)
        if zetzet == 'bar2':
            print('>>',zetzet, 'ada di i =', i, '| k =', k)
    print()


# OUTPUT #
# D:\Git\learn-py\examples>python find-index-list.py
# 1
# 1
#
# bar2
# nilai i = 0 | nilai j = ['foo2']
# nilai k = 0 | nilai m = foo2
# i = 0 k = 0 -> foo2
#
# nilai i = 1 | nilai j = ['bar2']
# nilai k = 0 | nilai m = bar2
# i = 1 k = 0 -> bar2
# >> bar2 ada di i = 1 | k = 0
#
# nilai i = 2 | nilai j = ['baz2']
# nilai k = 0 | nilai m = baz2
# i = 2 k = 0 -> baz2
#
#
# D:\Git\learn-py\examples>
