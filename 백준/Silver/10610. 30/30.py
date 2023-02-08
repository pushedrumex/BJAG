N = sorted(list(map(int, list(input()))), reverse=True)
if N[-1] == 0 and sum(N)%3 == 0: print("".join(list(map(str, N))))
else: print(-1)