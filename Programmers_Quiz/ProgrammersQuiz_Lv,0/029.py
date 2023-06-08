# 가장 큰 수 찾기


def solution(array):
    result = [max(array), array.index(max(array))]
    return result