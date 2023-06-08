# 분수의 덧셈

import fractions
def solution(denum1, num1, denum2, num2):
    answer = fractions.Fraction(denum1,num1) + fractions.Fraction(denum2,num2)
    if '/' in str(answer):
        answer = str(answer).split('/')
        return [int(answer[0]),int(answer[1])]
    else:
        answer = str(answer)
        return [int(answer),1]


solution(9, 9, 9, 9)