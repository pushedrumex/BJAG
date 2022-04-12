N = int(input())
d = sorted(list(map(int,input().split())))
t = 0
for j in d:
    t += N*j
    N -= 1
print(t)