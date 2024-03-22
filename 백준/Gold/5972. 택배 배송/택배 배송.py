# 다익스트라
from heapq import heappush, heappop

N, M = map(int, input().split())
INF = int(1e9)
distance =[INF] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

q = []
# 비용, 지점
heappush(q, (0, 1))
distance[1] = 0
while q:
    dist, now = heappop(q)
    if distance[now] < dist:
        continue

    for x, d in graph[now]:
        _dist = dist + d
        if distance[x] > _dist:
            distance[x] = _dist
            heappush(q, (_dist, x))

print(distance[N])