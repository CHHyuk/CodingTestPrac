# 소인수분해

def solution(n):
    answer = []
    d = 2

    while d <= n:
        if n % d == 0:
            n = n / d
            if d not in answer:
                answer.append(d)
        else:
            d = d + 1
    return answer



solution(12)