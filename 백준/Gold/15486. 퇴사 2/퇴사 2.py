N = int(input())
arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]

answer = 0
dp = [0] * (N+1)
t,p = arr[N]
# 마지막날 상담 가능하다면
if t + N - 1 <= N:
    dp[N] = p

for day in range(N-1, 0, -1):
    t,p = arr[day]
    if day+t-1 > N:
        dp[day] = dp[day+1]
        continue
    if day+t > N:
        temp = 0
    else:
        temp = dp[day+t]
    dp[day] = max(p + temp, dp[day+1])

print(dp[1])