import sys
t = int(input())
for _ in range(t):
    result = "YES"
    n = int(input())
    nums = []
    for _ in range(n): nums.append(sys.stdin.readline().rstrip())
    nums.sort()
    for i in range(n-1):
        if nums[i] == nums[i+1][:len(nums[i])]:
            result = "NO"
            break
    print(result)