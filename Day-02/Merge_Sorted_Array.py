# you can enter the values and check the answer
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
def merge(nums1, m, nums2, n):
  for i in range(len(nums1),m,-1):
    nums1.pop()
  for i in range(len(nums2)):
    nums1.append(nums2[i])
  return nums1
result = merge(nums1, m, nums2, n)
result.sort()
print(result)