# 피보나치 수

def solution(n):
    list1 = [0,1]
    for i in range(2,100001):
        list1.append(list1[i-2]+list1[i-1])
    return list1[n] % 1234567






solution(3)