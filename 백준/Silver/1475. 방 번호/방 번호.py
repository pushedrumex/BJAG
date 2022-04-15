N = list(input())
for i in range(len(N)):
    if N[i] == '9': N[i] = '6'
nums = [0]*9 # 0~8
for i in N: nums[int(i)] += 1
if nums[6]%2 > 0:nums[6] += 1
nums[6] //= 2
print(max(nums))