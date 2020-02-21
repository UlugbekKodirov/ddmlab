#!/usr/bin/env python3

"""USAGE: spark-submit --master spark://group4m1.dyn.mwn.de:7077 --executor-memory 6g --executor-cores 4 k-mers.py --kmers 3 --input test.fasta --output kmers-3-customfunc"""

import argparse
import sys
from operator import add
from pyspark import SparkContext, SparkConf

parser = argparse.ArgumentParser()
# required
parser.add_argument("--kmers", help="how many kmers we want", required=True)
parser.add_argument("--input", help="input file that is under /user/hadoop/protein in HDFS", required=True)
# optional
parser.add_argument("--output", help="output dir that will be under /user/hadoop/protein_output in HDFS")
parser.add_argument("--customfunc", dest='customfunc', action='store_true')

def slicing_ngram_generator(seq, k):
    """SLICING (generator) -> SET"""
    for i in range(len(seq)-k+1):
        yield seq[i:i+k]

def get_args(args):
    if args.input:
        input_file = args.input
    if args.kmers:
        kmers_n = int(args.kmers)
    # used function by default
    used_func = slicing_ngram_generator
    #if args.customfunc:
    #    used_func = customfuncx
    if args.output:
        output_dir = args.output
    else:
        if input_file == 'test.fasta':
            processed_file = 'test-data-small'
        elif input_file == 'test_10000000.fasta':
            processed_file = 'test-data-big'
        else:
            processed_file = 'full-data'
        output_dir = 'kmers-{}_{}_{}'.format(kmers_n, used_func.__name__, processed_file)
    return input_file, output_dir, kmers_n, used_func

ARGS = parser.parse_args()
INPUT_FILE, OUTPUT_DIR, KMERS_N, USED_FUNC = get_args(ARGS)
APP_NAME = OUTPUT_DIR

sc = SparkContext(appName=APP_NAME)
kmers = sc.textFile("hdfs:///user/hadoop/protein/{}".format(INPUT_FILE)).flatMap(lambda seq: set(USED_FUNC(seq, KMERS_N)))
kmers = kmers.map(lambda kmer: (kmer, 1)).reduceByKey(add)
kmers.repartition(1).saveAsTextFile("hdfs:///user/hadoop/protein_output/{}".format(OUTPUT_DIR))
