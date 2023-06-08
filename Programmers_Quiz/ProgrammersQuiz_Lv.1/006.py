# 정수 제곱근 판별

def solution(n):
    if n % n**(1/2) == 0:
        return (n**(1/2) + 1)**2
    else:
        return -1