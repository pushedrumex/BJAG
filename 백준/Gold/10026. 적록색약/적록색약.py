# dfs
import sys
sys.setrecursionlimit(10000)

dydx = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(is_RG, y, x):
    visited[y][x] = True
    for dy, dx in dydx:
        _y, _x = y + dy, x + dx
        if _y > N - 1 or _x > N - 1 or _y < 0 or _x < 0 or visited[_y][_x]:
            continue
        if graph[_y][_x] == graph[y][x]:
            dfs(is_RG, _y, _x)
        elif is_RG and graph[y][x] in "RG" and graph[_y][_x] in "RG":
            dfs(is_RG, _y, _x)

def countArea(is_RG, N):
    area = 0
    for j in range(N):
        for i in range(N):
            if not visited[j][i]:
                area += 1
                dfs(is_RG, j, i)

    print(area, end=" ")

N = int(input())
graph = [list(input()) for _ in range(N)]

visited = [[False] * N for _ in range(N)]
countArea(False, N)
visited = [[False] * N for _ in range(N)]
countArea(True, N)