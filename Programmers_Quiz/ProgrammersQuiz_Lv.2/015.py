# 점프와 순간 이동

def solution(n):
    answer = 0
    while n:
        if n % 2 == 0:
            n /= 2
        else:
            n -= 1
            answer +=1
    return answer
        






solution(5000)