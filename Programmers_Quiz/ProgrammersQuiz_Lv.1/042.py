# 2016년

def solution(a, b):
    answer = 0
    week = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    month = [31,29,31,30,31,30,31,31,30,31,30,31]

    for i in range(a-1):
        answer += month[i]
    answer += b-1
    answer = answer%7
    return week[answer]




solution(5,24)