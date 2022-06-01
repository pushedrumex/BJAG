# 나보다 둘 다 낮은(순위가 높은) 애가 있다면 나는 탈락

import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
	N = int(input())
	grade = []
	for i in range(N):
		grade.append([])
		grade[i] = list(map(int,input().split()))
	grade.sort(reverse=True) # 첫번째 값 기준으로 내림차순 정렬 후, 내 오른쪽에 있는 것들 중 두번째 값이 나보다 작으면 나는 탈락!
	stack = []
	for i in grade:
		while stack and stack[-1] > i[1]: # stack에 있는 값들은 오름차순으로 들어오게됨 오른쪽에 나보다 순위가 높은 애가 있다면 난 탈락 pop
			stack.pop()
		stack.append(i[1])
	print(len(stack))
