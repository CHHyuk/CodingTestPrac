def possible(num, broken):
    if num == 0:
        if 0 in broken:
            return 0
        else:
            return 1
    length = 0
    while num > 0:
        if num % 10 in broken:
            return 0
        length += 1
        num //= 10
    return length

N = int(input())  # 이동하려는 채널
M = int(input())  # 고장난 버튼 개수
broken = set(map(int, input().split()))  # 고장난 버튼 리스트

answer = abs(N - 100)  # +, - 버튼만으로 이동하는 경우

for i in range(1000000):  # 최대 100만까지 시도
    length = possible(i, broken)
    if length > 0:
        # 숫자 버튼을 누르는 경우, 해당 숫자에서 목표 채널까지 +, - 버튼을 누르는 횟수를 더해준다
        press = abs(N - i)
        answer = min(answer, length + press)

print(answer)
