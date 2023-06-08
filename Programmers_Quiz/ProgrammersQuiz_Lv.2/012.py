# 구명보트

def solution(people, limit):
    answer = 0
    people.sort()


    while people != []:
        k = people.pop()
        if people == []:
            answer += 1
            break
        else:
            if people[0] + k <= limit:
                people.pop(0)
                answer += 1
            else:
                answer +=  1

    return answer