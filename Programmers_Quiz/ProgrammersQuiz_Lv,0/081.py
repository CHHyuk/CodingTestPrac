# 직사각형 넓이 구하기

def solution(dots):
    list1 = [dots[i][0] for i in range(0,4)]
    list2 = [dots[i][1] for i in range(0,4)]
    return abs(max(list1) - min(list1)) * abs(max(list2) - min(list2))






solution([[1, 1], [2, 1], [2, 2], [1, 2]])