str1 = input()
str2 = input()

len1 = len(str1)
len2 = len(str2)

dp = [[0]*(len1+1) for _ in range(len2+1)]

for i in range(1, len1+1):
    for j in range(1, len2+1):
        # 같은 알파벳이라면
        # 알파벳 추가 전의 값 + 1
        if str1[i-1] == str2[j-1]:
            dp[j][i] = dp[j-1][i-1] + 1
        # 같은 알파벳이 아니라면
        # 현재까지의 값 중 가장 큰 값
        else:
            dp[j][i] = max(dp[j-1][i], dp[j][i-1])
print(dp[j][i])
