C, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
INF = int(1e9)

# i명 일 때의 최소 비용
dp = [int(1e9)] * (10001)
dp[0] = 0
for cost, count in arr:
    for i in range(count, 10001):
        dp[i] = min(dp[i-count]+cost, dp[i])

print(min(dp[C:]))