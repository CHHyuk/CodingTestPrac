

while True:
    n = int(input())
    divisors = []

    if n == -1:
        break
    
    for i in range(1, n//2 + 1):
        if n % i == 0:
            divisors.append(i)

    if sum(divisors) == n:
        answer = '{} = 1'.format(n)
        for i in range(len(divisors)-1):
            answer = answer + ' + ' + str(divisors[i+1])
        print(answer)
    else:
        print("{} is NOT perfect.".format(n))
    
