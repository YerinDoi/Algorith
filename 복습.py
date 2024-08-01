array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 값을 찾기
        while left <= end and array[left] <= array[pivot]:
            left += 1

        # 피벗보다 작은 값을 찾기
        while right >= start and array[right] >= array[pivot]:
            right -= 1

        # 수정된 부분: 교환 조건을 수정하여 left와 right가 엇갈렸을 때 피벗 교환
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            # 수정된 부분: left와 right의 값을 교환하는 부분의 주석
            array[left], array[right] = array[right], array[left]

    # 피벗이 제자리에 왔으니, 피벗 기준으로 분할하여 정렬
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)

print(array)