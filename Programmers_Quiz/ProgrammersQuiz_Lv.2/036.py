# 숫자 카드 나누기 xxxxxxxxxxxx
def divide(array, n):
    check = 0
    for i in range(len(array)):
        if array[i] % n == 0:
            check += 1
        if check == len(array):
            return 2
        if check == 0:
            return 1
    return 0

def solution(arrayA, arrayB):
    result = []
    max_num = [max(arrayA),max(arrayB)]
    for i in range(int(max(max_num) // 2)+1,1,-1):
        if divide(arrayA, i) == 2 and divide(arrayB, i) == 1:
            result.append(i)
        if divide(arrayA, i) == 1 and divide(arrayB, i) == 2:
            result.append(i)
        if result != []:
            break
    if result == []:
        return 0
    else:
        return max(result)
    
    


solution([10, 20],[5, 17])