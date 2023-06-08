# 실패율

def solution(N, stages):
    People = len(stages)
    fail = {}
    for i in range(1, N + 1):
        if People != 0:
            fail[i] = stages.count(i) / People
            People -= stages.count(i)
        else:
            fail[i] = 0

    return sorted(fail, key=lambda i: fail[i], reverse=True)



solution(5, [2, 1, 2, 6, 2, 4, 3, 3])