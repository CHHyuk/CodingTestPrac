# 외계어 사전

def solution(spell, dic):
    answer = 0
    result = 0
    for i in dic:
        for j in spell:
            if j in i:
                answer += 1
                if answer == len(spell):
                    result = 1
                    return result
            else:
                pass
        if answer != range(len(spell)):
            result = 2
            answer = 0
    
    return result



solution(["z", "d", "x"],["def", "dww", "dzx", "loveaw"])