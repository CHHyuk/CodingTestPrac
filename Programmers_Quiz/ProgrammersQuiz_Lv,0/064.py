# k의 개수

def solution(i, j, k):
    list1 = list(range(i,j+1))
    list2 = list(map(str,list1))
    A = ''
    B = 0
    C = str(k)
    for i in range(len(list2)):
        A = A + list2[i]
    return A.count(C)


solution(1, 13, 1)