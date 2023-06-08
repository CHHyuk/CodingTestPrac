# 문자열 정렬하기(2)

def solution(my_string):
    str = my_string.lower()
    list1 = list(str)
    list1.sort()
    result = ''.join(list1)
    return result

solution("Bcad")