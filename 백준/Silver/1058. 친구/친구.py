# 나랑 친구이거나 내 친구의 친구
from collections import deque

N = int(input())
friends= [[] for _ in range(N)]
for i in range(N):
    arr = list(input())
    for j in range(N):
        if arr[j] == "Y":
            friends[i].append(j)

def bfs(me):
    result = 0
    q = deque([(0, me)])
    visited = [False] * N
    visited[me] = True

    while q:
        degree, friend = q.popleft()
        for x in friends[friend]:
            if visited[x]: continue
            visited[x] = True
            result += 1
            if degree < 1:
                q.append((degree+1, x))

    return result

answer = 0
for i in range(N):
    answer = max(answer, bfs(i))

print(answer)