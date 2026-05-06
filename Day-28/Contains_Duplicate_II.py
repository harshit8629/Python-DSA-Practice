from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i, num in enumerate(nums):
            if num in seen:
                if i - seen[num] <= k:
                    return True

            seen[num] = i

        return False
solution = Solution()
print(solution.containsNearbyDuplicate([1, 2, 3, 1], 3))  # Output: True
print(solution.containsNearbyDuplicate([1, 0, 1, 1], 1))  # Output: True
print(solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # Output: False