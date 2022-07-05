from collections import deque
N,K = map(int,input().split())

if N>K:
    print(N-K)
    print(*list(range(N,K-1,-1)))
    exit()

check = [False]*100001
check[N] == True
q = deque([(N,0,[N])])

while q:
    a = q.popleft()
    if a[0] == K:
        print(a[1])
        print(*a[2])
        break
    for i in (a[0]-1,a[0]+1,a[0]*2):
        if 0<=i<=100000 and not check[i]:
            q.append((i,a[1]+1,a[2]+[i]))
            check[i] = True
