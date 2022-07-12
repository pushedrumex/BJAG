N = int(input())
dp = [int(1e9)]*(N+1)

for i in range(1,N+1):
    if i**0.5 == int(i**0.5):dp[i] = 1
    else:
        for k in range(1,i//2+1):
            dp[i] = min(dp[k]+dp[i-k],dp[i])
print(dp[N])