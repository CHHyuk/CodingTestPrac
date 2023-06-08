# 조이스틱 xxxxxxxxxxxxxxxxxxxx
from string import ascii_uppercase
alpha_list = list(ascii_uppercase)


def alpha_check(s):
        if alpha_list.index(s) > 13:
            return 26 - alpha_list.index(s)
        else:
            return alpha_list.index(s)
 

def solution(name):
    result = 0
    for i in range(len(name)):
        if name[i] == 'A':
            pass
        else:
            result += alpha_check(name[i])
        result += 1
    return result - 1

solution("JAN")

