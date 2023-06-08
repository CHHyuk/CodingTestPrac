# K번째 수

def solution(array, commands):
    answer = []
    
    for i in commands:
        ary = array[i[0]-1: i[1]]
        ary.sort()
        answer.append(ary[i[2]-1]) 
        
    return answer