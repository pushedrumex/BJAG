N = int(input())
K = 2**N -1

def move(N, start, end):

    # 맨 밑의 원반을 옮기기 위해 위에 있는 원반들을 다른 곳으로 옮김
    if N > 0:
        move(N-1, start, 6 - start - end)
        print(start, end)

    # 가장 마지막에 옮긴 원반은 1번 원반이어야함
    if N > 1:
        move(N-1, 6 - start - end, end)

print(K)

if N <= 20:
    move(N, 1, 3)