"""
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
"""

n = int(input())
array = []
for i in range(n):
    array.append(int(input()))
array.sort()
for i in range(n):
    print(array[i])