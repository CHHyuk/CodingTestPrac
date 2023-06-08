# 카펫

def solution(brown, yellow):
    x = 0
    y = 0
    s = brown + yellow
    for i in range(1,2000001):
        for j in range(1,i+1):
            if i * j == s and (i-2) * (j-2) == yellow:
                x ,y = i, j
                break
        if x != 0 and y != 0:
            break
    return [x,y]
        
                





solution(10,2)