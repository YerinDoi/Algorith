data = input()
result = []
value = 0

for x in data:
  if x.isalpha():        # isalpha 메소드 처음 봄
    result.append(x)
  else:
    value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 알파벳 뒤에 숫자 삽입
result.append(str(value))

# 리스트 result의 요소들을 빈 문자열 ''을 구분자로 사용하여 하나의 문자열로 결합
print(''.join(result))