# 짝수는 싫어요

def solution(n):
    list1 = range(1,101)
    result = []
    for i in range(len(list1)):
        if i == n + 1:
            break
        elif i % 2 != 0:
            result = result + [i]
        else:
            continue
    
    return result

print(solution(10))

