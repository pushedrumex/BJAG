# 빈칸인 곳만 -> 인접한 한 칸, 대각선 방향, 이동 X
# 인접한 위칸이 벽이라면 이동 가능 -> 이후는 이동 불가능
# 벽이 캐릭터가 있는 칸으로 이동하면 더이상 캐릭터가 이동할 수 없다
from collections import deque

chess = [list(input()) for _ in range(8)]
visited = [[[False] * 17 for _ in range(8)] for _ in range(8)]

dxdy = ((0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1))

answer = 0

# x, y, time
q = deque([(7, 0, 0)])
visited[7][0][0] = True
while q:
    x, y, time = q.popleft()

    # 오른쪽 윗칸에 도달했다면
    if (x, y) == (0, 7):
        answer = 1
        break
    
    if time > 15:
        break
    # 벽이 캐릭터가 있는 칸으로 이동했는데, 가장 오른쪽이 아니라면
    if x - time > -1 and chess[x - time][y] == "#" and y != 7:
        continue

    for dx, dy in dxdy:
        _x, _y = x + dx, y + dy
        if not (0 <= _x < 8 and 0 <= _y < 8) or visited[_x][_y][time + 1]: continue
        # 이동할 곳이 벽이라면
        if _x - time > -1 and chess[_x - time][_y] == "#": continue
        q.append((_x, _y, time + 1))
        visited[_x][_y][time + 1] = True

    # 이동하지 않음
    q.append((x, y, time + 1))

print(answer)
