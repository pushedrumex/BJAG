seg = [0, 1]
def solution(n, l, r):
    for _ in range(n-1):
        seg.append(seg[-1] * 4)
    return dfs(r, n) - dfs(l-1, n)

def dfs(i, n):
    if n == 0:
        return 0
    bit = 5 ** (n-1)
    a = i // bit
    if a == 2:
        return a * seg[n]

    if a > 2:
        a -= 1
    return a * seg[n] + dfs(i % bit, n-1)
    