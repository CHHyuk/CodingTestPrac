# 영어 끝말잇기

def solution(n, words):
    answer = [0, 0]
    index = -1
    
    while index + 1 < len(words):
        index += 1
        if index > 0 and words[index-1][-1] != words[index][0] or words[index] in words[:index]:
            answer = [(index % n) + 1, index // n + 1]
            break
    return answer