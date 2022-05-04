import sys

N = int(input())
L = []
for _ in range(N): L.append(int(sys.stdin.readline().strip()))
L.sort(reverse=True)
max = L[0]
for i in range(1, N):
    if L[i]*(i+1) > max:max = L[i]*(i+1)
print(max)