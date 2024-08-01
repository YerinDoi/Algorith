# data = input().split()
# N = int(data[0])
# K = int(data[1])

# print(N)
# print(K)

n, k = map(int, input().split())

cnt = 0

while True:
  # target: n을 k로 나눌 수 있는 가장 가까운 값
  # n = 25, k = 3인 경우, (n // k) * k는 (25 // 3) * 3 = 24
  target = (n // k) * k

  # n에서 target까지 1씩 빼야 하므로
  cnt += (n - target)
  n = target
  
  #먼저 나눌 수 있는 가장 가까운 값으로 이동한 후, 나눌 수 없으면 종료
  if n < k:
    break

  cnt += 1
  n //= k

# n이 k보다 작아졌을 때 남은 n을 1로 만들기
# n = 5, k = 7 인 경우, cnt += (5 - 1) -> 4번의 -1 후, n은 1이 됨
cnt += (n-1)
print(cnt)