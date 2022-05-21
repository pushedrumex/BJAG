import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N,M,X = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    p1,p2,d = map(int,input().split())
    graph[p1].append((p2,d))

def disjkstra(start):
    q = []
    distance = [INF]*(N+1)
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
    return distance

start_X = disjkstra(X)
max_time = 0

for std in range(1,N+1):
    start_std = disjkstra(std)
    max_time = max(max_time,start_X[std]+start_std[X])
print(max_time)