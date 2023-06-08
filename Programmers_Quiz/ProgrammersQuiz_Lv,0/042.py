# 숨어있는 숫자의 덧셈(1)

def solution(my_string):
    list1 = list(my_string)
    A = ''
    B = 0
    for i in range(len(list1)):
        if list1[i] in ['0','1','2','3','4','5','6','7','8','9']:
            A = A + list1[i]
        else:
            continue
    list2 = list(A)
    list3 = [int(i) for i in list2]
    for i in range(len(list3)):
        B = B + list3[i]
    
    return B

solution('aAb1B2cC34oOp')