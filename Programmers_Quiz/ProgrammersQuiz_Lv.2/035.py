# 귤 고르기

def solution(k, tangerine):
    t_dict = {}
    result = 0
    for i in range(len(tangerine)):
        try:
            t_dict[tangerine[i]] += 1
        except:
            t_dict[tangerine[i]] = 1
    t_dict = sorted(t_dict.items(), key = lambda x: x[1], reverse = True)
    
    for j in t_dict:
        if k >= j[1]:
            k -= j[1]
            result += 1
        else:
            if k == 0:
                break
            else:
                result += 1
                break
    return result

solution(6,[1, 3, 2, 5, 4, 5, 2, 3])