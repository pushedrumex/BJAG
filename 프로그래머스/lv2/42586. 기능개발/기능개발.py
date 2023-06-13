import math
from collections import deque

def solution(progresses, speeds):
    N = len(progresses)
    q = deque()
    for i in range(N):
        q.append(math.ceil((100-progresses[i])/speeds[i]))
        
    answer = []
    while q:
        N = q.popleft()
        day = 1
        while q and q[0]<=N:
            q.popleft()
            day+=1
        answer.append(day)
    return answer