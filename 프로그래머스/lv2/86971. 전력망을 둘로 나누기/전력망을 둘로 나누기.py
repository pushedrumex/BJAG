from collections import deque

def bfs(start, disconnect, tree, n):
    result = 0
    q = deque([start])
    visited = [False] * (n+1)
    
    while q:
        now = q.popleft()
        result += 1
        visited[now] = True
        for node in tree[now]:
            if node != disconnect and not visited[node]:
                q.append(node)
    return result

def solution(n, wires):
    answer = int(1e9)
    tree = [[] for _ in range(n+1)]

    for a, b in wires:
        tree[a].append(b)
        tree[b].append(a)

    for a, b in wires:
        answer = min(answer, abs(n - 2 * bfs(a, b, tree, n)))

    return answer    