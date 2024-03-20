from collections import deque

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            x, y = i, j

answer = [[-1] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
visited[x][y] = True
q = deque([(x, y, 0)])
answer[x][y] = 0
dxdy = ((1,0),(-1,0),(0,1),(0,-1))
while q:
    x, y, d = q.popleft()
    for dx, dy in dxdy:
        _x, _y = x + dx, y + dy
        if not (0<=_x<n and 0<=_y<m): continue
        if arr[_x][_y] == 0 or visited[_x][_y]:
            continue
        visited[_x][_y] = True
        answer[_x][_y] = answer[x][y] + 1
        q.append((_x, _y, answer[_x][_y]))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            answer[i][j] = 0

for row in answer:
    print(*row)

