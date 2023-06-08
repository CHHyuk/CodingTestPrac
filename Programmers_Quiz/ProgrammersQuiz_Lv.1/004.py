# 자릿수 더하기

def solution(n):
    answer = 0
    a = str(n)
    for i in a:
        answer = answer + int(i)
    return answer