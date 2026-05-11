from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        result = []

        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                result.append(i)

        return result
solution = Solution()
print(solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]))  # Output: [5, 6]