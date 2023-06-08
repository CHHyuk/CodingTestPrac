"""
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.
"""

n = int(input())
n_list = list(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))

answer = ''
n_list_plus = [False]*10000001
n_list_minus = [False]*10000000

for i in range(len(n_list)):
    if n_list[i] >= 0:
        n_list_plus[n_list[i]] = True
    else:
        n_list_minus[(n_list[i] * (-1))] = True

for j in range(len(m_list)):
    if m_list[j] >= 0:
        if n_list_plus[m_list[j]] == True:
            answer = answer + '1 '
        else:
            answer = answer + '0 '
    elif m_list[j] < 0:
        if n_list_minus[(m_list[j] * (-1))] == True:
            answer = answer + '1 '
        else:
            answer = answer + '0 '

print(answer)
