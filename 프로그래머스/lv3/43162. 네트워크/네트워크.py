from collections import deque

def bfs(node, graph, visited):
    q = deque([node])
    visited[node] = True
    while q:
        node = q.popleft()
        for _node in graph[node]:
            if not visited[_node]:
                visited[_node] = True
                q.append(_node)

def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [False] * n
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                graph[i].append(j)
    for i in range(n):
        if not visited[i]:
            answer += 1
            bfs(i, graph, visited)
    return answer