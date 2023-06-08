# 삼각형의 완성조건(1)

def solution(sides):
    answer = 1
    sides.sort()
    if sides[2] < sides[1] + sides[0]:
        answer = 1
    else:
        answer = 2
    return answer