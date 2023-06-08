# 배열 두배 만들기

def solution(numbers):
    list1 = [numbers[i] * 2 for i in range(len(numbers))]
    return list1