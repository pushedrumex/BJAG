N,K = map(int,input().split())
d = []
coin = 0
for _ in range(N): d.append(int(input()))
while K:
    coin += K//d[-1]
    K = K%d.pop()
print(coin)