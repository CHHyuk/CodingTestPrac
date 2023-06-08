# 문자열 나누기

def solution(s):
    stack = []
    s_list = list(s)
    result = 0
    alpha_check = ''
    for i in range(len(s_list)):
        if stack == []:
            stack.append(s_list[i])
            alpha_check = s_list[i]
        else:
            stack.append(s_list[i])
        if alpha_check != '':
            if len(stack) / 2 == stack.count(alpha_check):
                stack.clear()
                result += 1
        if i == len(s_list) - 1 and stack != []:
            result += 1
    return result
        
                



solution("aaabbaccccabba")