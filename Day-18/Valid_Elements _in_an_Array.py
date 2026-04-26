class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        if n == 1:
            return nums
        
        right_max = [0] * n
        right_max[-1] = nums[-1]
        
        for i in range(n - 2, -1, -1):
            right_max[i] = max(nums[i], right_max[i + 1])
        
        res = []
        left_max = float('-inf')
        
        for i in range(n):
            if i == 0 or i == n - 1:
                res.append(nums[i])
            else:
                if nums[i] > left_max or nums[i] > right_max[i + 1]:
                    res.append(nums[i])
            
            left_max = max(left_max, nums[i])
        
        return res
nums = [1, 2, 4, 2, 3, 2]

sol = Solution()
result = sol.findValidElements(nums)

print(result)