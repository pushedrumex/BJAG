N, K = map(int, input().split())
stones = [0] + list(map(int, input().split()))

dp = [False] * (N+1)
dp[1] = True

for i in range(2, N+1):
    # i번째로 올 수 있는 지
    for k in range(1, min(K, i)):
        if dp[i-k] == True:
            if k * (1 + abs(stones[i]-stones[i-k])) <= K:
                dp[i] = True
                break


print("YES" if dp[N] else "NO")