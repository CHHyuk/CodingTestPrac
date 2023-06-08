# 숫자의 표현

def solution(n):
    count = 0
    for i in range(1,(n//2)+ 2):
        for j in range(i+1, (n//2) + 2):
            if (i+j)/2 * (j-i+1) > n:
                break
            elif (i+j)/2 * (j-i+1) == n:
                count += 1
    return count + 1
        




solution(15)