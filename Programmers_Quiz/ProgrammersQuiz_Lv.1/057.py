# 가장 가까운 같은 글자

def solution(s):
    result = [-1]
    for i in range(1, len(s)):
        if s[i] in s[:i]:
            result.append(i - s[:i].rfind(s[i]))
        else:
            result.append(-1)
    return result