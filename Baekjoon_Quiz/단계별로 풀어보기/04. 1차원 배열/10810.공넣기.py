n,m = map(int,input().split())

array = [0] * n
for _ in range(m):
    i,j,k = map(int,input().split())
    for x in range(i-1,j):
        array[x] = k

answer = ''
for i in range(len(array)):
    answer = answer + str(array[i]) + ' '

print(answer)