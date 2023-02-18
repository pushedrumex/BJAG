import sys, heapq
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
jewels = sorted([list(map(int, input().rstrip().split())) for _ in range(N)])
bags = sorted([int(input().rstrip()) for _ in range(K)])

result = 0
jewels_tmp = []

for bag in bags:
    while jewels and bag >= jewels[0][0]:
        heapq.heappush(jewels_tmp, -heapq.heappop(jewels)[1])
    if jewels_tmp:
        result += heapq.heappop(jewels_tmp)
    elif not jewels:
        break;

print(-result)