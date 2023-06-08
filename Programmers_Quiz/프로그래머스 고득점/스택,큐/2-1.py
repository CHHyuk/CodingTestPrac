# 올바른 괄호

def solution(s):
    stack = []
    for i in range(len(s)):
        if len(stack) == 0:
            if s[i] == ')':
                return False
            else:
                stack.append(s[i])
        else:
            if s[i] == ')':
                stack.pop()
            else:
                stack.append(s[i])
    if len(stack) == 0:
        return True
    else:
        return False





solution("()()")