import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input())
    total = 0
    coins = []
    for _ in range(N):
        coin, n = map(int, input().split())
        coins.append((coin, n))
        total += coin * n
        
    if total % 2 > 0:
        print(0)
        continue

    target = total // 2
    dp = [False] * (target+1)
    dp[0] = True
    for coin, n in coins:
        for j in range(target,coin-1,-1):
            if not dp[j]:
                for i in range(1, n+1):
                    if coin*i > j or dp[j]:
                        break
                    dp[j] = dp[j] or dp[j-coin*i]
            if dp[target]:
                break

        if dp[target]:
            break

    print(1 if dp[target] else 0)