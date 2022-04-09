n = int(input())
d = [0]*1001
d[1],d[2],d[3] = 1,2,3
for i in range(4,n+1):
    k = i//2
    if i%2 == 0:d[i] = d[k]*d[k] + d[k-1]*d[k-1]
    else:d[i] = d[k]*d[k+1] + d[k-1]*d[k]
print(d[n]%10007)