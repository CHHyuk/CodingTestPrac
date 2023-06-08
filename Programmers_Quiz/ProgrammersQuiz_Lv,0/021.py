# 제곱수 판별하기

def solution(n):
    list1 = range(1,1000001)
    answer = 2
    for i in list1:
        if i ** 2 == n:
            answer = answer - 1
        elif answer == 1:
            break
         elif answer == 2:
            continue
    return answer

print(solution(3))