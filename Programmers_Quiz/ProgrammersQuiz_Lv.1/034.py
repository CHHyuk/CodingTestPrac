# 시저 암호

def solution(s, n):
    answer = ''
    for i in s:
        if i == " ":
            answer += " "
        else:
            k = chr(ord(i) + n)
            if k.isupper() != i.isupper() or not k.isalpha():
                k = chr(ord(k) - 26)
            answer += k
    return answer


solution("AB",1)