N, M = map(int, input().split())
graph = [[0] * N for _ in range(N)]

for _ in range(M):
    short, tall = map(int, input().split())
    graph[short-1][tall-1] = 1

for k in range(N):
    for p1 in range(N):
        for p2 in range(N):
            if (graph[p1][k] + graph[k][p2]) == 2:
                graph[p1][p2] = 1

result = 0
for p1 in range(N):
    check = 0
    for p2 in range(N):
        check += graph[p1][p2] + graph[p2][p1]
    if check == N-1:
        result += 1
    
print(result)