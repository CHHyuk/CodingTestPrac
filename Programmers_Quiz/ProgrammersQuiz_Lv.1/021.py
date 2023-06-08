# 가운데 글자 가져오기

def solution(numbers):
    a = 9
    answer = 0
    while a != 0:
        if a in numbers:
            pass
        else:
            answer += a
        a -= 1
    return answer