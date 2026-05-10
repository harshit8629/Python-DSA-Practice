from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []

        for i in range(len(nums)):
            while dq and dq[0] <= i - k:
                dq.popleft()

            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            if i >= k - 1:
                result.append(nums[dq[0]])

        return result


sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))      # [3, 3, 5, 5, 6, 7]
print(sol.maxSlidingWindow([1], 1))                      # [1]
print(sol.maxSlidingWindow([9,10,9,-7,-4,-8,2,-6], 5))   # [10, 10, 9, 2]