from collections import deque

N,K = map(int,input().split())
q = deque([(N,0)])
visit = [False]*100001

if K<N:print(N-K);exit()

while q:
    N,t = q.popleft()

    if N == K:print(t);break

    for a,b in ((N*2,0),(N-1,1),(N+1,1),(N*2,0)):
        if 0<=a<=100000 and not visit[a]:
            q.append((a,t+b))
            visit[a] = True