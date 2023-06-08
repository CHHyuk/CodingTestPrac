# 2차원으로 만들기

def solution(num_list, n):
    answer = []
    inner =[]
    a = 0
    for i in num_list:
        if a < n:
            inner.append(i)
            a += 1
            if a == n:
                answer.append(inner)
                inner = []
                a = 0
    print(answer)
        




solution([1,2,3,4,5,6,7,8],2)