from collections import deque

N,M = map(int,input().split())
miro = []
for _ in range(N):miro.append(list(input()))
q = deque([(0,0,1)])
miro[0][0] = '0'
dxdy = [(0,1),(1,0),(0,-1),(-1,0)]

while q:
    r,c,b = q.popleft()
    for dx,dy in dxdy:
        if 0<=r+dx<N and 0<=c+dy<M and miro[r+dx][c+dy] == '1':
            miro[r+dx][c+dy] = str(int(b)+1)
            q.append((r+dx,c+dy,str(int(b)+1)))

print(miro[N-1][M-1])