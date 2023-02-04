N = int(input())
k = int(input())

def bs(N, k, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        # mid보다 작은 수가 몇개인지
        count = 0
        for i in range(1, N+1):
            count += min(mid // i, N)
        if count < k:
            start = mid + 1
        else:
            result = mid
            end = mid - 1
    return result

# 최소 : 1, 최대 : N * N
print(bs(N, k, 1, N*N))