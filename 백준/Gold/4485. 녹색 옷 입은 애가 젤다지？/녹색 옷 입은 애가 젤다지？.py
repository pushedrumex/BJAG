from heapq import heappop, heappush
INF = int(1e9)
dydx = [(1,0), (-1,0), (0,1), (0,-1)]

def dijkstra():
    distance[1][1] = graph[0][0]
    q = []
    # (비용, y, x)
    heappush(q, (graph[0][0], 1, 1))
    while q:
        dist, y, x = heappop(q)
        if distance[y][x] < dist: continue
        for dy, dx in dydx:
            _y, _x = y + dy, x + dx
            if not (1 <= _y <= N and 1 <= _x <= N):
                continue
            d = dist + graph[_y-1][_x-1]
            if distance[_y][_x] > d:
                distance[_y][_x] = d
                heappush(q, (d, _y, _x))
num = 0
while True:
    N = int(input())
    num += 1
    if N == 0: break
    graph = [list(map(int, input().split())) for _ in range(N)]
    distance = [[INF for _ in range(N+1)] for _ in range(N+1)]
    dijkstra()
    print("Problem {0}: {1}".format(num, distance[N][N]))
