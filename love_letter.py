from math import *
for _ in range(input()):
    seq = raw_input()
    length = len(seq)
    changes_ctr = 0
    for i in range (length/2+1):
        if seq[i] != seq[length-i-1] and i <= length-i-1:
            val = abs(ord(seq[i])- ord(seq[length-i-1]))
            changes_ctr += val
    print changes_ctr
        