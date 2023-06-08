n = int(input())

def command(string,stack):
    if 'push' in string:
        stack.append(int(string[4:]))
    elif 'pop' in string:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif 'size' in string:
        print(len(stack))
    elif 'empty' in string:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif 'top' in string:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    return

        
stack = []
for i in range(n):
    string = input()
    command(string,stack)