from collections import defaultdict
N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))
d = defaultdict(int)
for i in A:
    d[i] = 1
for i in B: print(d[i])