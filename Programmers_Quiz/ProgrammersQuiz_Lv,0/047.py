# 대문자와 소문자

def solution(my_string):
    list1 = list(my_string)
    for i in range(len(list1)):
        if list1[i].isupper() == True:
            list1[i] = list1[i].lower()
        elif list1[i].isupper() == False:
            list1[i] = list1[i].upper()
    result = ''.join(list1)
    return result




solution('cccCCC')