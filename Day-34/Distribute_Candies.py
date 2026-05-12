class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        unique_candies = set(candyType)
        max_candies = len(candyType) // 2
        return min(len(unique_candies), max_candies)
solution = Solution()
print(solution.distributeCandies([1, 1, 2, 2, 3, 3]))  # Output: 3
print(solution.distributeCandies([1, 1, 2, 3]))  # Output: 2