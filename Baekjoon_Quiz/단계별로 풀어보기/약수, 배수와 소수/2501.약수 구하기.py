n,m = map(int,input().split())

divisor_list = []
for i in range(1,n+1):
    if n % i == 0:
        divisor_list.append(i)
    if len(divisor_list) == m:
        print(divisor_list[-1])
        break
if len(divisor_list) < m:
    print(0)