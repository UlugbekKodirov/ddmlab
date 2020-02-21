#!/usr/bin/env python3

"""
!!! The code works on the file where each sequence is in the following format:

>UnirefID
asdfasdsfasfasdfasdfasdsfasfsdfassdfassfadsf\n
asdfasdsfasfasdfasdfasdsfasfsdfassdfassfadsf\n
asdfasdsfasfasdfasdfasdsfasfsdfassdfassfadsf\n
asdfasdsfasfasdfasdfasdsfasfsdfassdfassfadsf\n
...

That is, the code works on sequences, where the remainder of the UnirefID's line is removed.


USAGE: python3 change.py input_file output_file
Note: It adds the symbol ">" between Uniref ids and protein sequences. Afterwards the symbol in the obtained sequences
can be replaced by newline delimiter by launching the terminal command:
cat input_file (outputted by change.py) | tr -d "\n" | tr ">" "\n" > target_file
Then you can run k-mer-presence.py on that data.
"""

import glob
import sys

OUTPUT_FILE = open(sys.argv[2], 'w')
INPUT_FILE = open(sys.argv[1], 'r')

output = ""
for line in INPUT_FILE:

    # print processed word to output file
    if line[0] == '>':
        OUTPUT_FILE.write(output)
        OUTPUT_FILE.write(line+'>')
        output = ""
    else:
        output += line

INPUT_FILE.close()
OUTPUT_FILE.close()
