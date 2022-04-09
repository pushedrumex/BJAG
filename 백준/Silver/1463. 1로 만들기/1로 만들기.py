N = int(input())
d = [0]*(1000001)
d[2],d[3] = 1,1 

for i in range(4,N+1):
    d[i] = d[i-1] + 1
    if i%3 == 0: d[i] = min(d[i//3],d[i-1]) + 1 
    if i%2 == 0: d[i] = min(d[i//2],d[i-1]) + 1
    if i%6 == 0: d[i] = min(d[i//3],d[i//2],d[i-1]) + 1

print(d[N])