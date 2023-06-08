# 3진법 뒤집기

def solution(n):
    rev_base = ''
    answer = 0
    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)
    
    N = rev_base[::-1]
    for i in range(len(rev_base)):
        if N[i] != '0':
            answer += int(N[i]) * (3 ** i)
        
    return answer


solution(45)
