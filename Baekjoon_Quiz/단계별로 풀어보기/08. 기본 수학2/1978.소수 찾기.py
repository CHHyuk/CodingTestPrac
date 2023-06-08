"""
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
"""

def prime_number(x):
    if x == 1:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

n = int(input())
num_list = list(map(int,input().split()))
count = 0
for i in range(len(num_list)):
    if prime_number(num_list[i]):
        count += 1
print(count)