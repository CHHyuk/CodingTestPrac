# 개미 군단

def solution(hp):
    hp_list = list(range(1, 1001))
    result = 0
    HP = hp
    for i in range(len(hp_list)):
        if HP >= 5:
            result = result + 1
            HP = HP - 5
        elif HP < 5 and HP >= 3:
            result = result + 1
            HP = HP - 3
        elif HP < 3 and HP >= 1:
            result = result + 1
            HP = HP - 1
        elif HP == 0:
            break
    return result

