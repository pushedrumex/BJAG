N = int(input())
if N == 1:print(3);exit()
dp = [0]*(N+1)
dp[1] = 3
dp[2] = 7
for i in range(3,N+1):
    dp[i] = 3*dp[i-1] - (dp[i-1] - dp[i-2])
# 00 01 10 이 추가되는 경우의 수 - (i-1)칸이 00 일때를 제외한 경우의 수
# i와 i-1칸에 세로로 연속으로 채워지는 경우의 수를 빼준 
print(dp[N]%9901)
