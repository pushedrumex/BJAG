from collections import deque

N,K = map(int,input().split())
if N == K:print(0);exit()
check = [False]*100001
check[N] = True
q = deque([(N,0)])

while True:
    a = q.popleft()
    if a[0] == K:print(a[1]);break

    if a[0]>0 and not check[a[0]-1]:
        q.append((a[0]-1,a[1]+1))
        check[a[0]-1] = True

    if a[0]<100000 and not check[a[0]+1]:
        q.append((a[0]+1,a[1]+1))
        check[a[0]+1] = True
    
    if a[0]*2<100001 and not check[a[0]*2]:
        q.append((a[0]*2,a[1]+1))
        check[a[0]*2] = True