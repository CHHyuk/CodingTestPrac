# 자연수 뒤집어 배열로 만들기

def solution(n):
    n_list = []
    n_list = list(map(int, str(n)))
    n_list.reverse()
    return n_list