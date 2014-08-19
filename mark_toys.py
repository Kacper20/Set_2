# Enter your code here. Read input from STDIN. Print output to STDOUT
def max_toys(prices, rupees):
  answer = 0
  i = 0
  prices.sort()
  while prices[i] < rupees and i < len(prices):
      rupees -= prices[i]
      answer += 1
      i += 1
  return answer

if __name__ == '__main__':
  n, k = map(int, raw_input().split())
  prices = map(int, raw_input().split())
  print max_toys(prices, k)
