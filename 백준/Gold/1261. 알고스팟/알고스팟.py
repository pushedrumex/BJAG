from collections import deque

N,M = map(int,input().split())
miro = []
block = [[int(1e9)]*N for _ in range(M)]
block[0][0] = 0
for _ in range(M):miro.append(input())
dxdy = [(1,0),(0,1),(-1,0),(0,-1)]

q = deque([(0,0,0)]) # 행,열,벽

while q:
    r,c,b = q.popleft()
    for dx,dy in dxdy:
        if 0<=r+dx<M and 0<=c+dy<N and block[r+dx][c+dy]>b+int(miro[r+dx][c+dy]):
            block[r+dx][c+dy] = b+int(miro[r+dx][c+dy])
            q.append((r+dx,c+dy,b+int(miro[r+dx][c+dy])))
print(block[M-1][N-1])