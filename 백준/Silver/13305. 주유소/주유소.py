N = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

i = 0
result = 0

# 현재 주유소보다 더 저렴한 주유소 전까지, 현재 주유소에서 기름 구매
while i < N-1:
    current = cost[i] # 현재 주유소 가격
    while i < N-1 and current <= cost[i]:
        result += current * dist[i]
        i += 1

print(result)
