H,W = map(int, input().split())
d = list(map(int, input().split()))
water = [0]*W
for i in range(1,W-1):
    lmax = max(d[:i]);rmax = max(d[i+1:])
    if lmax > d[i] and rmax > d[i]:water[i] = min(lmax,rmax) - d[i]
print(sum(water))
