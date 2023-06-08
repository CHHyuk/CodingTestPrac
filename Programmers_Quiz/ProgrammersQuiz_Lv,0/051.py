# 피자 나눠 먹기(2)

def solution(n):
    i = 1
    while (6 * i) % n != 0:
        i += 1
    print(i)




solution(10)