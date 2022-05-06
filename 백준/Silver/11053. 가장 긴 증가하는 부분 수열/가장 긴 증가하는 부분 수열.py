N = int(input())
A = list(map(int, input().split()))
LIS = [A[0]]
for i in A:
    if LIS[-1] == i:continue
    elif LIS[-1] < i:LIS.append(i)
    else:
        left, right = 0, len(LIS)-1
        while left <= right:
            mid = (left + right) // 2
            if LIS[mid] < i: left = mid + 1
            else: right = mid - 1;result = mid
        LIS[result] = i
print(len(LIS))