# 숫자 문자열과 영단어

def solution(s):
    list1 = ['zero','one','two','three','four','five','six','seven','eight','nine']
    answer = ''
    for index,num in enumerate(list1):
        if num in s:
            s = s.replace(num,str(index))
        answer = s
    return int(answer)