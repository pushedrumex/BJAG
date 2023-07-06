N = int(input())

if N == 1:
    print(0)
    exit()

arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(N-1)]
K = int(input())

if N == 2:
    print(arr[1][0])
    exit()

dp1 = [int(1e9)] * (N+1)
dp1[1] = 0
dp1[2] = arr[1][0]

for i in range(3, N+1):
    dp1[i] = min(dp1[i-1] + arr[i-1][0], dp1[i-2] + arr[i-2][1])

if N == 3:
    print(dp1[3])
    exit()

answer = int(1e9)
for i in range(1, N-2):
    dp2 = [int(1e9)] * (N+1)
    dp2[i+3] = dp1[i] + K

    if i != N-3:
        dp2[i+4] = dp2[i+3] + arr[i+3][0]

    for j in range(i+5, N+1):
        dp2[j] = min(dp2[j-1] + arr[j-1][0], dp2[j-2] + arr[j-2][1])

    answer = min(answer, dp2[N], dp1[N])

print(answer)