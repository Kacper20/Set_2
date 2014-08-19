N, K = raw_input().split()
diff = int(K)
numbers = map(int, raw_input().split())
# tworzymy set z wszystkich liczb
#Dla kazdego elementu w secie, sprawdzamy ile istnieje elementow wiekszych o
#K od niego. To zalatwi to, ze sprawdzimy kazda pare jeden raz(dwa razy gdybysmy sprawdzali rowniez mniejsze).
counter = 0
s = set(numbers)
for num in s:
    if num+diff in s:
        counter +=1
print counter
    