N = int(input())
A = list(map(int, input().split()))

LIS = [A[0]]

for i in A:
    if LIS[-1] < i:LIS.append(i)
    elif LIS[-1] == i:continue
    else:
        left = 0
        right = len(LIS)

        while left<right:
            mid = (left + right) // 2
            if LIS[mid] < i: left = mid + 1
            else: right = mid
        LIS[right] = i
print(len(LIS))