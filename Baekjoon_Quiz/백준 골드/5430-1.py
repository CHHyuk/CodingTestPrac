import ast
from collections import deque

def AC(arr, func, length):
    if length == 0:
        print ("error")
        return
    func_list = list(func)
    for i in range(len(func_list)):
        if func_list[i] == "R":
            arr = list(deque(arr).__reversed__())
        elif func_list[i] == "D":
            if arr == []:
                print ("error")
                return
            elif arr != []:
                arr.pop(0)
    print(arr)
    return


t = int(input())

for i in range(t):
    func = input()
    length = int(input())
    arr_str = input()
    try:
        arr = ast.literal_eval(arr_str)
        if not isinstance(arr, list):
            raise ValueError
    except (ValueError, SyntaxError):
        print("올바른 리스트 형식이 아닙니다.")
    AC(arr, func, length)
