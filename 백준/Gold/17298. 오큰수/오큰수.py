N = int(input())
T = list(map(int,input().split()))

answer = [-1] * N
stack = []   # 내림차순으로 값이 들어오고 이에 해당하는 인덱스가 쌓임 
stack.append(0)

for i in range(1,N):
  while stack and T[stack[-1]] < T[i]:
    answer[stack.pop()] = T[i]
  stack.append(i)
  
print(*answer)
