N = int(input())

negative = []
positive = []

for _ in range(N):
    n = int(input())
    if n <= 0: negative.append(n)
    else: positive.append(n)

negative.sort(reverse=True)
positive.sort()

result, n1, n2 = 0, 0, 0
while negative:
    n1 = negative.pop()
    if negative:
        n2 = negative.pop()
        result += n1 * n2
        n1 = 0
    else:result += n1

while positive:
    n1 = positive.pop()
    if positive:
        n2 = positive.pop()
        if n1 == 1 or n2 == 1:
            result += n1 + n2
        else:
            result += n1 * n2
        n1 = 0
    else: result += n1

print(result)