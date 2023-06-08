"""
자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.
"""

def prime_number(x):
    if x == 1:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

m = int(input())
n = int(input())
count = 0
sum = 0
min = 0
for i in range(m,n+1):
    if prime_number(i):
        if count == 0:
            min = i
        count += 1
        sum += i
if count != 0:
    print(sum)
    print(min)
else:
    print(-1)