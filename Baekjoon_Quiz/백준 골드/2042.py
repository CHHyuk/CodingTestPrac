# 세그먼트 트리 해결법
# 하나씩 다 더해가는 문제의 경우 세그먼트 트리를 활용하면 시간복잡도가 O(logN)
# 선형 배열로 풀면 O(N)

# 트리 정의
def define_tree(start, end, index):
    if start == end:
        segment_tree[index] = l[start-1]
        return segment_tree[index]

    mid = (start + end) // 2
    segment_tree[index] = define_tree(start, mid, index*2) + define_tree(mid+1, end, index*2+1)
    return segment_tree[index]



# 배열로만 풀기(시간초과)

# n, m, k = map(int,input().split())
# base_list = []

# for _ in range(n):
#     base_list.append(int(input()))

# for _ in range(m+k):
#     a,b,c = map(int,input().split())
#     if a == 1:
#         base_list[b-1] = c
#     elif a == 2:
#         print(sum(base_list[b-1:c]))

