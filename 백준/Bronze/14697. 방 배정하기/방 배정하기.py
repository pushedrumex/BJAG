A, B, C, N = map(int, input().split())

rooms = [A, B, C]
def dfs(n):
    for i in range(3):
        _n = n + rooms[i]
        if _n < N:
            dfs(_n)
        elif _n == N:
            print(1)
            exit()
        else:
            return

dfs(0)
print(0)