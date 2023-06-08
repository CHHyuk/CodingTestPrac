# k진수에서 소수 개수 구하기

def k_change(n,k):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)

    return rev_base[::-1]

def check(p):
    a = 0
    for i in range(2,(p//2)+1):
        if p%i == 0:
            a = 1
            break
    if a == 0:
        return 1
    else:
        return 0

def solution(n,k):
    str =  k_change(n,k)
    answer = 0
    temp = ''
    temp_list = []
    for i in range(len(str)):
        if str[i] == '0':
            if i == 0:
                continue
            elif temp != '':
                temp_list.append(temp)
                temp = ''
        elif str[i] != '0':
            temp = temp + str[i]
            if i == len(str)-1:
                temp_list.append(temp)

    for i in temp_list:
        if i == '1':
            continue
        else:
            answer += check(int(i))

    return answer








solution(437674,3)