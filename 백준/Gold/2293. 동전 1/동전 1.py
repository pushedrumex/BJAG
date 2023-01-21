n,k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [1]+[0]*k

for coin in coins:
    for j in range(1, k+1):
        if j - coin >= 0:
            dp[j] +=  dp[j-coin]
            
print(dp[k])