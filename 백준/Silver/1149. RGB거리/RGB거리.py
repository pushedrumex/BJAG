N = int(input())
RGB = []

for i in range(N):
    RGB.append(list(map(int,input().split())))
    if i!=0:
        for j in range(3):RGB[i][j] += min(RGB[i-1][(j+1)%3],RGB[i-1][(j+2)%3])
        # RGB 각각 선택했을 때, 최소값을 저장 dp
print(min(RGB[N-1]))
