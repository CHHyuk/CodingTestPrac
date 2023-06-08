# 특이한 정렬

def min(numlist,n):
    min_index = max(numlist)
    for i in range(len(numlist)):
        if abs(min_index - n) >= abs(numlist[i] -n):
            min_index = numlist[i]
    return min_index

def solution(numlist, n):
    array = []
    numlist.sort()
    while len(numlist) != 0:
        min_index = min(numlist,n)
        array.append(min_index)
        numlist.remove(min_index)
    return array




solution([10,9,8,7,6,5,4,3,2,1,11],6)