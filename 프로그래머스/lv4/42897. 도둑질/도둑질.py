def solution(money):
    N = len(money)
    dp1 = [0] * N
    dp2 = [0] * N
    
    dp1[0], dp1[1] = money[0], max(money[:2])
    dp2[1], dp2[2] = money[1], max(money[1:3])
    
    # 첫번째 집 포함
    for i in range(2, N):
        dp1[i] = max(money[i]+dp1[i-2], dp1[i-1])
    # 첫번째 집 불포함
    for i in range(3, N):
        dp2[i] = max(money[i]+dp2[i-2], dp2[i-1])
    
    return max(dp1[N-2], dp2[N-1])