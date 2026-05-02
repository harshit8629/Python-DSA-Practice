from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = Counter(nums)

        maximum = 0
        answer = 0

        for key, value in count.items():
            if value > maximum:
                maximum = value
                answer = key

        return answer
solution = Solution()
nums = [2,2,1,1,1,2,2]
print(solution.majorityElement(nums))