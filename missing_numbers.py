from collections import Counter
a_size = int(raw_input())
num_a = map(int, raw_input().split())
b_size = int(raw_input())
num_b = map(int, raw_input().split())
cnt_more = Counter()
result = []
if b_size > a_size:
    for num in num_b:
        cnt_more[num]+=1
    for l in num_a:
        cnt_more[l] -=1
    for num in cnt_more:
        result += [num] * cnt_more[num]
    # zostaly nam odpowiednie wyrazy.
if b_size < a_size:
    for num in num_a:
        cnt_more[num] += 1
    for l in num_b:
        cnt_more[l] -=1
    for num in cnt_more:
        result += [num] * cnt_more[num]
result = set(result)
result = list(result)
result.sort()
for num in result:
    print num,