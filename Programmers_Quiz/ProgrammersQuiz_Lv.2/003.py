# 최솟값 만들기

def solution(A,B):
    A.sort()
    B.sort()
    B.reverse()
    answer = 0
    for i in range(len(A)):
        answer += (A[i]*B[i])
    return answer




solution([1, 4, 2],[5, 4, 4])