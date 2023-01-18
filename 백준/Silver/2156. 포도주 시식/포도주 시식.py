n = int(input())
amount = [int(input()) for _ in range(n)]

if n == 1:
    print(amount[0])
elif n == 2: 
    print(amount[0] + amount[1])
elif n == 3:
    print(max(amount[2] + amount[0], amount[2] + amount[1], amount[0] + amount[1]))
else:
    dp = [0] * n
    dp[0] = amount[0]
    dp[1] = amount[0] + amount[1]
    dp[2] = max(amount[2] + amount[0], amount[2] + amount[1], amount[0] + amount[1])

    for i in range(3, n):
        dp[i] = max(amount[i] + dp[i-2], amount[i] + amount[i-1] + dp[i-3], dp[i-1])

    print(dp[n-1])