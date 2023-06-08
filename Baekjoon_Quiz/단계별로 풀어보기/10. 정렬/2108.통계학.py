n = int(input())
array= []

for _ in range(n):
    array.append(int(input()))

array.sort()

print(sum(array) // len(array))
print(array[(len(array)-1)//2])
print()
print(array[-1] - array[0])