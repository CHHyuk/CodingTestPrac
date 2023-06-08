# 숨어있는 숫자의 덧셈(2)

def solution(my_string):
    answer = 0
    temp = 0
    for i in my_string:
        if i.isdigit():
            temp = temp* 10 + int(i)
        else:
            answer += temp
            temp = 0
    print(answer)


solution('aAb1B2cC34oOp')