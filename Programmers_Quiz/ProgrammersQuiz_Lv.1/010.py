# 정수 내림차순으로 배치하기

def solution(n):
    a = 0
    list1 = list(map(int,str(n)))
    list1.sort()
    list1.reverse()
    a = ''.join(map(str,list1))
    return int(a)