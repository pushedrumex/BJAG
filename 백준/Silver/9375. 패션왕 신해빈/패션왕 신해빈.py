from collections import defaultdict
T = int(input())
for _ in range(T):
    d = defaultdict(lambda:1)
    n = int(input())
    for _ in range(n):d[list(input().split())[1]]+=1
    d = list(dict(d).values())
    result = 1
    for i in d:result*=i
    print(result-1)