n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

arr.sort()
answer = ''

for i in range(2,arr[0]):
    temp = arr[0] % i
    count = 0
    for j in range(len(arr)):
        if arr[j] % i == temp:
            count += 1
        else:
            break
    if count == len(arr):
        answer = answer + str(i) + ' '

print(int(answer))