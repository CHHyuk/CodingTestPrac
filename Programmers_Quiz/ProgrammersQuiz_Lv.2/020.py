# 튜플

def solution(s):
    temp = {}
    result = []
    str_list = s.split(',')
    for i in range(len(str_list)):
        if '{' in str_list[i]:
            str_list[i] = str_list[i].split('{')
            str_list[i] = ''.join(str_list[i])
        if '}' in str_list[i]:
            str_list[i] = str_list[i].split('}')
            str_list[i] = ''.join(str_list[i])
    for i in range(len(str_list)):
        if str_list[i] not in temp:
            temp[str_list[i]] = 1
        else:
            temp[str_list[i]] += 1
    temp = sorted(temp.items(),reverse=True,key=lambda item:item[1])
    for key,value in temp:
        result.append(int(key))
    return result            
    




solution("{{20,111},{111}}")