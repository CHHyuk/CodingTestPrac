# 최댓값 만들기(2)

def solution(numbers):
    numbers.sort()
    if numbers[0] * numbers[1] > numbers[-1] * numbers[-2]:
        result = numbers[0] * numbers[1]
    else:
        result = numbers[-1] * numbers[-2]
    return result






solution([1,2,-3,4,-5])