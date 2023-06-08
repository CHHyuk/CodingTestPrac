# 피로도 xxxxxxxxxxxxxxxxx

def solution(k,dungeons):
    dungeons.sort()
    dungeons.reverse()
    temp = []
    for i in range(len(dungeons)):
        temp.append(dungeons[i][0] - dungeons[i][1]) # [60 10 20]
    r_temp = sorted(temp) # [60 20 10]
    rank = []
    for i in temp:
        rank.append(r_temp.index(i)+1) # [3 1 2]    

    for i in rank:
        





solution(80,[[50,40],[80,20],[30,10]])