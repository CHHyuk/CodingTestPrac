# 기능 개발

def solution(progresses, speeds):
    result = []
    n = 0
    while len(progresses) != 0:
        if progresses[0] < 100:
            progresses = [progresses[i] + speeds[i] for i in range(len(speeds))]
        elif progresses[0] >= 100:
            for i in range(len(progresses)):
                if progresses[i] >= 100:
                    n += 1
                    progresses[i] = 0
                    speeds[i] = 0
                else:
                    break
            while 0 in progresses:
                progresses.remove(0)
                speeds.remove(0)

            result.append(n)
            n = 0
    return result
        
        





solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])