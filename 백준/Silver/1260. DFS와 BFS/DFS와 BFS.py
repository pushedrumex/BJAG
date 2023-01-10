from collections import defaultdict, deque

def bfs(start, dic):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for n in sorted(dic[node]):
            if not visited[n]:
                visited[n] = True
                queue.append(n)

def dfs(start, dic):
    visited[start] = True
    print(start, end=" ")
    for n in sorted(dic[start]):
        if not visited[n]:
            visited[n] = True
            dfs(n, dic)


dic = defaultdict(lambda: [])
N, M, V = map(int, input().split())

for _ in range(M):
    node1, node2 = map(int, input().split())
    dic[node1].append(node2)
    dic[node2].append(node1)

visited = [False] * (N + 1)
dfs(V, dic)
print()
visited = [False] * (N + 1)
bfs(V, dic)