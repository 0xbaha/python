# How do I count unique values inside an array in Python?
# https://stackoverflow.com/questions/12282232/how-do-i-count-unique-values-inside-an-array-in-python#12282286

list_values = [1, 1, 1, 1, 0, 1, 0, 0, 1, 0]
unique_values = len(set(list_values))
print('unique_values =',unique_values)

# OUTPUT #
# D:\Git\learn-py\examples>python unique-value-list.py
# unique_values = 2
#
# D:\Git\learn-py\examples>
