# 중앙값 구하기


def solution(array):
    array.sort()
    return array[int((len(array)-1) / 2)]