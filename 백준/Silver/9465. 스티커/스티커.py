T = int(input())
for _ in range(T):
    n = int(input())
    dp = []
    for _ in range(2):
        dp.append(list(map(int,input().split())))
    if n == 1:
        print(max(dp[0][0],dp[1][0]))
        continue
    dp[0][1]+=dp[1][0]
    dp[1][1]+=dp[0][0]
    for i in range(2,n):
        dp[0][i]+=max(dp[1][i-1],dp[1][i-2])
        dp[1][i]+=max(dp[0][i-1],dp[0][i-2])
    print(max(dp[0][n-1],dp[1][n-1]))
# 001  101  010  100
# 100  010  101  001

# 가장 큰 경우를 선택
