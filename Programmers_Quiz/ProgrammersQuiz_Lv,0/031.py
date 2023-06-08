# 옷가게 할인받기

def solution(price):
    if price >= 500000:
        price = price * 0.8
    elif price < 500000 and price >= 300000:
        price = price * 0.9
    elif price < 300000 and price >= 100000:
        price = price * 0.95
    else:
        pass
    
    result = int(price) 
    
    return result