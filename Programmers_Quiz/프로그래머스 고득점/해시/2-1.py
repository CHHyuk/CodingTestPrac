# 전화번호 목록

def solution(phone_book):
    phone_book.sort(key=len)
    hash_table = {}

    min_len = len(phone_book[0])

    for target in phone_book:
        hash_table[hash(target)] = target
        for i in range(min_len,len(target)):
            try:
                if hash_table[hash(target[0:i])]:
                    return False
            except:
                pass

    return True





solution(["12",'2535','43745','135','4372','8678',"567","88"])