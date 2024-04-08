import sys
input = sys.stdin.readline

N = int(input())
planets = []
for i in range(N):
    x, y, z = map(int, input().split())
    planets.append((i, x, y, z))

edges = []
planets.sort(key=lambda p: p[1])
for i in range(N-1):
    n1, x1, y1, z1 = planets[i]
    n2, x2, y2, z2 = planets[i+1]
    edges.append((abs(x1-x2), n1, n2))

planets.sort(key=lambda p: p[2])
for i in range(N-1):
    n1, x1, y1, z1 = planets[i]
    n2, x2, y2, z2 = planets[i+1]
    edges.append((abs(y1-y2), n1, n2))

planets.sort(key=lambda p: p[3])
for i in range(N-1):
    n1, x1, y1, z1 = planets[i]
    n2, x2, y2, z2 = planets[i+1]
    edges.append((abs(z1-z2), n1, n2))

parent = [0] * (N)
for i in range(N):
    parent[i] = i

def find_parent(node):
    if parent[node] != node:
        parent[node] = find_parent(parent[node])
    return parent[node]

def union(parent1, parent2):
    if parent1 > parent2:
        parent[parent2] = parent1
    else:
        parent[parent1] = parent2

answer = 0
edges.sort()
for cost, node1, node2 in edges:
    parent1, parent2 = find_parent(node1), find_parent(node2)
    if parent1 != parent2:
        union(parent1, parent2)
        answer += cost

print(answer)