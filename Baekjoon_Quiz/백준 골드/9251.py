import sys
word = sys.stdin.readline

w1, w2 = word().strip(), word().strip()
l1, l2 = len(w1), len(w2)
cache = [0] * l2

for i in range(l1):
    count = 0
    for j in range(l2):
        if count < cache[j]:
            count = cache[j]
        elif w1[i] == w2[j]:
            cache[j] = count + 1

print(max(cache))