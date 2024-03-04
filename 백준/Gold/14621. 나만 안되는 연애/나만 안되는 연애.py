from heapq import heappush, heappop

N, M = map(int, input().split())
school = [""] + input().split()
graph = [[] for _ in range(N+1)]
q = []
for _ in range(M):
    u, v, d = map(int, input().split())
    if school[v] != school[u]:
        heappush(q, (d, u, v))

# 남여가 번갈아 가면서 이어져야함
# 모든 대학교는 이어져야함
# 최단 거리여야함

parent = [0] * (N+1)
for i in range(1, N+1):
    parent[i] = i

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    ap = find_parent(a)
    bp = find_parent(b)
    if ap > bp: parent[bp] = ap
    else: parent[ap] = bp

visited = [0] * (N+1)
answer = 0
while q:
    d, u, v = heappop(q)
    if find_parent(u) != find_parent(v):
        union_parent(u, v)
        visited[u] = 1
        visited[v] = 1
        answer += d

print(answer if sum(visited) == N else -1)
