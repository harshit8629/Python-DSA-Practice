nums = [3,7]
ar =[]
for i in range(len(nums)):
  for j in range(i+1,len(nums)):
    result = (nums[i]-1)*(nums[j]-1)
    ar.append(result)
print(max(ar))