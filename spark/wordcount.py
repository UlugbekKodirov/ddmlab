#!/usr/bin/env python3

import sys
from operator import add
from pyspark import SparkContext


def main():
    sc = SparkContext(appName='SparkWordcount')
    #input_file = sc.textFile('hdfs://group4m1.dyn.mwn.de:9000/user/hadoop/wiki_chunk/wiki_chunk.txt')
    input_file = sc.textFile('hdfs://group4m1.dyn.mwn.de:9000/user/hadoop/clean_wiki/CLEAN_WIKI')
    counts = input_file.flatMap(lambda line: line.split(' ')) \
                       .map(lambda line: (line, 1)) \
                       .reduceByKey(add)
    counts.repartition(1).saveAsTextFile('output/wordcount_spark_output')

if __name__ == "__main__":
    main()

