# 팩토리얼

def solution(n):
    list1 = list(range(1,11))
    A = 1
    for i in range(len(list1)):
        A = A * (i+1)
        if A <= n:
            answer = i+1
    return answer





solution(3628800)