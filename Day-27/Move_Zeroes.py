nums = [0]
zeroes = 0
for i in range(len(nums)):
    if nums[i] == 0:
        zeroes += 1
j = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[j] = nums[i]
        j += 1
for i in range(len(nums) - zeroes, len(nums)):
    nums[i] = 0

print(nums)