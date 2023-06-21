N, M = map(int, input().split())
arr = [[0] * (M+1)]
for _ in range(N):
    arr.append([0] + list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, M+1):
        arr[i][j] += arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1]
        
answer = -10000
for i in range(1, N+1):
    for j in range(1, M+1):
        for x in range(i, N+1):
            for y in range(j, M+1):
                temp = arr[x][y] - arr[i-1][y] - arr[x][j-1] + arr[i-1][j-1]
                answer = max(answer, temp)

print(answer)