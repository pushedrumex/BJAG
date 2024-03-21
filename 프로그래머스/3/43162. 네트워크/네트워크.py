from collections import deque

linked = None
def solution(n, computers):
    global linked
    
    answer = 0
    linked = [False] * n
    for i in range(n):
        if linked[i] == False:
            linked[i] = True
            bfs(i, n, computers)
            answer += 1
    return answer

def bfs(i, n, computers):
    q = deque([i])
    while q:
        i = q.popleft()
        for j in range(n):
            if computers[i][j] == 1 and not linked[j]:
                linked[j] = True
                q.append(j)
    