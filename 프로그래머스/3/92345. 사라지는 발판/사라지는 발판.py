def solution(board, aloc, bloc):
    return play(board, aloc, bloc, 0)

dxdy = ((0,1),(1,0),(-1,0),(0,-1))
def play(board, me, op, count):
    x, y = me

    if board[x][y] == 0 or isFail(board, x, y):
        return count
    win, lose = [], []
    board[x][y] = 0
    for dx, dy in dxdy:
        _x, _y = x + dx, y + dy
        if not (0 <= _x < len(board) and 0 <= _y < len(board[0])) or board[_x][_y] == 0:
            continue
        result = play(board, op, (_x, _y), count + 1)

        if (count + result) % 2 != 0: # me가 이겼다면
            win.append(result)
        else: # me가 졌다면
            lose.append(result)

    board[x][y] = 1
    if win:
        return min(win)
    return max(lose)

def isFail(board, x, y):
    for dx, dy in dxdy:
        _x, _y = x + dx, y + dy
        if 0 <= _x < len(board) and 0 <= _y < len(board[0]) and board[_x][_y] == 1:
            return False
    return True