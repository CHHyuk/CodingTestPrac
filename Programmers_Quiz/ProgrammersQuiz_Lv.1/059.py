# 크기가 작은 부분문자열

def solution(t, p):
    answer_list = []
    answer = 0
    for i in range(0,len(t)-len(p)+1):
        temp = ''
        for j in range(len(p)):
            temp += t[i+j]
        answer_list.append(temp)
    
    for i in range(len(answer_list)):
        if int(answer_list[i]) <= int(p):
            answer += 1
    return answer


solution("3141592","271")