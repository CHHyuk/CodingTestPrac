n, m = map(int,input().split())
c = int(input())
n0 = int(input())

check = 0
if n0 == 1:
    if c < n + m:
        print(0)
        check += 1
elif n0 > 1:        
    for i in range(1,n0+1):
        if c * i < (n * i) + m:
            print(0)
            check += 1
            break

if check > 0:
    print(1)
