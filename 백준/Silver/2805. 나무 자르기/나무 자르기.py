N, M = map(int, input().split())
Tree = list(map(int, input().split()))

start = 0
end = max(Tree)

while end >= start:
    sum = 0
    mid = (end + start)//2
    for l in Tree:
        if l > mid:sum += l-mid
    if sum > M : start = mid + 1
    elif sum < M : end = mid - 1
    else: break
if sum < M: mid -= 1 # start == end 이고 sum < M 일때 예외처리
print(mid)
