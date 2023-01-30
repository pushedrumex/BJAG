import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0] * N for _ in range(N)]

for _ in range(M):
    short, tall = map(int, input().split())
    graph[short-1][tall-1] = 1 # short가 tall보다 작음

# 모든 경로를 탐색
for k in range(N):
    for p1 in range(N):
        for p2 in range(N):
            # p1 < k 이고 k < p2 라면 p1 < p2이다.
            # 알 수 있는 모든 키 순서 기록
            if (graph[p1][k] + graph[k][p2]) == 2:
                graph[p1][p2] = 1

result = 0
# 모든 노드를 탐색
for p1 in range(N):
    check = 0
    for p2 in range(N):
        # p1와 p2의 키 순서를 알 수 있다면 check += 1 없다면 check += 0
        check += graph[p1][p2] + graph[p2][p1]
    # 자신을 제외한 N-1명과의 키 순서를 알 수 있다면 자신의 순서 알 수 있음
    if check == N-1:
        result += 1
    
print(result)
