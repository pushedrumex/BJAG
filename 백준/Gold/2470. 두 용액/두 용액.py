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
    if temp < 0: p1 += 1
    else: p2 -= 1
    temp = abs(temp)
    if mix_min > temp:
        answer = [sol1, sol2]
        mix_min = temp

print(*answer)