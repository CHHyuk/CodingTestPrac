# 푸드 파이트 대회

def solution(food):
    answer = ''
    for i in range(1,len(food)):
        if food[i] % 2 != 0:
            food[i] -= 1
        while food[i] > 1:
            if food[i] / 2 >= 1:
                food[i] -= 2
                answer = answer + str(i)

    return answer + '0' + answer[::-1]


solution([1,3,4,6])