from collections import defaultdict
T = int(input())
for _ in range(T):
    d = defaultdict(int)
    n = int(input())
    
    for _ in range(n):d[list(input().split())[1]]+=1
        
    d = list(dict(d).values())
    result = 1
    for i in d:result*=(i+1)
    # 선택하지 않는 경우 +1
    print(result-1)
    # 아무것도 선택하지 않는 경우 -1
