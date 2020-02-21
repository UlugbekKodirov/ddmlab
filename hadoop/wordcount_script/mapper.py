#!/usr/bin/env python3
import sys
 
 #take input from STDIN
for line in sys.stdin:
    line = line.strip()  # eliminate \n
    words = line.split()	

    for word in words:
        print('{}\t{}'.format(word, 1))
