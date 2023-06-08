# 약수 구하기

def solution(n):
    list1 = list(range(1,n+2))
    result =[]
    for i in range(len(list1)):
        if i == 0:
            continue
        elif n % i == 0:
            result = result + [i]
        elif i == n:
            result = result + [i]
        else:
            pass
    return result