# 문자열 안에 문자열



def solution(str1, str2):
    answer = 0
    if str2 in str1:
        answer = answer + 1
    else:
        answer = answer + 2
    return answer