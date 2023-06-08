# 하샤드 수

def solution(x):
    str_x = str(x)
    check = 0
    for i in str_x:
        check += int(i)
    if x % check == 0:
        return True
    else:
        return False

solution(10)