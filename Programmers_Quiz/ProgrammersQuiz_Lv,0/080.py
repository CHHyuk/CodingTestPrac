# 삼각형의 완성 조건

def solution(sides):
    sides.sort()

    return (sides[1] + sides[0] - 1) -  (sides[1] - sides[0] + 1) + 1



solution([3,6])