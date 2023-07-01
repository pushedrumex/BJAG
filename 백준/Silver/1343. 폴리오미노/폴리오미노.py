from collections import deque

q = deque(list(input()))

answer = ""
while q:
    temp = q.popleft()
    if temp == ".":
        answer += "."
        continue

    while q and q[0] != ".":
        temp += q.popleft()
    m, n = len(temp) // 4, len(temp) % 4
    if n % 2 != 0:
        answer = -1
        break
    answer += "AAAA" * m + "BB" * (n // 2)

print(answer)