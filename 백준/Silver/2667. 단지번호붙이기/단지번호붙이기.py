N = int(input())
graph = []
for _ in range(N):graph.append(list(map(int,input())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    if x == N or y == N or x == -1 or y == -1 or graph[x][y] == 0:return 0 # 집이 아닌 경우 집 0개
    if graph[x][y] == 1:
        home = 1  # 내 집
        graph[x][y] = 0
        for i in range(4):
            home += dfs(x + dx[i],y + dy[i]) # 내 주변 집 개수 더하기
    return home

dangisu = 0
homes = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            dangisu += 1
            homes.append(dfs(i,j))
print(dangisu)
homes.sort()
for i in homes:print(i)
