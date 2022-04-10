N = int(input())

d = [0] + list(map(int,input().split()))

for i in range(2,N+1):   # 2개부터 차례대로 최대금액 찾기
    for j in range(i//2 + 1):
        if d[i] < d[j] + d[i-j]:d[i] = d[j] + d[i-j]
            
print(d[N])
