# 배열의 유사도

def solution(s1, s2):
    result = 0
    for i in range(len(s1)):
        if s1[i] in s2:
            result = result + 1
        else:
            continue
    return result