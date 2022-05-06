N, M = map(int, input().split())
Tree = list(map(int, input().split()))

start = 0
end = max(Tree)

while end >= start:
    sum = 0
    mid = (end + start)//2
    for l in Tree:
        if l > mid:sum += l-mid
    if sum > M : start = mid + 1;result = mid
    elif sum < M : end = mid - 1
    else: result = mid; break
print(result)