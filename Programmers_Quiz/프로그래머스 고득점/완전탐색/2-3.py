# 피로도

def solution(k, dungeons):
    answer = 0
    answerlist=[0]
    def dundfs(k2,dun2,count2):
        for i in range(len(dun2)):
            if i<len(dun2)-1 and k2>=dun2[i][0] and k2>=dun2[i][1]:
                dundfs(k2-dun2[i][1],dun2[:i]+dun2[i+1:],count2+1)
            elif i==len(dun2)-1 and k2>=dun2[i][0] and k2>=dun2[i][1]:
                dundfs(k2-dun2[i][1],dun2[:i],count2+1)
        answerlist.append(count2)

    count=0
    for i in range(len(dungeons)):
        if i<len(dungeons)-1 and k>=dungeons[i][0] and k>=dungeons[i][1]:
            dundfs(k-dungeons[i][1],dungeons[:i]+dungeons[i+1:],count+1)
        elif i==len(dungeons)-1 and k>=dungeons[i][0] and k>=dungeons[i][1]:
            dundfs(k-dungeons[i][1],dungeons[:i],count+1)
    answer=max(answerlist)

    return answer


solution(80, [[80,20],[50,40],[30,10]])