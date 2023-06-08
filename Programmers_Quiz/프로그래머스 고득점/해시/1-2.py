# 완주하지 못한 선수

def solution(participant, completion):
    p_dict = {}
    for i in range(len(participant)):
        if participant[i] in p_dict:
            p_dict[participant[i]] += 1
        else:
            p_dict[participant[i]] = 1
    
    for j in range(len(completion)):
        if completion[j] in p_dict:
            p_dict[completion[j]] -= 1
    
    for key,value in p_dict.items():
        if value == 1:
            return key
    



solution(["leo", "kiki", "eden"],["eden", "kiki"])