# 같은 숫자는 싫어

def solution(arr):
    answer = [arr[0]]
    for i in range(1,len(arr)):
        if answer[len(answer)-1] == arr[i]:
            continue
        answer.append(arr[i])
    return answer






solution([1,1,3,3,0,1,1])