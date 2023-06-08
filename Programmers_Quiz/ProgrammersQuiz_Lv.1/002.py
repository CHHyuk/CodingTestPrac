# 평균 구하기

def solution(arr):
    answer = 0
    for i in range(len(arr)):
        answer = answer + arr[i]
    return answer / len(arr)