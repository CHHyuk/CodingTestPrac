# 콜라 문제

def solution(a,b,n):
    answer = 0

    while True:
        if n < a:
            break
        given = n // a * a
        taken = n // a * b
        
        extra = n - given
        
        n = extra + taken
        
        answer += taken
    return answer




solution(2,1,20)