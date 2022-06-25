from collections import deque
for _ in range(int(input())):
    start,end = map(int,input().split())
    q = deque([["",start]])
    num = [False]*10000
    while q:
        cmd, n = q.popleft()
        d = (2*n)%10000
        if not num[d]:
            q.append([cmd+'D',d])
            num[d] = True
        if d == end:print(cmd+'D');break
        if n == 0:s = 9999
        else:s = n-1
        if not num[s]:
            q.append([cmd+'S',s])
            num[s] = True
        if s == end:print(cmd+'S');break
        if n*10>9999:l = (n%1000)*10 + n//1000
        else:l = n*10
        if not num[l]:
            q.append([cmd+'L',l])
            num[l] = True
        if l == end:print(cmd+'L');break
        if n%10>0:r = n//10 + (n%10)*1000
        else:r = n//10
        if not num[r]:
            q.append([cmd+'R',r])
            num[r] = True
        if r == end:print(cmd+'R');break