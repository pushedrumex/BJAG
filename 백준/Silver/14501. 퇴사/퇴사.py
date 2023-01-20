N = int(input())
works = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N+2)

# 일을 선택할지 말지를 판단하기 위해 끝 날짜부터 
for i in range(N, 0, -1):
    t, p = works[i-1]
    # 가능한 일이라면
    # 선택 or not
    if i+t-1 <= N:
        dp[i] = max(dp[i+t] + p, dp[i+1])
    # 불가능한 일이라면
    else:
        dp[i] = dp[i+1]
print(dp[1])
