N = int(input())
A = list(map(int,input().split()))
LIS = [A[0]]
index = [[]]

for i in range(N):
    if LIS[-1]<A[i]:
        LIS.append(A[i])
        index.append([])
        index[-1].append(i)
    else:
        left,right = 0,len(LIS)-1
        while left<=right:
            mid = (left+right)//2
            if LIS[mid]<A[i]:left = mid+1
            else:
                right = mid-1
                result = mid
        LIS[result] = A[i]
        index[result].append(i)
answer = [LIS[-1]]
k = index.pop()[-1]
index.reverse()
for l in index:
    while l[-1]>k:l.pop()
    answer.append(A[l[-1]])
    k = l.pop()
print(len(answer))
print(*sorted(answer))