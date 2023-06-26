N, S = map(int, input().split())
arr = list(map(int, input().split()))

answer = int(1e9)

left, right = 0, 0

temp = arr[0]
while right < N:
    if temp >= S:
        answer = min(answer, right - left + 1)
        temp -= arr[left]
        left += 1
    else:
        right += 1
        if right >= N:
            break
        temp += arr[right]

if answer == int(1e9):
    answer = 0

print(answer)