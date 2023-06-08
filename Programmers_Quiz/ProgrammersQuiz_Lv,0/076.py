# 구슬을 나누는 경우의 수

def solution(balls, share):
    temp_b = balls
    temp_s = share
    while temp_s != 1:
        if temp_s > 1 :
            temp_b -= 1
            balls = balls * temp_b
            temp_s -= 1
            share = share * temp_s
        else:
            pass
    
    answer = balls / share
    return int(answer)
            







solution(5,3)