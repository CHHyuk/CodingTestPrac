# n^2 배열 자르기

def solution(n, left, right):
    array = []
    result = []
    temp_left = left - ((left//n) * n)
    temp_right = right - ((left//n) * n)
    for _ in range(left//n,(right//n)+1):
        for i in range(1,n+1):
            if left//n >= i:
                array.append(int((left//n)+1))
            else:
                array.append(i)
        left += n
    for j in range(temp_left,temp_right + 1):
        result.append(array[j])
    return result
        



solution(4,7,14)