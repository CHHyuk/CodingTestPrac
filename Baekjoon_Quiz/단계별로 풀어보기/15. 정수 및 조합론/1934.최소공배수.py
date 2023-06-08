t = int(input())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)


for i in range(t):
    a,b = map(int,input().split())
    print(lcm(a,b))