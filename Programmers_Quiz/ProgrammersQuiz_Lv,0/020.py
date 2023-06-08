# 최댓값 만들기 (1)


def solution(numbers):
    numbers.sort()
    numbers.reverse()
    return numbers[0] * numbers[1]