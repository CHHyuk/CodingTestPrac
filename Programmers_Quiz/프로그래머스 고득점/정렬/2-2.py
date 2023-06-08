# H-Index

def solution(citations):

    n = 0
    while True:
        check = 0
        for i in citations:
            if i >= n:
                check += 1
        if check < n:
            break
        else:
            n += 1
    
    return n - 1