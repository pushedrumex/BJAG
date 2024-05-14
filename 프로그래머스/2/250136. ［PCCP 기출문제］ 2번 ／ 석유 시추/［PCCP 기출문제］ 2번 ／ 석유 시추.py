from collections import deque

dxdy = ((1, 0), (-1, 0), (0, 1), (0, -1))
def solution(land):
    n, m = len(land), len(land[0])
    
    record = {}
    oil_land = [[0] * m for _ in range(n)]
    oil_num = 1
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                oil_land[i][j] = oil_num
                size = 1
                land[i][j] = 0
                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    for dx, dy in dxdy:
                        _x = x + dx
                        _y = y + dy
                        if not (0 <= _x < n and 0 <= _y < m): continue
                        if land[_x][_y] == 0: continue
                        land[_x][_y] = 0
                        size += 1
                        oil_land[_x][_y] = oil_num
                        q.append((_x, _y))
                        
                record[oil_num] = size
                oil_num += 1
                
    answer = 0
    for j in range(m):
        size = 0
        visited = {}
        for i in range(n):
            oil_num = oil_land[i][j]
            if oil_num > 0 and oil_num not in visited:
                visited[oil_num] = True
                size += record[oil_num] 
        answer = max(answer, size)
    return answer