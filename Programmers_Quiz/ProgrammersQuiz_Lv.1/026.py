# 약수의 개수와 덧셈

def solution(left, right):
    y = 0
    answer = 0
    while left != right + 1:
        for i in range(1,right+1):
            if right % i == 0:
                y += 1
        if y % 2 == 0:
            answer += right
        elif y % 2 != 0:
            answer -= right
        right -= 1
        y = 0
    return answer

solution(13,17)