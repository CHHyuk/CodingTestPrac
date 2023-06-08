# 컨트롤 제트

def solution(s):
    result = 0
    list1 = list(s.split())
    for i in range(len(list1)):
        if list1[i] == 'Z':
            list1[i-1] = '0'
    for i in range(len(list1)):
        if list1[i] != 'Z':
            result += int(list1[i])
    return result



solution("-1 -2 -3 Z")