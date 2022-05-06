K, N = map(int, input().split())
L = []
for _ in range(K):L.append(int(input()))

start = 1
end = sum(L)//N

while start <= end:
    sum = 0
    mid = (start + end)//2
    for l in L: sum += l//mid
    if sum >= N: start = mid + 1; result = mid
    elif sum < N: end = mid - 1
print(result)