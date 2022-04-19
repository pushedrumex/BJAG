from collections import deque

N,M,V = map(int,input().split())
graph = []
for _ in range(N+1):graph.append([])

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(len(graph)):graph[i].sort()
visited_dfs = [False]*(N+1)
visited_bfs = [False]*(N+1)

def dfs(graph,V,visited):
    visited[V] = True
    print(V,end=" ")
    for i in graph[V]:
        if visited[i] == False:dfs(graph,i,visited)

def bfs(graph,V,visited):
    queue = deque()
    queue.append(V)
    visited[V] = True
    while queue:
        k = queue.popleft()
        print(k,end=" ")
        for i in graph[k]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

dfs(graph,V,visited_dfs)
print()
bfs(graph,V,visited_bfs)