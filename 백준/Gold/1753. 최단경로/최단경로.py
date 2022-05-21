import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

V,E = map(int,input().split())
start = int(input())

graph = [[] for _ in range(V+1)]
distance = [INF]*(V+1)

for _ in range(E):
    p1,p2,d = map(int,input().split())
    graph[p1].append((p2,d))

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))

    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:continue
        for i in graph[now]:
            d = dist + i[1]
            if d < distance[i[0]]:
                distance[i[0]] = d
                heapq.heappush(q,(d,i[0]))

dijkstra(start)

for i in range(1,V+1):
    if distance[i] == INF:print("INF")
    else:print(distance[i])