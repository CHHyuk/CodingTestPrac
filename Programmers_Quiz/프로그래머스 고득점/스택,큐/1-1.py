# 같은 숫자는 싫어

def solution(arr):
    stack = []
    answer = []
    for i in range(len(arr)):
        if arr[i] not in stack:
            if len(stack) == 0:
                stack.append(arr[i])
                answer.append(arr[i])
            else:
                stack.pop()
                stack.append(arr[i])
                answer.append(arr[i])
        else:
            pass
    return answer





solution([1,1,3,3,0,1,1])