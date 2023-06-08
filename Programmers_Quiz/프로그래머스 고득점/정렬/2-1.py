# 가장 큰 수 xxxxxxxxxxxxxxx

from itertools import permutations

def solution(numbers):
    answer = ''
    temp = []
    temp2 = []
    numbers = list(map(str,numbers))
    numbers = sorted(numbers, reverse=True)
    for i in range(9,-1,-1):
        for j in range(len(numbers)):
            if numbers[j][0] == str(i):
                temp.append(numbers[j])
            else:
                break
        if len(temp) != 0:
            temp = list(permutations(temp,len(temp)))
            for k in range(len(temp)):
                temp2.append(sum(temp[k]))
            temp2.sort()
            




solution([3, 30, 34, 5, 9])