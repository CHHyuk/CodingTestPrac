"""
총 N개의 문자열로 이루어진 집합 S가 주어진다.

입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.
"""

n,m = map(int,input().split())

n_list = []
m_list = []
answer = 0
for i in range(n):
    n_list.append(input())
for i in range(m):
    m_list.append(input())

for i in range(len(m_list)):
    for j in range(len(n_list)):
        if m_list[i] in n_list[j]:
            answer += 1
            break
        else:
            pass

print(answer)
