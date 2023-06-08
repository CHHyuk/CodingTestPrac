# 제일 작은 수 제거하기

def solution(arr):
    smallest = arr[0]
    for i in arr:
        if i < smallest:
            smallest = i
    arr.remove(smallest)
    if arr == []:
        return [-1]
    else:
        return arr