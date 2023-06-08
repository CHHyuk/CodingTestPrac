def sum_all_digit(n):
    sum = 0
    if len(str(n)) == 1:
        return n
    else:
        for i in range(len(str(n))):
            sum += int(str(n)[i])
        return sum

d = [False] * 10001

for i in range(1,10001):
    if i + sum_all_digit(i) <= 10000:
        d[i+sum_all_digit(i)] = True
    else:
        pass

for i in range(1, len(d)):
    if d[i] == False:
        print(i)
