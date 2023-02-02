import sys
input = sys.stdin.readline

N, C = map(int, input().split())
position = sorted([int(input()) for _ in range(N)])

def binary_search(position, C, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        current = position[0]
        router = 1 # 공유기 개수
        dist_min = int(1e9)
        for home in position[1:]:
            dist = home - current
            if mid <= dist: # 공유기 설치 가능하다면
                router += 1
                current = home
                dist_min = min(dist_min, dist)

        if router < C: # 공유기 수를 못채웠다면
            end = mid - 1
        else: # 공유기 수를 채웠다면
            start = mid + 1
            result = max(result, dist_min)

    return result

print(binary_search(position, C, 1, position[-1] - position[0]))