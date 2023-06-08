n = int(input())

array = []
check = 0
answer = 0
for i in range(n):
    string = input()
    for j in range(len(string)):
        if string[j] in array and string[j] != array[-1]:
            check += 1
            break
        elif string[j] not in array:
            array.append(string[j])
    if check == 0:
        answer += 1
    elif check > 1:
        pass
    check = 0
    array = []

print(answer)
        
        