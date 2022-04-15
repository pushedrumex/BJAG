N,M = map(int,input().split())
r,c,d = map(int,input().split())
map = [list(map(int,input().split())) for _ in range(N)]
dxdy = {0:[-1,0],1:[0,1],2:[1,0],3:[0,-1]}
map[r][c] = -1 # 청소한 부분
clean = 1
rotate = 0 # 회전 횟수

while True:
    d = (3+d)%4 # 0 3 2 1
    rotate += 1
    if map[r+dxdy[d][0]][c+dxdy[d][1]] == 0:
        map[r+dxdy[d][0]][c+dxdy[d][1]] = -1
        r += dxdy[d][0];c += dxdy[d][1]
        rotate = 0;clean += 1
    if rotate == 4:
        if map[r-dxdy[d][0]][c-dxdy[d][1]] == -1:
            r -= dxdy[d][0];c -= dxdy[d][1]
            rotate = 0
        else: print(clean);break
