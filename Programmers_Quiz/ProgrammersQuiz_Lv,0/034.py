# 문자 반복 출력하기


def solution(my_string, n):
    list1 = list(my_string)
    list2 = [list1[i]*n for i in range(len(list1))]
    result = ''.join(list2)
    return result