"""
(세 자리 수) * (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다. (그림)
(1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.
"""

A = input()
B = input()
list = []
for i in range(len(B)):
    list.append(int(B[i]) * int(A))
print(list[2])
print(list[1])
print(list[0])
print(int(A)*int(B))