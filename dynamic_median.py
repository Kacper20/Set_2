from collections import Counter
from math import *
def median(a,x): # a to informacje dot. dzialan, x to liczby. 
    min_set = Counter()
    max_set = Counter()
#IN PROGRESS>>>>>
    for i in range(len(x)):
        if (a[i] == 'a'): # dodajemy
            if len(min_set) != 0 and x[i] > max(min_set):
                max_set.insert(x[i])
            if len(max_set) != 0 and x[i] <= min(max_set):
                min_set.insert(x[i])
            if len(min_set) == 0 and len(max_set) == 0:
                min_set.insert(x[i])
            if len(min_set) == 0 and len(mex_set) != 0:
            
            if len(max_set) == 0 and len(min_set) != 0    
            if abs(len(max_set) - len(min_set)) == 2:
                if len(max_set) > len(min_set):
                    val = max_set.remove(min(max_set))
                    min_set.insert(val)
                else:
                    val = min_set.remove(max(min_set))
                    max_set.insert(val)
            # jesli sa takie same po dodaniu
            if len(max_set) == len(min_set):
                print float((min(max_set) + max(min_set))) / 2
            if len(max_set) > len(min_set):
                print min(max_set)
            if len(min_set) > len(max_set):
                print max(min_set)
        if (a[i] == 'r'): # usuwamy
            if len(min_set) == 0 and len(max_set) == 0:
                print 'Wrong'
            elif x[i] in min_set: # jesli istnieje - usuwamy element.
                min_set.remove(x[i])
                #jesli teraz brak balansu(2)
                if abs(len((max_set)-len(min_set))) == 2:
                    val max_set.remove(x[i])
                    min_set.insert(x[i])
                    print min(max_set)
            elif x[i] in max_set:
                max_set.remove(x[i])
                if abs(len((max_set) - len(min_set))) == 2:
                    min_set.remove(x[i])
                    max_set.insert(x[i])
                    print max(min_set)
            if len(max_set) == 0 and len(min_set) == 0:
                print 'Wrong'
            if len(max_set) == len(min_set):
                print (max(min_set) + min(max_set)) /2
            if len(max_set) > len(min_set):
                print min(max_set)
            if len(min_set) > len(max_set):
                print max(min_set)
N = input()
s = []
x = []
for i in range(0, N):
    tmp = raw_input().strip().split(' ')
    s.append(tmp[0])
    x.append(int(tmp[1]))
    
median(s,x)
