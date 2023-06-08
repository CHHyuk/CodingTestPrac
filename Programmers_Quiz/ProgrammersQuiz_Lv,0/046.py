# 가위 바위 보

def solution(rsp):
    list1 = list(rsp)
    for i in range(len(list1)):
        if list1[i] == '2':
            list1[i] = '0'
        elif list1[i] == '0':
            list1[i] = '5'
        elif list1[i] == '5':
            list1[i] = '2'
    
    result = ''.join(list1)
    return result

solution('205')