'''
The code has been created to solve the "position indeces are not in ascending order" error message encountered
when launching the decision tree code.
'''

import os

input = open(os.path.abspath("./backup/training_set_top200.txt"), "r")
output = open("sorted_training_set_top200_plus_minus.txt", "w")

a = "-1"
a = int(a)

for line in input:
    split = line.strip("\n").split(" ")
    if len(split) == 0:
        print("Found!")
    label = split[0]
    features = set()
    for i in range(1, len(split)):
        features.add(abs(int(split[i].split(":")[0])))

    write_line = ""
    if abs(int(label)) == 1:
        label = "+1"
    else:
        label = "-1"

    write_line += str(label)
    for position in sorted(list(features)):
        write_line += ' ' + str(position) + ':' + str(1)
    write_line += "\n"
    output.write(write_line)


