n = int(input())  # 5
# group = int(input().split()) 이거 안 됨 -> 원소마다 적용하려면 map을 사용해야 함, 
# 문자열리스트를 숫자로 변환 못해 타입에러 남
# 정수형 리스트가 아닌 이유는 map 함수가 바로 리스트를 반환하지 않고, 나중에 쓸 수 있는 **맵 객체(map object)**를 반환

data = list(map(int, input().split())) # 2 3 1 2 2 
data.sort() # 공포도 낮은 순으로 정렬

groupN = 0 # 총 그룹 수
cnt = 0 # 현재 포함된 그룹원 수

for i in data:
  count += 1
  if count >= i:
    groupN += 1
    cnt = 0

print(groupN)