from collections import deque

S = int(input())
visited = [0]*1001
visited[1] = 1
q = deque([(1,0,0)]) # 현재, 보드, 시간

while q:
    a = q.popleft()
    if a[0] == S:print(a[2]);break

    if 1<a[0] and visited[a[0]-1]<1000:
        q.append((a[0]-1,a[1],a[2]+1))
        visited[a[0]-1]+=1 

    if a[1] and a[0]+a[1]<=1000 and visited[a[0]+a[1]]<1000:
        q.append((a[0]+a[1],a[1],a[2]+1))
        visited[a[0]+a[1]]+=1

    q.append((a[0],a[0],a[2]+1))