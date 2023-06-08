# 순서쌍의 갯수

def solution(n):
    list1 = list(range(1,n+2))
    result = 0
    for i in range(len(list1)):
        if i == 0:
            continue
        elif n % i == 0:
            result = result + 1
        else:
            pass
    return result
