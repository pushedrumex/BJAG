A, B, C, N = map(int, input().split())

for a in range(300):
    for b in range(300):
        for c in range(300):
            if A*a + B*b + C*c == N:
                print(1)
                exit()

print(0)