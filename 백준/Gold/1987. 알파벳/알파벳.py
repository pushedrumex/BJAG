dydx = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(y, x, visited, cnt):
    global result
    visited[ord(graph[y][x]) - ord("A")] = True
    # 다른 방향이라면 여러 경로 가능, for문 안이 아닌 이 부분에서 방문체크!
    # for문 안에서 한다면 다른 방향일 때, visited에 방문하지 않은 경로 포함됨
    for dy, dx in dydx:
        _y, _x = y + dy, x + dx
        if _y > R - 1 or _x > C - 1 or _y < 0 or _x < 0 or visited[ord(graph[_y][_x]) - ord("A")] : continue
        result = max(cnt + 1, result)
        dfs(_y, _x, visited[:], cnt + 1)

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
result = 1
dfs(0, 0, [False] * 26, 1)
print(result)

# list보다 dict가 빠르다고 하는 것은 list에 원소들을 순차적으로 넣고,
# 탐색할 때에도 순차적으로 탐색해서 찾는 경우에 비해 dict에서 한 번에 
# 접근하는 것이 빠르다는 뜻입니다. 만일 list와 dict에서 동일하게 한 번에 
# visit[x]와 같이 접근할 수 있다면 list 쪽이 훨씬 빠릅니다.
