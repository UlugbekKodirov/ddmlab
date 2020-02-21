#!/usr/bin/env python3

"""USAGE: python3 generate_training_set.py positive_ids_file refined_raw_data_file
Note: It will output two files named positive_data.txt and negative_data.txt to the same folder where it is located."""

import sys

POSITIVE_IDS = open(sys.argv[1], 'r')  # ids of positive data samples
#POSITIVE_IDS = open('id_list.txt', 'r')  # ids of positive data samples
RAW_DATA = open(sys.argv[2], 'r')  # data samples with ids
#RAW_DATA = open('test.txt', 'r')  # data samples with ids

POSITIVE_SET = open('positive_data.txt', 'w')  # positive sequences from RAW_DATA
NEGATIVE_SET = open('negative_data.txt', 'w')  # negative sequences from RAW_DATA

positive_ids = set([id for id in POSITIVE_IDS.read().splitlines()])
output = ""

is_positive = False
for line in RAW_DATA.read().splitlines():
    if (line[:2] == "Un"):
        if (line in positive_ids):
            is_positive = True
        else:
            is_positive = False
    else:
        if is_positive:
            POSITIVE_SET.write(line+'\n')
        else:
            NEGATIVE_SET.write(line+'\n')

RAW_DATA.close()
POSITIVE_IDS.close()
POSITIVE_SET.close()
NEGATIVE_SET.close()

