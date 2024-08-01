# 완전 탐색

# 현재 나이트의 위치 입력 받기
input_data = input()
row = int(input_data[1])
column = ord(input_data[0]) - ord('a') + 1  # 아스키 코드 이용(문자 -> 숫자), ord()의 반환 타입은 int

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (2, -1), (-2, 1), (2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
  # 이동하고자 하는 위치 확인
  next_row = row + step[0]
  next_columns = column + step[1]

  # 해당 우치로 이동 가능하다면 카운트 증가
  if next_row >= 1 and next_row <= 8 and next_columns >= 1 and next_columns <= 8:
    result += 1

print(result)