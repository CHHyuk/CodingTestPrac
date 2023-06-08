"""
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
"""

n = int(input())

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(n))