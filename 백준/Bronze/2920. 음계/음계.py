a = list(map(int, input().split()))
da = "cdefgabC"
flag = 0
for i in range(8):
    a[i] = da[a[i]-1]
for i in range(8):
    if a[i] != da[i]:
        flag = 1
        break
if flag == 0:
    print("ascending")
    exit()
flag = 0
for i in range(7,-1,-1):
    if a[i] != da[7-i]:
        flag = 1
        break
if flag == 0:
    print("descending")
    exit()
print("mixed")