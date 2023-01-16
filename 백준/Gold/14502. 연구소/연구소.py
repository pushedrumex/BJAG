from itertools import combinations
from collections import deque
import copy

dydx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def bfs(y, x, graph):
    q = deque([(y, x)])
    infection = 0
    while q:
        y, x = q.popleft()
        for dy, dx in dydx:
            _y, _x = y + dy, x + dx
            if _y > N - 1 or _x > M - 1 or _y < 0 or _x < 0 or graph[_y][_x] != 0:
                continue
            graph[_y][_x] = 2
            infection += 1
            q.append((_y, _x))
    return infection

def infect(graph):
    infection = 0
    for virus_y, virus_x in virus:
        infection += bfs(virus_y, virus_x, graph)
    return infection

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

virus = []
blank = []
 
for j in range(N):
    for i in range(M):
        if graph[j][i] == 2:
            virus.append((j, i))
        elif graph[j][i] == 0:
            blank.append((j, i))

cases = list(combinations(blank, 3))
safe = 0

for case in cases:
    infection = 0
    _graph = copy.deepcopy(graph)
    for y, x in case:
        _graph[y][x] = 1
    safe = max(safe, len(blank) - 3 - infect(_graph))

print(safe)