nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

result = []

copy1 = nums1[:]
copy2 = nums2[:]

for i in copy1:
    if i in copy2:
        result.append(i)
        copy2.remove(i)

print(result)