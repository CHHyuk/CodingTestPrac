# 예산

def solution(d,budget):
    d.sort()
    answer = 0
    for i in range(len(d)):
        if d[i] <= budget:
            budget -= d[i]
            answer += 1
    return answer




solution([1,3,2,5,4],9)