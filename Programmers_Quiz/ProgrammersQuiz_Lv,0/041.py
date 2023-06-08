# 모음 제거

def solution(my_string):
    list1 = list(my_string)
    list1.remove('a','e','i','o','u')
    print(list1)

print(solution('asdewbergfqioua'))