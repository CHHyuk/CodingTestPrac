# 행렬의 곱셈
import numpy as np

def solution(arr1, arr2):
    a = np.array(arr1)
    b = np.array(arr2)
    c = np.dot(a,b)
    return c.tolist()





solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]])