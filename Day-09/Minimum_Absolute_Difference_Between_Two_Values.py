nums = [1,0,1,0]
difference =[]
for i in range(len(nums)):
  for j in range(len(nums)):
    if nums[i] == 1 and nums[j] == 2:
      difference.append(abs(i-j))
if difference:
  print(min(difference))
else:
  print(-1)