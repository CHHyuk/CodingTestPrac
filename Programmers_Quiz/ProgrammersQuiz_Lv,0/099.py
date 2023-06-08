# 옹알이(1)

def solution(babbling):
    result = 0
    able = ["aya", "ye", "woo", "ma"]
    for i in range(len(babbling)):
        for j in range(len(able)):
            if able[j] in babbling[i]:
                babbling[i] = babbling[i].replace(able[j],' ')
    for k in range(len(babbling)):
        babbling[k] = babbling[k].split()
        if babbling[k] == []:
            result += 1
    return result

solution(["aya", "yee", "u", "maa", "wyeoo"])
    
