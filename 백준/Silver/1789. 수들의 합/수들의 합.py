S = int(input())
n = 0
while S > 0:
    n += 1
    S -= n
if S < 0: n -= 1
print(n) 