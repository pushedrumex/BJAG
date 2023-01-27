import sys
input = sys.stdin.readline
from heapq import heappop, heappush

n = int(input())
m = int(input())
INF = int(1e9)

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    p1, p2, d = map(int, input().split())
    graph[p1].append((p2, d))

start, end = map(int, input().split())

def dijkstra(start, end):
    q = []
    heappush(q, (0, start, [start]))
    distance[start] = 0
    while q:
        dist, node, path = heappop(q)
        if distance[node] < dist:
            continue
        if node == end:
            return dist, path
        for _node, _dist in graph[node]:
            d = dist + _dist
            if distance[_node] > d:
                distance[_node] = d
                heappush(q, (d, _node, path + [_node]))
    return INF

dist, path = dijkstra(start, end)
print(dist)
print(len(path))
print(*path)