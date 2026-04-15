import numpy as np
nums1 = [1, 2]
nums2 = [3, 4]
num = []
for i in range(0,len(nums1),1):
    num.append(nums1[i])
for i in range(0,len(nums2),1):
    num.append(nums2[i])
    num.sort()
    result = np.median(num)
print(result)
