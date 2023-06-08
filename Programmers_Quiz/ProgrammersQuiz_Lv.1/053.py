# 다트 게임 xxxxxxxxxxxxxx

def solution(dartResult):
    SDT = ['S', 'D', 'T']
    SDT_score = [1, 2, 3]
    result = []
    temp = 0
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            if dartResult[i] == '0' and dartResult[i-1].isdigit():
                temp = 10
            elif dartResult[i+1].isdigit():
                result.append(temp)
                continue
            else:
                result.append(temp)
                temp = int(dartResult[i])
        if dartResult[i] in SDT:
            for j in range(len(SDT)):
                if SDT[j] == dartResult[i]:
                    temp = temp ** SDT_score[j]
                    break
        if dartResult[i] == '*':
            if result == [] or result == [0]:
                temp *= 4
            else:
                result[-1] *= 2
                temp *= 2
        if dartResult[i] == '#':
            temp *= -1
        if i == len(dartResult) - 1:
            result.append(temp)
    return sum(result)
        
solution("1S*2T*3S")