# 한 번만 등장한 문자


def solution(s):
    dict = {}
    str_list = list(s)
    answer = ''
    for i in str_list:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for key, value in dict.items():
        if value == 1:
            answer = answer + key
    answer = ''.join(sorted(answer))
    return answer


solution('abdc')