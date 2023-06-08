# 다항식 더하기

def solution(polynomial):
    array = list(polynomial.split())
    a = 0
    b = 0
    for i in range(len(array)):
        if 'x' in array[i]:
            if array[i] == 'x': 
                a += 1
            else:
                array[i] = array[i].replace('x','')
                a += int(array[i])
        elif array[i].isdigit() and 'x' not in array[i]:
            b += int(array[i])
    if a == 0 and b == 0:
        answer = 0
    elif a != 0 and b == 0:
        if a == 1:
            answer = 'x'
        else:
            answer = str(a)+'x'
    elif a == 0 and b != 0:
        answer = str(b)
    else:
        if a == 1:
            answer = 'x + '+str(b)
        else:
            answer = str(a)+'x + '+str(b)
    return answer

solution("33x + 7 + x")