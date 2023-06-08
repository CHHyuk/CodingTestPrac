# 두 정수 사이의 합

def solution(a, b):
    answer = 0
    if a == b:
        answer = a
    elif a > b:
        while a != b-1:
            answer += a
            a -= 1
    else:
        while b != a-1:
            answer += b
            b -= 1
    return answer