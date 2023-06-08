# 자릿수 더하기

def solution(n):
    list1 = list(map(int, str(n))) # 여러자리 숫자를 각 자릿수 별로 항목화시켜 리스트화
    return sum(list1) # 리스트 각 항목을 모두 더하는 함수