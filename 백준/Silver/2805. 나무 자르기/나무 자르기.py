N, M = map(int, input().split())
Tree = list(map(int, input().split()))

start = 0
end = max(Tree)

while end >= start:
    sum = 0 # 최소
    mid = (end + start)//2 # 최대
    
    for l in Tree:
        if l > mid:sum += l-mid # 잘린 나무의 총 길이
            
    if sum > M : start = mid + 1; result = mid # 요청보다 많은게 답이 될 수 있음
    elif sum < M : end = mid - 1
    else: result = mid; break # 찾았다면 break
print(result)
