N = int(input())
cnt = 0

array = [500, 100, 50, 10]

for coin in array:
  cnt += N // coin
  N %= coin

print(cnt)