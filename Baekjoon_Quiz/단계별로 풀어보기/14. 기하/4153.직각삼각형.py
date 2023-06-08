"""
과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다. 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.
"""

while True:
    vertex = list(map(int,input().split()))
    vertex.sort()
    if (vertex[0] ** 2) + (vertex[1] ** 2) == (vertex[2] ** 2) and 0 not in vertex:
        print('right')
    elif vertex == [0, 0, 0]:
        break
    else:
        print('wrong')