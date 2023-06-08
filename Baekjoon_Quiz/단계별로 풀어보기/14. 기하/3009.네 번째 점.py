"""
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
"""
x_list = []
y_list = []
x,y = 0,0
for i in range(3):
    a,b = map(int,input().split())
    x_list.append(a)
    y_list.append(b)
x_list.sort()
y_list.sort()

if x_list[0] == x_list[1]:
    x = x_list[2]
else:
    x = x_list[0]

if y_list[0] == y_list[1]:
    y = y_list[2]
else:
    y = y_list[0]

print(x, y)