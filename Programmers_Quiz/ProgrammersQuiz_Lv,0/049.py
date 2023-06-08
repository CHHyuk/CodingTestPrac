# 배열 회전시키기

def solution(numbers, direction):
    if direction == 'right':
        numbers.insert(0,(numbers[len(numbers)-1]))
        numbers.pop(len(numbers)-1)
    elif direction == 'left':
        numbers.append(numbers[0])
        numbers.pop(0)
    
    return numbers




solution([1,2,3],'right')