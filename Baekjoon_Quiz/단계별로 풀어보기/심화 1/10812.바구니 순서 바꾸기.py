n,m = map(int,input().split())

array = []
for i in range(n):
    array.append(i+1)


for _ in range(m):
    i,j,k = map(int,input().split())
    temp_front = []
    temp_back = []
    for x in range(i,j+1):
        if x >= k:
            temp_front.append(array[x-1])
        else:
            temp_back.append(array[x-1])
    temp = temp_front + temp_back
    order = 0
    for y in range(i-1,j):
        array[y] = temp[order]
        order += 1
answer = ''

for i in range(len(array)):
    answer = answer + str(array[i]) + ' '

print(answer)
