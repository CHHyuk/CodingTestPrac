# 위장

def solution(clothes):
    check = [clothes[i][1] for i in range(len(clothes))]
    count = {}
    result = 1
    for i in check:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    
    for key in count:
        result *= (count[key]+1)

    return result -1


solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])