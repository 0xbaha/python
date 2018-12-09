# https://medium.com/@urban_institute/using-multiprocessing-to-make-python-code-faster-23ea5ef996ba
import time
import multiprocessing

def basic_func(x):
    if x == 0:
        return 'zero'
    elif x%2 == 0:
        return 'even'
    else:
        return 'odd'

def multiprocessing_func(x):
    y = x*x
    time.sleep(2)
    print('{} squared results in a/an {} number'.format(x, basic_func(y)))

if __name__ == '__main__':

    starttime = time.time()
    pool = multiprocessing.Pool()
    pool.map(multiprocessing_func, range(0,10))
    pool.close()
    print('That took {} seconds'.format(time.time() - starttime))
