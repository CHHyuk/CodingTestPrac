# 올바른 괄호

def solution(s):
    check = 0
    for i in s:
        if i == '(':
            check += 1
        else:
            check -= 1
            if check < 0:
                return False
    if check == 0:
        return True
    elif check != 0:
        return False





solution("(())()")