
        
def computate(dollars, numbers):
    for i in range (len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] + numbers[j] == dollars and (i is not j):
                return (i+1, j+1)
                
                
results = []              
for _ in range (input()):
    dollars = int(raw_input())
    number_of_flavours = raw_input()
    numbers = map(int, raw_input().split())    
    result = list(computate(dollars, numbers))
    result.sort()
    results.append(result)

for result in results:
    for i in result:
        print i,
    print