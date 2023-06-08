n = int(input())

check = 0
answer = 0
for i in range(n):
    pa_string = input()
    for j in range(len(pa_string)):
        if pa_string[j] == '(':
            check += 1
        else:
            check -= 1
        if check < 0:
            answer += 1
            break
    if answer == 0 and check == 0:
        print('YES')
    else:
        print("NO")
    check = 0
    answer = 0