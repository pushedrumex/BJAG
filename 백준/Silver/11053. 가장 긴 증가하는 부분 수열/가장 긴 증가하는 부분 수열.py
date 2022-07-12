# 개수는 맞지만, 수열의 내용은 틀림

N = int(input())
A = list(map(int, input().split()))
LIS = [A[0]]
for i in A:
    if LIS[-1] == i:continue
    elif LIS[-1] < i:LIS.append(i) # 증가하는 수라면
    else: # 증가하는 수가 아니라면 LIS에서 i랑 같거나 가장 가까운 큰 수를 찾아서 교환
        left, right = 0, len(LIS)-1
        while left <= right:
            mid = (left + right) // 2
            if LIS[mid] < i: left = mid + 1
            else: right = mid - 1;result = mid
        LIS[result] = i
print(len(LIS))
