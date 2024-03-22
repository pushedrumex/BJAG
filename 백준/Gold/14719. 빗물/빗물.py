H, W = map(int, input().split())
walls = list(map(int, input().split()))

water = [0] * (W)
left = walls[0]
for i in range(1, W-1):
    if walls[i] >= left:
        left = walls[i]
        continue
    right = max(walls[i:])
    water[i] = min(left, right) - walls[i]

print(sum(water))