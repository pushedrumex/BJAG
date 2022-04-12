import sys

N = int(input())
time = []
for _ in range(N):time.append(list(map(int,sys.stdin.readline().rstrip().split())))

time.sort()
time.sort(key = lambda a : a[1])

max = 1
end = time[0][1]
for i in range(1,N):
    if time[i][0] >= end:
        max += 1
        end = time[i][1]
        
print(max)