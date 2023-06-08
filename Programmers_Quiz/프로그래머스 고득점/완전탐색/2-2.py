# 카펫

def solution(brown, yellow):
    x = 0
    y = 0
    for i in range(1,2000001):
        if yellow % i == 0:
            x = i
            y = yellow // i
            if ((x+2) * 2) + (y * 2) == brown:
                return [y+2,x+2]





solution(24,24)