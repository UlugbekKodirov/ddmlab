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

POSITIVE_LABEL_IDS=set([line.strip() for line in open('/mnt/transmembrane_ids.txt')])

def slicing_ngram_generator(seq, k):
    """SLICING (generator) -> SET"""
    seq_id, seq_secondpart = seq.split(" ")
    if seq_id in POSITIVE_LABEL_IDS:
        for i in range(len(seq_secondpart)-k+1):
            yield seq_secondpart[i:i+k], 1
    else:
         for i in range(len(seq_secondpart)-k+1):
            yield seq_secondpart[i:i+k], 0
    
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
        output_dir = 'kmers-{}_{}_{}'.format(kmers_n, used_func.__name__, input_file)
    return input_file, output_dir, kmers_n, used_func

ARGS = parser.parse_args()
INPUT_FILE, OUTPUT_DIR, KMERS_N, USED_FUNC = get_args(ARGS)
APP_NAME = OUTPUT_DIR

sc = SparkContext(appName=APP_NAME)
kmers = sc.textFile("hdfs:///user/hadoop/transmembrane/{}".format(INPUT_FILE)).flatMap(lambda seq: USED_FUNC(seq, KMERS_N))
kmers = kmers.map(lambda kmer: (kmer, 1)).reduceByKey(add)
kmers.saveAsTextFile("hdfs:///user/hadoop/transmembrane_output/{}_positive_negative".format(OUTPUT_DIR))

