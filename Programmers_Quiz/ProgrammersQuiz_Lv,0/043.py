# 문자열 정렬하기

def solution(my_string):
    list1 = list(my_string)
    A = ''
    for i in range(len(list1)):
        if list1[i] in ['0','1','2','3','4','5','6','7','8','9']:
            A = A + list1[i]
        else:
            continue
    
    list2 = list(A)
    list3 = [int(i) for i in list2]
    list3.sort()

    return list3

solution("hi12392")