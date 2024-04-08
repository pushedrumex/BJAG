N = int(input())
graph = [[] for _ in range(N+1)]
edges = []
for _ in range(N-1):
    a, b = map(int, input().split())
    edges.append((a, b))
    graph[a].append(b)
    graph[b].append(a)

q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    if t == 1:
        if len(graph[k]) > 1:
            print("yes")
        else:
            print("no")
    elif t == 2:
        print("yes")