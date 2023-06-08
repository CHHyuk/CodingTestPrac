# 369 게임

def solution(order):
    a = []
    result = 0
    for i in str(order):
        a.append(int(i))

    for i in range(len(a)):
        if a[i] == 0:
            pass
        elif a[i] % 3 == 0:
            result += 1
    
    return result






solution(29423)