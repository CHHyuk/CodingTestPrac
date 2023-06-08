"""
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
에라스토테네스의 체
"""

a,b = map(int,input().split())

d = [False,False] + [True]* (b-1)
primes = []

for i in range(2,b+1):
    if d[i]:
        primes.append(i)
        for j in range(2*i, b+1, i):
            d[j] = False
for i in range(len(primes)):
    if primes[i] >= a and primes[i] <= b:
        print(primes[i])
