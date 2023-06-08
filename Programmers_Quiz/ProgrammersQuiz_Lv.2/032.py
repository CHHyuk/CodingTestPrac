# 스킬트리 xxxxxxxxxxxxxxxxxxx

def solution(skill, skill_trees):
    answer = 0
    temp = 0
    s_list = list(skill)
    for i in range(len(skill_trees)):
        for j in range(len(skill)):
            if skill_trees[i].find(skill[j]) != -1:
                if temp <= skill_trees[i].find(skill[j]):
                    temp = skill_trees[i].find(skill[j])
                    if j == len(skill)-1:
                        answer += 1
                else:   
                    break
            elif j == 0:
                break
            else:
                for x in s_list[j+1:]:
                    if x in skill_trees[i]:
                        break
                    else:
                        pass
        temp = 0          
    return answer






solution("CBD",["CAED", "CBADF", "AECB", "BDA"])