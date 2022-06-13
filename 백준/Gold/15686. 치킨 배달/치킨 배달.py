from itertools import combinations
N,M = map(int,input().split())
city,home,chick = [],[],[]
for _ in range(N):city.append(list(map(int,input().split())))
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:home.append((i,j))
        elif city[i][j] == 2:chick.append((i,j))
slc_chick = list(combinations(chick,M))
result = []
for slc in slc_chick:
    temp = 0
    for h in home:
        cost = int(1e9)
        for c in slc:
            cost = min(cost,abs(h[0]-c[0])+abs(h[1]-c[1]))
        temp+=cost
    result.append(temp)
print(min(result))