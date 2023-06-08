# 이진 변환 반복하기

def solution(s):
    count_0 = 0
    count = 1
    count_0 += s.count('0')
    s = s.replace('0','')

    while s != '1':
        s = bin(len(s))[2:]
        count += 1
        count_0 += s.count('0')
        s = s.replace('0','')  
    return [count,count_0]

solution("110010101001")
