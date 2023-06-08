# 타겟 넘버

def solution(numbers, target):
    answer = 0
    pm = []
    temp = 0
    a = 2 ** len(numbers) -1
    for x in range(0,a+1):
        pm.append(bin(x)[2:].zfill(len(numbers)))
    
    for i in range(len(pm)):
        for j in range(len(numbers)):
            if pm[i][j] == '0':
                temp -= numbers[j]
            elif pm[i][j] == '1':
                temp += numbers[j]
        if temp == target:
            answer += 1
        temp = 0
    
    return answer


solution([4, 1, 2, 1],4)