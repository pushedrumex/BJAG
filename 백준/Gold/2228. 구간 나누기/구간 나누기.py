INF = int(1e9)
N, M = map(int, input().split())

dp1 = [[0] + [-INF] * M for _ in range(N+1)]
dp2 = [[0] + [-INF] * M for _ in range(N+1)]

for i in range(1, N+1):
    num = int(input())
    for j in range(1, min(M, (i+1) // 2) + 1):
        dp1[i][j] = max(dp1[i-1][j], dp2[i-1][j])
        dp2[i][j] = max(dp2[i-1][j], dp1[i-1][j-1]) + num

print(max(dp1[N][M], dp2[N][M]))