K, N = map(int, input().split())
L = []
for _ in range(K):L.append(int(input()))

start = 1 # 최소
end = sum(L)//N # 최대

while start <= end:
    sum = 0
    mid = (start + end)//2
    
    for l in L: sum += l//mid # 총 랜선 길이
        
    if sum >= N: start = mid + 1; result = mid 
    # 필요한 랜선 개수보다 많거나 같으면 답이 될 수 있음
    elif sum < N: end = mid - 1
        
print(result)
