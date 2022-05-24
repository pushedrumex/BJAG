from collections import deque

def bfs(graph,start,visited):
    visited[start] = 0
    q = deque()
    q.append(start)
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == False:
                q.append(i)
                if visited[v] == 0:
                    visited[i] = 1
                else:visited[i] = 0
            elif visited[i] == visited[v]:
                return "NO"
    return "YES"

K = int(input())
 
for _ in range(K):
    V,E = map(int,input().split())
    visited = [False]*(V+1)
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1,V+1):
        if not visited[i]:
            result = bfs(graph,i,visited)
        if result == "NO":break
    print(result)