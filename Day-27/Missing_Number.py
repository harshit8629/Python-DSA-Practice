nums = [0,1]
nums.sort()
for i in range(len(nums)):
    if i==nums[i]:
        continue
    else:
        print(i)
        break
else:
    print(len(nums))