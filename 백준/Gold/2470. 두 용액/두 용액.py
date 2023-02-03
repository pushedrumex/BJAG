# 투 포인터 알고리즘
# 절대값이 가장 비슷한 두 숫자의 최소 합

import sys
input = sys.stdin.readline

N = int(input())
sol = sorted(list(map(int, input().split())))

p1, p2 = 0, N-1
mix_min = abs(sol[p1] + sol[p2])
answer = [sol[p1], sol[p2]]

while p1 < p2:
    sol1, sol2 = sol[p1], sol[p2]
    temp = sol1 + sol2
    
    # 합이 음수인 경우
    # p2 이동 : 더 작은 음수
    # p1 이동 : 0이상의 정수
    if temp < 0: p1 += 1
        
    # 합이 0또는 양수인 경우
    # p1 이동 : 더 큰 양수
    # p2 이동 : 0이하의 정수
    else: p2 -= 1
    temp = abs(temp)
    if mix_min > temp:
        answer = [sol1, sol2]
        mix_min = temp

print(*answer)
