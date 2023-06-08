# 다음 큰 숫자

def solution(n):
    result = 0
    for i in range(n+1,1000001):
        if str(bin(n)[2:]).count('1') == str(bin(i)[2:]).count('1'):
            result += i
            break
    return result



solution(78)