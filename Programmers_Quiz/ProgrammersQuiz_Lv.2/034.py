# 점 찍기 xxxxxxxxxxxxxxx

def solution(k, d):
    result = 0
    for i in range(0, d+1, k):
        for j in range(0, d+1, k):
            if i**2 + j**2 <= d**2:
                result += 1
    return result

solution(2, 4)