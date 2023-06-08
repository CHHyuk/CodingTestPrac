# OX 퀴즈

def solution(quiz):
    check_list = []
    result = []
    for i in range(len(quiz)):
        check_list = quiz[i].split('=')
        if eval(check_list[0]) == int(check_list[1]):
            result.append("O")
        else:
            result.append('X')
    return result

solution(["3 - 4 = -3", "5 + 6 = 11"])