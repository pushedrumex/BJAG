dydx = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(y, x, visited, cnt):
    global result
    visited[ord(graph[y][x]) - ord("A")] = True
    for dy, dx in dydx:
        _y, _x = y + dy, x + dx
        if _y > R - 1 or _x > C - 1 or _y < 0 or _x < 0 or visited[ord(graph[_y][_x]) - ord("A")] : continue
        result = max(cnt + 1, result)
        dfs(_y, _x, visited[:], cnt + 1)

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
result = 1
dfs(0, 0, [False] * 26, 1)
print(result)