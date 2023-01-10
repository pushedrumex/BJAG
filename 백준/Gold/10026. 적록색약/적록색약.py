from collections import deque 

dydx = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(is_RG , y, x, visited):
    q = deque([(y, x)])
    while q:
        y, x = q.popleft()
        for dy, dx in dydx:
            _y, _x = y + dy, x + dx
            if _y > N - 1 or _x > N - 1 or _y < 0 or _x < 0 or visited[_y][_x]:
                continue
            if graph[_y][_x] == graph[y][x]:
                visited[_y][_x] = True
                q.append((_y, _x))            
            elif is_RG and graph[y][x] in "RG" and graph[_y][_x] in "RG":
                visited[_y][_x] = True
                q.append((_y, _x))
    return visited

def countArea(is_RG, N):
    visited = [[False] * N for _ in range(N)]
    area = 0

    for j in range(N):
        for i in range(N):
            if not visited[j][i]:
                area += 1
                visited = bfs(is_RG, j, i, visited)

    print(area, end=" ")

N = int(input())
graph = [list(input()) for _ in range(N)]

countArea(False, N)
countArea(True, N)