# 다음에 올 숫자

def solution(common):
    result = 0
    if common[1] - common[0] == common[2] - common[1]:
        result = common[len(common)-1] + (common[1] - common[0])
    else:
        result = common[len(common)-1] * (common[1] / common[0])
    return result


solution([1,2,3,4])