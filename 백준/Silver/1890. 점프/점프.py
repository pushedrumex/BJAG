from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for x in range(N):
    for y in range(N):
        if dp[x][y] > 0 and arr[x][y] > 0:
            
            _x, _y = x + arr[x][y], y
            if 0 <= _x < N and 0 <= _y < N:
                dp[_x][_y] += dp[x][y]

            _x, _y = x , y + arr[x][y]
            if 0 <= _x < N and 0 <= _y < N:
                dp[_x][_y] += dp[x][y]

print(dp[N-1][N-1])