import sys
input = sys.stdin.readline

def init(start, end, index):
    if start == end:
        tree[index] = arr[start-1]
        return tree[index]
    mid = (start + end) // 2
    tree[index] = init(start, mid, index*2) + init(mid+1, end, index*2+1)
    return tree[index]

def find(start, end, index, left, right):
    if start > right or end < left:
        return 0
    if start >= left and end <= right:
        return tree[index]
    mid = (start + end) // 2
    sum = find(start, mid, index*2, left, right) + find(mid+1, end, index*2+1, left, right)
    return sum

def update(start, end, index, idx, data):
    if start > idx or end < idx: return
    tree[index] += data
    if start == end: return
    
    mid = (start + end) // 2
    update(start, mid, index*2, idx, data)
    update(mid+1, end, index*2+1, idx, data)

N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
tree = [0]*N*4

init(1, N, 1)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, N, 1, b, c - arr[b-1])
        arr[b-1] = c
    else:
        print(find(1, N, 1, b, c))