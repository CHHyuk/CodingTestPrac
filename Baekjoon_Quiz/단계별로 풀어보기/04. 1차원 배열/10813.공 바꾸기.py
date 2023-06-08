n,m = map(int,input().split())

array = []
for i in range(n):
    array.append(i+1)

for _ in range(m):
    i,j = map(int,input().split())
    array[i-1],array[j-1] = array[j-1],array[i-1]

answer = ''
for i in range(len(array)):
    answer = answer + str(array[i]) + ' '

print(answer)