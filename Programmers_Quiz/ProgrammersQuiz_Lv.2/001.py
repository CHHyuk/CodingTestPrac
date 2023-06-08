# 최댓값과 최솟값

def solution(s):
    list = s.split()
    int_list = [int(i) for i in list]
    int_list.sort()
    a = int_list[0]
    b = int_list[len(int_list)-1]
    answer = str(a) + ' ' + str(b)
    return answer