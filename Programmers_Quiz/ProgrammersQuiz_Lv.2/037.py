#연속 부분 수열 합의 개수

def solution(elements):
    array = []
    elements_2 = elements+elements
    for i in range(1,len(elements)+1):            
        for j in range(len(elements)):
            if i == 1:
                array.append(elements_2[j])
            else:
                array.append(sum(elements_2[j:j+i]))
    array = set(array)
    return len(array)

solution([7,9,1,1,4])
