from math import *
import sys

rows = 0
cols = 0
str = raw_input()
area = len(str)
min_area = 10**10
min_columns = int(floor(sqrt(area)))
max_rows = int(ceil(sqrt(area)))
for i in range (1, max_rows+1):
    for j in range(min_columns, max_rows+1):
        if i * j < min_area and i*j >= area and j>=i:
            min_area = i*j
            rows = i
            cols = j
# i - number of rows(height)
# j - numbers of cols(width)
for a in range (cols):
    for b in range(rows):
        if b * cols + a < area:
            sys.stdout.write(str[b*cols+a])
    sys.stdout.write(" ")
sys.stdout.flush()
print
        
    