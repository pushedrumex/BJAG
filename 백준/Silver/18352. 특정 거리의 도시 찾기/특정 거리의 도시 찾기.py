import sys, heapq
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [int(1e9)] * (N+1)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if dist > distance[node]:
            continue
        for i in graph[node]:
            d = dist + 1
            if d < distance[i]:
                distance[i] = d
                heapq.heappush(q, (d, i))
dijkstra(X)

flag = False
for i in range(1, N+1):
    if distance[i] == K:
        flag = True
        print(i)
if not flag:
    print(-1)