str_list = []

for _ in range(5):
    str = input()
    str_list.append(list(str))

i = 0
answer = ''
while str_list != [[],[],[],[],[]]:
    try:
        answer = answer + str_list[i].pop(0)
    except:
        pass
    if i < 4:
        i += 1
    else:
        i = 0

print(answer)

