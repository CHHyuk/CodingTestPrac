# 캐릭터의 좌표

def solution(keyinput, board):
    y = 0
    x = 0
    for i in keyinput:
        if i == 'left':
            x -= 1
            if board[0] / 2 - 0.5 < abs(x):
                x += 1
        elif i == 'right':
            x += 1
            if board[0] / 2 - 0.5 < abs(x):
                x -= 1
        elif i == 'up':
            y += 1
            if board[1] / 2 - 0.5 < abs(y):
                y -= 1
        elif i == 'down':
            y -= 1
            if board[1] / 2 - 0.5 < abs(y):
                y += 1
    return [x,y]




solution(["down", "down", "down", "down", "down"],[7, 9])