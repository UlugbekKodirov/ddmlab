#!/usr/bin/env python3
 
import sys
from pyspark import SparkContext
 
def is_prime(n):
    if (n == 2) or (n == 3):
        return True
    if (n < 2) or (n % 2 == 0):
        return False
    if (n < 9):
        return True
    if (n % 3 == 0):
        return False
    r = int(n**0.5)
    f = 5
 
    while (f <= r):
        if ((n % f) == 0):
            return False
        if (n % (f + 2) == 0):
            return False
        f +=6
    return True

def main():
   sc = SparkContext(appName='SparkPrimes')
   input_file = sc.textFile('hdfs://group4m1.dyn.mwn.de:9000/user/hadoop/numbers/small_numbers.txt')
   counts = input_file.flatMap(lambda line: line.split()).map(lambda prime: is_prime(int(prime))).reduce(lambda a, b: a + b)
   print(counts)
   output = sc.parallelize([counts])
   output.repartition(1).saveAsTextFile('output/prime_output_1000')

if __name__ == "__main__":
    main()

