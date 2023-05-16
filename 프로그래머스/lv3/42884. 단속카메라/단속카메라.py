from collections import deque

def solution(routes):
    answer = 0
    routes.sort(key=lambda x:(x[1], [0]))
    q = deque(routes)
    print(q)
    while q:
        answer += 1
        start, end = q.popleft()
        while q and q[0][0] <= end:
            q.popleft()
    return answer