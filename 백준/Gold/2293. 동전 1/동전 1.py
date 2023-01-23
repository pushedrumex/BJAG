n,k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
# j와 coin이 같은 경우 dp[j-coin] = 1
dp = [1]+[0]*k

# 동전
for coin in coins:
    # 1~k
    for j in range(1, k+1):
        # 해당 동전을 포함해서 만들 수 있는 경우
        if j - coin >= 0:
            # 해당 동전이 없었던 경우의
수++
            dp[j] +=  dp[j-coin]
            
print(dp[k])
