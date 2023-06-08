# 암호 해독

def solution(cipher, code):
    list1 = list(cipher)
    result = ''
    for i in range(len(list1)):
        if (i+1) % code == 0:
            result = result + list1[i]
    
    return result





solution("dfjardstddetckdaccccdegk"	,4)