N = int(input())
A = list(map(int, input().split()))
M = int(input())

start = 1
end = max(A)

while start <= end:
    sum = 0
    mid = (start + end) // 2
    for i in A:
        if i > mid: sum += mid
        else: sum += i
    if sum > M: end = mid - 1
    elif sum <= M: start = mid + 1; result = mid
print(result)