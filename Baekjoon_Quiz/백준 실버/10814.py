import sys
input = sys.stdin.readline

n = int(input())
array = []
age = []

for _ in range(n):
    a,b = input().split()
    array.append((a,b))
    age.append(int(a))

age.sort()

for i in range(age[0], age[-1]+1):
    for j in range(len(array)):
        if array[j][0] == str(i):
            answer = ' '.join(array[j])
            print(answer)
