"""
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
"""

n = int(input())
array = [0] * 10001

for _ in range(n):
    array[int(input())] += 1

for i in range(len(array)):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)

