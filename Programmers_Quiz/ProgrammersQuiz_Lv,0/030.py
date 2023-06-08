# n의 배수 고르기

def solution(n, numlist):
    result = []
    for i in range(len(numlist)):
        if numlist[i] % n == 0:
            result = result + [numlist[i]]
        else:
            continue
    return result