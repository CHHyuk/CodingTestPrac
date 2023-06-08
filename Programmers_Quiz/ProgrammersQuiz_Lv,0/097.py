# 연속된 수의 합

def solution(num, total):
    result = []
    if num % 2 != 0:
        for i in range((total//num)-int((num-1)/2),(total//num)+int((num-1)/2)+1):
            result.append(i)
        return result
    else:
        for i in range((total//num)-int((num)/2)+1,(total//num)+int((num)/2)+1):
            result.append(i)
        return result

solution(4,14)