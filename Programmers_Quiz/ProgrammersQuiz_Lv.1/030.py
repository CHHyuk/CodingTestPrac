# 최대공약수와 최소공배수

def solution(n,m):
    answer =[]
    GCD = 0
    LCM = 0
    list1 = [n,m]
    for i in range(1,max(list1)+1):
        if n % i == 0 and m % i == 0:
            GCD = i
    answer.append(GCD)
    for i in range(1,(n*m)+1):
        if i % n == 0 and i % m == 0:
            LCM = i
            answer.append(LCM)
            break
    return answer




solution(3,12)