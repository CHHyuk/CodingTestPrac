import sys
input = sys.stdin.readline

n = int(input())
n_array = []

for i in range(len(str(n))):
    n_array.append(int(str(n)[i]))

n_array.sort(reverse=True)

answer = int(''.join(map(str,n_array)))
print(answer)
