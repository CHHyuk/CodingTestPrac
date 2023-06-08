# 핸드폰 번호 가리기

def solution(phone_number):
    answer = ''
    a = len(phone_number)
    for i in range(0,a-4):
        answer = answer + '*'
    for i in range(a-4,a):
        answer = answer + phone_number[i]
    return answer