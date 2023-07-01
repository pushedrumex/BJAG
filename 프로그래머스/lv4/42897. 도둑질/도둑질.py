def solution(money):
    N = len(money)
    dp1 = [0] * N
    dp2 = [0] * N
    dp1[0] = money[0]
    
    for i in range(N-1):
        dp1[i] = max(money[i] + dp1[i-2], dp1[i-1])
        
    for i in range(1, N):
        dp2[i] = max(money[i] + dp2[i-2], dp2[i-1])

    return max(dp1[N-2], dp2[N-1])