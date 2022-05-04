import sys
from collections import defaultdict
d = defaultdict(int)
N, M = map(int,input().split())
HS = []
for _ in range(N):d[sys.stdin.readline().rstrip()] = 1
for _ in range(M):
    name = sys.stdin.readline().rstrip()
    if d[name] == 1: HS.append(name)
HS.sort()
print(len(HS))
for i in HS:print(i)