# x만큼 간격이 있는 n개의 숫자

def solution(n):
    a = 0
    list1 = list(map(int,str(n)))
    list1.sort()
    list1.reverse()
    a = ''.join(map(str,list1))
    return int(a)