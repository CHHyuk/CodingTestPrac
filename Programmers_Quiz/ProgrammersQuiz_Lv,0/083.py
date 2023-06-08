# 문자열 밀기

def solution(A, B):
    list_A = list(A)
    list_B = list(B)
    answer = 0
    for i in range(len(list_A)):
        if list_A != list_B:
            list_A.insert(0,list_A[len(A)-1])
            list_A.pop()
            answer += 1
            if list_A == list_B:
                return answer
        elif list_A == list_B:
            return 0
    return -1




solution("apple","elppa")