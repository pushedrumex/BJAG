n,k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
# j와 coin이 같은 경우 = 1
dp = [1]+[0]*k

# 동전
for coin in coins:
    # 1~k
    for j in range(1, k+1):
        # 해당 동전 포함이 가능한 경우
        if j - coin >= 0:
            dp[j] +=  dp[j-coin]
            
print(dp[k])
