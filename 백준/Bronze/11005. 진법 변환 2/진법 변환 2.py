N,B = map(int,input().split())
if N == 0:print(N)
else:
    d = []
    while N:
        r = N%B
        if r>9:r = chr(ord('A')+r-10)
        d.append(str(r))
        N//=B
    d.reverse()
    print("".join(d))