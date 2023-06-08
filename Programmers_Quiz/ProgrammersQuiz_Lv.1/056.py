# 햄버거 만들기

def solution(ingredient):
    result = 0
    stack = []
    for i in range(len(ingredient)):
        if len(stack) == 0 and ingredient[i] == 1:
            stack.append(ingredient[i])
        elif len(stack) > 0:
            if stack[-1] == 1:
                if ingredient[i] == 2:
                    stack.append(ingredient[i])
                elif ingredient[i] == 1:
                    stack.append(ingredient[i])
                else:
                    pass
            elif stack[-1] == 2:
                if ingredient[i] == 3:
                    stack.append(ingredient[i])
                else:
                    stack.remove
            elif stack[-1] == 3:
                if ingredient[i] == 1:
                    stack.append(ingredient[i])
                    stack.remove(1)
                    stack.remove(2)
                    stack.remove(3)
                    stack.remove(1)
                    result += 1
                else:
                    stack.clear()
    return result

solution([1,1,1,2,3,1,2,3,1,2,3,1])