import sys
input = sys.stdin.readline

n = int(input())
count = n
answer = 0

while count != 0:
    for i in range(666,10000000000000):
        if '666' in str(i):
            count -= 1
            answer = int(i)
            if count == 0:
                break
print(answer)