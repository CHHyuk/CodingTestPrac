# 이상한 문자 만들기

def solution(s):
    answer = []
    s = s.lower()
    s_list = s.split(' ')
    for i in range(len(s_list)):
        temp = list(s_list[i])
        for j in range(len(temp)):
            if j % 2 != 0:
                temp[j] = temp[j].lower()
            else:
                temp[j] = temp[j].upper()
        temp_str = ''.join(temp)
        answer.append(temp_str)
    
    return ' '.join(answer)


solution("  tRy hello  WORLD    " )