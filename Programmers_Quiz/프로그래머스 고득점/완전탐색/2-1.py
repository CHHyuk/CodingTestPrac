# 소수 찾기
from itertools import permutations

def prime_number(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    num_list = list(numbers)
    temp1 = []
    for i in range(2,8):
        temp2 = []
        temp1 = list(permutations(num_list,i))
        for j in range(len(temp1)):
            for k in range(len(temp1[0])):
                temp2.append(temp1[j]) 





solution('17')