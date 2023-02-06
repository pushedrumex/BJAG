# tip : 두 카드 묶음을 섞음 == 새로운 카드 묶음이 생성

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    heappush(q, int(input()))

result = 0
while len(q) > 1:
    mix = heappop(q) + heappop(q)
    result += mix
    heappush(q, mix)

print(result)
