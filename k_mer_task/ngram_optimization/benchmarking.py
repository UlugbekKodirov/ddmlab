"""USAGE: python3 benchmarking_substrings.py --steps 1000000 --kmers 3"""
import argparse
import nltk
import time
from kmers_handlers import slicing_ngram_list, slicing_ngram_generator, slicing_ngram_set, custom_nltk_ngrams_list, custom_nltk_ngrams_generator, custom_nltk_ngrams_set

parser = argparse.ArgumentParser()
parser.add_argument('--steps', required=True)
parser.add_argument('--kmers', required=True)
args = parser.parse_args()

STEPS = int(args.steps)
KMERS_N = int(args.kmers)
SEQUENCE = 'MASNTVSAQGGSNRPVRDFSNIQDVAQFLLFDPIWNEQPGSIVPWKMNREQALAERYPELQTSEPSEDYSGPVESLELLPLEIKLDIMQYLSWEQISWCKHPWLWTRWYKDNVVRVSAITFEDFQREYAFPEKIQEIHFTDTRAEEIKAILETTPNVTRLVIRRIDDMNYNTHGDLGLDDLEFLTHLMVEDACGFTDFWAPSLTHLTIKNLDMHPRWFGPVMDGIKSMQSTLKYLYIFETYGVNKPFVQWCTDNIETFYCTNSYRYENVPRPIYVWVLFQEDEWHGYRVEDNKFHRRYMYSTILHKRDTDWVENNPLKTPAQVEMYKFLLRISQLNRDGTGYESDSDPENEHFDDESFSSGEEDSSDEDDPTWAPDSDDSDWETETEEEPSVAARILEKGKLTITNLMKSLGFKPKPKKIQSIDRYFCSLDSNYNSEDEDFEYDSDSEDDDSDSEDDC'

print('KMER SUBSTRING BENCHMARKING - {}k, {}steps:'.format(KMERS_N, STEPS))

### NLTK.NGRAMS (generator) -> SET ###
start = time.time()
for i in range(STEPS):
    set(nltk.ngrams(SEQUENCE, KMERS_N))
print('\t-nltk.ngrams(generator) -> set: {}'.format(time.time()-start))

### SLICING (list) -> SET ###
start = time.time()
for i in range(STEPS):
    set(slicing_ngram_list(SEQUENCE, KMERS_N))
print('\t-slicing(list) -> set: {}'.format(time.time()-start))

### SLICING (generator) -> SET ###
start = time.time()
for i in range(STEPS):
    set(slicing_ngram_generator(SEQUENCE, KMERS_N))
print('\t-slicing(generator) -> set: {}'.format(time.time()-start))

### SLICING - adding to set ###
start = time.time()
for i in range(STEPS):
    slicing_ngram_set(SEQUENCE, KMERS_N)
print('\t-slicing - adding to set: {}'.format(time.time()-start))

### CUSTOM NLTK.NGRAMS (list) -> SET ###
start = time.time()
for i in range(STEPS):
    set(custom_nltk_ngrams_list(SEQUENCE, KMERS_N))
print('\t-custom nltk(list) -> set: {}'.format(time.time()-start))

### CUSTOM NLTK.NGRAMS (generator) -> SET ###
start = time.time()
for i in range(STEPS):
    set(custom_nltk_ngrams_generator(SEQUENCE, KMERS_N))
print('\t-custom nltk(generator) -> set: {}'.format(time.time()-start))

### CUSTOM NLTK.NGRAMS - adding to set
start = time.time()
for i in range(STEPS):
    custom_nltk_ngrams_set(SEQUENCE, KMERS_N)
print('\t-custom nltk - adding to set: {}'.format(time.time()-start))
