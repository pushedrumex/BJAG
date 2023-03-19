from collections import deque
dxdy = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def solution(board):
    answer = 0
    X, Y = len(board), len(board[0])
    visited = [[False]*Y for _ in range(X)]
    start = []
    
    for i in range(X):
        for j in range(Y):
            if board[i][j] == "R":
                start = [i, j]
                break
        if start: break
    
    q = deque([start + [0]])
    while q:
        x, y, cnt = q.popleft()
        visited[x][y] = True
        for dx, dy in dxdy:
            _x, _y = x, y
            while 0 <= _x+dx < X and 0 <= _y+dy < Y and board[_x+dx][_y+dy] != "D":
                _x += dx
                _y += dy
            
            if visited[_x][_y]: continue
            elif board[_x][_y] == "G": return cnt+1  
            else: q.append([_x, _y, cnt + 1])

    return -1