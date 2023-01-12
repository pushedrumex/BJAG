from collections import deque

dydx = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]

def bfs(y, x):
    q = deque([(y, x)])
    
    while q:
        y, x = q.popleft()
        for dy, dx in dydx:
            _y, _x = y + dy, x + dx
            if _y > h - 1 or _x > w - 1 or _y < 0 or _x < 0 or graph[_y][_x] == 0: continue
            graph[_y][_x] = 0
            q.append((_y, _x))

while True:
    w, h = map(int, input().split()) 
    if w + h == 0: break

    graph = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0

    for j in range(h):
        for i in range(w):
            if graph[j][i] == 1:
                cnt += 1
                bfs(j, i)
    print(cnt)