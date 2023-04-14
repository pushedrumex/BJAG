from collections import deque

def solution(maps):
    dxdy = ((0,1),(1,0),(0,-1),(-1,0))
    N, M = len(maps), len(maps[0])
    visited = [[False] * M for _ in range(N)]
    q = deque([[0,0,1]])
    
    while q:
        x,y,cnt = q.popleft()
        if [x,y] == [N-1,M-1]: return cnt
        for dx,dy in dxdy:
            _x,_y = x+dx,y+dy
            if not (0 <= _x < N and 0 <= _y < M) or maps[_x][_y] == 0 or visited[_x][_y]: continue
            q.append([_x,_y,cnt+1])
            visited[_x][_y] = True

    return -1