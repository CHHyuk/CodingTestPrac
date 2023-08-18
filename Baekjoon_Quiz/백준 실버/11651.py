import sys
input = sys.stdin.readline

n = int(input())

array = []
for i in range(n):
    a,b = map(int,input().split())
    array.append((a,b))
    
array.sort()
sorted_array = sorted(array, key=lambda y: y[1])

for i in range(n):
    print(sorted_array[i][0], sorted_array[i][1])
