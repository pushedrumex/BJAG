
# 핵심 : 끝나는 시간이 빠른 순, 빨리 끝난다는건 그만큼 남는 시간이 많다는 것

import sys

N = int(input())
time = []

for _ in range(N):time.append(list(map(int,sys.stdin.readline().rstrip().split())))

time.sort()  # 시작시간 기준으로 오름차순, 시작시간 = 끝시간 고려
time.sort(key = lambda a : a[1])  # 끝시간 기준으로 오름차순

max = 1  # 가장 빨리 끝나는 것
end = time[0][1]  # 가장 빨리 끝나는 것

for i in range(1,N):
    if time[i][0] >= end:   # 나와 겹치지 않는다면 즉, 시작시간이 나의 끝시간보다 크거나 같다면
        max += 1       
        end = time[i][1]    # end 물려줌
        
print(max)
