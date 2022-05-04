N = int(input())
W = [int(i) for i in input().split()]
W.sort()
target = 1
for i in W:
    if target >= i:target += i
    else:break
print(target)