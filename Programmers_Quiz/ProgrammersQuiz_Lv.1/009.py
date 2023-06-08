# 하샤드 수

def solution(x):
    a = 0
    list1 = []
    list1 = list(map(int,str(x)))
    for i in range(len(list1)):
        a = a + list1[i]
    if x % a == 0:
        return True
    else:
        return False