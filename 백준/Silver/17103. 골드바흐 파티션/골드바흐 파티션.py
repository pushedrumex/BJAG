import sys
T = int(input())

max = 1000000
root = int(max**0.5)

d = [True]*(max+1)
d[0],d[1] = False,False

for i in range(2,root+1):
    if d[i]:
        for j in range(i*2,max+1,i):d[j] = False

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    num = 0
    for i in range(1,N//2+1):
        if d[i] == d[N-i] == True:num += 1
    print(num)