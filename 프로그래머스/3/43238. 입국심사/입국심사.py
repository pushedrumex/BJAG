def solution(n, times):
    left, right = 1, min(times) * n
    while left <= right:
        mid = (left + right) // 2
        count = 0
        for time in times:
            count += mid // time
        if count < n:
            left = mid + 1
        else:
            right = mid - 1
            answer = mid
            
    return answer