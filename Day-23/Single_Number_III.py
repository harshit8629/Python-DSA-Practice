from itertools import combinations

class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        ans = []

        for combo in combinations(range(1, 10), k):
            if sum(combo) == n:
                ans.append(list(combo))

        return ans
sol = Solution()
print(sol.combinationSum3(3, 9))