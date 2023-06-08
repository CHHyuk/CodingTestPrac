# A를 B로 만들기
def solution(before, after):
    list_b = list(before)
    list_a = list(after)
    list_b.sort()
    list_a.sort()
    if list_b == list_a:
        return 1
    else:
        return 0




solution("allpe",'apple')