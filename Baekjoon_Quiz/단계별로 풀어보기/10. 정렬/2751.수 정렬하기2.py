""" xxxxxxxxxxxxxxx
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
"""

import sys

n=int(sys.stdin.readline().rstrip())
unsorted_list=[]
sorted_list=[]

# [divide]
# 리스트 요소가 1개가 될때까지 나눔 / 왼쪽,오른쪽 merge
def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    return merge(leftList, rightList)

def merge(left, right):
    merged_list = []
    l=h=0

    while l < len(left) and h < len(right):
        if (left[l] < right[h]):
            merged_list.append(left[l])
            l+=1
        else:
            merged_list.append(right[h])
            h+=1
    merged_list += left[l:]
    merged_list += right[h:]
    return merged_list

for i in range(n):
    num=int(sys.stdin.readline())
    unsorted_list.append(num)

sorted_list=merge_sort(unsorted_list)

for i in sorted_list:
    print(i)

