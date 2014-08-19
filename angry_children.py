n = int(input())
k = int(input())

candies = [input() for _ in range(0,n)]
candies.sort()
min_diff = 10 ** 10
for i in range (0, n-k+1):
    if candies[k-1+i] - candies[i] < min_diff:
        min_diff = candies[k-1+i] - candies[i]
print min_diff