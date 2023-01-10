from collections import defaultdict, deque

def bfs(V):
    queue = deque([V])
    visited[V] = True # 시작 노드 방문 기록
    while queue:
        node = queue.popleft()
        visited[node] = True
        print(node, end=" ")
        for n in sorted(dic[node]):
            if not visited[n]:
                queue.append(n)
                visited[n] = True
                # 동일한 노드가 큐에 들어가는 것을 방지하기 위해 이 부분에서 방문처리
                

def dfs(V):
    visited[V] = True
    print(V, end=" ")
    for n in sorted(dic[V]):
        if not visited[n]:
            dfs(n)

dic = defaultdict(lambda: [])
N, M, V = map(int, input().split())

for _ in range(M):
    node1, node2 = map(int, input().split())
    dic[node1].append(node2)
    dic[node2].append(node1)

visited = [False] * (N + 1)
dfs(V)
print()
visited = [False] * (N + 1)
bfs(V)