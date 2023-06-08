# 부족한 금액 계산하기

def solution(price, money, count):
    fee = 0
    for i in range(1,count+1):
        fee += price * i
    if fee - money >= 0:
        return fee - money
    else:
        return 0







solution(3,20,4)
