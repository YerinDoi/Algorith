array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# 정렬 안된 부분 순회
for i in range(len(array)):
  min_index = i # 정렬 안 된 부분 중 첫번째 원소

  # 정렬 안 된 부분 중 첫번째 원소를 제외한 부분 순회
  for j in range(i + 1, len(array)): 
    if array[min_index] > array[j]: # 값이 가장 작은 인덱스 찾기
      min_index = j

  array[i], array[min_index] = array[min_index], array[i]

print(array)