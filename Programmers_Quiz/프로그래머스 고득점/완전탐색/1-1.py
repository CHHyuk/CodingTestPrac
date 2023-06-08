# 최소직사각형

def solution(sizes):
    X = []
    Y = []
    answer = 0
    for i in range(len(sizes)):
        sizes[i].sort()
        X.append(sizes[i][0])
        Y.append(sizes[i][1])
    answer = max(X) * max(Y)
    return answer
    



solution([[60, 50], [30, 70], [60, 30], [80, 40]])