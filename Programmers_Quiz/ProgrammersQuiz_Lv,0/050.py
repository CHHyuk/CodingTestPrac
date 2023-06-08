# 주사위의 개수

def solution(box, n):
    A = 1
    for i in range(len(box)):
        A = A * (box[i] // n)
    
    return A




solution([10,8,6],3)