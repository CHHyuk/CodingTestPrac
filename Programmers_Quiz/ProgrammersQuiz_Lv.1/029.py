# 직사각형 별찍기

a, b = map(int, input().split())
for i in range(b):
    for j in range(a):
        print('*',end='')
    print(end='\n')
    
