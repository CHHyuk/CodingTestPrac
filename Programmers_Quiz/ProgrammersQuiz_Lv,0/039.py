# 특정 문자 제거하기

def solution(my_string, letter):
    list1 = list(my_string)
    list2 = list(letter)
    for i in range(len(list1)):
        if letter in list1:
            list1.remove(letter)
        else:
            pass
    result = ''.join(list1)
    return result

print(solution('abcdea','a'))