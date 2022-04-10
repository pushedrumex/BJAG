import sys

T = int(input())
d = [[0]*4 for _ in range(100001)]
d[1] = [0,1,0,0]
d[2] = [0,0,1,0]
d[3] = [0,1,1,1]
for i in range(4,100001):
    d[i][1] = (d[i-1][2] + d[i-1][3])%1000000009
    d[i][2] = (d[i-2][1] + d[i-2][3])%1000000009
    d[i][3] = (d[i-3][1] + d[i-3][2])%1000000009
for _ in range(T):
    n = int(sys.stdin.readline().strip())
    print(sum(d[n])%1000000009)