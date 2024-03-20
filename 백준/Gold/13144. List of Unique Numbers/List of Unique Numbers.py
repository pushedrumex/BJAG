N = int(input())
nums = list(map(int, input().split()))
answer = 0

visited = [False] * (max(nums) + 1)
left, right = 0, 0

while left <= right and right < N:
    if not visited[nums[right]]:
        visited[nums[right]] = True
        right += 1
        answer += right - left
    else:
        while visited[nums[right]]:
            visited[nums[left]] = False
            left += 1

print(answer)