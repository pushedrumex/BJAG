A,B = map(int,input().split())
i, n = 1, 1
d = [0]

while i < B+1:
    for _ in range(n):d.append(d[i-1] + n);i += 1
    n += 1
print(d[B]-d[A-1])