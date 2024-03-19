n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

INF = int(1e9)
dp = [INF] * (100_000 + 1)
for coin in coins:
    dp[coin] = 1
    for i in range(coin+1, k+1):
        dp[i] = min(dp[i], dp[i-coin] + 1)

print(dp[k] if dp[k] != INF else -1)