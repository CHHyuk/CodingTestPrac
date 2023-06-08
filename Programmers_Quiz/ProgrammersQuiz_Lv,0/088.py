# 진료 순서 정하기
def solution(emergency):
    order = []
    sort = sorted(emergency, reverse=True)
    for i in range(len(sort)):
        order.append(sort.index(emergency[i]) + 1)
    return order

solution([30, 10, 23, 6, 100])