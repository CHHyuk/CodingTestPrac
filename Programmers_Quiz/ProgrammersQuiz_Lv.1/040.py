# 두 개 뽑아서 더하기

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                if numbers[i] + numbers[j] not in answer:
                    answer.append(numbers[i]+numbers[j])
    answer.sort()
    return answer





solution([2,1,3,4,1])