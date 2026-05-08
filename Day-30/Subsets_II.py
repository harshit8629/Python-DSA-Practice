class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = [[]]

        start = 0
        end = 0

        for i in range(len(nums)):
            # If current number is duplicate,
            # only use subsets added in previous step
            if i > 0 and nums[i] == nums[i - 1]:
                start = end + 1
            else:
                start = 0

            end = len(subsets) - 1

            for j in range(start, len(subsets)):
                subsets.append(subsets[j] + [nums[i]])

        return subsets
sol = Solution()
nums = [1, 2, 2]
result = sol.subsetsWithDup(nums)
print(result)  # [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]