# 체육복

def solution(n, lost, reverse):
    answer = n - len(lost)
    for i in range(len(reverse)):
        if reverse[i]+ 1 in lost or reverse[i] - 1 in lost:
            reverse[i] = 0
            answer += 1
    if answer > n:
        answer = n
    return answer





solution(5,[2,4],[3])