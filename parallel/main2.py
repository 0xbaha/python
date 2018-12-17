import multiprocessing

def do_something(number):
    return number ** 2

def do_something(number, another_number):
    return number ** 2 + another_number ** 2

number_of_workers = 4

###############################################################################
array_of_numbers = [x for x in range(0, 100000000000)]
# with Pool(number_of_workers) as p:
#     print(p.map(do_something, array_of_numbers))
with Pool(number_of_workers) as p:
    print(p.imap(do_something, array_of_numbers))
###############################################################################
# array_of_number_tuple = [(x, x + 1) for x in range(0, 100000000000)]
#
# with Pool(number_of_workers) as p:
#     print(p.starmap(do_something, array_of_number_tuple))
