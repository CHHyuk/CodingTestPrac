# 잘라서 배열로 저장하기

def solution(my_str, n):
    result = []
    while True:
        if len(my_str) > n:
            result.append(my_str[:n])
            my_str = my_str[n:]
        else:
            result.append(my_str)
            break
    return result





solution("abc1Addfggg4556b",6)