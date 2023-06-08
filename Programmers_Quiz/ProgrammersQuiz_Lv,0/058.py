# 7의 개수

def solution(array):
    list1 = list(map(str,array))
    A = ''
    for i in range(len(list1)):
        A = A + list1[i]
    list2 = list(A)
    print(list2)
    result = list2.count('7')
    return result


solution([7,77,17])