from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k
sol = Solution()
k = sol.removeDuplicates(nums)

print(k)          # 5
print(nums[:k])   # [0, 1, 2, 3, 4]