# 로또의 최고 순위와 최저 순위

def solution(lottos,win_nums):
    temp = 0
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            temp += 1
    if temp == 0 and lottos.count(0) == 0:
        return [6,6]
    elif temp == 0:
        return [7-lottos.count(0)-temp,6]
    else:
        return [7-lottos.count(0)-temp,7-temp]





solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19])