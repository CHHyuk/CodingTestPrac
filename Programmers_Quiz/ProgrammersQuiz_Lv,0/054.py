# 숫자 찾기

def solution(num,k):
    string = str(num)
    kk = str(k)
    result = 0
    list1 = list(string)
    
    if kk in list1:
        result = list1.index(kk) + 1
    else:
        result = -1

    return result




solution(232443,4)