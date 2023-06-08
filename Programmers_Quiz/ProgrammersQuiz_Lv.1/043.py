# 폰켓몬

def solution(nums):
    answer = 0
    l = len(nums) // 2
    temp = list(set(nums))
    
    for i in temp:
        if answer < l:
            answer += 1
    return answer





solution([3,3,3,2,2,4])