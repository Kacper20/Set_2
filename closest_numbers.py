n = int(raw_input())
arr = raw_input().split()
arr = [int(x) for x in arr]
arr.sort()
results = []
curr_min = 10**12
for i in range (len(arr)-1):
	if abs(arr[i] - arr[i+1]) <= curr_min:
         curr_min = abs(arr[i] - arr[i+1])
        
        
for i in range(len(arr) - 1):
    if (abs(arr[i] - arr[i+1]) == curr_min):
        results.append(arr[i])
        results.append(arr[i+1])
        
	
for i in results:
    print i,
	