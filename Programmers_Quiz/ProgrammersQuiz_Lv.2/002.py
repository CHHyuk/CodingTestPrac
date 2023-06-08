# JadenCase 문자열 만들기

def solution(s):
    a=list(s)
    b=s.lower() 
    c=list(b) 
    c[0]=a[0].upper() 
    for i in range(len(s)-1):
        if a[i]==' ':
            c[i+1]=a[i+1].upper()
    answer=''.join(c)
    print(answer)
    return answer




solution("3people unFollowed me")