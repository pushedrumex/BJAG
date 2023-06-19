N, M = map(int, input().split())
arr = [[0] * (M+1)]

for _ in range(N):
    arr.append([0] + list(map(int, input().split())))

# 누적합 구하기
for i in range(1, N+1):
    for j in range(1, M+1):
        arr[i][j] += arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1]
        
K = int(input())

for _ in range(K):
    i, j, x, y = map(int, input().split())
    
    answer = arr[x][y] - arr[i-1][y] - arr[x][j-1] + arr[i-1][j-1]
    
    print(answer)