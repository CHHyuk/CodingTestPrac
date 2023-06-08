# 완주하지 못한 선수
from collections import Counter

def solution(participant, completion):
    answer = ''
    
    P_dict = Counter(participant)
    C_dict = Counter(completion)
    for key,value in P_dict.items():
        if key not in list(C_dict.keys()):
            if P_dict[key] >= 1: 
                answer = answer + key
                P_dict[key] -= 1
        elif key in list(C_dict.keys()):
            if P_dict[key] > C_dict[key]:
                answer = answer + key
                P_dict[key] -= 1
    return answer





solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])