# 모의고사

def solution(answers):
    count = [0,0,0]
    first = [1,2,3,4,5] * 10000
    second = [2,1,2,3,2,4,2,5] * 10000
    third = [3,3,1,1,2,2,4,4,5,5] * 10000

    for i in range(len(answers)):
        if answers[i] == first[i]:
            count[0] += 1
        if answers[i] == second[i]:
            count[1] += 1
        if answers[i] == third[i]:
            count[2] += 1

    rank = []
    for j in range(len(count)):
        if max(count) == count[j]:
            rank.append(j+1)

    return rank 
  



solution([1,2,3,4,5])