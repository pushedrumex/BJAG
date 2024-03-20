from collections import deque

N = int(input())
M = int(input())

link = [list(map(int, input().split())) for _ in range(N)]
spot = list(map(int, input().split()))

start = spot[0]-1
visited = [False] * N

q = deque([start])
visited[start] = True
while q:
    x = q.popleft()
    for i in range(N):
        if link[x][i] == 1 and not visited[i]:
            visited[i] = True
            q.append(i)

for x in spot:
    if visited[x-1] == False:
        print("NO")
        exit()

print("YES")    