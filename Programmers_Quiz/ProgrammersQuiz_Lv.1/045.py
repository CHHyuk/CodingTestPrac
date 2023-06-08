# 소수 찾기

def solution(n):
    check = 0
    answer = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
            if i == 1:
                pass
            elif i % j == 0:
                check += 1
                if i == j and check == 2:
                    answer +=1 
                    check = 0
                elif i == j and check != 2:
                    check = 0
    return answer




solution(10)