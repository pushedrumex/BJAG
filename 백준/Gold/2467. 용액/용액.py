N = int(input())
arr = list(map(int, input().split()))

left, right = 0, N-1
answer = [arr[left], arr[right]]
diff = abs(arr[left] + arr[right])
while left < right:
    value = arr[left] + arr[right]
    if value == 0:
        answer = [arr[left], arr[right]]
        break
    
    if abs(value) < diff:
        answer = [arr[left], arr[right]]
        diff = abs(value)

    if value < 0:
        left += 1
    elif value > 0:
        right -= 1

print(*answer)