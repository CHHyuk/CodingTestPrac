# 합성수 찾기

def solution(n):
    a = 0
    result = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
            if i % j == 0:
                a += 1
            if a >= 3:
                result += 1
                a = 0
                break
        a = 0
    return result

solution(10)