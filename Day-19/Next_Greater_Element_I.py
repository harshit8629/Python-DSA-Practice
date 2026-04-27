nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

greater = []

for i in range(len(nums1)):
    for j in range(len(nums2)):
        if nums1[i] == nums2[j]:
            found = False
            for k in range(j + 1, len(nums2)):
                if nums2[k] > nums1[i]:
                    greater.append(nums2[k])
                    found = True
                    break
            if not found:
                greater.append(-1)

print(greater)