from collections import deque

s = input()
bomb = input()
n = len(bomb)

left = deque()
right = deque(list(s))
while right:
    temp = ""
    l = len(right)
    for i in range(min(n, l)):
        temp += right[i]
    if temp != bomb:
        left.append(right.popleft())
    else:
        for _ in range(n):
            right.popleft()
        for _ in range(n):
            if len(left) == 0:
                break
            right.appendleft(left.pop())

print("".join(left) if left else "FRULA")