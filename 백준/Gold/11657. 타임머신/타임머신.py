INF = int(1e9)
N, M = map(int, input().split())

edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

def bellmanFord():
    for i in range(N):
        for a, b, c in edges:
            cost = distance[a] + c
            if distance[a] != INF and distance[b] > cost:
                distance[b] = cost
                if i == N-1:
                    return True
    return False

distance = [INF] * (N+1)
distance[1] = 0

if bellmanFord():
    print(-1)
else:
    for i in range(2, N+1):
        print(distance[i] if distance[i] < INF else -1)