"""
n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
"""

n = int(input())
answer = 0
for i in range(1,n+1):
    answer += i
print(answer)