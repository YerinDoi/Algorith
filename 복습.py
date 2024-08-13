def dfs(x, y):
  if x < 0 or y < 0 or x >= n or y >= m:  # 0부터 시작하기 때문에 x >= n, y >= m 주의
    return False
  
  if graph[x][y] == 0:
    graph[x][y] = 1

    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)

    return True
  return False
    

input_data = list(map(int, input().split()))
n = input_data[0]
m = input_data[1]

graph = []
for i in range(n):
  graph.append(list(map(int, input())))

result = 0
for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      result += 1

print(result)