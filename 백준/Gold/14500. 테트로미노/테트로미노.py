N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

direc = [(1,1), (1,-1), (-1,1), (-1,-1)]
blocks = [[(0,1), (0,2), (0,3)],
          [(0,1), (1,0), (1,1)],
          [(1,0), (2,0), (2,1)],
          [(1,0), (1,1), (2,1)],
          [(0,1), (1,1), (0,2)]]

result = 0

for i in range(N):
    for j in range(M):
        # 5개의 블럭
        for block in blocks:
            for direc_y, direc_x in direc:
                temp = paper[i][j]
                flag = 0
                for dy, dx in block:
                    _y, _x = i + direc_y*dy, j + direc_x*dx
                    if not (0 <= _y < N and 0 <= _x < M):
                        flag = 1
                        break
                    temp += paper[_y][_x]
                if flag == 0: result = max(result, temp)

                temp = paper[i][j]
                flag = 0
                for dx, dy in block:
                    _y, _x = i + direc_y*dy, j + direc_x*dx
                    if not (0 <= _y < N and 0 <= _x < M):
                        flag = 1
                        break
                    temp += paper[_y][_x]
                if flag == 0: result = max(result, temp)

print(result)