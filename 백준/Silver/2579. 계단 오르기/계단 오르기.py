N = int(input())
floor = [0]
for _ in range(N):floor.append(int(input()))

dp = [0]*(N+1)
dp[1] = floor[1]

for i in range(2,N+1):
    dp[i] = max(dp[i-2],dp[i-3]+floor[i-1])+floor[i]
print(dp[N])