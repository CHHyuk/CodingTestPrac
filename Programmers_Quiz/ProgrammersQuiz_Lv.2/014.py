# 예상 대진표

def solution(n,a,b):
    round = 1
    
    while n != 1:
        if a % 2 != 0:
            a += 1
        if b % 2 != 0:
            b += 1
        if a // 2 == b // 2:
            return round
        else:
            a /= 2
            b /= 2
            round += 1
        n /= 2






solution(8,4,7)