N = int(input())
A = list(map(int, input().split()))

LIS = [A[0]]

for i in A:
    # 나보다 더 크다면 바로 추가
    if LIS[-1] < i: LIS.append(i)
    # 나와 같다면 무시
    elif LIS[-1] == i: continue

    # 나보다 작다면 LIS 왼쪽부터 탐색해서 처음으로 나보다 큰 원소와 교환 
    else:
        left, right = 0, len(LIS) - 1
        while left<=right:
            mid = (left + right) // 2
            # 가운데 숫자가 나보다 작으면
            if LIS[mid] < i: left = mid + 1
            # 가운데 숫자가 나보다 크거나 같으면
            else: right = mid - 1;result = mid
        LIS[result] = i
print(len(LIS))

# 주의 : LIS 실제 원소들과는 다르지만 개수는 동일
