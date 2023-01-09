from collections import deque

dydx = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(graph):
    ripe = deque()
    day = 0

    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1:
                ripe.append((y, x))
    
    ripe.append(0) # next day

    while ripe:
        if (ripe[0] == 0):
            day += 1
            ripe.popleft()
            
            if (len(ripe) == 0):
                break
            
            ripe.append(0) # next day
            continue

        y, x = ripe.popleft()

        for dy, dx in dydx:
            _y, _x = y + dy, x + dx
            if _y > N - 1 or _y < 0 or _x > M - 1 or _x < 0:
                continue
            if graph[_y][_x] == 0:
                graph[_y][_x] = 1
                ripe.append((_y, _x))

    for row in graph:
        for tomato in row:
            if (tomato == 0):
                print(-1)
                return

    print(day - 1)

M, N = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

bfs(graph)