'''
Sortujemy liste, poniewaz chcemy najpierw kupic najdrozsze kwiatki, by pozniej
kolejne, kupowane juz za cene z mnoznikiem zaleznym od liczby zakupionych kwiatkow kosztowaly mniej
'''




# code snippet illustrating input/output methods 
N, K = raw_input().split()
N = int(N)
K = int(K)
numbers = raw_input().split()
C = map(int, numbers)
C.sort(reverse=True)
result = 0
count = 0
for i in range (N): #kazdy z kwiatkow musimy kupic. 
	result += C[i] * (count / K + 1) 
	count += 1
print result
