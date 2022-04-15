N = int(input())
l = len(str(N))
num = 0
while l>0:
    num += l*(N-10**(l-1)+1)
    N = 10**(l-1)-1
    l -= 1
print(num)