import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())

distance = [INF]*(N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    p1,p2,d = map(int,input().split())
    graph[p1].append((p2,d))

start,end = map(int,input().split())

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        dist,now = heapq.heappop(q)
        if dist > distance[now]:continue
        for i in graph[now]:
            d = dist + i[1]
            if d < distance[i[0]]:
                distance[i[0]] = d
                heapq.heappush(q,(d,i[0]))
dijkstra(start)
print(distance[end])