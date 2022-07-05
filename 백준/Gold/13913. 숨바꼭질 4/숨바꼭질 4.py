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

# 100000 0 의 경우, 경로가 저장되는 a[2]의 크기가 1,2,3,4,..., 100001로 증가
# q에 append를 해주는 과정에서 a[2]의 크기가 클 수록 시간 오래걸림!! -> 시간초과
