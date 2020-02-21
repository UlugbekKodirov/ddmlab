#!/usr/bin/env python3
"""mapper.py"""

import sys
import math
import random
import time

def prime(num):
    """
    Return True if num is a prime number.
    Else return False.
    """
    # cater for 2 and 3 separately
    # if (num == 2) or (num == 3):
    #        return True
    # cater for even numbers, 1 and 0
    # if (num < 2) or (num % 2 == 0):
    #        return False
    # cater for odd numbers below 9,
    # i.e. 7, 5 and 3
    # if (num < 9):
    #        return True
    # cater for all multiples of 3
    # if (num % 3 == 0):
    #        return False

    # take square-root as r
    # root = int(num**0.5)
    # factor = 5
    # while (factor <= root):
    # cater for multiples of 5+6i,
    # i = {0, 1, ..., sqrt(n)}
    #        if (num % factor == 0):
    #                return False
    # cater for multiples of 7+6i
    #        if (num % (factor + 2) == 0):
    #                return False
    #        factor +=6

    # return True

    # if num <= 1:
    #    return False
    # if num == 2:
    #    return True
    # if num > 2 and num % 2 == 0:
    #    return False

    # max_div = math.floor(math.sqrt(num))
    # for i in range(3, 1 + max_div, 2):
    #    print(1)
    #    if num % i == 0:
    #        return False
    # return True

    # if num == 2:
    #   return True
    # if not num & 1:
    #    return False
    # return pow(2, num-1, num) == 1

    #fermat
    if (num > 1):
        for time in range(3):
            randomNumber = random.randint(2, num)-1
            if (pow(randomNumber, num-1, num) != 1):
                return False
        return True
    else:
        return False


for line in sys.stdin:
    line = line.strip()
    num = int(line)
    if prime(num):
        print(num)
