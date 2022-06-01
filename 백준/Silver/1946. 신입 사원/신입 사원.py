import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
	N = int(input())
	grade = []
	for i in range(N):
		grade.append([])
		grade[i] = list(map(int,input().split()))
	grade.sort(reverse=True)
	stack = []
	for i in grade:
		while stack and stack[-1] > i[1]:
			stack.pop()
		stack.append(i[1])
	print(len(stack))