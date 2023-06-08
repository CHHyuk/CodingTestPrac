string = input()

str_list = list(string)
temp = list(string)
temp.reverse()

if str_list == temp:
    print(1)
else:
    print(0)