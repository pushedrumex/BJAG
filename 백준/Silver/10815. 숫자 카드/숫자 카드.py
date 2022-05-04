from collections import defaultdict
d = defaultdict(int)

N = int(input())
n = list(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))

for i in n: d[i] = 1
for i in m:
    if d[i] == 1:print(1, end = " ")
    else: print(0, end=" ")