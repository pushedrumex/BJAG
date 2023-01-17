n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

for j in range(1, n):
    for i in range(j+1):
        if i == 0:
            triangle[j][i] += triangle[j-1][i]
        elif i == j:
            triangle[j][i] += triangle[j-1][i-1]
        else:
            triangle[j][i] += max(triangle[j-1][i-1], triangle[j-1][i])

print(max(triangle[n-1]))