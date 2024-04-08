import sys
input = sys.stdin.readline

N = int(input())
count = [0] * (N+1)
for _ in range(N-1):
    a, b = map(int, input().split())
    count[a] += 1
    count[b] += 1

q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    if t == 1:
        if count[k] > 1:
            print("yes")
        else:
            print("no")
    elif t == 2:
        print("yes")