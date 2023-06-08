# 폰켓몬

def solution(nums):
    mon_dict = {}
    for i in range(len(nums)):
        if nums[i] in mon_dict:
            mon_dict[nums[i]] += 1
        else:
            mon_dict[nums[i]] = 1
    
    if len(mon_dict) <= len(nums) // 2:
        return len(mon_dict)
    else:
        return len(nums) // 2
