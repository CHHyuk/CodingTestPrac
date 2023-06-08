# [1차] 비밀지도 (2018 카카오 시험)

def solution(n,arr1,arr2):
    answer = []
    temp = ''
    A = [bin(arr1[i])[2:].rjust(n,'0') for i in range(len(arr1))]
    B = [bin(arr2[i])[2:].rjust(n,'0') for i in range(len(arr2))]
    
    for i in range(len(A)):
        A[i] = list(A[i])
        B[i] = list(B[i])
        for j in range(n):
            if A[i][j] == '1' or B[i][j] == '1':
                temp += '#'
            elif A[i][j] == '0' and B[i][j] == '0':
                temp += ' '
        answer.append(temp)
        temp = ''
    return answer
                
        

solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28])