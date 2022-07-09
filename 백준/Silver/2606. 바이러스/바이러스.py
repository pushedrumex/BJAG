N = int(input())
M = int(input())

net = [[] for _ in range(N+1)]
visit = [False]*(N+1)

for _ in range(M):
    a,b = map(int,input().split())
    net[a].append(b)
    net[b].append(a)

def dfs(n):
    if not visit[n]:
        visit[n] = True
        for x in net[n]:dfs(x)
dfs(1)
print(visit.count(True)-1)