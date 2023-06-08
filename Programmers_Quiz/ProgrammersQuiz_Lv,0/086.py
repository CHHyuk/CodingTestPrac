# 저주의 숫자 3

def solution(n):
    i,j = 0,0
    a=[]
    while j<n:
        i+=1
        if i%3!=0 and '3' not in str(i):
            a.append(i)
            j+=1
    return a[n-1]




solution(40)