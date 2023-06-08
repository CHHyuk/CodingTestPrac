"""
정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
"""

n,std = map(int,input().split())
list = list(map(int,input().split()))
result = ''
for i in range(n):
    if list[i] < std:
        result = result + str(list[i]) + ' '
print(result)