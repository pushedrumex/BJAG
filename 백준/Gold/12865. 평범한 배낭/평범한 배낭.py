# 이중 dp -> n : 탐색 진행도, k : 무게

N, K = map(int, input().split())
good = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(K+1) for _ in range(N+1)]

# 탐색 진행도
for n in range(1, N+1):
    w, v = good[n-1][0], good[n-1][1]
    # 무게
    for k in range(1, K+1):
        # 가방에 담을 수 없다면 -> 담지 않는다
        if k < w:
            dp[n][k] = dp[n-1][k]
        # 가방에 담을 수 있다면 -> 담지 않는것 vs 담는 것
        else:
            dp[n][k] = max(dp[n-1][k], dp[n-1][k-w]+v)

print(dp[n][k])