N, a, b = map(int, input().split())

left = list(range(1, a+1))
right = list(range(b, 0, -1))
left[-1] = max(left[-1], right[0])
right[0] = left[-1]

building = left[:-1] + right
length = len(building)
if length > N:
    print(-1)
elif length == N:
    print(*building)
else:
    building = [building[0]] + [1] * (N-length) + building[1:]
    print(*building)