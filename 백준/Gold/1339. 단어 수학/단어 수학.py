N = int(input())
alpha = [0] * 26

for _ in range(N):
    word = input()
    n = len(word)
    for i in range(n):
        alpha[ord(word[i]) - ord('A')] += 10 ** (n-i-1)
n = 9
result = 0

for a in sorted(alpha, reverse=True):
    if a == 0: break
    result += a * n
    n -= 1

print(result)