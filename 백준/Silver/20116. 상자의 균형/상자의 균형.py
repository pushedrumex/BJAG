n, L = map(int, input().split())
arr = list(map(int, input().split()))

answer = "stable"

count = 1
m = 0
for i in range(n-1, 0, -1):
    m += arr[i]
    if not (arr[i-1] - L < m / count < arr[i-1] + L):
        answer = "unstable"
        break
    count += 1

print(answer)