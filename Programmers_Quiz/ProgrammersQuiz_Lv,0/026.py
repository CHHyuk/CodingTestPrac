# 배열 원소의 길이

def solution(strlist):
    result = [len(strlist[i]) for i in range(len(strlist))]
    return result