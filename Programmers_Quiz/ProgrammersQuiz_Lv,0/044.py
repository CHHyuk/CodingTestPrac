#모음 제거

def solution(my_string):
    list1 = list(my_string)
    for i in range(len(list1)):
        if 'a' in list1:
            list1.remove('a')
        elif 'e' in list1:
            list1.remove('e')
        elif 'i' in list1:
            list1.remove('i')
        elif 'o' in list1:
            list1.remove('o')
        elif 'u' in list1:
            list1.remove('u')
    result = ''.join(list1)
    return result

solution("nice to meet you")