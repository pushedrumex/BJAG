import sys
input = sys.stdin.readline

N = int(input())

# T: 기간, P: 금액
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (N+1)
t, p = arr[-1]
if t == 1:
    dp[N] = p
    
for i in range(N-1, 0, -1):
    t, p = arr[i-1]
    end = i+t-1
    if end > N:
        dp[i] = dp[i+1]
        continue

    dp[i] = max(dp[i+1], (0 if end >= N else dp[end+1])+p)

print(dp[1])