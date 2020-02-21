"""
The code should be used over the data, where each sequence is in the following format (k-mer-presence.py file's output):

('UnirefID', 'K-mer1 K-mer2 ... K-merN')
"""


# !usr/bin/env python3
import sys
from ast import literal_eval

input_file = open(sys.argv[1], "r")  # A file where there the sequences are in the above-mentioned format
positive_ids = open(sys.argv[2], "r")  # A list of positive uniref ids

label_file = open("labels.txt", "w")

pos_labels = set([line for line in positive_ids.read().splitlines()])

lines = [line for line in input_file.read().splitlines()]
for line in lines:
    l = literal_eval(line)
    kmers = l[1].split(" ")
    if l[0] in pos_labels:
        label_file.write(str(1))
    else:
        label_file.write(str(0))
    presence_position = []
    for kmer in kmers:
        presence_pos = 625 * (ord(kmer[0]) - ord('A')) + 25 * (ord(kmer[1]) - ord('A')) + (ord(kmer[2]) - ord('A'))
        presence_position.append(presence_pos)
    presence_position.sort()
    for pos in presence_position:
        if l[0] in pos_labels:
            label_file.write(' ' +str(pos) + ':' + str(1))
        else:
            label_file.write(' ' +str(pos) + ':' + str(1))
    label_file.write('\n')

input_file.close()
positive_ids.close()
label_file.close()


