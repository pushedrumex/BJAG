N = int(input())
graph = [[0] * (N+1)]

for _ in range(N):
    graph.append([0] + list(map(int, input().split())))

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for row in graph[1:]:
    print(*row[1:])