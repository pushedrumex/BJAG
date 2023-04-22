dydx = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(y, x, cnt):
    global result
    for dy, dx in dydx:
        _y, _x = y + dy, x + dx
        if not (0 <= _y < R and 0 <= _x < C) or visited[ord(graph[_y][_x]) - ord("A")] : continue
        visited[ord(graph[_y][_x]) - ord("A")] = True
        result = max(cnt + 1, result)
        dfs(_y, _x, cnt + 1)
        visited[ord(graph[_y][_x]) - ord("A")] = False

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
result = 1
visited = [False] * 26
visited[ord(graph[0][0]) - ord("A")] = True
dfs(0, 0, 1)
print(result)