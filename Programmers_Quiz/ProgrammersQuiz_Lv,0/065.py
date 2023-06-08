# 가까운 수

def solution(array, n):
    array.sort()
    return min(array, key=lambda x:abs(x-n))





solution([3,28,12], 20)