# 공 던지기

def solution(numbers, k):
    answer = 0
    for i in range(1,100):
        if (k - 1) * 2 >= len(numbers):
            numbers = numbers + numbers
    return numbers[int((k-1)*2)]