#!/usr/bin/env python3
import sys
 
counts = dict()  
 
for line in sys.stdin:
	line = line.strip()
 
	word, count = line.split('\t', 1)
 
	count = int(count)
	if(word in counts.keys()):
		counts[word] += + count
	else:
		counts[word] = count
 
# Print words and their counts:
for word in counts.keys():
	print('{}\t{}'.format(word, counts[word]))


