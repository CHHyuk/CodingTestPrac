"""
베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.

이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.

예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)

자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 
"""

while True:
    n = int(input())
    if n == 0:
        break
    if n == 1:
        print(1)
        continue
    d = [False,False] + [True]* ((2*n)-1)
    primes = []
    primes_filtered = []

    for i in range(2,(2*n)+1):
        if d[i]:
            primes.append(i)
            for j in range(2*i, (2*n)+1, i):
                d[j] = False
    for i in range(len(primes)):
        if primes[i] > n and primes[i] < 2*n:
            primes_filtered.append(primes[i])
    print(len(primes_filtered))