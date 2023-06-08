# 행렬의 덧셈

def solution(arr1,arr2):
    temp = []
    answer = []
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            if len(arr1[0]) > j:
                temp.append(arr1[i][j] + arr2[i][j])
                if len(arr1[0]) == j + 1:
                    answer.append(temp)
                    temp = []
    return answer






solution([[1,2],[2,3]],[[3,4],[5,6]])