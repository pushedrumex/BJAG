import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

N, E = map(int, input().split())

graph = [[]  for _ in range(N+1)]

for _ in range(E):
    a,b,c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start, end):
    q = []
    distance = [INF] * (N+1)
    heapq.heappush(q, (0, start))
    while q:
        dist, node = heapq.heappop(q)
        if dist > distance[node]:
            continue
        if node == end:
            return dist
        for _node, _dist in graph[node]:
            d = dist + _dist
            if distance[_node] > d:
                distance[_node] = d
                heapq.heappush(q, (d, _node))
    return INF

v1_v2 = dijkstra(v1, v2)

result = v1_v2 + min(dijkstra(1, v1) + dijkstra(v2, N), dijkstra(1, v2) + dijkstra(v1, N))

if result >= INF:
    print(-1)
else:
    print(result)