from collections import deque

def solution(priorities, location):
    dic = {}
    N = len(priorities)
    
    for i in range(N):
        dic[i] = priorities[i]

    q = deque(list(range(N)))
    while q:
        flag = True
        process = q.popleft()
        for _process in q:
            if dic[_process] > dic[process]:
                q.append(process)
                flag = False
                break

        if flag and process == location:
            return N - len(q)