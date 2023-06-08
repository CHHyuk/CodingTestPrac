# 짝지어 제거하기

def solution(s):
    s_list = list(s)
    if len(s) % 2 != 0:
        return 0
    while True:
        for i in range(1,len(s_list)):
            if s_list[i-1] == s_list[i]:
                s_list[i-1] = '0'
                s_list[i] = '0'
        if '0' not in s_list and s_list != []:
                return 0
        while '0' in s_list:
            s_list.remove('0')
        if s_list == []:
            return 1
        


solution('baabaa')



