# 유한소수 판별하기
import fractions

def solution(a, b):
    x = fractions.Fraction(a,b)
    y = str(x).split('/')
    if len(y) == 1:
        return 1
    deno = int(y[1])
    while True:
        while deno % 2 == 0:
            deno /= 2
        while deno % 5 == 0:
            deno /= 5
        if deno == 1:
            return 1
        else:
            return 2


solution(3500, 500)