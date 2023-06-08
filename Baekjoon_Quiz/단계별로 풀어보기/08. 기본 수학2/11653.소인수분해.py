"""
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.
"""
def prime_number(x):
    if x == 1:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

n = int(input())

while n != 1:
    for i in range(1,n+1):
        if prime_number(n):
            print(n)
            n = int(n / n)
            break
        
        if prime_number(i) and n % i == 0:
            n = int(n / i)
            print(i)
            break
