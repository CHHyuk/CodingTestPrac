# 인덱스 바꾸기

def solution(my_string, num1, num2):
    list1 = list(my_string)
    A = list1[num1]
    B = list1[num2]
    list1[num1] = B
    list1[num2] = A
    result = ''.join(list1)
    return result    



solution('i love you',3,6)