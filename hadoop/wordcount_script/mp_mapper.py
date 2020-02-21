# !/usr/bin/env python3
import sys
import multiprocessing as mp

# This is a mapper that uses multiple cores
# take input from STDIN

#    line = line.strip()  # eliminate \n
#    words = line.split(" ")

def init(l):
    global lock
    lock = l

def print_func(line):
    line = line.strip()
    words = line.split(" ")
    for word in words:
        lock.acquire()
        print('{}\t{}'.format(word, 1))
        lock.release()


if __name__=="__main__":

    lines = [line for line in sys.stdin]
    #p = mp.Pool(mp.cpu_count())
    #p.map(print_func, lines)

    l = mp.Lock()
    pool = mp.Pool(initializer=init, initargs=(l,), processes=mp.cpu_count())
    pool.map(print_func, lines)
    pool.close()
    pool.join()
