n = int(input())
dp = list(map(int,input().split()))

# 왼쪽부터 쭉 더해가면서 확인
# 앞 부분의 연속합들을 포함하고 갈 지, 아니면 내 자신부터 다시 시작할 지 선택
# 각 dp에는 왼쪽부터 시작하여 내 자신을 포함하여 가장 큰 연속합이 저장

for i in range(1,n):
    dp[i] = max(dp[i],dp[i]+dp[i-1])
print(max(dp))
