n, k = map(int, input().split())

coins = set([int(input()) for _ in range(n)])

dp = [int(1e9)] * (k+1)
for coin in coins:
    if coin <= k:
        dp[coin] = 1

for i in range(1, k+1):
    for coin in coins:
        if coin <= i:
            dp[i] = min(dp[i], dp[i-coin] + 1)

if dp[k] >= int(1e9):
    print(-1)
else:
    print(dp[k])