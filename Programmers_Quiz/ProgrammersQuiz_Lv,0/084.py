# 등수 매기기

def solution(score):
    score_average = [(score[i][0] + score[i][1]) / 2 for i in range(len(score))]
    sset = sorted(score_average)
    sset.reverse()
    s_ind = []
    for i in score_average:
        s_ind.append(sset.index(i)+1)
    return s_ind






solution([[80, 70], [90, 50], [40, 70], [50, 80]])