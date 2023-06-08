# 종이 자르기

def solution(M,N):
    if M == 1 and N == 1:
        return 0
    elif M >= N:
        return (N-1)+(N*(M-1))
    elif M < N:
        return (M-1)+(M*(N-1))




solution(2,5)