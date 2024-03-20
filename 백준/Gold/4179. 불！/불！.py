# 지훈이가 불에 타기 전에 탈출 할 수 있는 지
# 얼마나 빨리 탈출할 수 있는 지
# 지훈이와 불은 분마다 한칸씩 수평 또는 수직으로 이동
# 지훈이는 가장자리 접한 공간에서 탈출 가능
# 불은 네 방향으로 확산
import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
miro = [list(input()) for _ in range(R)]

q = deque()
fire = [[-1] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if miro[i][j] == "J":
            jx, jy = i, j
        elif miro[i][j] == "F":
            q.append((i, j))
            fire[i][j] = 0

dxdy = ((1,0),(-1,0),(0,-1),(0,1))

# 불을 미리 확산시켜놓음
while q:
    x, y = q.popleft()
    for dx, dy in dxdy:
        _x, _y = x + dx, y + dy
        if not (0 <= _x < R and 0 <= _y < C) or miro[_x][_y] == "#":
            continue
        # 이미 확산된 곳이라면
        if fire[_x][_y] > -1:
            continue
        fire[_x][_y] = fire[x][y] + 1
        q.append((_x, _y))

# 지훈이 출동
q = deque([(jx, jy, 0)])
visited = [[False] * C for _ in range(R)]
visited[jx][jy] = True
while q:
    x, y, t = q.popleft()
    if x in (0, R-1) or y in (0, C-1):
        print(t+1)
        exit()
    for dx, dy in dxdy:
        _x, _y = x + dx, y + dy
        if not (0 <= _x < R and 0 <= _y < C) or visited[_x][_y] or miro[_x][_y] == "#":
            continue
        if 0 <= fire[_x][_y] <= t+1:
            continue

        visited[_x][_y] = True
        q.append((_x, _y, t+1))

print("IMPOSSIBLE")