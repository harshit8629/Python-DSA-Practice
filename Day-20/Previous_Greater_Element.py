def previous_greater_element(nums1, nums2):
    ans = []

    for num in nums1:
        index = nums2.index(num)
        greater = -1

        for i in range(index - 1, -1, -1):
            if nums2[i] > num:
                greater = nums2[i]
                break

        ans.append(greater)

    return ans


nums1 = [3, 4, 2]
nums2 = [1, 3, 4, 2]

print(previous_greater_element(nums1, nums2))