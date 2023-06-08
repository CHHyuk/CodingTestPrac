"""
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
"""

n = int(input())
count = 0
for i in range(n):
    list = list(map(int,input().split()))
    check = list[0]
    del list[0]
    for j in range(len(list)):
        if list[j] > (sum(list) / check):
            count += 1
    x = count/check*100
    print(f'{x:.3f}%')
    x, check, count = 0, 0, 0
