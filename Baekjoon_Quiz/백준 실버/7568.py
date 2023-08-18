import sys
input = sys.stdin.readline

n = int(input())
people = []

for _ in range(n):
    weight, height = map(int,input().split())
    people.append((weight,height))

ranking = []
for i in range(n):
    rank = 1
    for j in range(n):
        if i != j and people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
    ranking.append(rank)

for i in ranking:
    print(i, end=' ')
