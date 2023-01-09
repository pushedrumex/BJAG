from collections import deque

dydx = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(graph):
    ripe = deque()
    day = 1
    
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1:
                ripe.append((y, x))

    while ripe:
        y, x = ripe.popleft()
        for dy, dx in dydx:
            _y, _x = y + dy, x + dx
            if _y > N - 1 or _y < 0 or _x > M - 1 or _x < 0:
                continue
            if graph[_y][_x] == 0:
                graph[_y][_x], day = graph[y][x] + 1, graph[y][x] + 1
                ripe.append((_y, _x))

    for row in graph:
        for tomato in row:
            if (tomato == 0):
                print(-1)
                return

    print(day - 1)

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

bfs(graph)
