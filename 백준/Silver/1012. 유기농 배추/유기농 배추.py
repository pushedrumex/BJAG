import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    if x < 0 or y < 0 or x >= M or y >= N: return
    if not graph[y][x]: 
        graph[y][x] = True
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)

T = int(input())

for _ in range(T):
    result = 0
    M, N, K = map(int, input().split())
    graph = [[True] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = False
    for y in range(N):
        for x in range(M):
            if (not graph[y][x]):
                dfs(x, y)
                result += 1
    print(result)